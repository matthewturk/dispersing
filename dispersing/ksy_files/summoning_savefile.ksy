meta:
  id: summoning_savefile
  file-extension: "SAV"
  endian: le
seq:
  - id: copyright_messages
    size: 0x100
  - id: save_game_name
    size: 0x32
    type: strz
    encoding: ascii
  - id: num_levels
    type: s2
  - id: levels
    type: level_info
    repeat: expr
    repeat-expr: num_levels - 1
  - id: level_terminator
    contents: [0xff, 0xff]
  - id: unknown
    size: 0x54f7
  - id: character_info
    size: 0x326
  - id: object_table
    size: 10000
types:
  level_info:
    seq:
      - id: level_id
        type: s2
      - id: unknown
        type: u4
      - id: level_size
        type: u2
      - id: level_info
        size: 0x2800
