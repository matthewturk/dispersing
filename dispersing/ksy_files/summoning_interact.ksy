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
            iopcode::end_command: opcode_args("")
            iopcode::continue_conversation: opcode_args("")
            iopcode::start_conversation: opcode_args("")
            iopcode::end_commandlist: opcode_args("")
            iopcode::unknown4: opcode_args("")
            iopcode::unknown5: opcode_args("")
            iopcode::receive_keyword: opcode_args("k")
            iopcode::interaction_end: opcode_args("")
            iopcode::check_items: opcode_args("uuu")
            iopcode::check_var_neq: opcode_args("uu")
            iopcode::check_var_eq: opcode_args("uu")
            iopcode::unused11: opcode_args("")
            iopcode::unknown12: opcode_args("u")
            iopcode::check_max_health: opcode_args("")
            iopcode::count_coins: opcode_args("u")
            iopcode::check_wearing_any_item: opcode_args("u")
            iopcode::check_item_wearing: opcode_args("uu")
            iopcode::unknown17: opcode_args("")
            iopcode::emit_text: opcode_args("t")
            iopcode::emit_keyword: opcode_args("k")
            iopcode::take_item: opcode_args("o")
            iopcode::terminate_reset: opcode_args("")
            iopcode::set_variable: opcode_args("Vv")
            iopcode::reset_variable: opcode_args("u")
            iopcode::give_item: opcode_args("o")
            iopcode::unknown25: opcode_args("uu")
            iopcode::heal_character: opcode_args("")
            iopcode::unknown27: opcode_args("")
            iopcode::toggle_transcription: opcode_args("u")
            iopcode::unknown29: opcode_args("u")
            iopcode::unknown30: opcode_args("")
            iopcode::run_procedure: opcode_args("t")
            iopcode::continue: opcode_args("")
            iopcode::end_game_sequence: opcode_args("")
            iopcode::quit: opcode_args("")
            iopcode::save_game: opcode_args("")
            iopcode::restore_game: opcode_args("")
            iopcode::delete_save_game: opcode_args("")
            iopcode::unknown38: opcode_args("u")
            iopcode::player_emit_text: opcode_args("uu")
            iopcode::unknown40: opcode_args("u")
            iopcode::give_items: opcode_args("oooooo")
            iopcode::unknown42: opcode_args("")
            iopcode::teach_spell: opcode_args("u")
            iopcode::unknown44: opcode_args("u")
            iopcode::return_to_main_menu: opcode_args("uu")
            iopcode::get_save_game_name: opcode_args("uu")
  opcode_args:
    params:
      - id: targs
        type: str
    seq:
      - id: args
        type: s2
        repeat: expr
        repeat-expr: targs.length
# conv 20 has the iron smith, who needs chunk of iron ore and strip of cured leather. and mithril ore.
# opcodes seem to have the args and the opcode combined.
enums:
  iopcode:
    65532: end_command          # 0 args
    65533: continue_conversation # 0 args
    65534: start_conversation   # 0 args
    65535: end_commandlist      # 0 args
    4: unknown4                 # 0 args something to do with initiating?
    5: unknown5                 # 0 args
    6: receive_keyword          # 1 arg
    7: interaction_end          # 0 args
    8: check_items              # 3 args: item type, item type, item type
    9: check_var_gt             # 2 args? checking variable? var != val?
    10: check_var_eq            # 2 args? checking variable?
    11: check_var_lt                # 0 args
    12: unknown12               # 1 arg, maybe object category & 2?
    13: check_max_health        # 0 arg
    14: count_coins             # 1 arg - required number
    15: check_wearing_any_item  # 1 arg - inventory position
    16: check_item_wearing      # 2 args - position and item. check if wearing.
    17: unknown17               # 0 args - check not null? but no args
    18: emit_text               # 1 arg
    19: emit_keyword            # 1 arg
    20: take_item               # 1 arg
    21: terminate_reset         # 0 args some form of termination
    22: set_variable            # 2 args
    23: increment_variable      # 1 arg, does something to variable
    24: give_item               # 1 arg
    25: unknown25               # 2 args, maybe another head and text.  calls kill_charpos on the NPC.
    26: heal_character          # 0 arg
    27: unknown27               # 0 arg -- maybe something with saves?  It calls memory-fill with 0xc.
    28: toggle_transcription    # 1 arg
    29: unknown29               # 1 arg?
    30: unknown30               # 0 arg
    31: run_procedure           # 1 args -- procedure id
    32: continue                # 0 args
    33: end_game_sequence       # 0 args
    34: quit                    # 0 args
    35: save_game               # 0 args
    36: restore_game            # 0 args
    37: delete_save_game        # 0 args
    38: unknown38               # 1 arg?
    39: player_emit_text        # 2 args -- player character head, then text
    40: unknown40               # 1 arg
    41: give_items              # ... (6 arg?)
    42: unknown42               # 0 arg
    43: teach_spell             # 1 arg hand movement?  give?
    44: unknown44               # 1 arg (tr[22,5])
    45: return_to_main_menu     # 2 args? 1st is something, 2nd is text
    46: get_save_game_name      # 2 args? 1st is something (var?) and 2nd is text
  conv_flags:
     4: speak_again
     5: speak_first
     13: again_fully_healed
     #13: first_fully_healed #??

# Arguments:
#  6: 1
#  18: 1
#  19: 1
#
