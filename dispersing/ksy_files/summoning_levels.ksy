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
      - id: temporary_overlay
        type: u1
      - id: overlay_flags
        type: u1
        enum: overlay_flags
      - id: floor_args
        if: overlay_flags != overlay_flags::item_stack
        type:
          switch-on: overlay_flags
          cases:
            overlay_flags::decoration: u1
            overlay_flags::container: u1
            overlay_flags::teleporter_hidden: teleporter_info
            overlay_flags::floor_hazard: u1
            overlay_flags::unused: u1
            overlay_flags::toggle: u2
            overlay_flags::teleporter_active: teleporter_info
            overlay_flags::level_exit: portal_info
            overlay_flags::npc: u1
            overlay_flags::pressure_plate: u1
            overlay_flags::mouth: u1
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
      # A few notes!
      # The tile types 40 through 53 (inclusive) are special cases.
      # Tile 40 is the seal hole, which also somehow will change with pieces
      # added to it, which is in Broken Seal One.
      # Tiles 41 through 53 are the big gate in End Five.
      # I think that 23 is a keyhole, 24 is a hole, 25 is a switch, 26 is the
      # opposite switch.
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
      - id: wall_decor1
        type: s2
      - id: wall_decor2
        type: s2
      - id: wall_decor3
        type: s2
      - id: wall_overlay_tiles
        type: s2
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
  overlay_flags:
    0: item_stack
    1: decoration
    2: container
    3: teleporter_hidden
    4: floor_hazard
    5: unused
    6: toggle
    7: teleporter_active
    8: level_exit
    9: npc
    10: pressure_plate
    11: mouth
  procedure_opcode:
    0: teleporter_enable
    1: unknown1
    2: unknown2
    3: unknown3
    4: unknown4
    5: unknown5
    6: unknown6
    7: unknown7
    8: unknown8
    9: unknown9
    10: unknown10
    11: create_object
