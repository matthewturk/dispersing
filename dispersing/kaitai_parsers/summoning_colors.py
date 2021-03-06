# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version("0.7"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s"
        % (ks_version)
    )


class SummoningColors(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.ncolors = self._io.read_u1()
        self.palettes = [None] * ((self._root._io.size() - 1) // (self.ncolors * 3))
        for i in range((self._root._io.size() - 1) // (self.ncolors * 3)):
            self.palettes[i] = self._root.Palette(self._io, self, self._root)

    class Palette(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.colors = [None] * (self._root.ncolors)
            for i in range(self._root.ncolors):
                self.colors[i] = self._root.Rgb(self._io, self, self._root)

    class Rgb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.red = self._io.read_u1()
            self.green = self._io.read_u1()
            self.blue = self._io.read_u1()
