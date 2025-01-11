meta:
  id: darkspyre_objdat
  file-extension: dat
  endian: le
seq:
  - id: nitems
    type: u2
  - id: fill
    type: u1
  - id: iteminfo
    size: 57
    repeat: expr
    repeat-expr: nitems
  - id: names
    type: strz
    encoding: ascii
    repeat: expr
    repeat-expr: nitems
