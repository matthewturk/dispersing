# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningKeywords(KaitaiStruct):
    SEQ_FIELDS = ["count", "offsets", "keyword"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningKeywords, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['count']['start'] = self._io.pos()
        self.count = self._io.read_u2le()
        self._debug['count']['end'] = self._io.pos()
        self._debug['offsets']['start'] = self._io.pos()
        self._debug['offsets']['arr'] = []
        self.offsets = []
        for i in range(self.count):
            self._debug['offsets']['arr'].append({'start': self._io.pos()})
            self.offsets.append(self._io.read_u2le())
            self._debug['offsets']['arr'][i]['end'] = self._io.pos()

        self._debug['offsets']['end'] = self._io.pos()
        self._debug['keyword']['start'] = self._io.pos()
        self._debug['keyword']['arr'] = []
        self.keyword = []
        for i in range(self.count):
            self._debug['keyword']['arr'].append({'start': self._io.pos()})
            self.keyword.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
            self._debug['keyword']['arr'][i]['end'] = self._io.pos()

        self._debug['keyword']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.offsets)):
            pass

        for i in range(len(self.keyword)):
            pass



