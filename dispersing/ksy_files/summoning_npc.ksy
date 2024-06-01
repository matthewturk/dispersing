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
      - id: maybe_n_hit_dice # maybe n hit dice
        type: u1
      - id: damage_resistance # col4
        type: u1
      - id: damage_bonus # col5
        type: u1
        # seems like this is 0 or 2, where 2 requires specific conditions like
        # footwear removal and shadow weaver costume.  col6
      - id: conditionally_hostile 
        type: u1
      - id: sprite_id
        type: u1
      - id: col8
        type: u1
      - id: action
        type: u1
      - id: col10 # maybe accuracy
        type: u1
      - id: col11
        type: u1
      - id: magic_attack # not sure about this one; col12
        type: u1
        enum: magic_attack_types
      - id: weapon_vulnerabilities
        type: u1
        enum: weapon_classes
      - id: col14
        type: u1
      - id: behavior_flags
        type: u1
enums:
  weapon_classes:
    0: none
    9: edged
    10: bashing
    11: polearms
    12: projectile
  magic_attack_types:
    0: none
    1: stone
    3: poison
    4: fire
    5: lightning
    9: unknown
