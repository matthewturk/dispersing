# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningResources(KaitaiStruct):

    class RecordTypes(Enum):
        sprite = 1
        font = 2
        music = 3
        unknown3 = 5
    SEQ_FIELDS = ["count", "offsets", "records"]
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
        self._debug['records']['start'] = self._io.pos()
        self.records = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['records']:
                self._debug['records']['arr'] = []
            self._debug['records']['arr'].append({'start': self._io.pos()})
            self.records[i] = SummoningResources.ResourceRecord(i, self._io, self, self._root)
            self._debug['records']['arr'][i]['end'] = self._io.pos()

        self._debug['records']['end'] = self._io.pos()

    class SpriteHeader(KaitaiStruct):
        SEQ_FIELDS = ["field1", "field2", "width_over_eight", "field_4", "algo", "field_6"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['field1']['start'] = self._io.pos()
            self.field1 = self._io.read_u2le()
            self._debug['field1']['end'] = self._io.pos()
            self._debug['field2']['start'] = self._io.pos()
            self.field2 = self._io.read_u1()
            self._debug['field2']['end'] = self._io.pos()
            self._debug['width_over_eight']['start'] = self._io.pos()
            self.width_over_eight = self._io.read_u1()
            self._debug['width_over_eight']['end'] = self._io.pos()
            self._debug['field_4']['start'] = self._io.pos()
            self.field_4 = self._io.read_u1()
            self._debug['field_4']['end'] = self._io.pos()
            self._debug['algo']['start'] = self._io.pos()
            self.algo = self._io.read_u1()
            self._debug['algo']['end'] = self._io.pos()
            self._debug['field_6']['start'] = self._io.pos()
            self.field_6 = self._io.read_u1()
            self._debug['field_6']['end'] = self._io.pos()

        @property
        def count(self):
            if hasattr(self, '_m_count'):
                return self._m_count if hasattr(self, '_m_count') else None

            self._m_count = (self.field1 if self.field2 > 1 else self.field2)
            return self._m_count if hasattr(self, '_m_count') else None

        @property
        def height(self):
            if hasattr(self, '_m_height'):
                return self._m_height if hasattr(self, '_m_height') else None

            self._m_height = (self.field2 if self.field2 > 1 else self.field1)
            return self._m_height if hasattr(self, '_m_height') else None

        @property
        def width(self):
            if hasattr(self, '_m_width'):
                return self._m_width if hasattr(self, '_m_width') else None

            self._m_width = (self.width_over_eight * 8)
            return self._m_width if hasattr(self, '_m_width') else None


    class ResourceRecord(KaitaiStruct):
        SEQ_FIELDS = ["ehmagic", "type", "header_size", "header", "contents"]
        def __init__(self, i, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.i = i
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ehmagic']['start'] = self._io.pos()
            self.ehmagic = self._io.read_bytes(2)
            self._debug['ehmagic']['end'] = self._io.pos()
            if not self.ehmagic == b"\x45\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x48", self.ehmagic, self._io, u"/types/resource_record/seq/0")
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(SummoningResources.RecordTypes, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['header_size']['start'] = self._io.pos()
            self.header_size = self._io.read_u2le()
            self._debug['header_size']['end'] = self._io.pos()
            self._debug['header']['start'] = self._io.pos()
            _on = self.type
            if _on == SummoningResources.RecordTypes.sprite:
                self.header = SummoningResources.SpriteHeader(self._io, self, self._root)
            elif _on == SummoningResources.RecordTypes.font:
                self.header = SummoningResources.FontHeader(self._io, self, self._root)
            elif _on == SummoningResources.RecordTypes.music:
                self.header = SummoningResources.MusicHeader(self._io, self, self._root)
            else:
                self.header = SummoningResources.GenericHeader(self.header_size, self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            self.contents = self._io.read_bytes((self.record_end - self._root._io.pos()))
            self._debug['contents']['end'] = self._io.pos()

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


    class GenericHeader(KaitaiStruct):
        SEQ_FIELDS = ["contents"]
        def __init__(self, size, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.size = size
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['contents']['start'] = self._io.pos()
            self.contents = self._io.read_bytes(self.size)
            self._debug['contents']['end'] = self._io.pos()


    class MusicHeader(KaitaiStruct):
        SEQ_FIELDS = ["tick_beat", "beat_measure", "total_tick", "data_size", "nr_command", "sound_mode", "pitch_b_range", "basic_tempo", "unknown1", "unknown2", "unknown3", "unknown4", "unknown5", "i_inst_count"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tick_beat']['start'] = self._io.pos()
            self.tick_beat = self._io.read_u1()
            self._debug['tick_beat']['end'] = self._io.pos()
            self._debug['beat_measure']['start'] = self._io.pos()
            self.beat_measure = self._io.read_u1()
            self._debug['beat_measure']['end'] = self._io.pos()
            self._debug['total_tick']['start'] = self._io.pos()
            self.total_tick = self._io.read_s4le()
            self._debug['total_tick']['end'] = self._io.pos()
            self._debug['data_size']['start'] = self._io.pos()
            self.data_size = self._io.read_s4le()
            self._debug['data_size']['end'] = self._io.pos()
            self._debug['nr_command']['start'] = self._io.pos()
            self.nr_command = self._io.read_s4le()
            self._debug['nr_command']['end'] = self._io.pos()
            self._debug['sound_mode']['start'] = self._io.pos()
            self.sound_mode = self._io.read_u1()
            self._debug['sound_mode']['end'] = self._io.pos()
            self._debug['pitch_b_range']['start'] = self._io.pos()
            self.pitch_b_range = self._io.read_u1()
            self._debug['pitch_b_range']['end'] = self._io.pos()
            self._debug['basic_tempo']['start'] = self._io.pos()
            self.basic_tempo = self._io.read_u2le()
            self._debug['basic_tempo']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u1()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u1()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_u1()
            self._debug['unknown3']['end'] = self._io.pos()
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_u1()
            self._debug['unknown4']['end'] = self._io.pos()
            self._debug['unknown5']['start'] = self._io.pos()
            self.unknown5 = self._io.read_u1()
            self._debug['unknown5']['end'] = self._io.pos()
            self._debug['i_inst_count']['start'] = self._io.pos()
            self.i_inst_count = self._io.read_u1()
            self._debug['i_inst_count']['end'] = self._io.pos()


    class FontHeader(KaitaiStruct):
        SEQ_FIELDS = ["clip_info", "font_sprite_header"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['clip_info']['start'] = self._io.pos()
            self.clip_info = self._io.read_bytes(128)
            self._debug['clip_info']['end'] = self._io.pos()
            self._debug['font_sprite_header']['start'] = self._io.pos()
            self.font_sprite_header = SummoningResources.SpriteHeader(self._io, self, self._root)
            self._debug['font_sprite_header']['end'] = self._io.pos()



