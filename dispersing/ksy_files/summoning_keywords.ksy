meta:
  id: summoning_keywords
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u2
  - id: offsets
    type: u2
    repeat: expr
    repeat-expr: count
  - id: keyword
    type: strz
    encoding: ASCII
    repeat: expr
    repeat-expr: count
