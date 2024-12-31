# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningNpc(KaitaiStruct):

    class WeaponClasses(Enum):
        none = 0
        edged = 9
        bashing = 10
        polearms = 11
        projectile = 12

    class MagicAttackTypes(Enum):
        none = 0
        stone = 1
        poison = 3
        fire = 4
        lightning = 5
        unknown = 9
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
        SEQ_FIELDS = ["npc_id", "head_id", "flags", "maybe_n_hit_dice", "damage_resistance", "damage_bonus", "conditionally_hostile", "sprite_id", "col8", "action", "agility", "col11", "magic_attack", "weapon_vulnerabilities", "col14", "behavior_flags"]
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
            self._debug['maybe_n_hit_dice']['start'] = self._io.pos()
            self.maybe_n_hit_dice = self._io.read_u1()
            self._debug['maybe_n_hit_dice']['end'] = self._io.pos()
            self._debug['damage_resistance']['start'] = self._io.pos()
            self.damage_resistance = self._io.read_u1()
            self._debug['damage_resistance']['end'] = self._io.pos()
            self._debug['damage_bonus']['start'] = self._io.pos()
            self.damage_bonus = self._io.read_u1()
            self._debug['damage_bonus']['end'] = self._io.pos()
            self._debug['conditionally_hostile']['start'] = self._io.pos()
            self.conditionally_hostile = self._io.read_u1()
            self._debug['conditionally_hostile']['end'] = self._io.pos()
            self._debug['sprite_id']['start'] = self._io.pos()
            self.sprite_id = self._io.read_u1()
            self._debug['sprite_id']['end'] = self._io.pos()
            self._debug['col8']['start'] = self._io.pos()
            self.col8 = self._io.read_u1()
            self._debug['col8']['end'] = self._io.pos()
            self._debug['action']['start'] = self._io.pos()
            self.action = self._io.read_u1()
            self._debug['action']['end'] = self._io.pos()
            self._debug['agility']['start'] = self._io.pos()
            self.agility = self._io.read_u1()
            self._debug['agility']['end'] = self._io.pos()
            self._debug['col11']['start'] = self._io.pos()
            self.col11 = self._io.read_u1()
            self._debug['col11']['end'] = self._io.pos()
            self._debug['magic_attack']['start'] = self._io.pos()
            self.magic_attack = KaitaiStream.resolve_enum(SummoningNpc.MagicAttackTypes, self._io.read_u1())
            self._debug['magic_attack']['end'] = self._io.pos()
            self._debug['weapon_vulnerabilities']['start'] = self._io.pos()
            self.weapon_vulnerabilities = KaitaiStream.resolve_enum(SummoningNpc.WeaponClasses, self._io.read_u1())
            self._debug['weapon_vulnerabilities']['end'] = self._io.pos()
            self._debug['col14']['start'] = self._io.pos()
            self.col14 = self._io.read_u1()
            self._debug['col14']['end'] = self._io.pos()
            self._debug['behavior_flags']['start'] = self._io.pos()
            self.behavior_flags = self._io.read_u1()
            self._debug['behavior_flags']['end'] = self._io.pos()



