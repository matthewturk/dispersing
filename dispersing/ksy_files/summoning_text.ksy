meta:
  id: summoning_text
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u4
  - id: offsets
    type: u4
    repeat: expr
    repeat-expr: count
  - id: text
    type: xorstr
    repeat: expr
    repeat-expr: count
types:
  xorstrz:
    seq:
     - id: text
       type: str
       encoding: ascii
       terminator: 0xda
  xorstr:
    seq:
     - id: text
       process: xor(218)
       terminator: 0x0
    instances:
      value:
        value: text.as<xorstrz>
