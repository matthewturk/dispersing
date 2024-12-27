# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class VeilRooms(KaitaiStruct):

    class TileFlags(Enum):
        nothing = 0
        movable_object = 1
        unknown2 = 2
        teleporter_dest = 3
        unknown4 = 4
        unknown5 = 5
        unknown6 = 6
        teleporter = 7
        level_exit = 8
        npc = 9
        unknown10 = 10
        mouth = 11
    SEQ_FIELDS = ["file_header", "levels"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_header']['start'] = self._io.pos()
        self.file_header = VeilRooms.Header(self._io, self, self._root)
        self._debug['file_header']['end'] = self._io.pos()
        self._debug['levels']['start'] = self._io.pos()
        self.levels = [None] * (self.file_header.count)
        for i in range(self.file_header.count):
            if not 'arr' in self._debug['levels']:
                self._debug['levels']['arr'] = []
            self._debug['levels']['arr'].append({'start': self._io.pos()})
            self.levels[i] = VeilRooms.Level(self._io, self, self._root)
            self._debug['levels']['arr'][i]['end'] = self._io.pos()

        self._debug['levels']['end'] = self._io.pos()

    class PortalInfo(KaitaiStruct):
        SEQ_FIELDS = ["opcode", "level", "dest_x", "dest_y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opcode']['start'] = self._io.pos()
            self.opcode = self._io.read_u1()
            self._debug['opcode']['end'] = self._io.pos()
            self._debug['level']['start'] = self._io.pos()
            self.level = self._io.read_u1()
            self._debug['level']['end'] = self._io.pos()
            self._debug['dest_x']['start'] = self._io.pos()
            self.dest_x = self._io.read_u1()
            self._debug['dest_x']['end'] = self._io.pos()
            self._debug['dest_y']['start'] = self._io.pos()
            self.dest_y = self._io.read_u1()
            self._debug['dest_y']['end'] = self._io.pos()


    class ItemData(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "info"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_u1()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_u1()
            self._debug['y']['end'] = self._io.pos()
            if self.x != 255:
                self._debug['info']['start'] = self._io.pos()
                self.info = VeilRooms.TileInfo(self._io, self, self._root)
                self._debug['info']['end'] = self._io.pos()



    class SpeechStrings(KaitaiStruct):
        SEQ_FIELDS = ["size", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2be()
            self._debug['size']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = self._io.read_bytes(self.size)
            self._debug['text']['end'] = self._io.pos()


    class OtherData(KaitaiStruct):
        SEQ_FIELDS = ["size", "contents"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            self.contents = [None] * (self.size)
            for i in range(self.size):
                if not 'arr' in self._debug['contents']:
                    self._debug['contents']['arr'] = []
                self._debug['contents']['arr'].append({'start': self._io.pos()})
                self.contents[i] = self._io.read_u1()
                self._debug['contents']['arr'][i]['end'] = self._io.pos()

            self._debug['contents']['end'] = self._io.pos()


    class TeleporterInfo(KaitaiStruct):
        SEQ_FIELDS = ["unknown"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(5)
            self._debug['unknown']['end'] = self._io.pos()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["count", "offsets"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = self._io.read_u4le()
            self._debug['count']['end'] = self._io.pos()
            self._debug['offsets']['start'] = self._io.pos()
            self.offsets = [None] * (self.count)
            for i in range(self.count):
                if not 'arr' in self._debug['offsets']:
                    self._debug['offsets']['arr'] = []
                self._debug['offsets']['arr'].append({'start': self._io.pos()})
                self.offsets[i] = self._io.read_u4le()
                self._debug['offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['offsets']['end'] = self._io.pos()


    class TileInfo(KaitaiStruct):
        SEQ_FIELDS = ["n1", "items", "floor_flags", "tile_args", "wall_flags", "wall_args"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['n1']['start'] = self._io.pos()
            self.n1 = self._io.read_u1()
            self._debug['n1']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self.items = [None] * (self.n1)
            for i in range(self.n1):
                if not 'arr' in self._debug['items']:
                    self._debug['items']['arr'] = []
                self._debug['items']['arr'].append({'start': self._io.pos()})
                self.items[i] = self._io.read_u1()
                self._debug['items']['arr'][i]['end'] = self._io.pos()

            self._debug['items']['end'] = self._io.pos()
            self._debug['floor_flags']['start'] = self._io.pos()
            self.floor_flags = KaitaiStream.resolve_enum(VeilRooms.TileFlags, self._io.read_u1())
            self._debug['floor_flags']['end'] = self._io.pos()
            if  ((self.floor_flags != VeilRooms.TileFlags.nothing) and (self.floor_flags != VeilRooms.TileFlags.movable_object)) :
                self._debug['tile_args']['start'] = self._io.pos()
                _on = self.floor_flags
                if _on == VeilRooms.TileFlags.teleporter:
                    self.tile_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown4:
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.movable_object:
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown6:
                    self.tile_args = self._io.read_u2le()
                elif _on == VeilRooms.TileFlags.mouth:
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown10:
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.level_exit:
                    self.tile_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown2:
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown5:
                    self.tile_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.npc:
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.teleporter_dest:
                    self.tile_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                self._debug['tile_args']['end'] = self._io.pos()

            self._debug['wall_flags']['start'] = self._io.pos()
            self.wall_flags = KaitaiStream.resolve_enum(VeilRooms.TileFlags, self._io.read_u1())
            self._debug['wall_flags']['end'] = self._io.pos()
            if self.wall_flags != VeilRooms.TileFlags.nothing:
                self._debug['wall_args']['start'] = self._io.pos()
                _on = self.wall_flags
                if _on == VeilRooms.TileFlags.teleporter:
                    self.wall_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown4:
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.movable_object:
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown6:
                    self.wall_args = self._io.read_u2le()
                elif _on == VeilRooms.TileFlags.mouth:
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown10:
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.level_exit:
                    self.wall_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown2:
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown5:
                    self.wall_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.npc:
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.teleporter_dest:
                    self.wall_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                self._debug['wall_args']['end'] = self._io.pos()



    class Level(KaitaiStruct):
        SEQ_FIELDS = ["ehmagic", "unknown", "height", "width", "vals", "map", "items", "speech", "other"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ehmagic']['start'] = self._io.pos()
            self.ehmagic = self._io.read_bytes(2)
            self._debug['ehmagic']['end'] = self._io.pos()
            if not self.ehmagic == b"\x45\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x48", self.ehmagic, self._io, u"/types/level/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_u1()
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['vals']['start'] = self._io.pos()
            self.vals = [None] * (32)
            for i in range(32):
                if not 'arr' in self._debug['vals']:
                    self._debug['vals']['arr'] = []
                self._debug['vals']['arr'].append({'start': self._io.pos()})
                self.vals[i] = self._io.read_s2le()
                self._debug['vals']['arr'][i]['end'] = self._io.pos()

            self._debug['vals']['end'] = self._io.pos()
            self._debug['map']['start'] = self._io.pos()
            self.map = self._io.read_bytes((self.width * self.height))
            self._debug['map']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self.items = []
            i = 0
            while True:
                if not 'arr' in self._debug['items']:
                    self._debug['items']['arr'] = []
                self._debug['items']['arr'].append({'start': self._io.pos()})
                _ = VeilRooms.ItemData(self._io, self, self._root)
                self.items.append(_)
                self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                if  ((_.x == 255) and (_.y == 255)) :
                    break
                i += 1
            self._debug['items']['end'] = self._io.pos()
            self._debug['speech']['start'] = self._io.pos()
            self.speech = VeilRooms.SpeechStrings(self._io, self, self._root)
            self._debug['speech']['end'] = self._io.pos()
            self._debug['other']['start'] = self._io.pos()
            self.other = VeilRooms.OtherData(self._io, self, self._root)
            self._debug['other']['end'] = self._io.pos()



