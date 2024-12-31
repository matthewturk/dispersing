# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningDatasegment(KaitaiStruct):

    class ObjectCategories(Enum):
        helmet = 0
        shirt = 1
        boots = 2
        gloves = 3
        quiver = 4
        medallion = 5
        object = 6
        arrow = 7
        bottle = 8
        sword_1handed = 73
        shield_axe = 74
        projectile = 76
        sword_2handed = 201
        staff_of_the_serpent = 202
        polearm = 203
        bow = 204
    SEQ_FIELDS = ["bytes"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['bytes']['start'] = self._io.pos()
        self.bytes = self._io.read_bytes(65535)
        self._debug['bytes']['end'] = self._io.pos()

    class SpeechStrings(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self.text = []
            i = 0
            while not self._io.is_eof():
                if not 'arr' in self._debug['text']:
                    self._debug['text']['arr'] = []
                self._debug['text']['arr'].append({'start': self._io.pos()})
                self.text.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ascii"))
                self._debug['text']['arr'][len(self.text) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['text']['end'] = self._io.pos()


    class CharacterRecord(KaitaiStruct):
        SEQ_FIELDS = ["character_name", "unknown1", "magic_levels", "weapon_levels", "character_level", "current_magic_level_exp", "next_magic_level_exp", "current_weapon_level_exp", "next_weapon_level_exp", "current_experience", "next_experience", "next_level_experience", "unknown2", "hp_current", "hp_max", "mp_current", "mp_max", "armor_class", "current_attributes", "max_attributes"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['character_name']['start'] = self._io.pos()
            self.character_name = (self._io.read_bytes(26)).decode(u"ascii")
            self._debug['character_name']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(4)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['magic_levels']['start'] = self._io.pos()
            self.magic_levels = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['magic_levels']:
                    self._debug['magic_levels']['arr'] = []
                self._debug['magic_levels']['arr'].append({'start': self._io.pos()})
                self.magic_levels[i] = self._io.read_u1()
                self._debug['magic_levels']['arr'][i]['end'] = self._io.pos()

            self._debug['magic_levels']['end'] = self._io.pos()
            self._debug['weapon_levels']['start'] = self._io.pos()
            self.weapon_levels = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['weapon_levels']:
                    self._debug['weapon_levels']['arr'] = []
                self._debug['weapon_levels']['arr'].append({'start': self._io.pos()})
                self.weapon_levels[i] = self._io.read_u1()
                self._debug['weapon_levels']['arr'][i]['end'] = self._io.pos()

            self._debug['weapon_levels']['end'] = self._io.pos()
            self._debug['character_level']['start'] = self._io.pos()
            self.character_level = self._io.read_u1()
            self._debug['character_level']['end'] = self._io.pos()
            self._debug['current_magic_level_exp']['start'] = self._io.pos()
            self.current_magic_level_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['current_magic_level_exp']:
                    self._debug['current_magic_level_exp']['arr'] = []
                self._debug['current_magic_level_exp']['arr'].append({'start': self._io.pos()})
                self.current_magic_level_exp[i] = self._io.read_u2le()
                self._debug['current_magic_level_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['current_magic_level_exp']['end'] = self._io.pos()
            self._debug['next_magic_level_exp']['start'] = self._io.pos()
            self.next_magic_level_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['next_magic_level_exp']:
                    self._debug['next_magic_level_exp']['arr'] = []
                self._debug['next_magic_level_exp']['arr'].append({'start': self._io.pos()})
                self.next_magic_level_exp[i] = self._io.read_u2le()
                self._debug['next_magic_level_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['next_magic_level_exp']['end'] = self._io.pos()
            self._debug['current_weapon_level_exp']['start'] = self._io.pos()
            self.current_weapon_level_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['current_weapon_level_exp']:
                    self._debug['current_weapon_level_exp']['arr'] = []
                self._debug['current_weapon_level_exp']['arr'].append({'start': self._io.pos()})
                self.current_weapon_level_exp[i] = self._io.read_u2le()
                self._debug['current_weapon_level_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['current_weapon_level_exp']['end'] = self._io.pos()
            self._debug['next_weapon_level_exp']['start'] = self._io.pos()
            self.next_weapon_level_exp = [None] * (4)
            for i in range(4):
                if not 'arr' in self._debug['next_weapon_level_exp']:
                    self._debug['next_weapon_level_exp']['arr'] = []
                self._debug['next_weapon_level_exp']['arr'].append({'start': self._io.pos()})
                self.next_weapon_level_exp[i] = self._io.read_u2le()
                self._debug['next_weapon_level_exp']['arr'][i]['end'] = self._io.pos()

            self._debug['next_weapon_level_exp']['end'] = self._io.pos()
            self._debug['current_experience']['start'] = self._io.pos()
            self.current_experience = self._io.read_u2le()
            self._debug['current_experience']['end'] = self._io.pos()
            self._debug['next_experience']['start'] = self._io.pos()
            self.next_experience = self._io.read_u2le()
            self._debug['next_experience']['end'] = self._io.pos()
            self._debug['next_level_experience']['start'] = self._io.pos()
            self.next_level_experience = self._io.read_u2le()
            self._debug['next_level_experience']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u2le()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['hp_current']['start'] = self._io.pos()
            self.hp_current = self._io.read_u2le()
            self._debug['hp_current']['end'] = self._io.pos()
            self._debug['hp_max']['start'] = self._io.pos()
            self.hp_max = self._io.read_u2le()
            self._debug['hp_max']['end'] = self._io.pos()
            self._debug['mp_current']['start'] = self._io.pos()
            self.mp_current = self._io.read_u2le()
            self._debug['mp_current']['end'] = self._io.pos()
            self._debug['mp_max']['start'] = self._io.pos()
            self.mp_max = self._io.read_u2le()
            self._debug['mp_max']['end'] = self._io.pos()
            self._debug['armor_class']['start'] = self._io.pos()
            self.armor_class = self._io.read_u2le()
            self._debug['armor_class']['end'] = self._io.pos()
            self._debug['current_attributes']['start'] = self._io.pos()
            self.current_attributes = SummoningDatasegment.CharacterAttributes(self._io, self, self._root)
            self._debug['current_attributes']['end'] = self._io.pos()
            self._debug['max_attributes']['start'] = self._io.pos()
            self.max_attributes = SummoningDatasegment.CharacterAttributes(self._io, self, self._root)
            self._debug['max_attributes']['end'] = self._io.pos()


    class CharacterPosition(KaitaiStruct):
        SEQ_FIELDS = ["x_pos_32", "y_pos_32", "maybe_num_charges", "unknown1", "final_object", "mobility", "unknown2", "unknown3", "unknown4", "maybe_creation_time", "unknown5", "unknown6", "unknown7", "unknown8", "unknown9", "index", "unknown10", "direction", "base_npc_id", "unknown11", "sprite_id", "unknown12", "maybe_current_hp", "unknown13", "unknown14"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x_pos_32']['start'] = self._io.pos()
            self.x_pos_32 = self._io.read_u2le()
            self._debug['x_pos_32']['end'] = self._io.pos()
            self._debug['y_pos_32']['start'] = self._io.pos()
            self.y_pos_32 = self._io.read_u2le()
            self._debug['y_pos_32']['end'] = self._io.pos()
            self._debug['maybe_num_charges']['start'] = self._io.pos()
            self.maybe_num_charges = self._io.read_u2le()
            self._debug['maybe_num_charges']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u2le()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['final_object']['start'] = self._io.pos()
            self.final_object = self._io.read_u2le()
            self._debug['final_object']['end'] = self._io.pos()
            self._debug['mobility']['start'] = self._io.pos()
            self.mobility = self._io.read_u1()
            self._debug['mobility']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u1()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_u1()
            self._debug['unknown3']['end'] = self._io.pos()
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_u1()
            self._debug['unknown4']['end'] = self._io.pos()
            self._debug['maybe_creation_time']['start'] = self._io.pos()
            self.maybe_creation_time = self._io.read_u2le()
            self._debug['maybe_creation_time']['end'] = self._io.pos()
            self._debug['unknown5']['start'] = self._io.pos()
            self.unknown5 = self._io.read_u1()
            self._debug['unknown5']['end'] = self._io.pos()
            self._debug['unknown6']['start'] = self._io.pos()
            self.unknown6 = self._io.read_u1()
            self._debug['unknown6']['end'] = self._io.pos()
            self._debug['unknown7']['start'] = self._io.pos()
            self.unknown7 = self._io.read_u1()
            self._debug['unknown7']['end'] = self._io.pos()
            self._debug['unknown8']['start'] = self._io.pos()
            self.unknown8 = self._io.read_u1()
            self._debug['unknown8']['end'] = self._io.pos()
            self._debug['unknown9']['start'] = self._io.pos()
            self.unknown9 = self._io.read_u1()
            self._debug['unknown9']['end'] = self._io.pos()
            self._debug['index']['start'] = self._io.pos()
            self.index = self._io.read_u1()
            self._debug['index']['end'] = self._io.pos()
            self._debug['unknown10']['start'] = self._io.pos()
            self.unknown10 = self._io.read_u1()
            self._debug['unknown10']['end'] = self._io.pos()
            self._debug['direction']['start'] = self._io.pos()
            self.direction = self._io.read_u1()
            self._debug['direction']['end'] = self._io.pos()
            self._debug['base_npc_id']['start'] = self._io.pos()
            self.base_npc_id = self._io.read_u1()
            self._debug['base_npc_id']['end'] = self._io.pos()
            self._debug['unknown11']['start'] = self._io.pos()
            self.unknown11 = self._io.read_u1()
            self._debug['unknown11']['end'] = self._io.pos()
            self._debug['sprite_id']['start'] = self._io.pos()
            self.sprite_id = self._io.read_u2le()
            self._debug['sprite_id']['end'] = self._io.pos()
            self._debug['unknown12']['start'] = self._io.pos()
            self.unknown12 = self._io.read_u2le()
            self._debug['unknown12']['end'] = self._io.pos()
            self._debug['maybe_current_hp']['start'] = self._io.pos()
            self.maybe_current_hp = self._io.read_u2le()
            self._debug['maybe_current_hp']['end'] = self._io.pos()
            self._debug['unknown13']['start'] = self._io.pos()
            self.unknown13 = self._io.read_u1()
            self._debug['unknown13']['end'] = self._io.pos()
            self._debug['unknown14']['start'] = self._io.pos()
            self.unknown14 = self._io.read_u1()
            self._debug['unknown14']['end'] = self._io.pos()


    class CharacterAttributes(KaitaiStruct):
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


    class ObjectRecord(KaitaiStruct):
        SEQ_FIELDS = ["ac_bonus", "col0", "object_name_id", "weight", "container_flags", "col4", "col5", "act1_dmg", "act1_flags", "act2_dmg", "act2_flags", "act3_dmg", "act3_flags", "charges", "image_id", "col11", "subroutine_id", "obj_type", "col14"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ac_bonus']['start'] = self._io.pos()
            self.ac_bonus = self._io.read_bits_int_be(4)
            self._debug['ac_bonus']['end'] = self._io.pos()
            self._debug['col0']['start'] = self._io.pos()
            self.col0 = self._io.read_bits_int_be(4)
            self._debug['col0']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['object_name_id']['start'] = self._io.pos()
            self.object_name_id = self._io.read_u1()
            self._debug['object_name_id']['end'] = self._io.pos()
            self._debug['weight']['start'] = self._io.pos()
            self.weight = self._io.read_u1()
            self._debug['weight']['end'] = self._io.pos()
            self._debug['container_flags']['start'] = self._io.pos()
            self.container_flags = self._io.read_u1()
            self._debug['container_flags']['end'] = self._io.pos()
            self._debug['col4']['start'] = self._io.pos()
            self.col4 = self._io.read_u1()
            self._debug['col4']['end'] = self._io.pos()
            self._debug['col5']['start'] = self._io.pos()
            self.col5 = self._io.read_u1()
            self._debug['col5']['end'] = self._io.pos()
            self._debug['act1_dmg']['start'] = self._io.pos()
            self.act1_dmg = self._io.read_bits_int_be(4)
            self._debug['act1_dmg']['end'] = self._io.pos()
            self._debug['act1_flags']['start'] = self._io.pos()
            self.act1_flags = self._io.read_bits_int_be(4)
            self._debug['act1_flags']['end'] = self._io.pos()
            self._debug['act2_dmg']['start'] = self._io.pos()
            self.act2_dmg = self._io.read_bits_int_be(4)
            self._debug['act2_dmg']['end'] = self._io.pos()
            self._debug['act2_flags']['start'] = self._io.pos()
            self.act2_flags = self._io.read_bits_int_be(4)
            self._debug['act2_flags']['end'] = self._io.pos()
            self._debug['act3_dmg']['start'] = self._io.pos()
            self.act3_dmg = self._io.read_bits_int_be(4)
            self._debug['act3_dmg']['end'] = self._io.pos()
            self._debug['act3_flags']['start'] = self._io.pos()
            self.act3_flags = self._io.read_bits_int_be(4)
            self._debug['act3_flags']['end'] = self._io.pos()
            self._io.align_to_byte()
            self._debug['charges']['start'] = self._io.pos()
            self.charges = self._io.read_u1()
            self._debug['charges']['end'] = self._io.pos()
            self._debug['image_id']['start'] = self._io.pos()
            self.image_id = self._io.read_u1()
            self._debug['image_id']['end'] = self._io.pos()
            self._debug['col11']['start'] = self._io.pos()
            self.col11 = self._io.read_u1()
            self._debug['col11']['end'] = self._io.pos()
            self._debug['subroutine_id']['start'] = self._io.pos()
            self.subroutine_id = self._io.read_u1()
            self._debug['subroutine_id']['end'] = self._io.pos()
            self._debug['obj_type']['start'] = self._io.pos()
            self.obj_type = KaitaiStream.resolve_enum(SummoningDatasegment.ObjectCategories, self._io.read_u1())
            self._debug['obj_type']['end'] = self._io.pos()
            self._debug['col14']['start'] = self._io.pos()
            self.col14 = self._io.read_u1()
            self._debug['col14']['end'] = self._io.pos()


    class SpellInfo(KaitaiStruct):
        SEQ_FIELDS = ["elem1", "elem2", "elem3", "elem4", "elem5", "gestures"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['elem1']['start'] = self._io.pos()
            self.elem1 = self._io.read_u1()
            self._debug['elem1']['end'] = self._io.pos()
            self._debug['elem2']['start'] = self._io.pos()
            self.elem2 = self._io.read_u1()
            self._debug['elem2']['end'] = self._io.pos()
            self._debug['elem3']['start'] = self._io.pos()
            self.elem3 = self._io.read_u1()
            self._debug['elem3']['end'] = self._io.pos()
            self._debug['elem4']['start'] = self._io.pos()
            self.elem4 = self._io.read_u1()
            self._debug['elem4']['end'] = self._io.pos()
            self._debug['elem5']['start'] = self._io.pos()
            self.elem5 = self._io.read_u1()
            self._debug['elem5']['end'] = self._io.pos()
            self._debug['gestures']['start'] = self._io.pos()
            self.gestures = (self._io.read_bytes(9)).decode(u"ascii")
            self._debug['gestures']['end'] = self._io.pos()


    @property
    def pc_info(self):
        if hasattr(self, '_m_pc_info'):
            return self._m_pc_info if hasattr(self, '_m_pc_info') else None

        _pos = self._io.pos()
        self._io.seek(8997)
        self._debug['_m_pc_info']['start'] = self._io.pos()
        self._m_pc_info = SummoningDatasegment.CharacterPosition(self._io, self, self._root)
        self._debug['_m_pc_info']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_pc_info if hasattr(self, '_m_pc_info') else None

    @property
    def character_info(self):
        if hasattr(self, '_m_character_info'):
            return self._m_character_info if hasattr(self, '_m_character_info') else None

        _pos = self._io.pos()
        self._io.seek(27945)
        self._debug['_m_character_info']['start'] = self._io.pos()
        self._m_character_info = SummoningDatasegment.CharacterRecord(self._io, self, self._root)
        self._debug['_m_character_info']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_character_info if hasattr(self, '_m_character_info') else None

    @property
    def spell_table(self):
        if hasattr(self, '_m_spell_table'):
            return self._m_spell_table if hasattr(self, '_m_spell_table') else None

        _pos = self._io.pos()
        self._io.seek(28053)
        self._debug['_m_spell_table']['start'] = self._io.pos()
        self._m_spell_table = [None] * (40)
        for i in range(40):
            if not 'arr' in self._debug['_m_spell_table']:
                self._debug['_m_spell_table']['arr'] = []
            self._debug['_m_spell_table']['arr'].append({'start': self._io.pos()})
            self._m_spell_table[i] = SummoningDatasegment.SpellInfo(self._io, self, self._root)
            self._debug['_m_spell_table']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_spell_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_spell_table if hasattr(self, '_m_spell_table') else None

    @property
    def object_template_table_ptr(self):
        if hasattr(self, '_m_object_template_table_ptr'):
            return self._m_object_template_table_ptr if hasattr(self, '_m_object_template_table_ptr') else None

        _pos = self._io.pos()
        self._io.seek(31903)
        self._debug['_m_object_template_table_ptr']['start'] = self._io.pos()
        self._m_object_template_table_ptr = self._io.read_u2le()
        self._debug['_m_object_template_table_ptr']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_object_template_table_ptr if hasattr(self, '_m_object_template_table_ptr') else None

    @property
    def speech_strings_size(self):
        if hasattr(self, '_m_speech_strings_size'):
            return self._m_speech_strings_size if hasattr(self, '_m_speech_strings_size') else None

        _pos = self._io.pos()
        self._io.seek(25942)
        self._debug['_m_speech_strings_size']['start'] = self._io.pos()
        self._m_speech_strings_size = self._io.read_u2le()
        self._debug['_m_speech_strings_size']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_speech_strings_size if hasattr(self, '_m_speech_strings_size') else None

    @property
    def speech_strings(self):
        if hasattr(self, '_m_speech_strings'):
            return self._m_speech_strings if hasattr(self, '_m_speech_strings') else None

        _pos = self._io.pos()
        self._io.seek(25944)
        self._debug['_m_speech_strings']['start'] = self._io.pos()
        self._raw__m_speech_strings = self._io.read_bytes(self._root.speech_strings_size)
        _io__raw__m_speech_strings = KaitaiStream(BytesIO(self._raw__m_speech_strings))
        self._m_speech_strings = SummoningDatasegment.SpeechStrings(_io__raw__m_speech_strings, self, self._root)
        self._debug['_m_speech_strings']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_speech_strings if hasattr(self, '_m_speech_strings') else None

    @property
    def keywords_table_ptr(self):
        if hasattr(self, '_m_keywords_table_ptr'):
            return self._m_keywords_table_ptr if hasattr(self, '_m_keywords_table_ptr') else None

        _pos = self._io.pos()
        self._io.seek(36029)
        self._debug['_m_keywords_table_ptr']['start'] = self._io.pos()
        self._m_keywords_table_ptr = self._io.read_u2le()
        self._debug['_m_keywords_table_ptr']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_keywords_table_ptr if hasattr(self, '_m_keywords_table_ptr') else None

    @property
    def object_template_table_count(self):
        if hasattr(self, '_m_object_template_table_count'):
            return self._m_object_template_table_count if hasattr(self, '_m_object_template_table_count') else None

        _pos = self._io.pos()
        self._io.seek(34572)
        self._debug['_m_object_template_table_count']['start'] = self._io.pos()
        self._m_object_template_table_count = self._io.read_u2le()
        self._debug['_m_object_template_table_count']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_object_template_table_count if hasattr(self, '_m_object_template_table_count') else None

    @property
    def npc_info(self):
        if hasattr(self, '_m_npc_info'):
            return self._m_npc_info if hasattr(self, '_m_npc_info') else None

        _pos = self._io.pos()
        self._io.seek((8997 + 34))
        self._debug['_m_npc_info']['start'] = self._io.pos()
        self._m_npc_info = [None] * (99)
        for i in range(99):
            if not 'arr' in self._debug['_m_npc_info']:
                self._debug['_m_npc_info']['arr'] = []
            self._debug['_m_npc_info']['arr'].append({'start': self._io.pos()})
            self._m_npc_info[i] = SummoningDatasegment.CharacterPosition(self._io, self, self._root)
            self._debug['_m_npc_info']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_npc_info']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_npc_info if hasattr(self, '_m_npc_info') else None

    @property
    def keywords_table(self):
        if hasattr(self, '_m_keywords_table'):
            return self._m_keywords_table if hasattr(self, '_m_keywords_table') else None

        _pos = self._io.pos()
        self._io.seek(self._root.keywords_table_ptr)
        self._debug['_m_keywords_table']['start'] = self._io.pos()
        self._m_keywords_table = self._io.read_bytes(20)
        self._debug['_m_keywords_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_keywords_table if hasattr(self, '_m_keywords_table') else None

    @property
    def object_template_table(self):
        if hasattr(self, '_m_object_template_table'):
            return self._m_object_template_table if hasattr(self, '_m_object_template_table') else None

        _pos = self._io.pos()
        self._io.seek(self._root.object_template_table_ptr)
        self._debug['_m_object_template_table']['start'] = self._io.pos()
        self._m_object_template_table = [None] * (self._root.object_template_table_count)
        for i in range(self._root.object_template_table_count):
            if not 'arr' in self._debug['_m_object_template_table']:
                self._debug['_m_object_template_table']['arr'] = []
            self._debug['_m_object_template_table']['arr'].append({'start': self._io.pos()})
            self._m_object_template_table[i] = SummoningDatasegment.ObjectRecord(self._io, self, self._root)
            self._debug['_m_object_template_table']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_object_template_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_object_template_table if hasattr(self, '_m_object_template_table') else None

    @property
    def num_level_procedures(self):
        if hasattr(self, '_m_num_level_procedures'):
            return self._m_num_level_procedures if hasattr(self, '_m_num_level_procedures') else None

        _pos = self._io.pos()
        self._io.seek(25441)
        self._debug['_m_num_level_procedures']['start'] = self._io.pos()
        self._m_num_level_procedures = self._io.read_u1()
        self._debug['_m_num_level_procedures']['end'] = self._io.pos()
        self._io.seek(_pos)
        return self._m_num_level_procedures if hasattr(self, '_m_num_level_procedures') else None


