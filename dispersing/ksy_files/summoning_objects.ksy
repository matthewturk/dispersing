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
      - id: col0
        type: u1
      - id: object_name_id
        type: u1
      - id: weight
        type: u1
# Field three seems to be related to capacity.
# Chest, 8 items:
# >>> np.unpackbits(np.array([167], 'u1'))
# array([1, 0, 1, 0, 0, 1, 1, 1], dtype=uint8)
# Sack, 10 items:
# >>> np.unpackbits(np.array([233], 'u1'))
# array([1, 1, 1, 0, 1, 0, 0, 1], dtype=uint8)
      - id: container_flags
        type: u1
      - id: col4
        type: u1
      - id: col5
        type: u1
      - id: col6
        type: u1
      - id: col7
        type: u1
      - id: col8
        type: u1
      - id: col9
        type: u1
      - id: image_id
        type: u1
      - id: col11
        type: u1
      - id: col12
        type: u1
      - id: obj_type
        type: u1
        enum: object_categories
      - id: col14
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
