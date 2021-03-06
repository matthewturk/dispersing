# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningResources(KaitaiStruct):

    class RecordTypes(Enum):
        sprite = 1
        unknown2 = 2
        music = 3
        unknown3 = 5
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

        self.records = [None] * (self.count)
        for i in range(self.count):
            self.records[i] = SummoningResources.ResourceRecord(i, self._io, self, self._root)


    class ResourceRecord(KaitaiStruct):
        def __init__(self, i, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.i = i
            self._read()

        def _read(self):
            self.ehmagic = self._io.read_bytes(2)
            if not self.ehmagic == b"\x45\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x48", self.ehmagic, self._io, u"/types/resource_record/seq/0")
            self.type = KaitaiStream.resolve_enum(SummoningResources.RecordTypes, self._io.read_u1())
            self.header_size = self._io.read_u2le()
            _on = self.type
            if _on == SummoningResources.RecordTypes.sprite:
                self.header = SummoningResources.SpriteHeader(self._io, self, self._root)
            elif _on == SummoningResources.RecordTypes.music:
                self.header = SummoningResources.MusicHeader(self._io, self, self._root)
            else:
                self.header = SummoningResources.GenericHeader(self.header_size, self._io, self, self._root)
            self.contents = self._io.read_bytes((self.record_end - self._root._io.pos()))

        @property
        def record_start(self):
            if hasattr(self, '_m_record_start'):
                return self._m_record_start if hasattr(self, '_m_record_start') else None

            self._m_record_start = self._parent.offsets[self.i]
            return self._m_record_start if hasattr(self, '_m_record_start') else None

        @property
        def record_end(self):
            if hasattr(self, '_m_record_end'):
                return self._m_record_end if hasattr(self, '_m_record_end') else None

            self._m_record_end = (self._parent.offsets[(self.i + 1)] if self.i < (self._parent.count - 1) else self._root._io.size())
            return self._m_record_end if hasattr(self, '_m_record_end') else None


    class SpriteHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.height = self._io.read_u2le()
            self.count = self._io.read_u1()
            self.width_over_eight = self._io.read_u1()
            self.field_4 = self._io.read_u1()
            self.algo = self._io.read_u1()
            self.field_6 = self._io.read_u1()

        @property
        def width(self):
            if hasattr(self, '_m_width'):
                return self._m_width if hasattr(self, '_m_width') else None

            self._m_width = (self.width_over_eight * 8)
            return self._m_width if hasattr(self, '_m_width') else None


    class MusicHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tick_beat = self._io.read_u1()
            self.beat_measure = self._io.read_u1()
            self.total_tick = self._io.read_s4le()
            self.data_size = self._io.read_s4le()
            self.nr_command = self._io.read_s4le()
            self.sound_mode = self._io.read_u1()
            self.pitch_b_range = self._io.read_u1()
            self.basic_tempo = self._io.read_u2le()
            self.unknown1 = self._io.read_u1()
            self.unknown2 = self._io.read_u1()
            self.unknown3 = self._io.read_u1()
            self.unknown4 = self._io.read_u1()
            self.unknown5 = self._io.read_u1()
            self.i_inst_count = self._io.read_u1()


    class GenericHeader(KaitaiStruct):
        def __init__(self, size, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.size = size
            self._read()

        def _read(self):
            self.contents = self._io.read_bytes(self.size)



