# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningKeywords(KaitaiStruct):
    SEQ_FIELDS = ["count", "offsets", "keyword"]
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
        self._debug['offsets']['start'] = self._io.pos()
        self.offsets = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['offsets']:
                self._debug['offsets']['arr'] = []
            self._debug['offsets']['arr'].append({'start': self._io.pos()})
            self.offsets[i] = self._io.read_u2le()
            self._debug['offsets']['arr'][i]['end'] = self._io.pos()

        self._debug['offsets']['end'] = self._io.pos()
        self._debug['keyword']['start'] = self._io.pos()
        self.keyword = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['keyword']:
                self._debug['keyword']['arr'] = []
            self._debug['keyword']['arr'].append({'start': self._io.pos()})
            self.keyword[i] = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['keyword']['arr'][i]['end'] = self._io.pos()

        self._debug['keyword']['end'] = self._io.pos()


