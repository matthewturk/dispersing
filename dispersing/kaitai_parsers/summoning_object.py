# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from enum import Enum

from kaitaistruct import BytesIO, KaitaiStream, KaitaiStruct, __version__ as ks_version
from pkg_resources import parse_version

if parse_version(ks_version) < parse_version("0.7"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s"
        % (ks_version)
    )


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

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.count = self._io.read_u2le()
        self.name_offset = self._io.read_u2le()
        self.object = [None] * (self.count)
        for i in range(self.count):
            self.object[i] = self._root.ObjectRecord(self._io, self, self._root)

    class ObjectRecord(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ac_bonus = self._io.read_bits_int(4)
            self.col0 = self._io.read_bits_int(4)
            self._io.align_to_byte()
            self.object_name_id = self._io.read_u1()
            self.weight = self._io.read_u1()
            self.container_flags = self._io.read_u1()
            self.col4 = self._io.read_u1()
            self.col5 = self._io.read_u1()
            self.act1_dmg = self._io.read_bits_int(4)
            self.act1_flags = self._io.read_bits_int(4)
            self.act2_dmg = self._io.read_bits_int(4)
            self.act2_flags = self._io.read_bits_int(4)
            self.act3_dmg = self._io.read_bits_int(4)
            self.act3_flags = self._io.read_bits_int(4)
            self._io.align_to_byte()
            self.charges = self._io.read_u1()
            self.image_id = self._io.read_u1()
            self.col11 = self._io.read_u1()
            self.col12 = self._io.read_u1()
            self.obj_type = self._root.ObjectCategories(self._io.read_u1())
            self.col14 = self._io.read_u1()

        @property
        def text_record(self):
            if hasattr(self, "_m_text_record"):
                return self._m_text_record if hasattr(self, "_m_text_record") else None

            self._m_text_record = self.object_name_id + self._root.name_offset
            return self._m_text_record if hasattr(self, "_m_text_record") else None

        @property
        def small_image_record(self):
            if hasattr(self, "_m_small_image_record"):
                return (
                    self._m_small_image_record
                    if hasattr(self, "_m_small_image_record")
                    else None
                )

            self._m_small_image_record = self.image_id + 100
            return (
                self._m_small_image_record
                if hasattr(self, "_m_small_image_record")
                else None
            )

        @property
        def large_image_record(self):
            if hasattr(self, "_m_large_image_record"):
                return (
                    self._m_large_image_record
                    if hasattr(self, "_m_large_image_record")
                    else None
                )

            self._m_large_image_record = self.image_id + 333
            return (
                self._m_large_image_record
                if hasattr(self, "_m_large_image_record")
                else None
            )
