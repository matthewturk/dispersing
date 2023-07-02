# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningLevels(KaitaiStruct):

    class TileFlags(Enum):
        nothing = 0
        movable_object = 1
        unknown2 = 2
        teleporter_dest = 3
        unknown4 = 4
        unknown5 = 5
        unknown6 = 6
        teleporter = 7
        level_exit = 8
        npc = 9
        unknown10 = 10
        mouth = 11

    class ProcedureOpcode(Enum):
        teleporter_enable = 0
        unknown1 = 1
        unknown2 = 2
        unknown3 = 3
        unknown4 = 4
        unknown5 = 5
        unknown6 = 6
        unknown7 = 7
        unknown8 = 8
        unknown9 = 9
        unknown10 = 10
        create_object = 11
    SEQ_FIELDS = ["file_header", "levels"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_header']['start'] = self._io.pos()
        self.file_header = SummoningLevels.Header(self._io, self, self._root)
        self._debug['file_header']['end'] = self._io.pos()
        self._debug['levels']['start'] = self._io.pos()
        self.levels = [None] * (self.file_header.count)
        for i in range(self.file_header.count):
            if not 'arr' in self._debug['levels']:
                self._debug['levels']['arr'] = []
            self._debug['levels']['arr'].append({'start': self._io.pos()})
            self.levels[i] = SummoningLevels.Level(self._io, self, self._root)
            self._debug['levels']['arr'][i]['end'] = self._io.pos()

        self._debug['levels']['end'] = self._io.pos()

    class PortalInfo(KaitaiStruct):
        SEQ_FIELDS = ["opcode", "level", "dest_x", "dest_y"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opcode']['start'] = self._io.pos()
            self.opcode = self._io.read_u1()
            self._debug['opcode']['end'] = self._io.pos()
            self._debug['level']['start'] = self._io.pos()
            self.level = self._io.read_u1()
            self._debug['level']['end'] = self._io.pos()
            self._debug['dest_x']['start'] = self._io.pos()
            self.dest_x = self._io.read_u1()
            self._debug['dest_x']['end'] = self._io.pos()
            self._debug['dest_y']['start'] = self._io.pos()
            self.dest_y = self._io.read_u1()
            self._debug['dest_y']['end'] = self._io.pos()


    class ProcedureDefs(KaitaiStruct):
        SEQ_FIELDS = ["procedures"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['procedures']['start'] = self._io.pos()
            self.procedures = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['procedures']:
                    self._debug['procedures']['arr'] = []
                self._debug['procedures']['arr'].append({'start': self._io.pos()})
                self.procedures.append(SummoningLevels.ProcedureInfo(self._io, self, self._root))
                self._debug['procedures']['arr'][len(self.procedures) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['procedures']['end'] = self._io.pos()


    class Procedure(KaitaiStruct):
        SEQ_FIELDS = ["opcode", "arg1", "arg2", "arg3", "arg4"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opcode']['start'] = self._io.pos()
            self.opcode = KaitaiStream.resolve_enum(SummoningLevels.ProcedureOpcode, self._io.read_u1())
            self._debug['opcode']['end'] = self._io.pos()
            self._debug['arg1']['start'] = self._io.pos()
            self.arg1 = self._io.read_u1()
            self._debug['arg1']['end'] = self._io.pos()
            self._debug['arg2']['start'] = self._io.pos()
            self.arg2 = self._io.read_u1()
            self._debug['arg2']['end'] = self._io.pos()
            self._debug['arg3']['start'] = self._io.pos()
            self.arg3 = self._io.read_u1()
            self._debug['arg3']['end'] = self._io.pos()
            self._debug['arg4']['start'] = self._io.pos()
            self.arg4 = self._io.read_u1()
            self._debug['arg4']['end'] = self._io.pos()


    class ItemData(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "info"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x']['start'] = self._io.pos()
            self.x = self._io.read_u1()
            self._debug['x']['end'] = self._io.pos()
            self._debug['y']['start'] = self._io.pos()
            self.y = self._io.read_u1()
            self._debug['y']['end'] = self._io.pos()
            if self.x != 255:
                self._debug['info']['start'] = self._io.pos()
                self.info = SummoningLevels.TileInfo(self._io, self, self._root)
                self._debug['info']['end'] = self._io.pos()



    class SpeechStrings(KaitaiStruct):
        SEQ_FIELDS = ["size", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = self._io.read_bytes(self.size)
            self._debug['text']['end'] = self._io.pos()


    class ProcedureInfo(KaitaiStruct):
        SEQ_FIELDS = ["opcode_count", "procedures"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opcode_count']['start'] = self._io.pos()
            self.opcode_count = self._io.read_u1()
            self._debug['opcode_count']['end'] = self._io.pos()
            self._debug['procedures']['start'] = self._io.pos()
            self.procedures = [None] * (self.opcode_count)
            for i in range(self.opcode_count):
                if not 'arr' in self._debug['procedures']:
                    self._debug['procedures']['arr'] = []
                self._debug['procedures']['arr'].append({'start': self._io.pos()})
                self.procedures[i] = SummoningLevels.Procedure(self._io, self, self._root)
                self._debug['procedures']['arr'][i]['end'] = self._io.pos()

            self._debug['procedures']['end'] = self._io.pos()


    class LevelProps(KaitaiStruct):
        SEQ_FIELDS = ["wall_tiles", "floor_tiles", "floor_special_tiles", "gate_tiles", "keys_switches", "door_tiles", "wall_decor1", "wall_decor2", "wall_decor3", "wall_overlay_tiles", "blank11", "unk12", "big_wooden_thing", "big_boulder", "blank15"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['wall_tiles']['start'] = self._io.pos()
            self.wall_tiles = self._io.read_s2le()
            self._debug['wall_tiles']['end'] = self._io.pos()
            self._debug['floor_tiles']['start'] = self._io.pos()
            self.floor_tiles = self._io.read_s2le()
            self._debug['floor_tiles']['end'] = self._io.pos()
            self._debug['floor_special_tiles']['start'] = self._io.pos()
            self.floor_special_tiles = self._io.read_s2le()
            self._debug['floor_special_tiles']['end'] = self._io.pos()
            self._debug['gate_tiles']['start'] = self._io.pos()
            self.gate_tiles = self._io.read_s2le()
            self._debug['gate_tiles']['end'] = self._io.pos()
            self._debug['keys_switches']['start'] = self._io.pos()
            self.keys_switches = self._io.read_s2le()
            self._debug['keys_switches']['end'] = self._io.pos()
            self._debug['door_tiles']['start'] = self._io.pos()
            self.door_tiles = self._io.read_s2le()
            self._debug['door_tiles']['end'] = self._io.pos()
            self._debug['wall_decor1']['start'] = self._io.pos()
            self.wall_decor1 = self._io.read_s2le()
            self._debug['wall_decor1']['end'] = self._io.pos()
            self._debug['wall_decor2']['start'] = self._io.pos()
            self.wall_decor2 = self._io.read_s2le()
            self._debug['wall_decor2']['end'] = self._io.pos()
            self._debug['wall_decor3']['start'] = self._io.pos()
            self.wall_decor3 = self._io.read_s2le()
            self._debug['wall_decor3']['end'] = self._io.pos()
            self._debug['wall_overlay_tiles']['start'] = self._io.pos()
            self.wall_overlay_tiles = self._io.read_s2le()
            self._debug['wall_overlay_tiles']['end'] = self._io.pos()
            self._debug['blank11']['start'] = self._io.pos()
            self.blank11 = self._io.read_bytes(2)
            self._debug['blank11']['end'] = self._io.pos()
            if not self.blank11 == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.blank11, self._io, u"/types/level_props/seq/10")
            self._debug['unk12']['start'] = self._io.pos()
            self.unk12 = self._io.read_s2le()
            self._debug['unk12']['end'] = self._io.pos()
            self._debug['big_wooden_thing']['start'] = self._io.pos()
            self.big_wooden_thing = self._io.read_s2le()
            self._debug['big_wooden_thing']['end'] = self._io.pos()
            self._debug['big_boulder']['start'] = self._io.pos()
            self.big_boulder = self._io.read_s2le()
            self._debug['big_boulder']['end'] = self._io.pos()
            self._debug['blank15']['start'] = self._io.pos()
            self.blank15 = self._io.read_bytes(36)
            self._debug['blank15']['end'] = self._io.pos()
            if not self.blank15 == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.blank15, self._io, u"/types/level_props/seq/14")

        @property
        def wall_corners(self):
            if hasattr(self, '_m_wall_corners'):
                return self._m_wall_corners if hasattr(self, '_m_wall_corners') else None

            self._m_wall_corners = (self.wall_tiles + 1)
            return self._m_wall_corners if hasattr(self, '_m_wall_corners') else None


    class OtherData(KaitaiStruct):
        SEQ_FIELDS = ["size", "contents"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            self._raw_contents = self._io.read_bytes(self.size)
            _io__raw_contents = KaitaiStream(BytesIO(self._raw_contents))
            self.contents = SummoningLevels.ProcedureDefs(_io__raw_contents, self, self._root)
            self._debug['contents']['end'] = self._io.pos()


    class TeleporterInfo(KaitaiStruct):
        SEQ_FIELDS = ["unknown"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(5)
            self._debug['unknown']['end'] = self._io.pos()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["count", "offsets"]
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


    class TileInfo(KaitaiStruct):
        SEQ_FIELDS = ["n1", "items", "wall_flags", "wall_args", "floor_flags", "floor_args"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['n1']['start'] = self._io.pos()
            self.n1 = self._io.read_u1()
            self._debug['n1']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self.items = [None] * (self.n1)
            for i in range(self.n1):
                if not 'arr' in self._debug['items']:
                    self._debug['items']['arr'] = []
                self._debug['items']['arr'].append({'start': self._io.pos()})
                self.items[i] = self._io.read_u1()
                self._debug['items']['arr'][i]['end'] = self._io.pos()

            self._debug['items']['end'] = self._io.pos()
            self._debug['wall_flags']['start'] = self._io.pos()
            self.wall_flags = KaitaiStream.resolve_enum(SummoningLevels.TileFlags, self._io.read_u1())
            self._debug['wall_flags']['end'] = self._io.pos()
            if  ((self.wall_flags != SummoningLevels.TileFlags.nothing) and (self.wall_flags != SummoningLevels.TileFlags.movable_object)) :
                self._debug['wall_args']['start'] = self._io.pos()
                _on = self.wall_flags
                if _on == SummoningLevels.TileFlags.teleporter:
                    self.wall_args = SummoningLevels.TeleporterInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.unknown4:
                    self.wall_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.movable_object:
                    self.wall_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown6:
                    self.wall_args = self._io.read_u2le()
                elif _on == SummoningLevels.TileFlags.mouth:
                    self.wall_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown10:
                    self.wall_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.level_exit:
                    self.wall_args = SummoningLevels.PortalInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.unknown2:
                    self.wall_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown5:
                    self.wall_args = SummoningLevels.PortalInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.npc:
                    self.wall_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.teleporter_dest:
                    self.wall_args = SummoningLevels.TeleporterInfo(self._io, self, self._root)
                self._debug['wall_args']['end'] = self._io.pos()

            self._debug['floor_flags']['start'] = self._io.pos()
            self.floor_flags = KaitaiStream.resolve_enum(SummoningLevels.TileFlags, self._io.read_u1())
            self._debug['floor_flags']['end'] = self._io.pos()
            if self.floor_flags != SummoningLevels.TileFlags.nothing:
                self._debug['floor_args']['start'] = self._io.pos()
                _on = self.floor_flags
                if _on == SummoningLevels.TileFlags.teleporter:
                    self.floor_args = SummoningLevels.TeleporterInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.unknown4:
                    self.floor_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.movable_object:
                    self.floor_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown6:
                    self.floor_args = self._io.read_u2le()
                elif _on == SummoningLevels.TileFlags.mouth:
                    self.floor_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown10:
                    self.floor_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.level_exit:
                    self.floor_args = SummoningLevels.PortalInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.unknown2:
                    self.floor_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown5:
                    self.floor_args = SummoningLevels.PortalInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.npc:
                    self.floor_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.teleporter_dest:
                    self.floor_args = SummoningLevels.TeleporterInfo(self._io, self, self._root)
                self._debug['floor_args']['end'] = self._io.pos()



    class Level(KaitaiStruct):
        SEQ_FIELDS = ["height", "width", "properties", "map", "items", "speech", "other"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u1()
            self._debug['height']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u1()
            self._debug['width']['end'] = self._io.pos()
            self._debug['properties']['start'] = self._io.pos()
            self.properties = SummoningLevels.LevelProps(self._io, self, self._root)
            self._debug['properties']['end'] = self._io.pos()
            self._debug['map']['start'] = self._io.pos()
            self.map = self._io.read_bytes((self.width * self.height))
            self._debug['map']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self.items = []
            i = 0
            while True:
                if not 'arr' in self._debug['items']:
                    self._debug['items']['arr'] = []
                self._debug['items']['arr'].append({'start': self._io.pos()})
                _ = SummoningLevels.ItemData(self._io, self, self._root)
                self.items.append(_)
                self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                if  ((_.x == 255) and (_.y == 255)) :
                    break
                i += 1
            self._debug['items']['end'] = self._io.pos()
            self._debug['speech']['start'] = self._io.pos()
            self.speech = SummoningLevels.SpeechStrings(self._io, self, self._root)
            self._debug['speech']['end'] = self._io.pos()
            self._debug['other']['start'] = self._io.pos()
            self.other = SummoningLevels.OtherData(self._io, self, self._root)
            self._debug['other']['end'] = self._io.pos()



