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
        repeat-until: _.opcode == iopcode::end_commandlist
  sequence:
    seq:
      - id: opcode
        type: s2
        enum: iopcode
      - id: contents
        if: opcode != iopcode::end_commandlist
        type: s2
        repeat: until
        repeat-until: _ == -4
enums:
  iopcode:
    -4: end_command
    -3: continue_conversation
    -2: start_conversation
    -1: end_commandlist
    6: receive_keyword
    9: unknown9
    18: emit_text
    19: emit_keyword
    22: set_variable
    31: turn_on_teleporter
    20: take_item
    22: set_variable
    26: heal_character
    31: turn_on_teleporter
    41: give_items
  conv_flags:
     4: speak_again
     5: speak_first
     13: again_fully_healed
     13: first_fully_healed #??

# Arguments:
#  18: 1
#  19: 1
#  
