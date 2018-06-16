meta:
  id: summoning_resources
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u4
  - id: offsets
    type: u4
    repeat: expr
    repeat-expr: count
  - id: records
    type: resource_record
    repeat: expr
    repeat-expr: count
types:
  resource_record:
    seq:
      - id: ehmagic
        contents: 'EH'
      - id: type
        enum: record_types
        type: u1
      - id: header_size
        type: u2
      - id: header
        type: 
          switch-on: type
          cases:
            record_types::sprite: sprite_header
            _: empty
      - id: body
        size: 1
  sprite_header:
    seq:
      - id: height
        type: u2
      - id: count
        type: u1
      - id: width
        type: u2
      - id: algo
        type: u2
  empty:
    seq:
      - id: contents
        size: 10
enums:
  record_types:
    1: sprite
    2: unknown2
    5: unknown3
