meta:
  id: summoning_colors
  file-extension: ""
  endian: le
seq:
  - id: ncolors
    type: u1
  - id: palettes
    type: palette
    repeat: expr
    repeat-expr: (_root._io.size - 1) / (ncolors * 3)
types:
  palette:
    seq:
      - id: colors
        type: rgb
        repeat: expr
        repeat-expr: _root.ncolors
  rgb:
    # Note that these are 0 .. 63, not 0 .. 255
    seq:
      - id: red
        type: u1
      - id: green
        type: u1
      - id: blue
        type: u1
