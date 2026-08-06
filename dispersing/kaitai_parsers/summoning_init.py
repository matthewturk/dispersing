# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningInit(KaitaiStruct):
    SEQ_FIELDS = ["sprite_offsets", "unknown1", "unknown2", "unknown3", "unknown4", "unknown5", "spell_cost", "unknown7", "spells", "unknown8", "unknown9", "unknown10", "unknown11"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningInit, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['sprite_offsets']['start'] = self._io.pos()
        self.sprite_offsets = SummoningInit.SpriteOffsets(self._io, self, self._root)
        self._debug['sprite_offsets']['end'] = self._io.pos()
        self._debug['unknown1']['start'] = self._io.pos()
        self.unknown1 = SummoningInit.Unknown1T(self._io, self, self._root)
        self._debug['unknown1']['end'] = self._io.pos()
        self._debug['unknown2']['start'] = self._io.pos()
        self.unknown2 = self._io.read_bytes(256)
        self._debug['unknown2']['end'] = self._io.pos()
        self._debug['unknown3']['start'] = self._io.pos()
        self.unknown3 = self._io.read_bytes(256)
        self._debug['unknown3']['end'] = self._io.pos()
        self._debug['unknown4']['start'] = self._io.pos()
        self.unknown4 = self._io.read_bytes(96)
        self._debug['unknown4']['end'] = self._io.pos()
        self._debug['unknown5']['start'] = self._io.pos()
        self.unknown5 = self._io.read_bytes(1536)
        self._debug['unknown5']['end'] = self._io.pos()
        self._debug['spell_cost']['start'] = self._io.pos()
        self._debug['spell_cost']['arr'] = []
        self.spell_cost = []
        for i in range(40):
            self._debug['spell_cost']['arr'].append({'start': self._io.pos()})
            self.spell_cost.append(self._io.read_u1())
            self._debug['spell_cost']['arr'][i]['end'] = self._io.pos()

        self._debug['spell_cost']['end'] = self._io.pos()
        self._debug['unknown7']['start'] = self._io.pos()
        self._debug['unknown7']['arr'] = []
        self.unknown7 = []
        for i in range(40):
            self._debug['unknown7']['arr'].append({'start': self._io.pos()})
            self.unknown7.append(SummoningInit.SpellInfo(self._io, self, self._root))
            self._debug['unknown7']['arr'][i]['end'] = self._io.pos()

        self._debug['unknown7']['end'] = self._io.pos()
        self._debug['spells']['start'] = self._io.pos()
        self._debug['spells']['arr'] = []
        self.spells = []
        for i in range(40):
            self._debug['spells']['arr'].append({'start': self._io.pos()})
            self.spells.append((self._io.read_bytes(9)).decode(u"ASCII"))
            self._debug['spells']['arr'][i]['end'] = self._io.pos()

        self._debug['spells']['end'] = self._io.pos()
        self._debug['unknown8']['start'] = self._io.pos()
        self.unknown8 = self._io.read_bytes(16)
        self._debug['unknown8']['end'] = self._io.pos()
        self._debug['unknown9']['start'] = self._io.pos()
        self.unknown9 = self._io.read_bytes(11)
        self._debug['unknown9']['end'] = self._io.pos()
        self._debug['unknown10']['start'] = self._io.pos()
        self._debug['unknown10']['arr'] = []
        self.unknown10 = []
        for i in range(20):
            self._debug['unknown10']['arr'].append({'start': self._io.pos()})
            self.unknown10.append(SummoningInit.Unknown10T(self._io, self, self._root))
            self._debug['unknown10']['arr'][i]['end'] = self._io.pos()

        self._debug['unknown10']['end'] = self._io.pos()
        self._debug['unknown11']['start'] = self._io.pos()
        self.unknown11 = self._io.read_bytes(3)
        self._debug['unknown11']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.sprite_offsets._fetch_instances()
        self.unknown1._fetch_instances()
        for i in range(len(self.spell_cost)):
            pass

        for i in range(len(self.unknown7)):
            pass
            self.unknown7[i]._fetch_instances()

        for i in range(len(self.spells)):
            pass

        for i in range(len(self.unknown10)):
            pass
            self.unknown10[i]._fetch_instances()


    class SpellInfo(KaitaiStruct):
        SEQ_FIELDS = ["unknown1", "unknown2", "unknown3"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInit.SpellInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u1()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u1()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_u1()
            self._debug['unknown3']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SpriteOffsets(KaitaiStruct):
        SEQ_FIELDS = ["intro_anim_offset", "ingame_anim_offset", "endgame_anim_offset", "small_object", "worn_object", "tiny_object", "people", "music", "scroll", "char_anim", "item_anim", "terrain", "npc", "wall_decoration"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInit.SpriteOffsets, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['intro_anim_offset']['start'] = self._io.pos()
            self.intro_anim_offset = self._io.read_u2le()
            self._debug['intro_anim_offset']['end'] = self._io.pos()
            self._debug['ingame_anim_offset']['start'] = self._io.pos()
            self.ingame_anim_offset = self._io.read_u2le()
            self._debug['ingame_anim_offset']['end'] = self._io.pos()
            self._debug['endgame_anim_offset']['start'] = self._io.pos()
            self.endgame_anim_offset = self._io.read_u2le()
            self._debug['endgame_anim_offset']['end'] = self._io.pos()
            self._debug['small_object']['start'] = self._io.pos()
            self.small_object = self._io.read_s2le()
            self._debug['small_object']['end'] = self._io.pos()
            self._debug['worn_object']['start'] = self._io.pos()
            self.worn_object = self._io.read_s2le()
            self._debug['worn_object']['end'] = self._io.pos()
            self._debug['tiny_object']['start'] = self._io.pos()
            self.tiny_object = self._io.read_s2le()
            self._debug['tiny_object']['end'] = self._io.pos()
            self._debug['people']['start'] = self._io.pos()
            self.people = self._io.read_s2le()
            self._debug['people']['end'] = self._io.pos()
            self._debug['music']['start'] = self._io.pos()
            self.music = self._io.read_s2le()
            self._debug['music']['end'] = self._io.pos()
            self._debug['scroll']['start'] = self._io.pos()
            self.scroll = self._io.read_s2le()
            self._debug['scroll']['end'] = self._io.pos()
            self._debug['char_anim']['start'] = self._io.pos()
            self.char_anim = self._io.read_s2le()
            self._debug['char_anim']['end'] = self._io.pos()
            self._debug['item_anim']['start'] = self._io.pos()
            self.item_anim = self._io.read_s2le()
            self._debug['item_anim']['end'] = self._io.pos()
            self._debug['terrain']['start'] = self._io.pos()
            self.terrain = self._io.read_s2le()
            self._debug['terrain']['end'] = self._io.pos()
            self._debug['npc']['start'] = self._io.pos()
            self.npc = self._io.read_s2le()
            self._debug['npc']['end'] = self._io.pos()
            self._debug['wall_decoration']['start'] = self._io.pos()
            self.wall_decoration = self._io.read_s2le()
            self._debug['wall_decoration']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Unknown10T(KaitaiStruct):
        SEQ_FIELDS = ["bitfield1", "bitfield2", "blank"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInit.Unknown10T, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['bitfield1']['start'] = self._io.pos()
            self.bitfield1 = self._io.read_bits_int_le(1) != 0
            self._debug['bitfield1']['end'] = self._io.pos()
            self._debug['bitfield2']['start'] = self._io.pos()
            self.bitfield2 = self._io.read_bits_int_le(1) != 0
            self._debug['bitfield2']['end'] = self._io.pos()
            self._debug['blank']['start'] = self._io.pos()
            self.blank = self._io.read_bits_int_le(6)
            self._debug['blank']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Unknown1T(KaitaiStruct):
        SEQ_FIELDS = ["count", "values"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInit.Unknown1T, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = self._io.read_u1()
            self._debug['count']['end'] = self._io.pos()
            self._debug['values']['start'] = self._io.pos()
            self._debug['values']['arr'] = []
            self.values = []
            for i in range(self.count):
                self._debug['values']['arr'].append({'start': self._io.pos()})
                self.values.append(SummoningInit.ValuePair(self._io, self, self._root))
                self._debug['values']['arr'][i]['end'] = self._io.pos()

            self._debug['values']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.values)):
                pass
                self.values[i]._fetch_instances()



    class Unknown5T(KaitaiStruct):
        SEQ_FIELDS = ["val1", "val2", "val3", "val4"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInit.Unknown5T, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['val1']['start'] = self._io.pos()
            self.val1 = self._io.read_s1()
            self._debug['val1']['end'] = self._io.pos()
            self._debug['val2']['start'] = self._io.pos()
            self.val2 = self._io.read_s1()
            self._debug['val2']['end'] = self._io.pos()
            self._debug['val3']['start'] = self._io.pos()
            self.val3 = self._io.read_s1()
            self._debug['val3']['end'] = self._io.pos()
            self._debug['val4']['start'] = self._io.pos()
            self.val4 = self._io.read_s1()
            self._debug['val4']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ValuePair(KaitaiStruct):
        SEQ_FIELDS = ["val1", "val2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInit.ValuePair, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['val1']['start'] = self._io.pos()
            self.val1 = self._io.read_s1()
            self._debug['val1']['end'] = self._io.pos()
            self._debug['val2']['start'] = self._io.pos()
            self.val2 = self._io.read_s1()
            self._debug['val2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



