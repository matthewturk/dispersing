# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningObject(KaitaiStruct):

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
    SEQ_FIELDS = ["count", "name_offset", "object"]
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
        self._debug['name_offset']['start'] = self._io.pos()
        self.name_offset = self._io.read_u2le()
        self._debug['name_offset']['end'] = self._io.pos()
        self._debug['object']['start'] = self._io.pos()
        self.object = [None] * (self.count)
        for i in range(self.count):
            if not 'arr' in self._debug['object']:
                self._debug['object']['arr'] = []
            self._debug['object']['arr'].append({'start': self._io.pos()})
            self.object[i] = SummoningObject.ObjectRecord(self._io, self, self._root)
            self._debug['object']['arr'][i]['end'] = self._io.pos()

        self._debug['object']['end'] = self._io.pos()

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
            self.obj_type = KaitaiStream.resolve_enum(SummoningObject.ObjectCategories, self._io.read_u1())
            self._debug['obj_type']['end'] = self._io.pos()
            self._debug['col14']['start'] = self._io.pos()
            self.col14 = self._io.read_u1()
            self._debug['col14']['end'] = self._io.pos()

        @property
        def text_record(self):
            if hasattr(self, '_m_text_record'):
                return self._m_text_record if hasattr(self, '_m_text_record') else None

            self._m_text_record = (self.object_name_id + self._root.name_offset)
            return self._m_text_record if hasattr(self, '_m_text_record') else None

        @property
        def small_image_record(self):
            if hasattr(self, '_m_small_image_record'):
                return self._m_small_image_record if hasattr(self, '_m_small_image_record') else None

            self._m_small_image_record = (self.image_id + 100)
            return self._m_small_image_record if hasattr(self, '_m_small_image_record') else None

        @property
        def large_image_record(self):
            if hasattr(self, '_m_large_image_record'):
                return self._m_large_image_record if hasattr(self, '_m_large_image_record') else None

            self._m_large_image_record = (self.image_id + 333)
            return self._m_large_image_record if hasattr(self, '_m_large_image_record') else None



