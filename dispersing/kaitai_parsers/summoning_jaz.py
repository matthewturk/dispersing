# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class SummoningJaz(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.count = self._io.read_u2le()
        self.unknown1 = self._io.read_u2le()
        self.unknown2 = self._io.read_u2le()

    class Frecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.col1 = self._io.read_u1()
            self.col2 = self._io.read_u1()
            self.col3 = self._io.read_u1()
            self.col4 = self._io.read_u1()
            self.col5 = self._io.read_u1()
            self.col6 = self._io.read_u1()
            self.col7 = self._io.read_u1()
            self.col8 = self._io.read_u1()
            self.col9 = self._io.read_u1()
            self.col10 = self._io.read_u1()
            self.col11 = self._io.read_u1()
            self.col12 = self._io.read_u1()
            self.col13 = self._io.read_u1()
            self.col14 = self._io.read_u1()
            self.col15 = self._io.read_u1()
            self.col16 = self._io.read_u1()



