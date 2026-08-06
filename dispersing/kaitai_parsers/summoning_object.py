# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningObject(KaitaiStruct):

    class ObjectCategories(IntEnum):
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
        super(SummoningObject, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
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
        self._debug['object']['arr'] = []
        self.object = []
        for i in range(self.count):
            self._debug['object']['arr'].append({'start': self._io.pos()})
            self.object.append(SummoningObject.ObjectRecord(self._io, self, self._root))
            self._debug['object']['arr'][i]['end'] = self._io.pos()

        self._debug['object']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.object)):
            pass
            self.object[i]._fetch_instances()


    class ObjectRecord(KaitaiStruct):
        SEQ_FIELDS = ["ac_bonus", "col0", "object_name_id", "weight", "container_size", "container_capacity", "act1_icon", "act2_icon", "act1_dmg", "act1_flags", "act2_dmg", "act2_flags", "act3_dmg", "act3_flags", "charges", "image_id", "col11", "subroutine_id", "obj_type", "scroll_id"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningObject.ObjectRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ac_bonus']['start'] = self._io.pos()
            self.ac_bonus = self._io.read_bits_int_be(4)
            self._debug['ac_bonus']['end'] = self._io.pos()
            self._debug['col0']['start'] = self._io.pos()
            self.col0 = self._io.read_bits_int_be(4)
            self._debug['col0']['end'] = self._io.pos()
            self._debug['object_name_id']['start'] = self._io.pos()
            self.object_name_id = self._io.read_u1()
            self._debug['object_name_id']['end'] = self._io.pos()
            self._debug['weight']['start'] = self._io.pos()
            self.weight = self._io.read_u1()
            self._debug['weight']['end'] = self._io.pos()
            self._debug['container_size']['start'] = self._io.pos()
            self.container_size = self._io.read_bits_int_be(4)
            self._debug['container_size']['end'] = self._io.pos()
            self._debug['container_capacity']['start'] = self._io.pos()
            self.container_capacity = self._io.read_bits_int_be(4)
            self._debug['container_capacity']['end'] = self._io.pos()
            self._debug['act1_icon']['start'] = self._io.pos()
            self.act1_icon = self._io.read_u1()
            self._debug['act1_icon']['end'] = self._io.pos()
            self._debug['act2_icon']['start'] = self._io.pos()
            self.act2_icon = self._io.read_u1()
            self._debug['act2_icon']['end'] = self._io.pos()
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
            self._debug['scroll_id']['start'] = self._io.pos()
            self.scroll_id = self._io.read_u1()
            self._debug['scroll_id']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def large_image_record(self):
            if hasattr(self, '_m_large_image_record'):
                return self._m_large_image_record

            self._m_large_image_record = self.image_id + 333
            return getattr(self, '_m_large_image_record', None)

        @property
        def small_image_record(self):
            if hasattr(self, '_m_small_image_record'):
                return self._m_small_image_record

            self._m_small_image_record = self.image_id + 100
            return getattr(self, '_m_small_image_record', None)

        @property
        def text_record(self):
            if hasattr(self, '_m_text_record'):
                return self._m_text_record

            self._m_text_record = self.object_name_id + self._root.name_offset
            return getattr(self, '_m_text_record', None)



