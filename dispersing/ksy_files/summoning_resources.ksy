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
    type: resource_record(_index)
    repeat: expr
    repeat-expr: count
types:
  resource_record:
    params:
      - id: i
        type: u4
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
      - id: contents
        size: record_end - _root._io.pos
    instances:
      record_start:
        value: '_parent.offsets[i]'
      record_end:
        value: 'i < _parent.count - 1 ? _parent.offsets[i + 1] : _root._io.size'
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
