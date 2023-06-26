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
    type: character_table
    size: 0x326
  - id: object_table
    size: 10000
types:
  level_info:
    seq:
      - id: level_id
        type: s2
      - id: level_size
        type: u4
      - id: level_info
        size: 0x49e2
  character_table:
    seq:
      - id: character_name
        type: strz
        encoding: ascii
        size: 30
      - id: unknown1
        type: u1
        repeat: expr
        repeat-expr: 59
      - id: current_attributes
        type: attributes
      - id: maximum_attributes
        type: attributes
      - id: unknown2
        size: 8
      - id: spells
        size: 14
        repeat: expr
        repeat-expr: 40
      - id: unknown3
        size: 137
  attributes:
    seq:
      - id: strength
        type: u1
      - id: agility
        type: u1
      - id: endurance
        type: u1
      - id: accuracy
        type: u1
      - id: talent
        type: u1
      - id: power
        type: u1
