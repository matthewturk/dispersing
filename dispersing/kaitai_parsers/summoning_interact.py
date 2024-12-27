# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import collections


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningInteract(KaitaiStruct):

    class Iopcode(Enum):
        unknown4 = 4
        unknown5 = 5
        receive_keyword = 6
        unknown7 = 7
        check_items = 8
        check_var_neq = 9
        check_var_eq = 10
        unused11 = 11
        unknown12 = 12
        unknown13 = 13
        unknown14 = 14
        unknown15 = 15
        check_item_wearing = 16
        unknown17 = 17
        emit_text = 18
        emit_keyword = 19
        take_item = 20
        terminate_reset = 21
        set_variable = 22
        unknown23 = 23
        give_item = 24
        unknown25 = 25
        heal_character = 26
        unknown27 = 27
        unknown28 = 28
        unknown29 = 29
        unknown30 = 30
        run_procedure = 31
        unused32 = 32
        unused33 = 33
        unknown34 = 34
        unknown35 = 35
        restore = 36
        unknown37 = 37
        unknown38 = 38
        player_emit_text = 39
        unknown40 = 40
        give_items = 41
        set_flag_true = 42
        teach_spell = 43
        switch_npc_portrait = 44
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
    SEQ_FIELDS = ["file_header", "npc_interactions"]
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_header']['start'] = self._io.pos()
        self.file_header = SummoningInteract.Header(self._io, self, self._root)
        self._debug['file_header']['end'] = self._io.pos()
        self._debug['npc_interactions']['start'] = self._io.pos()
        self.npc_interactions = [None] * (self.file_header.count)
        for i in range(self.file_header.count):
            if not 'arr' in self._debug['npc_interactions']:
                self._debug['npc_interactions']['arr'] = []
            self._debug['npc_interactions']['arr'].append({'start': self._io.pos()})
            self.npc_interactions[i] = SummoningInteract.NpcInteraction(self._io, self, self._root)
            self._debug['npc_interactions']['arr'][i]['end'] = self._io.pos()

        self._debug['npc_interactions']['end'] = self._io.pos()

    class OpcodeArgs(KaitaiStruct):
        SEQ_FIELDS = ["args"]
        def __init__(self, targs, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.targs = targs
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['args']['start'] = self._io.pos()
            self.args = [None] * (len(self.targs))
            for i in range(len(self.targs)):
                if not 'arr' in self._debug['args']:
                    self._debug['args']['arr'] = []
                self._debug['args']['arr'].append({'start': self._io.pos()})
                self.args[i] = self._io.read_s2le()
                self._debug['args']['arr'][i]['end'] = self._io.pos()

            self._debug['args']['end'] = self._io.pos()


    class NpcInteraction(KaitaiStruct):
        SEQ_FIELDS = ["npc_name", "size", "operations"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['npc_name']['start'] = self._io.pos()
            self.npc_name = (self._io.read_bytes(20)).decode(u"ASCII")
            self._debug['npc_name']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u2le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['operations']['start'] = self._io.pos()
            self.operations = []
            i = 0
            while True:
                if not 'arr' in self._debug['operations']:
                    self._debug['operations']['arr'] = []
                self._debug['operations']['arr'].append({'start': self._io.pos()})
                _ = SummoningInteract.Sequence(self._io, self, self._root)
                self.operations.append(_)
                self._debug['operations']['arr'][len(self.operations) - 1]['end'] = self._io.pos()
                if _.base_opcode == SummoningInteract.Iopcode.end_commandlist:
                    break
                i += 1
            self._debug['operations']['end'] = self._io.pos()


    class Sequence(KaitaiStruct):
        SEQ_FIELDS = ["base_opcode", "contents"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['base_opcode']['start'] = self._io.pos()
            self.base_opcode = KaitaiStream.resolve_enum(SummoningInteract.Iopcode, self._io.read_u2le())
            self._debug['base_opcode']['end'] = self._io.pos()
            if self.base_opcode != SummoningInteract.Iopcode.end_commandlist:
                self._debug['contents']['start'] = self._io.pos()
                self.contents = []
                i = 0
                while True:
                    if not 'arr' in self._debug['contents']:
                        self._debug['contents']['arr'] = []
                    self._debug['contents']['arr'].append({'start': self._io.pos()})
                    _ = SummoningInteract.ConvOpcode(self._io, self, self._root)
                    self.contents.append(_)
                    self._debug['contents']['arr'][len(self.contents) - 1]['end'] = self._io.pos()
                    if _.opcode == SummoningInteract.Iopcode.end_command:
                        break
                    i += 1
                self._debug['contents']['end'] = self._io.pos()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["count", "text_offset", "offsets"]
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
            self._debug['text_offset']['start'] = self._io.pos()
            self.text_offset = self._io.read_u2le()
            self._debug['text_offset']['end'] = self._io.pos()
            self._debug['offsets']['start'] = self._io.pos()
            self.offsets = [None] * (self.count)
            for i in range(self.count):
                if not 'arr' in self._debug['offsets']:
                    self._debug['offsets']['arr'] = []
                self._debug['offsets']['arr'].append({'start': self._io.pos()})
                self.offsets[i] = self._io.read_u4le()
                self._debug['offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['offsets']['end'] = self._io.pos()


    class ConvOpcode(KaitaiStruct):
        SEQ_FIELDS = ["opcode", "args"]
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opcode']['start'] = self._io.pos()
            self.opcode = KaitaiStream.resolve_enum(SummoningInteract.Iopcode, self._io.read_u2le())
            self._debug['opcode']['end'] = self._io.pos()
            self._debug['args']['start'] = self._io.pos()
            _on = self.opcode
            if _on == SummoningInteract.Iopcode.unknown38:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.run_procedure:
                self.args = SummoningInteract.OpcodeArgs(u"t", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.give_item:
                self.args = SummoningInteract.OpcodeArgs(u"o", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown40:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.emit_keyword:
                self.args = SummoningInteract.OpcodeArgs(u"k", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown42:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused11:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown37:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.set_variable:
                self.args = SummoningInteract.OpcodeArgs(u"Vv", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown35:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.receive_keyword:
                self.args = SummoningInteract.OpcodeArgs(u"k", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown7:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown28:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused33:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.check_items:
                self.args = SummoningInteract.OpcodeArgs(u"uuu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.terminate_reset:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown17:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown12:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused32:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.heal_character:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.player_emit_text:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.start_conversation:
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
            elif _on == SummoningInteract.Iopcode.check_var_neq:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.restore:
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown45:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown15:
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.give_items:
                self.args = SummoningInteract.OpcodeArgs(u"oooooo", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.check_item_wearing:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown25:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.check_var_eq:
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            self._debug['args']['end'] = self._io.pos()



