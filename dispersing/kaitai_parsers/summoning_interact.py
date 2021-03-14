# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningInteract(KaitaiStruct):

    class Iopcode(Enum):
        unknown4 = 4
        unknown5 = 5
        receive_keyword = 6
        unknown7 = 7
        unknown8 = 8
        unknown9 = 9
        unknown10 = 10
        unused11 = 11
        unknown12 = 12
        unknown13 = 13
        unknown14 = 14
        unknown15 = 15
        unknown16 = 16
        unknown17 = 17
        emit_text = 18
        emit_keyword = 19
        take_item = 20
        unknown21 = 21
        set_variable = 22
        unknown23 = 23
        give_item = 24
        unknown25 = 25
        heal_character = 26
        unknown27 = 27
        unknown28 = 28
        unknown29 = 29
        unknown30 = 30
        turn_on_teleporter = 31
        unused32 = 32
        unused33 = 33
        unknown34 = 34
        unknown35 = 35
        restore = 36
        unknown37 = 37
        unknown38 = 38
        unknown39 = 39
        unknown40 = 40
        give_items = 41
        unknown42 = 42
        unknown43 = 43
        unknown44 = 44
        unknown45 = 45
        unknown46 = 46
        end_command = 65532
        continue_conversation = 65533
        start_conversation = 65534
        end_commandlist = 65535

    class ConvFlags(Enum):
        speak_again = 4
        speak_first = 5
        again_fully_healed = 13
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_header = SummoningInteract.Header(self._io, self, self._root)
        self.npc_interactions = [None] * (self.file_header.count)
        for i in range(self.file_header.count):
            self.npc_interactions[i] = SummoningInteract.NpcInteraction(self._io, self, self._root)


    class OpcodeArgs(KaitaiStruct):
        def __init__(self, targs, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.targs = targs
            self._read()

        def _read(self):
            self.args = [None] * (len(self.targs))
            for i in range(len(self.targs)):
                self.args[i] = self._io.read_s2le()



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
                _ = SummoningInteract.Sequence(self._io, self, self._root)
                self.operations.append(_)
                if _.base_opcode == SummoningInteract.Iopcode.end_commandlist:
                    break
                i += 1


    class Sequence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.base_opcode = KaitaiStream.resolve_enum(SummoningInteract.Iopcode, self._io.read_u2le())
            if self.base_opcode != SummoningInteract.Iopcode.end_commandlist:
                self.contents = []
                i = 0
                while True:
                    _ = SummoningInteract.ConvOpcode(self._io, self, self._root)
                    self.contents.append(_)
                    if _.opcode == SummoningInteract.Iopcode.end_command:
                        break
                    i += 1



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



    class ConvOpcode(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.opcode = KaitaiStream.resolve_enum(SummoningInteract.Iopcode, self._io.read_u2le())
            _on = self.opcode
            if _on == SummoningInteract.Iopcode.unknown38:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.give_item:
                self.args = SummoningInteract.OpcodeArgs(u"o", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown40:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.emit_keyword:
                self.args = SummoningInteract.OpcodeArgs(u"k", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown10:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown42:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused11:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown8:
                self.args = SummoningInteract.OpcodeArgs(u"uuu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown37:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.set_variable:
                self.args = SummoningInteract.OpcodeArgs(u"Vv", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown16:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown35:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.receive_keyword:
                self.args = SummoningInteract.OpcodeArgs(u"k", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown7:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.turn_on_teleporter:
                self.args = SummoningInteract.OpcodeArgs(u"t", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown28:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused33:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown17:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown9:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown12:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused32:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.heal_character:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.start_conversation:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown6:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.emit_text:
                self.args = SummoningInteract.OpcodeArgs(u"t", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown13:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown14:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown44:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown46:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.end_command:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.take_item:
                self.args = SummoningInteract.OpcodeArgs(u"o", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown34:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown5:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown4:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown23:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown27:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.continue_conversation:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown30:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown43:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown29:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.end_commandlist:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.restore:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown21:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown45:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown15:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.give_items:
                self.args = SummoningInteract.OpcodeArgs(u"oooooo", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown39:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown25:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)



