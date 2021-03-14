# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningText(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.count = self._io.read_u4le()
        self.offsets = [None] * (self.count)
        for i in range(self.count):
            self.offsets[i] = self._io.read_u4le()

        self.text = [None] * (self.count)
        for i in range(self.count):
            self.text[i] = SummoningText.Xorstr(self._io, self, self._root)


    class Xorstrz(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.text = (self._io.read_bytes_term(218, False, True, True)).decode(u"ascii")


    class Xorstr(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self._raw_text = self._io.read_bytes_term(0, False, True, True)
            self.text = KaitaiStream.process_xor_one(self._raw_text, 218)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = self.text
            return self._m_value if hasattr(self, '_m_value') else None



