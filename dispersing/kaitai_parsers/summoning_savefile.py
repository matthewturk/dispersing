# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningSavefile(KaitaiStruct):
    SEQ_FIELDS = ["copyright_messages", "save_game_name", "num_levels", "levels", "level_terminator", "unknown", "character_info", "object_table"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['copyright_messages']['start'] = self._io.pos()
        self.copyright_messages = self._io.read_bytes(256)
        self._debug['copyright_messages']['end'] = self._io.pos()
        self._debug['save_game_name']['start'] = self._io.pos()
        self.save_game_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(50), 0, False)).decode(u"ascii")
        self._debug['save_game_name']['end'] = self._io.pos()
        self._debug['num_levels']['start'] = self._io.pos()
        self.num_levels = self._io.read_s2le()
        self._debug['num_levels']['end'] = self._io.pos()
        self._debug['levels']['start'] = self._io.pos()
        self.levels = [None] * ((self.num_levels - 1))
        for i in range((self.num_levels - 1)):
            if not 'arr' in self._debug['levels']:
                self._debug['levels']['arr'] = []
            self._debug['levels']['arr'].append({'start': self._io.pos()})
            self.levels[i] = SummoningSavefile.LevelInfo(self._io, self, self._root)
            self._debug['levels']['arr'][i]['end'] = self._io.pos()

        self._debug['levels']['end'] = self._io.pos()
        self._debug['level_terminator']['start'] = self._io.pos()
        self.level_terminator = self._io.read_bytes(2)
        self._debug['level_terminator']['end'] = self._io.pos()
        if not self.level_terminator == b"\xFF\xFF":
            raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF", self.level_terminator, self._io, u"/seq/4")
        self._debug['unknown']['start'] = self._io.pos()
        self.unknown = self._io.read_bytes(21751)
        self._debug['unknown']['end'] = self._io.pos()
        self._debug['character_info']['start'] = self._io.pos()
        self._raw_character_info = self._io.read_bytes(806)
        _io__raw_character_info = KaitaiStream(BytesIO(self._raw_character_info))
        self.character_info = SummoningSavefile.CharacterTable(_io__raw_character_info, self, self._root)
        self._debug['character_info']['end'] = self._io.pos()
        self._debug['object_table']['start'] = self._io.pos()
        self.object_table = self._io.read_bytes(10000)
        self._debug['object_table']['end'] = self._io.pos()

    class SpellRecord(KaitaiStruct):
        SEQ_FIELDS = ["memorized", "cost", "info", "gestures"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['memorized']['start'] = self._io.pos()
            self.memorized = self._io.read_u1()
            self._debug['memorized']['end'] = self._io.pos()
            self._debug['cost']['start'] = self._io.pos()
            self.cost = self._io.read_u1()
            self._debug['cost']['end'] = self._io.pos()
            self._debug['info']['start'] = self._io.pos()
            self.info = self._io.read_bytes(3)
            self._debug['info']['end'] = self._io.pos()
            self._debug['gestures']['start'] = self._io.pos()
            self.gestures = (KaitaiStream.bytes_terminate(self._io.read_bytes(9), 0, False)).decode(u"ascii")
            self._debug['gestures']['end'] = self._io.pos()


    class Attributes(KaitaiStruct):
        SEQ_FIELDS = ["strength", "agility", "endurance", "accuracy", "talent", "power"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['strength']['start'] = self._io.pos()
            self.strength = self._io.read_u1()
            self._debug['strength']['end'] = self._io.pos()
            self._debug['agility']['start'] = self._io.pos()
            self.agility = self._io.read_u1()
            self._debug['agility']['end'] = self._io.pos()
            self._debug['endurance']['start'] = self._io.pos()
            self.endurance = self._io.read_u1()
            self._debug['endurance']['end'] = self._io.pos()
            self._debug['accuracy']['start'] = self._io.pos()
            self.accuracy = self._io.read_u1()
            self._debug['accuracy']['end'] = self._io.pos()
            self._debug['talent']['start'] = self._io.pos()
            self.talent = self._io.read_u1()
            self._debug['talent']['end'] = self._io.pos()
            self._debug['power']['start'] = self._io.pos()
            self.power = self._io.read_u1()
            self._debug['power']['end'] = self._io.pos()


    class WeaponLevels(KaitaiStruct):
        SEQ_FIELDS = ["long_edged", "hacking", "polearms", "projectile"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['long_edged']['start'] = self._io.pos()
            self.long_edged = self._io.read_u1()
            self._debug['long_edged']['end'] = self._io.pos()
            self._debug['hacking']['start'] = self._io.pos()
            self.hacking = self._io.read_u1()
            self._debug['hacking']['end'] = self._io.pos()
            self._debug['polearms']['start'] = self._io.pos()
            self.polearms = self._io.read_u1()
            self._debug['polearms']['end'] = self._io.pos()
            self._debug['projectile']['start'] = self._io.pos()
            self.projectile = self._io.read_u1()
            self._debug['projectile']['end'] = self._io.pos()


    class LevelInfo(KaitaiStruct):
        SEQ_FIELDS = ["level_id", "level_size", "level_info"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['level_id']['start'] = self._io.pos()
            self.level_id = self._io.read_s2le()
            self._debug['level_id']['end'] = self._io.pos()
            self._debug['level_size']['start'] = self._io.pos()
            self.level_size = self._io.read_u4le()
            self._debug['level_size']['end'] = self._io.pos()
            self._debug['level_info']['start'] = self._io.pos()
            self.level_info = self._io.read_bytes(18914)
            self._debug['level_info']['end'] = self._io.pos()


    class CharacterTable(KaitaiStruct):
        SEQ_FIELDS = ["character_name", "magic_levels", "weapon_levels", "character_level", "current_magic_exp", "next_magic_exp", "current_weapon_exp", "next_weapon_exp", "current_exp", "last_level_exp", "next_level_exp", "unknown1", "hp_cur", "hp_max", "mp_cur", "mp_max", "armor_class", "current_attributes", "maximum_attributes", "unknown2", "agility_modifier", "fatigue", "unknown3", "endurance_modifier", "spells", "currently_memorized", "unknown4"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['character_name']['start'] = self._io.pos()
            self.character_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(30), 0, False)).decode(u"ascii")
            self._debug['character_name']['end'] = self._io.pos()
            self._debug['magic_levels']['start'] = self._io.pos()
            self.magic_levels = SummoningSavefile.MagicLevels(self._io, self, self._root)
            self._debug['magic_levels']['end'] = self._io.pos()
            self._debug['weapon_levels']['start'] = self._io.pos()
            self.weapon_levels = SummoningSavefile.WeaponLevels(self._io, self, self._root)
            self._debug['weapon_levels']['end'] = self._io.pos()
            self._debug['character_level']['start'] = self._io.pos()
            self.character_level = self._io.read_u1()
            self._debug['character_level']['end'] = self._io.pos()
            self._debug['current_magic_exp']['start'] = self._io.pos()
            self.current_magic_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['current_magic_exp']:
                    self._debug['current_magic_exp']['arr'] = []
                self._debug['current_magic_exp']['arr'].append({'start': self._io.pos()})
                self.current_magic_exp[i] = self._io.read_u2le()
                self._debug['current_magic_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['current_magic_exp']['end'] = self._io.pos()
            self._debug['next_magic_exp']['start'] = self._io.pos()
            self.next_magic_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['next_magic_exp']:
                    self._debug['next_magic_exp']['arr'] = []
                self._debug['next_magic_exp']['arr'].append({'start': self._io.pos()})
                self.next_magic_exp[i] = self._io.read_u2le()
                self._debug['next_magic_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['next_magic_exp']['end'] = self._io.pos()
            self._debug['current_weapon_exp']['start'] = self._io.pos()
            self.current_weapon_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['current_weapon_exp']:
                    self._debug['current_weapon_exp']['arr'] = []
                self._debug['current_weapon_exp']['arr'].append({'start': self._io.pos()})
                self.current_weapon_exp[i] = self._io.read_u2le()
                self._debug['current_weapon_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['current_weapon_exp']['end'] = self._io.pos()
            self._debug['next_weapon_exp']['start'] = self._io.pos()
            self.next_weapon_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['next_weapon_exp']:
                    self._debug['next_weapon_exp']['arr'] = []
                self._debug['next_weapon_exp']['arr'].append({'start': self._io.pos()})
                self.next_weapon_exp[i] = self._io.read_u2le()
                self._debug['next_weapon_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['next_weapon_exp']['end'] = self._io.pos()
            self._debug['current_exp']['start'] = self._io.pos()
            self.current_exp = self._io.read_u2le()
            self._debug['current_exp']['end'] = self._io.pos()
            self._debug['last_level_exp']['start'] = self._io.pos()
            self.last_level_exp = self._io.read_u2le()
            self._debug['last_level_exp']['end'] = self._io.pos()
            self._debug['next_level_exp']['start'] = self._io.pos()
            self.next_level_exp = self._io.read_u2le()
            self._debug['next_level_exp']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u2le()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['hp_cur']['start'] = self._io.pos()
            self.hp_cur = self._io.read_u2le()
            self._debug['hp_cur']['end'] = self._io.pos()
            self._debug['hp_max']['start'] = self._io.pos()
            self.hp_max = self._io.read_u2le()
            self._debug['hp_max']['end'] = self._io.pos()
            self._debug['mp_cur']['start'] = self._io.pos()
            self.mp_cur = self._io.read_u2le()
            self._debug['mp_cur']['end'] = self._io.pos()
            self._debug['mp_max']['start'] = self._io.pos()
            self.mp_max = self._io.read_u2le()
            self._debug['mp_max']['end'] = self._io.pos()
            self._debug['armor_class']['start'] = self._io.pos()
            self.armor_class = self._io.read_u2le()
            self._debug['armor_class']['end'] = self._io.pos()
            self._debug['current_attributes']['start'] = self._io.pos()
            self.current_attributes = SummoningSavefile.Attributes(self._io, self, self._root)
            self._debug['current_attributes']['end'] = self._io.pos()
            self._debug['maximum_attributes']['start'] = self._io.pos()
            self.maximum_attributes = SummoningSavefile.Attributes(self._io, self, self._root)
            self._debug['maximum_attributes']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_s1()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['agility_modifier']['start'] = self._io.pos()
            self.agility_modifier = self._io.read_s1()
            self._debug['agility_modifier']['end'] = self._io.pos()
            self._debug['fatigue']['start'] = self._io.pos()
            self.fatigue = self._io.read_s1()
            self._debug['fatigue']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_bytes(3)
            self._debug['unknown3']['end'] = self._io.pos()
            self._debug['endurance_modifier']['start'] = self._io.pos()
            self.endurance_modifier = self._io.read_s1()
            self._debug['endurance_modifier']['end'] = self._io.pos()
            self._debug['spells']['start'] = self._io.pos()
            self.spells = [None] * (40)
            for i in range(40):
                if not 'arr' in self._debug['spells']:
                    self._debug['spells']['arr'] = []
                self._debug['spells']['arr'].append({'start': self._io.pos()})
                self.spells[i] = SummoningSavefile.SpellRecord(self._io, self, self._root)
                self._debug['spells']['arr'][i]['end'] = self._io.pos()

            self._debug['spells']['end'] = self._io.pos()
            self._debug['currently_memorized']['start'] = self._io.pos()
            self.currently_memorized = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['currently_memorized']:
                    self._debug['currently_memorized']['arr'] = []
                self._debug['currently_memorized']['arr'].append({'start': self._io.pos()})
                self.currently_memorized[i] = self._io.read_u1()
                self._debug['currently_memorized']['arr'][i]['end'] = self._io.pos()

            self._debug['currently_memorized']['end'] = self._io.pos()
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_bytes(133)
            self._debug['unknown4']['end'] = self._io.pos()


    class MagicLevels(KaitaiStruct):
        SEQ_FIELDS = ["wizardry", "sorcery", "enchantry", "healing"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['wizardry']['start'] = self._io.pos()
            self.wizardry = self._io.read_u1()
            self._debug['wizardry']['end'] = self._io.pos()
            self._debug['sorcery']['start'] = self._io.pos()
            self.sorcery = self._io.read_u1()
            self._debug['sorcery']['end'] = self._io.pos()
            self._debug['enchantry']['start'] = self._io.pos()
            self.enchantry = self._io.read_u1()
            self._debug['enchantry']['end'] = self._io.pos()
            self._debug['healing']['start'] = self._io.pos()
            self.healing = self._io.read_u1()
            self._debug['healing']['end'] = self._io.pos()



