# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class SummoningInteract(KaitaiStruct):

    class Iopcode(Enum):
        end_command = -4
        continue_conversation = -3
        start_conversation = -2
        end_commandlist = -1
        receive_keyword = 6
        unknown9 = 9
        emit_text = 18
        emit_keyword = 19
        take_item = 20
        set_variable = 22
        heal_character = 26
        turn_on_teleporter = 31
        give_items = 41

    class ConvFlags(Enum):
        speak_again = 4
        speak_first = 5
        first_fully_healed = 13
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_header = self._root.Header(self._io, self, self._root)
        self.npc_interactions = [None] * (self.file_header.count)
        for i in range(self.file_header.count):
            self.npc_interactions[i] = self._root.NpcInteraction(self._io, self, self._root)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()
            self.text_offset = self._io.read_u2le()
            self.offsets = [None] * (self.count)
            for i in range(self.count):
                self.offsets[i] = self._io.read_u4le()



    class NpcInteraction(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.npc_name = (self._io.read_bytes(20)).decode(u"ASCII")
            self.size = self._io.read_u2le()
            self.operations = []
            i = 0
            while True:
                _ = self._root.Sequence(self._io, self, self._root)
                self.operations.append(_)
                if _.opcode == self._root.Iopcode.end_commandlist:
                    break
                i += 1


    class Sequence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.opcode = self._root.Iopcode(self._io.read_s2le())
            if self.opcode != self._root.Iopcode.end_commandlist:
                self.contents = []
                i = 0
                while True:
                    _ = self._io.read_s2le()
                    self.contents.append(_)
                    if _ == -4:
                        break
                    i += 1




