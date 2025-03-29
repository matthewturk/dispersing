meta:
  id: summoning_levels
  file-extension: ""
  endian: le
seq:
  - id: file_header
    type: header
  - id: levels
    type: level
    repeat: expr
    repeat-expr: file_header.count
types:
  header:
    seq:
      - id: count
        type: u4
      - id: offsets
        type: u4
        repeat: expr
        repeat-expr: count
  item_data:
    seq:
      - id: x
        type: u1
      - id: y
        type: u1
      - id: info
        if: x != 255
        type: tile_info
  tile_info:
    seq:
      - id: n1
        type: u1
      - id: items
        type: u1
        repeat: expr
        repeat-expr: n1
      - id: big_wooden
        type: u1
      - id: floor_flags
        type: u1
        enum: tile_flags
      - id: floor_args
        if: floor_flags != tile_flags::nothing
        type:
          switch-on: floor_flags
          cases:
            tile_flags::display_overlay: u1
            tile_flags::unknown2: u1
            tile_flags::teleporter_dest: procedure
            tile_flags::unknown4: u1
            tile_flags::unknown5: portal_info
            tile_flags::boulder: u2
            tile_flags::teleporter: procedure
            tile_flags::level_exit: portal_info
            tile_flags::npc: u1
            tile_flags::unknown10: u1
            tile_flags::mouth: u1
  portal_info:
    seq:
      - id: opcode
        type: u1
      - id: level
        type: u1
      - id: dest_x
        type: u1
      - id: dest_y
        type: u1
  teleporter_info:
    seq:
      - id: unknown
        size: 5
  speech_strings:
    seq:
      - id: size
        type: u2
      - id: text
        size: size
  other_data:
    seq:
      - id: size
        type: u2
      - id: contents
        type: procedure_defs
        size: size
        # Some notes on this:
        #   It once again seems to have coordinates embedded.  For instance, in
        #   level 0, there's this sequence:
        #   1, 0, 11, 4, 0, 0, 1, 2
        # This seems to me to be an opcode (1), maybe a set of flags for it,
        # and then the entry point, then two additional flags, and a
        # destination.  It's also possible that the 1 and 2 are not the
        # destination.
        # Next set:
        #   13, 18, 0, 0, 1, 11
        # Funny thing is that we teleport from 11,4 to what amounts to the same
        # location as objects 229, 226, 232, which is 2, 3
        # So where do we find out that info?
  procedure_defs:
    seq:
        - id: procedures
          type: procedure_info
          repeat: eos
  procedure_info:
    seq:
      - id: opcode_count
        type: u1
      - id: procedures
        type: procedure
        repeat: expr
        repeat-expr: opcode_count
  procedure:
    seq:
      - id: opcode
        type: u1
        enum: procedure_opcode
      - id: arg1
        type: u1
      - id: arg2
        type: u1
      - id: arg3
        type: u1
      - id: arg4
        type: u1
  level_props:
    seq:
      - id: wall_tiles
        type: s2
      - id: floor_tiles
        type: s2
      - id: floor_special_tiles
        type: s2
      - id: gate_tiles
        type: s2
      - id: keys_switches
        type: s2
      - id: door_tiles
        type: s2
      - id: wall_decor_offsets
        type: s2
        repeat: expr
        repeat-expr: 4
      - id: blank11
        contents: [0, 0]
      - id: unk12
        type: s2
      - id: big_wooden_thing
        type: s2
      - id: big_boulder
        type: s2
      - id: blank15
        contents:
          [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
          ]
    instances:
      wall_corners:
        value: 'wall_tiles + 1'
  level:
    seq:
      - id: height
        type: u1
      - id: width
        type: u1
      - id: properties
        type: level_props
      - id: map
        size: width * height
      - id: items
        type: item_data
        repeat: until
        repeat-until: _.x == 255 and _.y == 255
      - id: speech
        type: speech_strings
      - id: other
        type: other_data
enums:
  tile_flags:
    1: display_overlay # "case_0" -- floordiv by ten to get offset index, frame is mod by ten
    2: unknown2 # "case_1"
    3: teleporter_dest # "case_4" -- actually a procedure opcode?
    4: unknown4 # "case_6"
    5: unknown5 # "case_10"
    6: boulder # "case_7"
    7: teleporter # "case_5"
    8: level_exit # "case_8"
    9: npc # "case_2"
    10: unknown10 # "case_3" -- sets occupied to | 0x20
    11: mouth # "case_9"
  procedure_opcode:
    0: teleporter_enable
                # 38 is a pit.  39 is a plate.
    1: unknown1 # Looks for tiles of values 38 and 39.  Maybe pit / plate?
    2: unknown2 # Looks for tiles of values 38 and 39.  Maybe pit / plate?
    3: unknown3
    4: unknown4
    5: unknown5
    6: unknown6
    7: unknown7
    8: shoot_projectile
    9: cast_spell
    10: unknown10 # it checks the occupied items and then sets a parameter elsewhere. Maybe it moves an object?
    11: create_object
