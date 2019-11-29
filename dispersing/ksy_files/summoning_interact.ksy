meta:
  id: summoning_interact
  file-extension: ""
  endian: le
seq:
  - id: file_header
    type: header
  - id: npc_interactions
    type: npc_interaction
    repeat: expr
    repeat-expr: file_header.count
types:
  header:
    seq:
      - id: count
        type: u2
      - id: text_offset
        type: u2
      - id: offsets
        type: u4
        repeat: expr
        repeat-expr: count
  npc_interaction:
    seq:
      - id: npc_name
        type: str
        encoding: ASCII
        size: 20
      - id: size
        type: u2
      - id: operations
        type: sequence
        repeat: until
        repeat-until: _.base_opcode == iopcode::end_commandlist
  sequence:
    seq:
     - id: base_opcode
       type: u2
       enum: iopcode
     - id: contents
       if: base_opcode != iopcode::end_commandlist
       type: conv_opcode
       repeat: until
       repeat-until: _.opcode == iopcode::end_command
  conv_opcode:
    seq:
      - id: opcode
        type: u2
        enum: iopcode
      - id: args
        type:
          switch-on: opcode
          cases:
            iopcode::end_command: opcode_0args
            iopcode::continue_conversation: opcode_0args
            iopcode::start_conversation: opcode_0args
            iopcode::end_commandlist: opcode_0args
            iopcode::unknown5: opcode_0args
            iopcode::receive_keyword: opcode_1args
            iopcode::unknown7: opcode_0args
            iopcode::unknown8: opcode_2args
            iopcode::unknown9: opcode_2args
            iopcode::unknown10: opcode_2args
            iopcode::unused11: opcode_0args
            iopcode::unknown12: opcode_1args
            iopcode::unknown13: opcode_0args
            iopcode::unknown14: opcode_1args
            iopcode::unknown15: opcode_1args
            iopcode::unknown16: opcode_2args
            iopcode::unknown17: opcode_0args
            iopcode::emit_text: opcode_1args
            iopcode::emit_keyword: opcode_1args
            iopcode::take_item: opcode_1args
            iopcode::unknown21: opcode_0args
            iopcode::set_variable: opcode_2args
            iopcode::unknown23: opcode_1args
            iopcode::give_item: opcode_1args
            iopcode::unknown25: opcode_2args
            iopcode::heal_character: opcode_0args
            iopcode::unknown27: opcode_0args
            iopcode::unknown28: opcode_1args
            iopcode::unknown29: opcode_1args
            iopcode::unknown30: opcode_0args
            iopcode::turn_on_teleporter: opcode_1args
            iopcode::unused32: opcode_0args
            iopcode::unused33: opcode_0args
            iopcode::unknown34: opcode_0args
            iopcode::unknown35: opcode_0args
            iopcode::restore: opcode_0args
            iopcode::unknown37: opcode_0args
            iopcode::unknown38: opcode_1args
            iopcode::unknown39: opcode_2args
            iopcode::unknown40: opcode_1args
            iopcode::give_items: opcode_6args
            iopcode::unknown42: opcode_0args
            iopcode::unknown43: opcode_1args
            iopcode::unknown44: opcode_1args
            iopcode::unknown45: opcode_2args
            iopcode::unknown46: opcode_2args
  opcode_0args:
    seq: []
  opcode_1args:
    seq:
      - id: arg1
        type: s2
  opcode_2args:
    seq:
      - id: arg1
        type: s2
      - id: arg2
        type: s2
  opcode_6args:
    seq:
      - id: arg1
        type: s2
      - id: arg2
        type: s2
      - id: arg3
        type: s2
      - id: arg4
        type: s2
      - id: arg5
        type: s2
      - id: arg6
        type: s2

# conv 20 has the iron smith, who needs chunk of iron ore and strip of cured leather. and mithril ore.
# opcodes seem to have the args and the opcode combined.
enums:
  iopcode:
    65532: end_command          # 0 args
    65533: continue_conversation # 0 args
    65534: start_conversation   # 0 args
    65535: end_commandlist      # 0 args
    5: unknown5                 # 0 args
    6: receive_keyword          # 1 arg
    7: unknown7                 # 0 args
    8: unknown8                 # some kind of receive? sometimes 2 arg, sometimes 1?
    9: unknown9                 # 2 args? checking variable? var != val?
    10: unknown10               # 2 args? checking variable?
    11: unused11                # 0 args
    12: unknown12               # 1 arg
    13: unknown13               # 0 arg
    14: unknown14               # 1 arg
    15: unknown15               # 1 arg
    16: unknown16               # 2 args - position and item. check if wearing.
    17: unknown17               # 0 args
    18: emit_text               # 1 arg
    19: emit_keyword            # 1 arg
    20: take_item               # 1 arg
    21: unknown21               # 0 args some form of termination
    22: set_variable            # 2 args
    23: unknown23               # 1 arg, does something to variable
    24: give_item               # 1 arg
    25: unknown25               # 2 args, maybe another head and text
    26: heal_character          # 0 arg
    27: unknown27               # 0 arg -- maybe something with saves?
    28: unknown28               # 1 arg
    29: unknown29               # 1 arg?
    30: unknown30               # 0 arg
    31: turn_on_teleporter      # 1 args -- teleporter id
    32: unused32                # 0 args
    33: unused33                # 0 args
    34: unknown34               # 0 args
    35: unknown35               # 0 args
    36: restore                 # 0 args
    37: unknown37               # 0 args
    38: unknown38               # 1 arg?
    39: unknown39               # 2 args -- player character head, then text
    40: unknown40               # 1 arg
    41: give_items              # ... (6 arg?)
    42: unknown42               # 0 arg
    43: unknown43               # 1 arg hand movement?  give?
    44: unknown44               # 1 arg (tr[22,5])
    45: unknown45               # 2 args? 1st is something, 2nd is text
    46: unknown46               # 2 args? 1st is something (var?) and 2nd is text
  conv_flags:
     4: speak_again
     5: speak_first
     13: again_fully_healed
     13: first_fully_healed #??

# Arguments:
#  6: 1
#  18: 1
#  19: 1
#
