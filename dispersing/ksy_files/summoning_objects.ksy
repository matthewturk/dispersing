meta:
  id: summoning_object
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u2
  - id: name_offset
    type: u2
  - id: object
    type: object_record
    repeat: expr
    repeat-expr: count
types:
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
#- id: container_flags # 0xf0 is the size it can contain
# 0x0f is the number of items
#        type: u1
      - id: container_size
        type: b4
      - id: container_capacity
        type: b4
      - id: act1_icon
        type: u1
      - id: act2_icon
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
    instances:
      text_record:
        value: 'object_name_id + _root.name_offset'
      small_image_record:
        value: 'image_id + 100'
      large_image_record:
        value: 'image_id + 333'
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
