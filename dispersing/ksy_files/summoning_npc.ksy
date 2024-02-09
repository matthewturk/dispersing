meta:
  id: summoning_npc
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u2
  - id: npcs
    type: npc
    repeat: expr
    repeat-expr: count
types:
  npc:
    seq:
      - id: npc_id
        type: u1
      - id: head_id
        type: u1
      - id: flags
        type: u1
      - id: col3
        type: u1
      - id: col4
        type: u1
      - id: col5
        type: u1
      - id: col6
        type: u1
      - id: sprite_id
        type: u1
      - id: body_sprite
        type: u1
      - id: action_dmg_ndice
        type: b4
      - id: action_dmg_nsides
        type: b4
      - id: agility
        type: u1
      - id: col11
        type: u1
      - id: col12
        type: u1
      - id: col13
        type: u1
      - id: col14
        type: u1
      - id: col15
        type: u1
