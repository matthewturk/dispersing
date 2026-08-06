# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class VeilRooms(KaitaiStruct):

    class TileFlags(IntEnum):
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
    SEQ_FIELDS = ["file_header", "levels"]
    def __init__(self, _io, _parent=None, _root=None):
        super(VeilRooms, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_header']['start'] = self._io.pos()
        self.file_header = VeilRooms.Header(self._io, self, self._root)
        self._debug['file_header']['end'] = self._io.pos()
        self._debug['levels']['start'] = self._io.pos()
        self._debug['levels']['arr'] = []
        self.levels = []
        for i in range(self.file_header.count):
            self._debug['levels']['arr'].append({'start': self._io.pos()})
            self.levels.append(VeilRooms.Level(self._io, self, self._root))
            self._debug['levels']['arr'][i]['end'] = self._io.pos()

        self._debug['levels']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.file_header._fetch_instances()
        for i in range(len(self.levels)):
            pass
            self.levels[i]._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["count", "offsets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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


        def _fetch_instances(self):
            pass
            for i in range(len(self.offsets)):
                pass



    class ItemData(KaitaiStruct):
        SEQ_FIELDS = ["x", "y", "info"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.ItemData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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
                pass
                self._debug['info']['start'] = self._io.pos()
                self.info = VeilRooms.TileInfo(self._io, self, self._root)
                self._debug['info']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.x != 255:
                pass
                self.info._fetch_instances()



    class Level(KaitaiStruct):
        SEQ_FIELDS = ["ehmagic", "unknown", "height", "width", "vals", "map", "items", "speech", "other"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.Level, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ehmagic']['start'] = self._io.pos()
            self.ehmagic = self._io.read_bytes(2)
            self._debug['ehmagic']['end'] = self._io.pos()
            if not self.ehmagic == b"\x45\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x48", self.ehmagic, self._io, u"/types/level/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_u1()
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['vals']['start'] = self._io.pos()
            self._debug['vals']['arr'] = []
            self.vals = []
            for i in range(32):
                self._debug['vals']['arr'].append({'start': self._io.pos()})
                self.vals.append(self._io.read_s2le())
                self._debug['vals']['arr'][i]['end'] = self._io.pos()

            self._debug['vals']['end'] = self._io.pos()
            self._debug['map']['start'] = self._io.pos()
            self.map = self._io.read_bytes(self.width * self.height)
            self._debug['map']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self._debug['items']['arr'] = []
            self.items = []
            i = 0
            while True:
                self._debug['items']['arr'].append({'start': self._io.pos()})
                _ = VeilRooms.ItemData(self._io, self, self._root)
                self.items.append(_)
                self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                if  ((_.x == 255) and (_.y == 255)) :
                    break
                i += 1
            self._debug['items']['end'] = self._io.pos()
            self._debug['speech']['start'] = self._io.pos()
            self.speech = VeilRooms.SpeechStrings(self._io, self, self._root)
            self._debug['speech']['end'] = self._io.pos()
            self._debug['other']['start'] = self._io.pos()
            self.other = VeilRooms.OtherData(self._io, self, self._root)
            self._debug['other']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.vals)):
                pass

            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()

            self.speech._fetch_instances()
            self.other._fetch_instances()


    class OtherData(KaitaiStruct):
        SEQ_FIELDS = ["size", "contents"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.OtherData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            self._debug['contents']['arr'] = []
            self.contents = []
            for i in range(self.size):
                self._debug['contents']['arr'].append({'start': self._io.pos()})
                self.contents.append(self._io.read_u1())
                self._debug['contents']['arr'][i]['end'] = self._io.pos()

            self._debug['contents']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.contents)):
                pass



    class PortalInfo(KaitaiStruct):
        SEQ_FIELDS = ["opcode", "level", "dest_x", "dest_y"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.PortalInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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


        def _fetch_instances(self):
            pass


    class SpeechStrings(KaitaiStruct):
        SEQ_FIELDS = ["size", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.SpeechStrings, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2be()
            self._debug['size']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = self._io.read_bytes(self.size)
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TeleporterInfo(KaitaiStruct):
        SEQ_FIELDS = ["unknown"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.TeleporterInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(5)
            self._debug['unknown']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TileInfo(KaitaiStruct):
        SEQ_FIELDS = ["n1", "items", "floor_flags", "tile_args", "wall_flags", "wall_args"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VeilRooms.TileInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['n1']['start'] = self._io.pos()
            self.n1 = self._io.read_u1()
            self._debug['n1']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self._debug['items']['arr'] = []
            self.items = []
            for i in range(self.n1):
                self._debug['items']['arr'].append({'start': self._io.pos()})
                self.items.append(self._io.read_u1())
                self._debug['items']['arr'][i]['end'] = self._io.pos()

            self._debug['items']['end'] = self._io.pos()
            self._debug['floor_flags']['start'] = self._io.pos()
            self.floor_flags = KaitaiStream.resolve_enum(VeilRooms.TileFlags, self._io.read_u1())
            self._debug['floor_flags']['end'] = self._io.pos()
            if  ((self.floor_flags != VeilRooms.TileFlags.nothing) and (self.floor_flags != VeilRooms.TileFlags.movable_object)) :
                pass
                self._debug['tile_args']['start'] = self._io.pos()
                _on = self.floor_flags
                if _on == VeilRooms.TileFlags.level_exit:
                    pass
                    self.tile_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.mouth:
                    pass
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.movable_object:
                    pass
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.npc:
                    pass
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.teleporter:
                    pass
                    self.tile_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.teleporter_dest:
                    pass
                    self.tile_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown10:
                    pass
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown2:
                    pass
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown4:
                    pass
                    self.tile_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown5:
                    pass
                    self.tile_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown6:
                    pass
                    self.tile_args = self._io.read_u2le()
                self._debug['tile_args']['end'] = self._io.pos()

            self._debug['wall_flags']['start'] = self._io.pos()
            self.wall_flags = KaitaiStream.resolve_enum(VeilRooms.TileFlags, self._io.read_u1())
            self._debug['wall_flags']['end'] = self._io.pos()
            if self.wall_flags != VeilRooms.TileFlags.nothing:
                pass
                self._debug['wall_args']['start'] = self._io.pos()
                _on = self.wall_flags
                if _on == VeilRooms.TileFlags.level_exit:
                    pass
                    self.wall_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.mouth:
                    pass
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.movable_object:
                    pass
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.npc:
                    pass
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.teleporter:
                    pass
                    self.wall_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.teleporter_dest:
                    pass
                    self.wall_args = VeilRooms.TeleporterInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown10:
                    pass
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown2:
                    pass
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown4:
                    pass
                    self.wall_args = self._io.read_u1()
                elif _on == VeilRooms.TileFlags.unknown5:
                    pass
                    self.wall_args = VeilRooms.PortalInfo(self._io, self, self._root)
                elif _on == VeilRooms.TileFlags.unknown6:
                    pass
                    self.wall_args = self._io.read_u2le()
                self._debug['wall_args']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass

            if  ((self.floor_flags != VeilRooms.TileFlags.nothing) and (self.floor_flags != VeilRooms.TileFlags.movable_object)) :
                pass
                _on = self.floor_flags
                if _on == VeilRooms.TileFlags.level_exit:
                    pass
                    self.tile_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.mouth:
                    pass
                elif _on == VeilRooms.TileFlags.movable_object:
                    pass
                elif _on == VeilRooms.TileFlags.npc:
                    pass
                elif _on == VeilRooms.TileFlags.teleporter:
                    pass
                    self.tile_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.teleporter_dest:
                    pass
                    self.tile_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.unknown10:
                    pass
                elif _on == VeilRooms.TileFlags.unknown2:
                    pass
                elif _on == VeilRooms.TileFlags.unknown4:
                    pass
                elif _on == VeilRooms.TileFlags.unknown5:
                    pass
                    self.tile_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.unknown6:
                    pass

            if self.wall_flags != VeilRooms.TileFlags.nothing:
                pass
                _on = self.wall_flags
                if _on == VeilRooms.TileFlags.level_exit:
                    pass
                    self.wall_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.mouth:
                    pass
                elif _on == VeilRooms.TileFlags.movable_object:
                    pass
                elif _on == VeilRooms.TileFlags.npc:
                    pass
                elif _on == VeilRooms.TileFlags.teleporter:
                    pass
                    self.wall_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.teleporter_dest:
                    pass
                    self.wall_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.unknown10:
                    pass
                elif _on == VeilRooms.TileFlags.unknown2:
                    pass
                elif _on == VeilRooms.TileFlags.unknown4:
                    pass
                elif _on == VeilRooms.TileFlags.unknown5:
                    pass
                    self.wall_args._fetch_instances()
                elif _on == VeilRooms.TileFlags.unknown6:
                    pass




