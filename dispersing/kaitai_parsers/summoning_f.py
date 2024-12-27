# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningF(KaitaiStruct):
    SEQ_FIELDS = ["num_portraits", "portraits_offset", "unknown2", "num_character", "portraits", "characters"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['num_portraits']['start'] = self._io.pos()
        self.num_portraits = self._io.read_u2le()
        self._debug['num_portraits']['end'] = self._io.pos()
        self._debug['portraits_offset']['start'] = self._io.pos()
        self.portraits_offset = self._io.read_u2le()
        self._debug['portraits_offset']['end'] = self._io.pos()
        self._debug['unknown2']['start'] = self._io.pos()
        self.unknown2 = self._io.read_u2le()
        self._debug['unknown2']['end'] = self._io.pos()
        self._debug['num_character']['start'] = self._io.pos()
        self.num_character = self._io.read_u2le()
        self._debug['num_character']['end'] = self._io.pos()
        self._debug['portraits']['start'] = self._io.pos()
        self.portraits = [None] * (self.num_portraits)
        for i in range(self.num_portraits):
            if not 'arr' in self._debug['portraits']:
                self._debug['portraits']['arr'] = []
            self._debug['portraits']['arr'].append({'start': self._io.pos()})
            self.portraits[i] = SummoningF.Portrait(self._io, self, self._root)
            self._debug['portraits']['arr'][i]['end'] = self._io.pos()

        self._debug['portraits']['end'] = self._io.pos()
        self._debug['characters']['start'] = self._io.pos()
        self.characters = [None] * (self.num_character)
        for i in range(self.num_character):
            if not 'arr' in self._debug['characters']:
                self._debug['characters']['arr'] = []
            self._debug['characters']['arr'].append({'start': self._io.pos()})
            self.characters[i] = SummoningF.Character(self._io, self, self._root)
            self._debug['characters']['arr'][i]['end'] = self._io.pos()

        self._debug['characters']['end'] = self._io.pos()

    class Portrait(KaitaiStruct):
        SEQ_FIELDS = ["col1", "col2", "portrait_id", "col4", "gender"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['col1']['start'] = self._io.pos()
            self.col1 = self._io.read_u1()
            self._debug['col1']['end'] = self._io.pos()
            self._debug['col2']['start'] = self._io.pos()
            self.col2 = self._io.read_bytes(4)
            self._debug['col2']['end'] = self._io.pos()
            self._debug['portrait_id']['start'] = self._io.pos()
            self.portrait_id = self._io.read_u1()
            self._debug['portrait_id']['end'] = self._io.pos()
            self._debug['col4']['start'] = self._io.pos()
            self.col4 = self._io.read_u1()
            self._debug['col4']['end'] = self._io.pos()
            self._debug['gender']['start'] = self._io.pos()
            self.gender = self._io.read_u1()
            self._debug['gender']['end'] = self._io.pos()


    class Character(KaitaiStruct):
        SEQ_FIELDS = ["name", "portrait", "strength", "agility", "endurance", "accuracy", "talent", "power", "spell_type", "weapon_type"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(26), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['portrait']['start'] = self._io.pos()
            self.portrait = self._io.read_u1()
            self._debug['portrait']['end'] = self._io.pos()
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
            self._debug['spell_type']['start'] = self._io.pos()
            self.spell_type = self._io.read_u1()
            self._debug['spell_type']['end'] = self._io.pos()
            self._debug['weapon_type']['start'] = self._io.pos()
            self.weapon_type = self._io.read_u1()
            self._debug['weapon_type']['end'] = self._io.pos()



