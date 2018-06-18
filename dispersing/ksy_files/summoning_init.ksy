meta:
  id: summoning_init
  file-extension: ""
  endian: le
seq:
    # 333 seems to be offset for items
    # 566 is something else... fonts?
    # 799 is people
    # 1487 is music
    # array([ 1232,  1315,  1440,   100,   333,   566,   799,  1487,   894,
    #    919,   963,  1012,  1080,  1186,  7913, 13583,  2582, 25126,
    #   9762,  7972, 10794, 13361, 13592, 11312, 11309, 12333,  7980,
    #   3626,  9510,  7985,  7696,  7951,  7441,  7452,  7439,  7440,
    #   6672,  7440,  7437,  7697,  7185,  3342,  2854,  1573,   294,
    #   2850,  2086, 13605, 13590, 13846], dtype=uint16)
    # We eventually have spells.
  - id: count1
    type: u2
  - id: offset1
    type: u2
  - id: offset2
    type: u2
