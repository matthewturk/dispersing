# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningV(KaitaiStruct):
    SEQ_FIELDS = ["count", "unk1", "unk2", "unk3", "unk4", "rec_info", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningV, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['count']['start'] = self._io.pos()
        self.count = self._io.read_u1()
        self._debug['count']['end'] = self._io.pos()
        self._debug['unk1']['start'] = self._io.pos()
        self.unk1 = self._io.read_u1()
        self._debug['unk1']['end'] = self._io.pos()
        self._debug['unk2']['start'] = self._io.pos()
        self.unk2 = self._io.read_u1()
        self._debug['unk2']['end'] = self._io.pos()
        self._debug['unk3']['start'] = self._io.pos()
        self.unk3 = self._io.read_u1()
        self._debug['unk3']['end'] = self._io.pos()
        self._debug['unk4']['start'] = self._io.pos()
        self.unk4 = self._io.read_u1()
        self._debug['unk4']['end'] = self._io.pos()
        self._debug['rec_info']['start'] = self._io.pos()
        self._debug['rec_info']['arr'] = []
        self.rec_info = []
        for i in range(self.count):
            self._debug['rec_info']['arr'].append({'start': self._io.pos()})
            self.rec_info.append(self._io.read_u2le())
            self._debug['rec_info']['arr'][i]['end'] = self._io.pos()

        self._debug['rec_info']['end'] = self._io.pos()
        self._debug['records']['start'] = self._io.pos()
        self._debug['records']['arr'] = []
        self.records = []
        for i in range(self.count):
            self._debug['records']['arr'].append({'start': self._io.pos()})
            self.records.append(SummoningV.Frecord(self._io, self, self._root))
            self._debug['records']['arr'][i]['end'] = self._io.pos()

        self._debug['records']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.rec_info)):
            pass

        for i in range(len(self.records)):
            pass
            self.records[i]._fetch_instances()


    class Frecord(KaitaiStruct):
        SEQ_FIELDS = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningV.Frecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['col1']['start'] = self._io.pos()
            self.col1 = self._io.read_u1()
            self._debug['col1']['end'] = self._io.pos()
            self._debug['col2']['start'] = self._io.pos()
            self.col2 = self._io.read_u1()
            self._debug['col2']['end'] = self._io.pos()
            self._debug['col3']['start'] = self._io.pos()
            self.col3 = self._io.read_u1()
            self._debug['col3']['end'] = self._io.pos()
            self._debug['col4']['start'] = self._io.pos()
            self.col4 = self._io.read_u1()
            self._debug['col4']['end'] = self._io.pos()
            self._debug['col5']['start'] = self._io.pos()
            self.col5 = self._io.read_u1()
            self._debug['col5']['end'] = self._io.pos()
            self._debug['col6']['start'] = self._io.pos()
            self.col6 = self._io.read_u1()
            self._debug['col6']['end'] = self._io.pos()
            self._debug['col7']['start'] = self._io.pos()
            self.col7 = self._io.read_u1()
            self._debug['col7']['end'] = self._io.pos()
            self._debug['col8']['start'] = self._io.pos()
            self.col8 = self._io.read_u1()
            self._debug['col8']['end'] = self._io.pos()
            self._debug['col9']['start'] = self._io.pos()
            self.col9 = self._io.read_u1()
            self._debug['col9']['end'] = self._io.pos()
            self._debug['col10']['start'] = self._io.pos()
            self.col10 = self._io.read_u1()
            self._debug['col10']['end'] = self._io.pos()
            self._debug['col11']['start'] = self._io.pos()
            self.col11 = self._io.read_u1()
            self._debug['col11']['end'] = self._io.pos()
            self._debug['col12']['start'] = self._io.pos()
            self.col12 = self._io.read_u1()
            self._debug['col12']['end'] = self._io.pos()
            self._debug['col13']['start'] = self._io.pos()
            self.col13 = self._io.read_u1()
            self._debug['col13']['end'] = self._io.pos()
            self._debug['col14']['start'] = self._io.pos()
            self.col14 = self._io.read_u1()
            self._debug['col14']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



