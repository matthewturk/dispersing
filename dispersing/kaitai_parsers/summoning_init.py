# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningInit(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.sprite_offsets = SummoningInit.SpriteOffsets(self._io, self, self._root)
        self.unknown1 = SummoningInit.Unknown1T(self._io, self, self._root)
        self.unknown2 = self._io.read_bytes(256)
        self.unknown3 = self._io.read_bytes(256)
        self.unknown4 = self._io.read_bytes(96)
        self.unknown5 = self._io.read_bytes(1536)
        self.spells = [None] * (40)
        for i in range(40):
            self.spells[i] = self._io.read_bytes(9)

        self.unknown9 = [None] * (51)
        for i in range(51):
            self.unknown9[i] = self._io.read_s1()


    class SpriteOffsets(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.intro_anim_offset = self._io.read_u2le()
            self.ingame_anim_offset = self._io.read_u2le()
            self.endgame_anim_offset = self._io.read_u2le()
            self.small_object = self._io.read_s2le()
            self.worn_object = self._io.read_s2le()
            self.tiny_object = self._io.read_s2le()
            self.people = self._io.read_s2le()
            self.music = self._io.read_s2le()
            self.scroll = self._io.read_s2le()
            self.char_anim = self._io.read_s2le()
            self.item_anim = self._io.read_s2le()
            self.terrain = self._io.read_s2le()
            self.npc = self._io.read_s2le()
            self.wall_decoration = self._io.read_s2le()


    class Unknown1T(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u1()
            self.values = [None] * (self.count)
            for i in range(self.count):
                self.values[i] = self._io.read_s2le()




