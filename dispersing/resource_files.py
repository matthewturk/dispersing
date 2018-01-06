import os
import stat
import numpy as np
import pandas as pd
import ipywidgets
import ipythonblocks

resource_registry = {}

class RegisteredResource(type):
    def __init__(cls, name, bases, nmspc):
        super(RegisteredResource, cls).__init__(name, bases, nmspc)
        if getattr(cls, "name", None) is not None:
            resource_registry[cls.name] = cls

class PackedResourceFile(metaclass = RegisteredResource):
    countsize = 1
    indexsize = 2
    name = "packed_resource_file"
    def __init__(self, filename, countsize = None, indexsize = None):
        dtype_c = 'u{}'.format(countsize or self.countsize)
        dtype_i = 'u{}'.format(indexsize or self.indexsize)
        size = os.stat(filename)[stat.ST_SIZE]
        self.locations = []
        with open(filename, "rb") as f:
            n_rec, = np.fromfile(f, dtype=dtype_c, count=1)
            self.read_header(f)
            indices = np.fromfile(f, dtype=dtype_i, count=n_rec)
            indices = np.concatenate([indices, [size]])
            self.records = []
            self.indices = indices[:-1]
            for si, ei in zip(indices[:-1], indices[1:]):
                self.locations.append(f.tell())
                self.records.append(self.process_record(np.fromfile(f, count=ei-si, dtype='u1')))
            self.process_records()
        self.sizes = [len(_) for _ in self.records]
            
    def read_header(self, f):
        pass
    
    def process_record(self, rec):
        return rec
    
    def process_records(self):
        pass

_REC1_HEADER = np.dtype( [
    ('height', 'u2'),
    ('count', 'u1'),
    ('width', 'u1'),
    ('field_4', 'u1'),
    ('algo', 'u1'),
    ('field_6', 'u1')]
)

class ResourceFile(PackedResourceFile):
    name = "resource"
    countsize = 4
    indexsize = 4
    def process_record(self, rec):
        assert(rec[:2].tostring() == b"EH")
        return rec[2:]

    def unpack(self, rec_id):
        rec = self.records[rec_id]
        if rec[0] == 1:
            # Some type of sprite
            header, value = self._unpack_rec1(rec_id)
        elif rec[0] == 2:
            # Still not sure what this is.
            raise NotImplementedError
        elif rec[0] == 3:
            # This is an MUS file and an SND file
            # for adlib
            raise NotImplementedError
        else:
            raise NotImplementedError
        return header, value

    def _unpack_rec1(self, rec_id):
        record = self.records[rec_id]
        header = record[3:10].view(_REC1_HEADER)
        pos = 0
        s = record[10:].view('i1').copy()
        d = []
        # These are inspired by the Unveiled project
        if header['algo'][0] == 1:
            while pos < s.size:
                v = s[pos]
                pos += 1
                if v < 0:
                    count = -v + 1
                    d.extend(count * s[pos:pos+1].tolist())
                    pos += 1
                else:
                    count = v + 1
                    d.extend(s[pos:pos+count])
                    pos += count
        elif header['algo'][0] == 3:
            s = s.view('u1')
            history = np.zeros(0x1000, dtype='u1')
            history[:] = 0xFE
            it = 0xFEE
            si = 0
            while pos < s.size:
                si >>= 1
                if (si & 0x100) == 0:
                    si = s[pos]
                    pos += 1
                    si |= 0xFF00
                if (si & 1) != 0:
                    v = s[pos]
                    pos += 1
                    d.append(v)
                    history[it] = v
                    it = (it+1) & 0xFFF
                else:
                    v1 = s[pos]
                    pos += 1
                    v2 = s[pos]
                    pos += 1
                    v1 |= (v2 & 0xF0) << 4
                    di = (v2 & 0x0F) + 2
                    cx = 0
                    while cx <= di:
                        bx = (v1 + cx) & 0xFFF
                        v = history[bx]
                        d.append(v)
                        history[it] = v
                        it = (it+1) & 0xFFF
                        cx += 1
        else:
            raise KeyError(header['algo'][0])
        d = np.array(d, dtype='uint8')
        return header, d
    
class PackedRecordFile(metaclass = RegisteredResource):
    name = "packed_record"
    countsize = 2
    column_names = None
    footer_size = 0
    def __init__(self, filename, countsize = None):
        dtype_c = "u{}".format(countsize or self.countsize)
        size = os.stat(filename)[stat.ST_SIZE]
        with open(filename, "rb") as f:
            n_obj, = np.fromfile(f, dtype=dtype_c, count = 1)
            self.read_header(f)
            obj_data = np.fromfile(f, dtype="u1")
            s = (obj_data.size - self.footer_size) / n_obj
            if s != np.ceil(s):
                raise RuntimeError("Size mismatch.")
            obj_data = obj_data.reshape((n_obj, int(s)))
        self.data = pd.DataFrame(obj_data)
        self.process_dataframe()
            
    def read_header(self, f):
        pass
    
    def process_dataframe(self):
        pass
    
class UnknownRecordFile(PackedRecordFile):
    name = "unknown_record_file"
    countsize = 1
    def read_header(self, f):
        self.header = np.fromfile(f, dtype="u1", count=4)
    
class ObjectRecordFile(PackedRecordFile):
    name = "objects"
    def read_header(self, f):
        self.offset = np.fromfile(f, dtype="u2", count = 1)

class ColorRecordFile(PackedRecordFile):
    name = "colors"
    countsize = 1
    def process_dataframe(self):
        self.data.T
        cnames = dict(enumerate([ ("P%02i" % i, "RGB"[j]) for i in range(16) for j in range(3)]))
        self.data.rename(cnames, axis="columns", inplace=True)
        self.data.index.name = "Color"
        self.data = self.data.transpose()
        
    def plot(self):
        image = np.zeros((self.data.shape[0], self.data.shape[1]//3, 3))
        image[:,:,0] = self.data.loc[:, pd.IndexSlice[:, "R"]] * 4
        image[:,:,1] = self.data.loc[:, pd.IndexSlice[:, "G"]] * 4
        image[:,:,2] = self.data.loc[:, pd.IndexSlice[:, "B"]] * 4
        return image
        
class InteractionResourceFile(PackedResourceFile):
    countsize = 2
    indexsize = 4
    name = "interact"
    def read_header(self, f):
        self.offset = np.fromfile(f, dtype='u2', count = 1)
        
class TextResourceFile(PackedResourceFile):
    countsize = 4
    indexsize = 4
    name = "text"
    def process_record(self, rec):
        return (rec ^ 218).tostring().replace(b"\xda", b"")
    
class LevelMap:
    def __init__(self, level_id, data):
        # Some info about the level map item data:
        #   The way it seems to work is that there are locations and then
        #   opcodes.
        #   \x08\x04 => portal info, followed by level, location on level
        #   Items seem to be in form X,Y,N,[N item codes]
        #   I'm not sure how to differentiate items from the other.
        # Maybe it goes:
        #   X Y N_t1(t1 info) N_t2(t2 info) N_t3(t3 info)
        # Could it be item, NPC, portal?
        #self.name = level_names[level_id]
        self.height = int(data[0])
        self.width = int(data[1])
        self.header = data[2:66].view('u2').astype('int64')
        self.map_data = data[66:66+self.height*self.width].reshape((self.height, self.width), order='C')
        self.item_data = data[66+self.height*self.width:]
        self.n_cells = (self.map_data != 255).sum()
        self.cell_count = np.bincount(self.map_data.ravel(), minlength=256)
        self.size = data.size
        
    def __len__(self):
        return self.size
        
    def block_grid(self):
        bg = ipythonblocks.BlockGrid(width = self.width, height = self.height, lines_on = False, block_size = 20)
        for i in range(self.height):
            for j in range(self.width):
                if self.map_data[i,j] == 255:
                    bg[i,j].rgb = (0, 0, 0)
                else:
                    bg[i,j].rgb = (100, 100, 100)
        return bg
    
    def highlighter(self):
        lg = self.block_grid()
        @ipywidgets.interact(highlight = np.unique(self.map_data).tolist())
        def highlight_map(highlight = 0):
            for i in range(self.map_data.shape[0]):
                for j in range(self.map_data.shape[1]):
                    if self.map_data[i,j] == highlight:
                        lg[i,j].rgb = (255, 255, 255)
                    elif self.map_data[i,j] < 255:
                        lg[i,j].rgb = (100, 100, 0)
                    else:
                        lg[i,j].rgb = (0, 0, 0)
            print(np.unpackbits(np.array([highlight], dtype='u1')))
            return lg
        return highlight_map

class LevelResourceFile(PackedResourceFile):
    countsize = 4
    indexsize = 4
    name = "levels"   
    def process_record(self, rec):
        return LevelMap(-1, rec)

class KeywordResourceFile(PackedResourceFile):
    countsize = 2
    indexsize = 2
    name = "keywords"
    def process_record(self, rec):
        return rec[:-1].tostring().decode("ascii")

class NPCRecordFile(PackedRecordFile):
    countsize = 2
