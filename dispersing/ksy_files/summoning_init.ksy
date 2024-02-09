meta:
  id: summoning_init
  file-extension: ""
  endian: le
seq:
  - id: sprite_offsets
    type: sprite_offsets
  - id: unknown1
    type: unknown1_t
  - id: unknown2
    size: 256
  - id: unknown3
    size: 256
  - id: unknown4
    size: 96
  - id: unknown5
    size: 1536
  - id: spell_cost # one for each spell
    type: u1
    repeat: expr
    repeat-expr: 40
  - id: spell_dice # 3 for each spell
    type: spell_info
    repeat: expr
    repeat-expr: 40
  - id: spells # spell info
    size: 9
    type: str
    encoding: ascii
    repeat: expr
    repeat-expr: 40
  - id: unknown8
    size: 16
  - id: unknown9
    size: 11
  - id: unknown10
    repeat: expr
    repeat-expr: 20
    type: unknown10_t
  - id: unknown11
    size: 3
types:
  sprite_offsets:
    seq:
      - id: intro_anim_offset
        type: u2
      - id: ingame_anim_offset
        type: u2
      - id: endgame_anim_offset
        type: u2
      - id: small_object
        type: s2
      - id: worn_object
        type: s2
      - id: tiny_object
        type: s2
      - id: people
        type: s2
      - id: music
        type: s2
      - id: scroll
        type: s2
      - id: char_anim # character components
        type: s2
      - id: item_anim # held items
        type: s2
      - id: terrain
        type: s2
      - id: npc
        type: s2
      - id: wall_decoration
        type: s2
  unknown10_t:
    seq:
      - id: bitfield1
        type: b1le
      - id: bitfield2
        type: b1le
      - id: blank
        type: b6le
  unknown1_t:
    seq:
      - id: count
        type: u1
      - id: values
        type: value_pair
        repeat: expr
        repeat-expr: count
  value_pair:
    seq:
      - id: val1
        type: s1
      - id: val2
        type: s1
  unknown5_t:
    seq:
      - id: val1
        type: s1
      - id: val2
        type: s1
      - id: val3
        type: s1
      - id: val4
        type: s1
  spell_info:
    seq:
      - id: num_dice
        type: u1
      - id: dice_faces
        type: u1
      - id: offset_dice_faces
        type: u1
