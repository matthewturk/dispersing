# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from kaitaistruct import BytesIO, KaitaiStream, KaitaiStruct, __version__ as ks_version
from pkg_resources import parse_version

if parse_version(ks_version) < parse_version("0.7"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s"
        % (ks_version)
    )


class SummoningKeywords(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.count = self._io.read_u2le()
        self.offsets = [None] * (self.count)
        for i in range(self.count):
            self.offsets[i] = self._io.read_u2le()

        self.keyword = [None] * (self.count)
        for i in range(self.count):
            self.keyword[i] = (self._io.read_bytes_term(0, False, True, True)).decode(
                "ASCII"
            )
