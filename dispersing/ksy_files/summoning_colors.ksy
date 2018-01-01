meta:
  id: summoning_colors
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u1
  - id: palettes
    type: palette
    repeat: expr
    repeat-expr: count
types:
  palette:
    seq:
      - id: colors
        type: rgb
        repeat: expr
        repeat-expr: 16
  rgb:
    # Note that these are 0 .. 63, not 0 .. 255
    seq:
      - id: red
        type: u1
      - id: green
        type: u1
      - id: blue
        type: u1
