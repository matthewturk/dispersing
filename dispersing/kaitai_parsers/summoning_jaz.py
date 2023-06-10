# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningJaz(KaitaiStruct):
    SEQ_FIELDS = ["count", "unknown1", "unknown2"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['count']['start'] = self._io.pos()
        self.count = self._io.read_u2le()
        self._debug['count']['end'] = self._io.pos()
        self._debug['unknown1']['start'] = self._io.pos()
        self.unknown1 = self._io.read_u2le()
        self._debug['unknown1']['end'] = self._io.pos()
        self._debug['unknown2']['start'] = self._io.pos()
        self.unknown2 = self._io.read_u2le()
        self._debug['unknown2']['end'] = self._io.pos()

    class Frecord(KaitaiStruct):
        SEQ_FIELDS = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13", "col14", "col15", "col16"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
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
            self._debug['col15']['start'] = self._io.pos()
            self.col15 = self._io.read_u1()
            self._debug['col15']['end'] = self._io.pos()
            self._debug['col16']['start'] = self._io.pos()
            self.col16 = self._io.read_u1()
            self._debug['col16']['end'] = self._io.pos()



