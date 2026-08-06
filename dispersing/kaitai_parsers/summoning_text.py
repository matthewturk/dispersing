# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningText(KaitaiStruct):
    SEQ_FIELDS = ["count", "offsets", "text"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningText, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['count']['start'] = self._io.pos()
        self.count = self._io.read_u4le()
        self._debug['count']['end'] = self._io.pos()
        self._debug['offsets']['start'] = self._io.pos()
        self._debug['offsets']['arr'] = []
        self.offsets = []
        for i in range(self.count):
            self._debug['offsets']['arr'].append({'start': self._io.pos()})
            self.offsets.append(self._io.read_u4le())
            self._debug['offsets']['arr'][i]['end'] = self._io.pos()

        self._debug['offsets']['end'] = self._io.pos()
        self._debug['text']['start'] = self._io.pos()
        self._debug['text']['arr'] = []
        self.text = []
        for i in range(self.count):
            self._debug['text']['arr'].append({'start': self._io.pos()})
            self.text.append(SummoningText.Xorstr(self._io, self, self._root))
            self._debug['text']['arr'][i]['end'] = self._io.pos()

        self._debug['text']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.offsets)):
            pass

        for i in range(len(self.text)):
            pass
            self.text[i]._fetch_instances()


    class Xorstr(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningText.Xorstr, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self._raw_text = self._io.read_bytes_term(0, False, True, True)
            self.text = KaitaiStream.process_xor_one(self._raw_text, 218)
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.text
            return getattr(self, '_m_value', None)


    class Xorstrz(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningText.Xorstrz, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_term(218, False, True, True)).decode(u"ASCII")
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



