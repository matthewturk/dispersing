# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningInit(KaitaiStruct):
    SEQ_FIELDS = ["sprite_offsets", "unknown1", "unknown2", "unknown3", "unknown4", "unknown5", "spell_cost", "unknown7", "spells", "unknown8", "unknown9", "unknown10"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
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
        self.spell_cost = [None] * (40)
        for i in range(40):
            if not 'arr' in self._debug['spell_cost']:
                self._debug['spell_cost']['arr'] = []
            self._debug['spell_cost']['arr'].append({'start': self._io.pos()})
            self.spell_cost[i] = self._io.read_u1()
            self._debug['spell_cost']['arr'][i]['end'] = self._io.pos()

        self._debug['spell_cost']['end'] = self._io.pos()
        self._debug['unknown7']['start'] = self._io.pos()
        self.unknown7 = [None] * (40)
        for i in range(40):
            if not 'arr' in self._debug['unknown7']:
                self._debug['unknown7']['arr'] = []
            self._debug['unknown7']['arr'].append({'start': self._io.pos()})
            self.unknown7[i] = SummoningInit.SpellInfo(self._io, self, self._root)
            self._debug['unknown7']['arr'][i]['end'] = self._io.pos()

        self._debug['unknown7']['end'] = self._io.pos()
        self._debug['spells']['start'] = self._io.pos()
        self.spells = [None] * (40)
        for i in range(40):
            if not 'arr' in self._debug['spells']:
                self._debug['spells']['arr'] = []
            self._debug['spells']['arr'].append({'start': self._io.pos()})
            self.spells[i] = (self._io.read_bytes(9)).decode(u"ascii")
            self._debug['spells']['arr'][i]['end'] = self._io.pos()

        self._debug['spells']['end'] = self._io.pos()
        self._debug['unknown8']['start'] = self._io.pos()
        self.unknown8 = self._io.read_u4le()
        self._debug['unknown8']['end'] = self._io.pos()
        self._debug['unknown9']['start'] = self._io.pos()
        self.unknown9 = self._io.read_bytes(11)
        self._debug['unknown9']['end'] = self._io.pos()
        self._debug['unknown10']['start'] = self._io.pos()
        self.unknown10 = self._io.read_bytes(20)
        self._debug['unknown10']['end'] = self._io.pos()

    class SpriteOffsets(KaitaiStruct):
        SEQ_FIELDS = ["intro_anim_offset", "ingame_anim_offset", "endgame_anim_offset", "small_object", "worn_object", "tiny_object", "people", "music", "scroll", "char_anim", "item_anim", "terrain", "npc", "wall_decoration"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
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


    class Unknown1T(KaitaiStruct):
        SEQ_FIELDS = ["count", "values"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = self._io.read_u1()
            self._debug['count']['end'] = self._io.pos()
            self._debug['values']['start'] = self._io.pos()
            self.values = [None] * (self.count)
            for i in range(self.count):
                if not 'arr' in self._debug['values']:
                    self._debug['values']['arr'] = []
                self._debug['values']['arr'].append({'start': self._io.pos()})
                self.values[i] = self._io.read_s2le()
                self._debug['values']['arr'][i]['end'] = self._io.pos()

            self._debug['values']['end'] = self._io.pos()


    class SpellInfo(KaitaiStruct):
        SEQ_FIELDS = ["unknown1", "unknown2", "unknown3"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
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



