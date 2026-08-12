meta:
  id: darkspyre_map
  file-extension: map
  endian: le
seq:
  - id: height
    type: u1
  - id: width
    type: u1
  - id: map
    size: width * height
  - id: nitems
    type: u1
  - id: items
    type: item_info(0x40, 6)
    repeat: expr
    repeat-expr: nitems
  - id: nitems2
    type: u1
  - id: items2
    type: item_info(0x80, 6)
    repeat: expr
    repeat-expr: nitems2
types:
  item_info:
    params:
      - id: magic
        type: u1
      - id: nvals
        type: u1
    seq:
      - id: v1
        type: u1
        valid: magic
      - id: vals
        type: u1
        repeat: expr
        repeat-expr: nvals
