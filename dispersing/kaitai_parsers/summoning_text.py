# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningText(KaitaiStruct):
    SEQ_FIELDS = ["count", "offsets", "text"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['count']['start'] = self._io.pos()
        self.count = self._io.read_u4le()
        self._debug['count']['end'] = self._io.pos()
        self._debug['offsets']['start'] = self._io.pos()
        self.offsets = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['offsets']:
                self._debug['offsets']['arr'] = []
            self._debug['offsets']['arr'].append({'start': self._io.pos()})
            self.offsets[i] = self._io.read_u4le()
            self._debug['offsets']['arr'][i]['end'] = self._io.pos()

        self._debug['offsets']['end'] = self._io.pos()
        self._debug['text']['start'] = self._io.pos()
        self.text = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['text']:
                self._debug['text']['arr'] = []
            self._debug['text']['arr'].append({'start': self._io.pos()})
            self.text[i] = SummoningText.Xorstr(self._io, self, self._root)
            self._debug['text']['arr'][i]['end'] = self._io.pos()

        self._debug['text']['end'] = self._io.pos()

    class Xorstrz(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_term(218, False, True, True)).decode(u"ascii")
            self._debug['text']['end'] = self._io.pos()


    class Xorstr(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self._raw_text = self._io.read_bytes_term(0, False, True, True)
            self.text = KaitaiStream.process_xor_one(self._raw_text, 218)
            self._debug['text']['end'] = self._io.pos()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = self.text
            return self._m_value if hasattr(self, '_m_value') else None



