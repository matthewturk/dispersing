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
    size: 2048
  - id: unknown3
    size: 256
  - id: spells
    size: 9
    repeat: expr
    repeat-expr: 40
  - id: unknown9
    type: s1
    repeat: expr
    repeat-expr: 51
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
  unknown1_t:
    seq:
      - id: count
        type: u1
      - id: values
        type: s2
        repeat: expr
        repeat-expr: count
