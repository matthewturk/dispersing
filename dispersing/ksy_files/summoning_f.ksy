meta:
  id: summoning_f
  file-extension: ""
  endian: le
seq:
  - id: count
    type: u2
  - id: unknown1
    type: u2
  - id: unknown2
    type: u2
  - id: num_character
    type: u2
  - id: records
    type: frecord
    repeat: expr
    repeat-expr: count
  - id: characters
    type: character
    repeat: expr
    repeat-expr: num_character
types:
  frecord:
    seq:
      - id: col1
        type: u1
      - id: col2
        type: u1
      - id: col3
        type: u1
      - id: col4
        type: u1
      - id: col5
        type: u1
      - id: col6
        type: u1
      - id: col7
        type: u1
      - id: col8
        type: u1
  character:
    seq:
      - id: name
        type: str
        size: 26
        terminator: 0
        encoding: ASCII
      - id: portrait
        type: u1
      - id: strength
        type: u1
      - id: agility
        type: u1
      - id: endurance
        type: u1
      - id: accuracy
        type: u1
      - id: talent
        type: u1
      - id: power
        type: u1
      - id: spell_type
        type: u1
      - id: weapon_type
        type: u1
