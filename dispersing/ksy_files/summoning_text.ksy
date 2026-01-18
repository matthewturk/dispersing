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
    type: xorstr_wrapper
    process: xor(0xda)
    terminator: 0x0
    repeat: expr
    repeat-expr: count
types:
  xorstr_wrapper:
    seq:
     - id: text
       type: str
       size-eos: true
       encoding: ascii
