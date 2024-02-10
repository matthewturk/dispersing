# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningNpc(KaitaiStruct):
    SEQ_FIELDS = ["count", "npcs"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['count']['start'] = self._io.pos()
        self.count = self._io.read_u2le()
        self._debug['count']['end'] = self._io.pos()
        self._debug['npcs']['start'] = self._io.pos()
        self.npcs = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['npcs']:
                self._debug['npcs']['arr'] = []
            self._debug['npcs']['arr'].append({'start': self._io.pos()})
            self.npcs[i] = SummoningNpc.Npc(self._io, self, self._root)
            self._debug['npcs']['arr'][i]['end'] = self._io.pos()

        self._debug['npcs']['end'] = self._io.pos()

    class Npc(KaitaiStruct):
        SEQ_FIELDS = ["npc_id", "head_id", "flags", "col3", "col4", "col5", "col6", "sprite_id", "body_sprite", "action_dmg_ndice", "action_dmg_nsides", "agility", "col11", "col12", "col13", "behavior_flags"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['npc_id']['start'] = self._io.pos()
            self.npc_id = self._io.read_u1()
            self._debug['npc_id']['end'] = self._io.pos()
            self._debug['head_id']['start'] = self._io.pos()
            self.head_id = self._io.read_u1()
            self._debug['head_id']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['col3']['start'] = self._io.pos()
            self.col3 = self._io.read_u1()
            self._debug['col3']['end'] = self._io.pos()
            self._debug['col4']['start'] = self._io.pos()
            self.col4 = self._io.read_u1()
            self._debug['col4']['end'] = self._io.pos()
            self._debug['col5']['start'] = self._io.pos()
            self.col5 = self._io.read_u1()
            self._debug['col5']['end'] = self._io.pos()
            self._debug['col6']['start'] = self._io.pos()
            self.col6 = self._io.read_u1()
            self._debug['col6']['end'] = self._io.pos()
            self._debug['sprite_id']['start'] = self._io.pos()
            self.sprite_id = self._io.read_u1()
            self._debug['sprite_id']['end'] = self._io.pos()
            self._debug['body_sprite']['start'] = self._io.pos()
            self.body_sprite = self._io.read_u1()
            self._debug['body_sprite']['end'] = self._io.pos()
            self._debug['action_dmg_ndice']['start'] = self._io.pos()
            self.action_dmg_ndice = self._io.read_bits_int_be(4)
            self._debug['action_dmg_ndice']['end'] = self._io.pos()
            self._debug['action_dmg_nsides']['start'] = self._io.pos()
            self.action_dmg_nsides = self._io.read_bits_int_be(4)
            self._debug['action_dmg_nsides']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['agility']['start'] = self._io.pos()
            self.agility = self._io.read_u1()
            self._debug['agility']['end'] = self._io.pos()
            self._debug['col11']['start'] = self._io.pos()
            self.col11 = self._io.read_u1()
            self._debug['col11']['end'] = self._io.pos()
            self._debug['col12']['start'] = self._io.pos()
            self.col12 = self._io.read_u1()
            self._debug['col12']['end'] = self._io.pos()
            self._debug['col13']['start'] = self._io.pos()
            self.col13 = self._io.read_u1()
            self._debug['col13']['end'] = self._io.pos()
            self._debug['behavior_flags']['start'] = self._io.pos()
            self.behavior_flags = self._io.read_u2le()
            self._debug['behavior_flags']['end'] = self._io.pos()



