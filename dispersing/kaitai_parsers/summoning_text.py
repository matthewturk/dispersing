# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version("0.7"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s"
        % (ks_version)
    )


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
            self.text[i] = self._root.Xorstr(self._io, self, self._root)

    class Xorstrz(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.text = (self._io.read_bytes_term(218, False, True, True)).decode(
                "ascii"
            )

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
            if hasattr(self, "_m_value"):
                return self._m_value if hasattr(self, "_m_value") else None

            self._m_value = self.text
            return self._m_value if hasattr(self, "_m_value") else None
