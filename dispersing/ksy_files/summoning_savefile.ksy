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
      - id: magic_levels
        type: magic_levels
      - id: weapon_levels
        type: weapon_levels
      - id: character_level
        type: u1
      - id: current_magic_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: next_magic_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: current_weapon_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: next_weapon_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: current_exp
        type: u2
      - id: last_level_exp
        type: u2
      - id: next_level_exp
        type: u2
      - id: unknown1
        type: u2
      - id: hp_cur
        type: u2
      - id: hp_max
        type: u2
      - id: mp_cur
        type: u2
      - id: mp_max
        type: u2
      - id: armor_class
        type: u2
      - id: current_attributes
        type: attributes
      - id: maximum_attributes
        type: attributes
      - id: unknown2
        type: s1
      - id: agility_modifier
        type: s1
      - id: fatigue
        type: s1
      - id: unknown3
        size: 3
      - id: endurance_modifier
        type: s1
      - id: spells
        type: spell_record
        repeat: expr
        repeat-expr: 40
      - id: currently_memorized
        type: u1
        repeat: expr
        repeat-expr: 4
      - id: unknown4
        size: 133
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
  magic_levels:
    seq:
      - id: wizardry
        type: u1
      - id: sorcery
        type: u1
      - id: enchantry
        type: u1
      - id: healing
        type: u1
  weapon_levels:
    seq:
      - id: long_edged
        type: u1
      - id: hacking
        type: u1
      - id: polearms
        type: u1
      - id: projectile
        type: u1
  spell_record:
    seq:
      - id: memorized
        type: u1
      - id: cost
        type: u1
      - id: info
        size: 3
      - id: gestures
        type: strz
        encoding: ascii
        size: 9
