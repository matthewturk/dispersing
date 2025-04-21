meta:
  id: summoning_coredump
  file-extension: .bin
  endian: le
  imports:
    - summoning_datasegment
instances:
  ds:
    pos: 0x2beb * 16
    type: summoning_datasegment
    size-eos: true