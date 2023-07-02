# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningColors(KaitaiStruct):
    SEQ_FIELDS = ["ncolors", "palettes"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['ncolors']['start'] = self._io.pos()
        self.ncolors = self._io.read_u1()
        self._debug['ncolors']['end'] = self._io.pos()
        self._debug['palettes']['start'] = self._io.pos()
        self.palettes = [None] * ((self._root._io.size() - 1) // (self.ncolors * 3))
        for i in range((self._root._io.size() - 1) // (self.ncolors * 3)):
            if not 'arr' in self._debug['palettes']:
                self._debug['palettes']['arr'] = []
            self._debug['palettes']['arr'].append({'start': self._io.pos()})
            self.palettes[i] = SummoningColors.Palette(self._io, self, self._root)
            self._debug['palettes']['arr'][i]['end'] = self._io.pos()

        self._debug['palettes']['end'] = self._io.pos()

    class Palette(KaitaiStruct):
        SEQ_FIELDS = ["colors"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['colors']['start'] = self._io.pos()
            self.colors = [None] * (self._root.ncolors)
            for i in range(self._root.ncolors):
                if not 'arr' in self._debug['colors']:
                    self._debug['colors']['arr'] = []
                self._debug['colors']['arr'].append({'start': self._io.pos()})
                self.colors[i] = SummoningColors.Rgb(self._io, self, self._root)
                self._debug['colors']['arr'][i]['end'] = self._io.pos()

            self._debug['colors']['end'] = self._io.pos()


    class Rgb(KaitaiStruct):
        SEQ_FIELDS = ["red", "green", "blue"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['red']['start'] = self._io.pos()
            self.red = self._io.read_u1()
            self._debug['red']['end'] = self._io.pos()
            self._debug['green']['start'] = self._io.pos()
            self.green = self._io.read_u1()
            self._debug['green']['end'] = self._io.pos()
            self._debug['blue']['start'] = self._io.pos()
            self.blue = self._io.read_u1()
            self._debug['blue']['end'] = self._io.pos()



