meta:
  id: darkspyre_faces
  file-extension: darkspyre_faces
  endian: le
seq:
  - id: count
    type: u4
  - id: offsets
    repeat: expr
    repeat-expr: count
    type: u4
  - id: faces
    type: face(_index)
    repeat: expr
    repeat-expr: count
types:
  face:
    params:
      - id: i
        type: u2
    seq:
      - id: contents
        size: record_end - record_start
    instances:
      record_start:
        value: _parent.offsets[i]
      record_end:
        value: 'i < _parent.count - 1 ? _parent.offsets[i + 1] : _root._io.size'
