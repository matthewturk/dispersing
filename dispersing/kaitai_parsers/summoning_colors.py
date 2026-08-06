# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningColors(KaitaiStruct):
    SEQ_FIELDS = ["ncolors", "palettes"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningColors, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['ncolors']['start'] = self._io.pos()
        self.ncolors = self._io.read_u1()
        self._debug['ncolors']['end'] = self._io.pos()
        self._debug['palettes']['start'] = self._io.pos()
        self._debug['palettes']['arr'] = []
        self.palettes = []
        for i in range((self._root._io.size() - 1) // (self.ncolors * 3)):
            self._debug['palettes']['arr'].append({'start': self._io.pos()})
            self.palettes.append(SummoningColors.Palette(self._io, self, self._root))
            self._debug['palettes']['arr'][i]['end'] = self._io.pos()

        self._debug['palettes']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.palettes)):
            pass
            self.palettes[i]._fetch_instances()


    class Palette(KaitaiStruct):
        SEQ_FIELDS = ["colors"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningColors.Palette, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['colors']['start'] = self._io.pos()
            self._debug['colors']['arr'] = []
            self.colors = []
            for i in range(self._root.ncolors):
                self._debug['colors']['arr'].append({'start': self._io.pos()})
                self.colors.append(SummoningColors.Rgb(self._io, self, self._root))
                self._debug['colors']['arr'][i]['end'] = self._io.pos()

            self._debug['colors']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.colors)):
                pass
                self.colors[i]._fetch_instances()



    class Rgb(KaitaiStruct):
        SEQ_FIELDS = ["red", "green", "blue"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningColors.Rgb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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


        def _fetch_instances(self):
            pass



