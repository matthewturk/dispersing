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
      - id: wall_flags
        type: u1
        enum: tile_flags
      - id: wall_args
        if: wall_flags != tile_flags::nothing and wall_flags != tile_flags::movable_object
        type:
          switch-on: wall_flags
          cases:
            tile_flags::movable_object: u1
            tile_flags::unknown2: u1
            tile_flags::teleporter_dest: teleporter_info
            tile_flags::unknown4: u1
            tile_flags::unknown5: portal_info
            tile_flags::unknown6: u2
            tile_flags::teleporter: teleporter_info
            tile_flags::level_exit: portal_info
            tile_flags::npc: u1
            tile_flags::unknown10: u1
            tile_flags::mouth: u1
      - id: floor_flags
        type: u1
        enum: tile_flags
      - id: floor_args
        if: floor_flags != tile_flags::nothing
        type:
          switch-on: floor_flags
          cases:
            tile_flags::movable_object: u1
            tile_flags::unknown2: u1
            tile_flags::teleporter_dest: teleporter_info
            tile_flags::unknown4: u1
            tile_flags::unknown5: portal_info
            tile_flags::unknown6: u2
            tile_flags::teleporter: teleporter_info
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
        type: u1
        repeat: expr
        repeat-expr: size
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
  level_props:
    seq:
      - id: internal_wall_edges
        type: s2
      - id: floor
        type: s2
      - id: floor_special_tile
        type: s2
      - id: wall_edges
        type: s2
      - id: keys_switches
        type: s2
      - id: door
        type: s2
      - id: unk7
        type: s2
      - id: unk8
        type: s2
      - id: unk9
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
    0: nothing
    1: movable_object
    2: unknown2
    3: teleporter_dest
    4: unknown4
    5: unknown5
    6: unknown6
    7: teleporter
    8: level_exit
    9: npc
    10: unknown10
    11: mouth
