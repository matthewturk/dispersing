meta:
  id: summoning_datasegment
  file-extension: .bin
  endian: le
  imports:
    - summoning_objects
instances:
  pc_info:
    pos: 0x2325
    type: character_position
  npc_info:
    pos: 0x2325 + 0x22
    type: character_position
    repeat: expr
    repeat-expr: 99
  character_info:
    pos: 0x6d29
    type: character_record
  spell_table:
    pos: 0x6d95
    type: spell_info
    repeat: expr
    repeat-expr: 40
  object_template_table_ptr:
    pos: 0x7c9f
    type: u2
  object_template_table_count:
    pos: 0x870c
    type: u2
  object_template_table:
    pos: _root.object_template_table_ptr
    type: object_record
    repeat: expr
    repeat-expr: _root.object_template_table_count
  keywords_table_ptr:
    pos: 0x8cbd
    type: u2
  keywords_table:
    pos: _root.keywords_table_ptr
    size: 20
types:
  spell_info:
    seq:
      - id: elem1
        type: u1
      - id: elem2
        type: u1
      - id: elem3
        type: u1
      - id: elem4
        type: u1
      - id: elem5
        type: u1
      - id: gestures
        type: str
        size: 9
        encoding: ascii
  object_record:
    seq:
      # the first column gives, in the upper bits, the AC bonus
      # to get AC bonus, ((col0 >> 4) & 15)
      - id: ac_bonus
        type: b4
      - id: col0 # the size of the object
        type: b4
      - id: object_name_id
        type: u1
      - id: weight
        type: u1
      # Field three seems to be related to capacity.
      # Quiver, 12 items, only arrows
      # Chest, 8 items:
      # >>> np.unpackbits(np.array([167], 'u1'))
      # array([1, 0, 1, 0, 0, 1, 1, 1], dtype=uint8)
      # Sack, 10 items:
      # >>> np.unpackbits(np.array([233], 'u1'))
      # array([1, 1, 1, 0, 1, 0, 0, 1], dtype=uint8)
      - id: container_flags # 0xf0 is the size it can contain
        type: u1
      - id: col4
        type: u1
      - id: col5
        type: u1
      # col6 is projectile info
      - id: act1_dmg
        type: b4
      - id: act1_flags
        type: b4
      - id: act2_dmg
        type: b4
      - id: act2_flags
        type: b4
      - id: act3_dmg
        type: b4
      - id: act3_flags
        type: b4
      - id: charges
        type: u1
      - id: image_id
        type: u1
        # col11 0x80 checked in the random object routine, 0x7f in
        # helmetshirtsboots. might be something about wearable.
      - id: col11
        type: u1
      # col12 seems to be a key for the subroutine to call when it gets used
      - id: subroutine_id
        type: u1
      - id: obj_type
        type: u1
        enum: object_categories
      - id: col14
        type: u1
  character_attributes:
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
  character_record:
    seq:
      - id: character_name
        type: str
        encoding: ascii
        size: 26
      - id: unknown1
        size: 4
      - id: magic_levels
        type: u1
        repeat: expr
        repeat-expr: 4
      - id: weapon_levels
        type: u1
        repeat: expr
        repeat-expr: 4
      - id: character_level
        type: u1
      - id: current_magic_level_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: next_magic_level_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: current_weapon_level_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: next_weapon_level_exp
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: current_experience
        type: u2
      - id: next_experience
        type: u2
      - id: next_level_experience
        type: u2
      - id: unknown2
        type: u2
      - id: hp_current
        type: u2
      - id: hp_max
        type: u2
      - id: mp_current
        type: u2
      - id: mp_max
        type: u2
      - id: armor_class
        type: u2
      - id: current_attributes
        type: character_attributes
      - id: max_attributes
        type: character_attributes
  character_position:
    seq:
      - id: x_pos_32
        type: u2
      - id: y_pos_32
        type: u2
      - id: maybe_num_charges
        type: u2
      - id: unknown1
        type: u2
      - id: final_object
        type: u2
      - id: maybe_direction
        type: u1
      - id: unknown2
        type: u1
      - id: unknown3
        type: u1
      - id: unknown4
        type: u1
      - id: maybe_creation_time
        type: u2
      - id: unknown5
        type: u1
      - id: unknown6
        type: u1
      - id: unknown7
        type: u1
      - id: unknown8
        type: u1
      - id: unknown9
        type: u1
      - id: index
        type: u1
      - id: unknown10
        type: u1
      - id: unk_field
        type: u1
      - id: base_npc_id
        type: u1
      - id: unknown11
        type: u1
      - id: sprite_id
        type: u2
      - id: unknown12
        type: u2
      - id: maybe_current_hp
        type: u2
      - id: unknown13
        type: u1
      - id: unknown14
        type: u1

enums:
  object_categories:
    0: helmet
    1: shirt
    2: boots
    3: gloves
    4: quiver
    5: medallion
    6: object
    7: arrow
    8: bottle
    73: sword_1handed
    74: shield_axe
    76: projectile
    201: sword_2handed
    202: staff_of_the_serpent
    203: polearm
    204: bow
