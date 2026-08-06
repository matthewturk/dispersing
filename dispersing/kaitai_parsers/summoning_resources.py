# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningResources(KaitaiStruct):

    class RecordTypes(IntEnum):
        sprite = 1
        font = 2
        music = 3
        unknown3 = 5
    SEQ_FIELDS = ["count", "offsets", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningResources, self).__init__(_io)
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
        self._debug['records']['start'] = self._io.pos()
        self._debug['records']['arr'] = []
        self.records = []
        for i in range(self.count):
            self._debug['records']['arr'].append({'start': self._io.pos()})
            self.records.append(SummoningResources.ResourceRecord(i, self._io, self, self._root))
            self._debug['records']['arr'][i]['end'] = self._io.pos()

        self._debug['records']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.offsets)):
            pass

        for i in range(len(self.records)):
            pass
            self.records[i]._fetch_instances()


    class ChannelPressureEvent(KaitaiStruct):
        SEQ_FIELDS = ["pressure"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.ChannelPressureEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['pressure']['start'] = self._io.pos()
            self.pressure = self._io.read_u1()
            self._debug['pressure']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ControllerEvent(KaitaiStruct):
        SEQ_FIELDS = ["controller", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.ControllerEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['controller']['start'] = self._io.pos()
            self.controller = self._io.read_u1()
            self._debug['controller']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u1()
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Empty(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.Empty, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class FontHeader(KaitaiStruct):
        SEQ_FIELDS = ["clip_info", "font_sprite_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.FontHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['clip_info']['start'] = self._io.pos()
            self.clip_info = self._io.read_bytes(128)
            self._debug['clip_info']['end'] = self._io.pos()
            self._debug['font_sprite_header']['start'] = self._io.pos()
            self.font_sprite_header = SummoningResources.SpriteHeader(self._io, self, self._root)
            self._debug['font_sprite_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.font_sprite_header._fetch_instances()


    class GenericHeader(KaitaiStruct):
        SEQ_FIELDS = ["contents"]
        def __init__(self, size, _io, _parent=None, _root=None):
            super(SummoningResources.GenericHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.size = size
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['contents']['start'] = self._io.pos()
            self.contents = self._io.read_bytes(self.size)
            self._debug['contents']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InstrumentParameters(KaitaiStruct):
        SEQ_FIELDS = ["opl_modulator", "opl_carrier", "i_mod_wave_sel", "i_car_wave_sel", "extra"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.InstrumentParameters, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opl_modulator']['start'] = self._io.pos()
            self.opl_modulator = SummoningResources.SndOplregs(self._io, self, self._root)
            self._debug['opl_modulator']['end'] = self._io.pos()
            self._debug['opl_carrier']['start'] = self._io.pos()
            self.opl_carrier = SummoningResources.SndOplregs(self._io, self, self._root)
            self._debug['opl_carrier']['end'] = self._io.pos()
            self._debug['i_mod_wave_sel']['start'] = self._io.pos()
            self.i_mod_wave_sel = self._io.read_u2le()
            self._debug['i_mod_wave_sel']['end'] = self._io.pos()
            self._debug['i_car_wave_sel']['start'] = self._io.pos()
            self.i_car_wave_sel = self._io.read_u2le()
            self._debug['i_car_wave_sel']['end'] = self._io.pos()
            self._debug['extra']['start'] = self._io.pos()
            self.extra = self._io.read_u2le()
            self._debug['extra']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.opl_modulator._fetch_instances()
            self.opl_carrier._fetch_instances()


    class MusicContents(KaitaiStruct):
        SEQ_FIELDS = ["instruments", "music_commands"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.MusicContents, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instruments']['start'] = self._io.pos()
            self._debug['instruments']['arr'] = []
            self.instruments = []
            for i in range(self._parent.header.i_inst_count):
                self._debug['instruments']['arr'].append({'start': self._io.pos()})
                self.instruments.append(SummoningResources.InstrumentParameters(self._io, self, self._root))
                self._debug['instruments']['arr'][i]['end'] = self._io.pos()

            self._debug['instruments']['end'] = self._io.pos()
            self._debug['music_commands']['start'] = self._io.pos()
            self._debug['music_commands']['arr'] = []
            self.music_commands = []
            i = 0
            while not self._io.is_eof():
                self._debug['music_commands']['arr'].append({'start': self._io.pos()})
                self.music_commands.append(SummoningResources.TrackEvent(i, self._io, self, self._root))
                self._debug['music_commands']['arr'][len(self.music_commands) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['music_commands']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.instruments)):
                pass
                self.instruments[i]._fetch_instances()

            for i in range(len(self.music_commands)):
                pass
                self.music_commands[i]._fetch_instances()

            _ = self.contents
            if hasattr(self, '_m_contents'):
                pass


        @property
        def contents(self):
            if hasattr(self, '_m_contents'):
                return self._m_contents

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_contents']['start'] = self._io.pos()
            self._m_contents = self._io.read_bytes_full()
            self._debug['_m_contents']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_contents', None)


    class MusicHeader(KaitaiStruct):
        SEQ_FIELDS = ["tick_beat", "beat_measure", "total_tick", "data_size", "nr_command", "sound_mode", "pitch_b_range", "basic_tempo", "unknown1", "unknown2", "unknown3", "unknown4", "unknown5", "i_inst_count"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.MusicHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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


        def _fetch_instances(self):
            pass


    class NoteOffEvent(KaitaiStruct):
        SEQ_FIELDS = ["note", "volume"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.NoteOffEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['note']['start'] = self._io.pos()
            self.note = self._io.read_u1()
            self._debug['note']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u1()
            self._debug['volume']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class NoteOnEvent(KaitaiStruct):
        SEQ_FIELDS = ["note", "volume"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.NoteOnEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['note']['start'] = self._io.pos()
            self.note = self._io.read_u1()
            self._debug['note']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u1()
            self._debug['volume']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class OverflowTime(KaitaiStruct):
        SEQ_FIELDS = ["groups"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.OverflowTime, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['groups']['start'] = self._io.pos()
            self._debug['groups']['arr'] = []
            self.groups = []
            i = 0
            while True:
                self._debug['groups']['arr'].append({'start': self._io.pos()})
                _ = self._io.read_u1()
                self.groups.append(_)
                self._debug['groups']['arr'][len(self.groups) - 1]['end'] = self._io.pos()
                if _ != 248:
                    break
                i += 1
            self._debug['groups']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.groups)):
                pass


        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = (len(self.groups) - 1) * 240 + self.groups[-1]
            return getattr(self, '_m_value', None)


    class PitchBendEvent(KaitaiStruct):
        SEQ_FIELDS = ["b1", "b2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.PitchBendEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['b1']['start'] = self._io.pos()
            self.b1 = self._io.read_u1()
            self._debug['b1']['end'] = self._io.pos()
            self._debug['b2']['start'] = self._io.pos()
            self.b2 = self._io.read_u1()
            self._debug['b2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def adj_bend_value(self):
            if hasattr(self, '_m_adj_bend_value'):
                return self._m_adj_bend_value

            self._m_adj_bend_value = self.bend_value - 16384
            return getattr(self, '_m_adj_bend_value', None)

        @property
        def bend_value(self):
            if hasattr(self, '_m_bend_value'):
                return self._m_bend_value

            self._m_bend_value = ((self.b2 << 7) + self.b1) - 16384
            return getattr(self, '_m_bend_value', None)


    class PolyphonicPressureEvent(KaitaiStruct):
        SEQ_FIELDS = ["volume"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.PolyphonicPressureEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u1()
            self._debug['volume']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ProgramChangeEvent(KaitaiStruct):
        SEQ_FIELDS = ["program"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.ProgramChangeEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['program']['start'] = self._io.pos()
            self.program = self._io.read_u1()
            self._debug['program']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ResourceRecord(KaitaiStruct):
        SEQ_FIELDS = ["ehmagic", "type", "header_size", "header", "contents"]
        def __init__(self, i, _io, _parent=None, _root=None):
            super(SummoningResources.ResourceRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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
            if _on == SummoningResources.RecordTypes.font:
                pass
                self.header = SummoningResources.FontHeader(self._io, self, self._root)
            elif _on == SummoningResources.RecordTypes.music:
                pass
                self.header = SummoningResources.MusicHeader(self._io, self, self._root)
            elif _on == SummoningResources.RecordTypes.sprite:
                pass
                self.header = SummoningResources.SpriteHeader(self._io, self, self._root)
            else:
                pass
                self.header = SummoningResources.GenericHeader(self.header_size, self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            _on = self.type
            if _on == SummoningResources.RecordTypes.music:
                pass
                self._raw_contents = self._io.read_bytes(self.record_end - self._root._io.pos())
                _io__raw_contents = KaitaiStream(BytesIO(self._raw_contents))
                self.contents = SummoningResources.MusicContents(_io__raw_contents, self, self._root)
            else:
                pass
                self.contents = self._io.read_bytes(self.record_end - self._root._io.pos())
            self._debug['contents']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == SummoningResources.RecordTypes.font:
                pass
                self.header._fetch_instances()
            elif _on == SummoningResources.RecordTypes.music:
                pass
                self.header._fetch_instances()
            elif _on == SummoningResources.RecordTypes.sprite:
                pass
                self.header._fetch_instances()
            else:
                pass
                self.header._fetch_instances()
            _on = self.type
            if _on == SummoningResources.RecordTypes.music:
                pass
                self.contents._fetch_instances()
            else:
                pass

        @property
        def record_end(self):
            if hasattr(self, '_m_record_end'):
                return self._m_record_end

            self._m_record_end = (self._parent.offsets[self.i + 1] if self.i < self._parent.count - 1 else self._root._io.size())
            return getattr(self, '_m_record_end', None)

        @property
        def record_start(self):
            if hasattr(self, '_m_record_start'):
                return self._m_record_start

            self._m_record_start = self._parent.offsets[self.i]
            return getattr(self, '_m_record_start', None)


    class SndOplregs(KaitaiStruct):
        SEQ_FIELDS = ["ksl", "multiple", "feedback", "attack", "sustain", "eg", "decay", "release_rate", "total_level", "am", "vib", "ksr", "con"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.SndOplregs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ksl']['start'] = self._io.pos()
            self.ksl = self._io.read_u2le()
            self._debug['ksl']['end'] = self._io.pos()
            self._debug['multiple']['start'] = self._io.pos()
            self.multiple = self._io.read_u2le()
            self._debug['multiple']['end'] = self._io.pos()
            self._debug['feedback']['start'] = self._io.pos()
            self.feedback = self._io.read_u2le()
            self._debug['feedback']['end'] = self._io.pos()
            self._debug['attack']['start'] = self._io.pos()
            self.attack = self._io.read_u2le()
            self._debug['attack']['end'] = self._io.pos()
            self._debug['sustain']['start'] = self._io.pos()
            self.sustain = self._io.read_u2le()
            self._debug['sustain']['end'] = self._io.pos()
            self._debug['eg']['start'] = self._io.pos()
            self.eg = self._io.read_u2le()
            self._debug['eg']['end'] = self._io.pos()
            self._debug['decay']['start'] = self._io.pos()
            self.decay = self._io.read_u2le()
            self._debug['decay']['end'] = self._io.pos()
            self._debug['release_rate']['start'] = self._io.pos()
            self.release_rate = self._io.read_u2le()
            self._debug['release_rate']['end'] = self._io.pos()
            self._debug['total_level']['start'] = self._io.pos()
            self.total_level = self._io.read_u2le()
            self._debug['total_level']['end'] = self._io.pos()
            self._debug['am']['start'] = self._io.pos()
            self.am = self._io.read_u2le()
            self._debug['am']['end'] = self._io.pos()
            self._debug['vib']['start'] = self._io.pos()
            self.vib = self._io.read_u2le()
            self._debug['vib']['end'] = self._io.pos()
            self._debug['ksr']['start'] = self._io.pos()
            self.ksr = self._io.read_u2le()
            self._debug['ksr']['end'] = self._io.pos()
            self._debug['con']['start'] = self._io.pos()
            self.con = self._io.read_u2le()
            self._debug['con']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SpriteHeader(KaitaiStruct):
        SEQ_FIELDS = ["field1", "field2", "width_over_eight", "field_4", "algo", "field_6"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.SpriteHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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


        def _fetch_instances(self):
            pass

        @property
        def count(self):
            if hasattr(self, '_m_count'):
                return self._m_count

            self._m_count = (self.field1 if self.field2 > 1 else self.field2)
            return getattr(self, '_m_count', None)

        @property
        def height(self):
            if hasattr(self, '_m_height'):
                return self._m_height

            self._m_height = (self.field2 if self.field2 > 1 else self.field1)
            return getattr(self, '_m_height', None)

        @property
        def width(self):
            if hasattr(self, '_m_width'):
                return self._m_width

            self._m_width = self.width_over_eight * 8
            return getattr(self, '_m_width', None)


    class StopEvent(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.StopEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class SystemEvent(KaitaiStruct):
        SEQ_FIELDS = ["event_body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.SystemEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['event_body']['start'] = self._io.pos()
            _on = self._parent.channel
            if _on == 0:
                pass
                self.event_body = SummoningResources.TempoMultiplierEvent(self._io, self, self._root)
            elif _on == 12:
                pass
                self.event_body = SummoningResources.StopEvent(self._io, self, self._root)
            self._debug['event_body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self._parent.channel
            if _on == 0:
                pass
                self.event_body._fetch_instances()
            elif _on == 12:
                pass
                self.event_body._fetch_instances()


    class TempoMultiplierEvent(KaitaiStruct):
        SEQ_FIELDS = ["event_start", "integer_part", "fractional_part", "event_end"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningResources.TempoMultiplierEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['event_start']['start'] = self._io.pos()
            self.event_start = self._io.read_bytes(2)
            self._debug['event_start']['end'] = self._io.pos()
            if not self.event_start == b"\x7F\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x7F\x00", self.event_start, self._io, u"/types/tempo_multiplier_event/seq/0")
            self._debug['integer_part']['start'] = self._io.pos()
            self.integer_part = self._io.read_u1()
            self._debug['integer_part']['end'] = self._io.pos()
            self._debug['fractional_part']['start'] = self._io.pos()
            self.fractional_part = self._io.read_u1()
            self._debug['fractional_part']['end'] = self._io.pos()
            self._debug['event_end']['start'] = self._io.pos()
            self.event_end = self._io.read_bytes(1)
            self._debug['event_end']['end'] = self._io.pos()
            if not self.event_end == b"\xF7":
                raise kaitaistruct.ValidationNotEqualError(b"\xF7", self.event_end, self._io, u"/types/tempo_multiplier_event/seq/3")


        def _fetch_instances(self):
            pass


    class TrackEvent(KaitaiStruct):
        SEQ_FIELDS = ["v_time", "event_header", "event_body"]
        def __init__(self, i, _io, _parent=None, _root=None):
            super(SummoningResources.TrackEvent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['v_time']['start'] = self._io.pos()
            self.v_time = SummoningResources.OverflowTime(self._io, self, self._root)
            self._debug['v_time']['end'] = self._io.pos()
            if self.first_byte > 127:
                pass
                self._debug['event_header']['start'] = self._io.pos()
                self.event_header = self._io.read_u1()
                self._debug['event_header']['end'] = self._io.pos()

            self._debug['event_body']['start'] = self._io.pos()
            _on = self.event_type
            if _on == 128:
                pass
                self.event_body = SummoningResources.NoteOffEvent(self._io, self, self._root)
            elif _on == 144:
                pass
                self.event_body = SummoningResources.NoteOnEvent(self._io, self, self._root)
            elif _on == 160:
                pass
                self.event_body = SummoningResources.PolyphonicPressureEvent(self._io, self, self._root)
            elif _on == 176:
                pass
                self.event_body = SummoningResources.ControllerEvent(self._io, self, self._root)
            elif _on == 192:
                pass
                self.event_body = SummoningResources.ProgramChangeEvent(self._io, self, self._root)
            elif _on == 208:
                pass
                self.event_body = SummoningResources.ChannelPressureEvent(self._io, self, self._root)
            elif _on == 224:
                pass
                self.event_body = SummoningResources.PitchBendEvent(self._io, self, self._root)
            elif _on == 240:
                pass
                self.event_body = SummoningResources.SystemEvent(self._io, self, self._root)
            self._debug['event_body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.v_time._fetch_instances()
            if self.first_byte > 127:
                pass

            _on = self.event_type
            if _on == 128:
                pass
                self.event_body._fetch_instances()
            elif _on == 144:
                pass
                self.event_body._fetch_instances()
            elif _on == 160:
                pass
                self.event_body._fetch_instances()
            elif _on == 176:
                pass
                self.event_body._fetch_instances()
            elif _on == 192:
                pass
                self.event_body._fetch_instances()
            elif _on == 208:
                pass
                self.event_body._fetch_instances()
            elif _on == 224:
                pass
                self.event_body._fetch_instances()
            elif _on == 240:
                pass
                self.event_body._fetch_instances()
            _ = self.first_byte
            if hasattr(self, '_m_first_byte'):
                pass


        @property
        def channel(self):
            if hasattr(self, '_m_channel'):
                return self._m_channel

            self._m_channel = (self.first_byte & 15 if self.first_byte > 127 else self._parent.music_commands[self.i - 1].channel)
            return getattr(self, '_m_channel', None)

        @property
        def event_type(self):
            if hasattr(self, '_m_event_type'):
                return self._m_event_type

            self._m_event_type = (self.first_byte & 240 if self.first_byte > 127 else self._parent.music_commands[self.i - 1].event_type)
            return getattr(self, '_m_event_type', None)

        @property
        def first_byte(self):
            if hasattr(self, '_m_first_byte'):
                return self._m_first_byte

            _pos = self._io.pos()
            self._io.seek(self._io.pos())
            self._debug['_m_first_byte']['start'] = self._io.pos()
            self._m_first_byte = self._io.read_u1()
            self._debug['_m_first_byte']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_first_byte', None)



