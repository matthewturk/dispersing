# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningF(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.count = self._io.read_u2le()
        self.unknown1 = self._io.read_u2le()
        self.unknown2 = self._io.read_u2le()
        self.num_character = self._io.read_u2le()
        self.records = [None] * (self.count)
        for i in range(self.count):
            self.records[i] = SummoningF.Frecord(self._io, self, self._root)

        self.characters = [None] * (self.num_character)
        for i in range(self.num_character):
            self.characters[i] = SummoningF.Character(self._io, self, self._root)


    class Frecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.col1 = self._io.read_u1()
            self.col2 = self._io.read_bytes(4)
            self.col3 = self._io.read_u1()
            self.col4 = self._io.read_u1()
            self.col5 = self._io.read_u1()


    class Character(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(26), 0, False)).decode(u"ASCII")
            self.portrait = self._io.read_u1()
            self.strength = self._io.read_u1()
            self.agility = self._io.read_u1()
            self.endurance = self._io.read_u1()
            self.accuracy = self._io.read_u1()
            self.talent = self._io.read_u1()
            self.power = self._io.read_u1()
            self.spell_type = self._io.read_u1()
            self.weapon_type = self._io.read_u1()



