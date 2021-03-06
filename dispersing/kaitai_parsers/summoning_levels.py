# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


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
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_header = SummoningLevels.Header(self._io, self, self._root)
        self.levels = [None] * (self.file_header.count)
        for i in range(self.file_header.count):
            self.levels[i] = SummoningLevels.Level(self._io, self, self._root)


    class PortalInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.opcode = self._io.read_u1()
            self.level = self._io.read_u1()
            self.dest_x = self._io.read_u1()
            self.dest_y = self._io.read_u1()


    class ItemData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()
            if self.x != 255:
                self.info = SummoningLevels.TileInfo(self._io, self, self._root)



    class SpeechStrings(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u2le()
            self.text = self._io.read_bytes(self.size)


    class LevelProps(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.internal_wall_edges = self._io.read_s2le()
            self.floor = self._io.read_s2le()
            self.floor_special_tile = self._io.read_s2le()
            self.wall_edges = self._io.read_s2le()
            self.keys_switches = self._io.read_s2le()
            self.door = self._io.read_s2le()
            self.unk7 = self._io.read_s2le()
            self.unk8 = self._io.read_s2le()
            self.unk9 = self._io.read_s2le()
            self.wall_overlay_tiles = self._io.read_s2le()
            self.blank11 = self._io.read_bytes(2)
            if not self.blank11 == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.blank11, self._io, u"/types/level_props/seq/10")
            self.unk12 = self._io.read_s2le()
            self.big_wooden_thing = self._io.read_s2le()
            self.big_boulder = self._io.read_s2le()
            self.blank15 = self._io.read_bytes(36)
            if not self.blank15 == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.blank15, self._io, u"/types/level_props/seq/14")


    class OtherData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.size = self._io.read_u2le()
            self.contents = [None] * (self.size)
            for i in range(self.size):
                self.contents[i] = self._io.read_u1()



    class TeleporterInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes(5)


    class Header(KaitaiStruct):
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



    class TileInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.n1 = self._io.read_u1()
            self.items = [None] * (self.n1)
            for i in range(self.n1):
                self.items[i] = self._io.read_u1()

            self.floor_flags = KaitaiStream.resolve_enum(SummoningLevels.TileFlags, self._io.read_u1())
            if  ((self.floor_flags != SummoningLevels.TileFlags.nothing) and (self.floor_flags != SummoningLevels.TileFlags.movable_object)) :
                _on = self.floor_flags
                if _on == SummoningLevels.TileFlags.teleporter:
                    self.tile_args = SummoningLevels.TeleporterInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.unknown4:
                    self.tile_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.movable_object:
                    self.tile_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown6:
                    self.tile_args = self._io.read_u2le()
                elif _on == SummoningLevels.TileFlags.mouth:
                    self.tile_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown10:
                    self.tile_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.level_exit:
                    self.tile_args = SummoningLevels.PortalInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.unknown2:
                    self.tile_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.unknown5:
                    self.tile_args = SummoningLevels.PortalInfo(self._io, self, self._root)
                elif _on == SummoningLevels.TileFlags.npc:
                    self.tile_args = self._io.read_u1()
                elif _on == SummoningLevels.TileFlags.teleporter_dest:
                    self.tile_args = SummoningLevels.TeleporterInfo(self._io, self, self._root)

            self.wall_flags = KaitaiStream.resolve_enum(SummoningLevels.TileFlags, self._io.read_u1())
            if self.wall_flags != SummoningLevels.TileFlags.nothing:
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



    class Level(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.height = self._io.read_u1()
            self.width = self._io.read_u1()
            self.properties = SummoningLevels.LevelProps(self._io, self, self._root)
            self.map = self._io.read_bytes((self.width * self.height))
            self.items = []
            i = 0
            while True:
                _ = SummoningLevels.ItemData(self._io, self, self._root)
                self.items.append(_)
                if  ((_.x == 255) and (_.y == 255)) :
                    break
                i += 1
            self.speech = SummoningLevels.SpeechStrings(self._io, self, self._root)
            self.other = SummoningLevels.OtherData(self._io, self, self._root)



