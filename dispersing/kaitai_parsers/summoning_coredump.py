# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from dispersing.kaitai_parsers import summoning_datasegment
class SummoningCoredump(KaitaiStruct):
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        pass

    @property
    def ds(self):
        if hasattr(self, '_m_ds'):
            return self._m_ds if hasattr(self, '_m_ds') else None

        _pos = self._io.pos()
        self._io.seek((11243 * 16))
        self._debug['_m_ds']['start'] = self._io.pos()
        self._raw__m_ds = self._io.read_bytes_full()
        _io__raw__m_ds = KaitaiStream(BytesIO(self._raw__m_ds))
        self._m_ds = summoning_datasegment.SummoningDatasegment(_io__raw__m_ds)
        self._debug['_m_ds']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_ds if hasattr(self, '_m_ds') else None


