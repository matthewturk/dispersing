# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SummoningInteract(KaitaiStruct):

    class ConvFlags(IntEnum):
        speak_again = 4
        speak_first = 5
        again_fully_healed = 13

    class Iopcode(IntEnum):
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
    SEQ_FIELDS = ["file_header", "npc_interactions"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SummoningInteract, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_header']['start'] = self._io.pos()
        self.file_header = SummoningInteract.Header(self._io, self, self._root)
        self._debug['file_header']['end'] = self._io.pos()
        self._debug['npc_interactions']['start'] = self._io.pos()
        self._debug['npc_interactions']['arr'] = []
        self.npc_interactions = []
        for i in range(self.file_header.count):
            self._debug['npc_interactions']['arr'].append({'start': self._io.pos()})
            self.npc_interactions.append(SummoningInteract.NpcInteraction(self._io, self, self._root))
            self._debug['npc_interactions']['arr'][i]['end'] = self._io.pos()

        self._debug['npc_interactions']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.file_header._fetch_instances()
        for i in range(len(self.npc_interactions)):
            pass
            self.npc_interactions[i]._fetch_instances()


    class ConvOpcode(KaitaiStruct):
        SEQ_FIELDS = ["opcode", "args"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInteract.ConvOpcode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['opcode']['start'] = self._io.pos()
            self.opcode = KaitaiStream.resolve_enum(SummoningInteract.Iopcode, self._io.read_u2le())
            self._debug['opcode']['end'] = self._io.pos()
            self._debug['args']['start'] = self._io.pos()
            _on = self.opcode
            if _on == SummoningInteract.Iopcode.check_item_wearing:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.check_items:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uuu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.check_var_eq:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.check_var_neq:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.continue_conversation:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.emit_keyword:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"k", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.emit_text:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"t", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.end_command:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.end_commandlist:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.give_item:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"o", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.give_items:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"oooooo", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.heal_character:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.player_emit_text:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.receive_keyword:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"k", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.restore:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.run_procedure:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"t", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.set_flag_true:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.set_variable:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"Vv", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.start_conversation:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.switch_npc_portrait:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.take_item:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"o", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.teach_spell:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.terminate_reset:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown12:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown13:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown14:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown15:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown17:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown23:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown25:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown27:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown28:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown29:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown30:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown34:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown35:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown37:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown38:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown4:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown40:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"u", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown45:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown46:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"uu", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown5:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unknown7:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused11:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused32:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            elif _on == SummoningInteract.Iopcode.unused33:
                pass
                self.args = SummoningInteract.OpcodeArgs(u"", self._io, self, self._root)
            self._debug['args']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.opcode
            if _on == SummoningInteract.Iopcode.check_item_wearing:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.check_items:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.check_var_eq:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.check_var_neq:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.continue_conversation:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.emit_keyword:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.emit_text:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.end_command:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.end_commandlist:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.give_item:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.give_items:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.heal_character:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.player_emit_text:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.receive_keyword:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.restore:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.run_procedure:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.set_flag_true:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.set_variable:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.start_conversation:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.switch_npc_portrait:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.take_item:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.teach_spell:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.terminate_reset:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown12:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown13:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown14:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown15:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown17:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown23:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown25:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown27:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown28:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown29:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown30:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown34:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown35:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown37:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown38:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown4:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown40:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown45:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown46:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown5:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unknown7:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unused11:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unused32:
                pass
                self.args._fetch_instances()
            elif _on == SummoningInteract.Iopcode.unused33:
                pass
                self.args._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["count", "text_offset", "offsets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInteract.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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
            self._debug['offsets']['arr'] = []
            self.offsets = []
            for i in range(self.count):
                self._debug['offsets']['arr'].append({'start': self._io.pos()})
                self.offsets.append(self._io.read_u4le())
                self._debug['offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['offsets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.offsets)):
                pass



    class NpcInteraction(KaitaiStruct):
        SEQ_FIELDS = ["npc_name", "size", "operations"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInteract.NpcInteraction, self).__init__(_io)
            self._parent = _parent
            self._root = _root
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
            self._debug['operations']['arr'] = []
            self.operations = []
            i = 0
            while True:
                self._debug['operations']['arr'].append({'start': self._io.pos()})
                _ = SummoningInteract.Sequence(self._io, self, self._root)
                self.operations.append(_)
                self._debug['operations']['arr'][len(self.operations) - 1]['end'] = self._io.pos()
                if _.base_opcode == SummoningInteract.Iopcode.end_commandlist:
                    break
                i += 1
            self._debug['operations']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.operations)):
                pass
                self.operations[i]._fetch_instances()



    class OpcodeArgs(KaitaiStruct):
        SEQ_FIELDS = ["args"]
        def __init__(self, targs, _io, _parent=None, _root=None):
            super(SummoningInteract.OpcodeArgs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.targs = targs
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['args']['start'] = self._io.pos()
            self._debug['args']['arr'] = []
            self.args = []
            for i in range(len(self.targs)):
                self._debug['args']['arr'].append({'start': self._io.pos()})
                self.args.append(self._io.read_s2le())
                self._debug['args']['arr'][i]['end'] = self._io.pos()

            self._debug['args']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.args)):
                pass



    class Sequence(KaitaiStruct):
        SEQ_FIELDS = ["base_opcode", "contents"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SummoningInteract.Sequence, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['base_opcode']['start'] = self._io.pos()
            self.base_opcode = KaitaiStream.resolve_enum(SummoningInteract.Iopcode, self._io.read_u2le())
            self._debug['base_opcode']['end'] = self._io.pos()
            if self.base_opcode != SummoningInteract.Iopcode.end_commandlist:
                pass
                self._debug['contents']['start'] = self._io.pos()
                self._debug['contents']['arr'] = []
                self.contents = []
                i = 0
                while True:
                    self._debug['contents']['arr'].append({'start': self._io.pos()})
                    _ = SummoningInteract.ConvOpcode(self._io, self, self._root)
                    self.contents.append(_)
                    self._debug['contents']['arr'][len(self.contents) - 1]['end'] = self._io.pos()
                    if _.opcode == SummoningInteract.Iopcode.end_command:
                        break
                    i += 1
                self._debug['contents']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.base_opcode != SummoningInteract.Iopcode.end_commandlist:
                pass
                for i in range(len(self.contents)):
                    pass
                    self.contents[i]._fetch_instances()





