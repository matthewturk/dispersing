# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class SummoningInit(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.sprite_offsets = self._root.SpriteOffsets(self._io, self, self._root)
        self.unknown1 = self._root.Unknown1T(self._io, self, self._root)
        self.unknown2 = [None] * (9)
        for i in range(9):
            self.unknown2[i] = self._io.read_bytes(256)

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




