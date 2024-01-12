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
            record_types::font: font_header
            record_types::music: music_header
            _: generic_header(header_size)
      - id: contents
        type:
          switch-on: type
          cases:
            record_types::music: music_contents
        size: record_end - _root._io.pos
    instances:
      record_start:
        value: '_parent.offsets[i]'
      record_end:
        value: 'i < _parent.count - 1 ? _parent.offsets[i + 1] : _root._io.size'
  font_header:
    seq:
      - id: clip_info
        size: 128
      - id: font_sprite_header
        type: sprite_header
  sprite_header:
    seq:
      - id: field1
        type: u2
      - id: field2
        type: u1
      - id: width_over_eight
        type: u1
      - id: field_4
        type: u1
      - id: algo
        type: u1
      - id: field_6
        type: u1
    instances:
      # I'm not sure why this is the case.
      count:
        value: 'field2 > 1 ? field1 : field2'
      height:
        value: 'field2 > 1 ? field2 : field1'
      width:
        value: 'width_over_eight * 8'
  music_header:
    seq:
      - id: tick_beat
        type: u1
      - id: beat_measure
        type: u1
      - id: total_tick
        type: s4le
      - id: data_size
        type: s4le
      - id: nr_command
        type: s4le
      - id: sound_mode
        type: u1
      - id: pitch_b_range
        type: u1
      - id: basic_tempo
        type: u2le
      - id: unknown1
        type: u1
      - id: unknown2
        type: u1
      - id: unknown3
        type: u1
      - id: unknown4
        type: u1
      - id: unknown5
        type: u1
      - id: i_inst_count
        type: u1
  music_contents:
    seq:
      - id: instruments
        type: instrument_parameters
        repeat: expr
        repeat-expr: _parent.header.as<music_header>.i_inst_count
      - id: music_commands
        type: track_event(_index)
        repeat: eos
    instances:
      contents:
        pos: 0
        size-eos: true
  generic_header:
    params:
      - id: size
        type: u4
    seq:
      - id: contents
        size: size
  instrument_parameters:
    seq:
      - id: opl_modulator
        type: snd_oplregs
      - id: opl_carrier
        type: snd_oplregs
      - id: i_mod_wave_sel
        type: u2le
      - id: i_car_wave_sel
        type: u2le
      - id: extra
        type: u2le
  snd_oplregs:
    seq:
      - id: ksl
        type: u2le
      - id: multiple
        type: u2le
      - id: feedback
        type: u2le
      - id: attack
        type: u2le
      - id: sustain
        type: u2le
      - id: eg
        type: u2le
      - id: decay
        type: u2le
      - id: release_rate
        type: u2le
      - id: total_level
        type: u2le
      - id: am
        type: u2le
      - id: vib
        type: u2le
      - id: ksr
        type: u2le
      - id: con
        type: u2le
  track_event:
    params:
      - id: i
        type: u4
    seq:
      - id: v_time
        type: overflow_time
      - id: event_header
        if: first_byte > 0x7f
        type: u1
      - id: event_body
        type:
          switch-on: event_type
          cases:
            0x80: note_off_event
            0x90: note_on_event
            0xa0: polyphonic_pressure_event
            0xb0: controller_event
            0xc0: program_change_event
            0xd0: channel_pressure_event
            0xe0: pitch_bend_event
            # the only system exclusive event supported here is tempo
            0xf0: system_event
    instances:
      first_byte:
        type: u1
        pos: _io.pos
      event_type:
        value: 'first_byte > 0x7f ? first_byte & 0xf0 : _parent.music_commands[i - 1].event_type.as<u1>'
      channel:
        value: 'first_byte > 0x7f ? first_byte & 0xf : _parent.music_commands[i - 1].channel.as<u1>'
  empty:
    seq: []
  system_event:
    seq:
      - id: event_body
        type:
          switch-on: _parent.channel
          cases:
            0x0: tempo_multiplier_event
            0xc: stop_event
  stop_event:
    seq: []
  tempo_multiplier_event:
    seq:
      - id: event_start
        contents: [0x7F, 0x00]
      - id: integer_part
        type: u1
      - id: fractional_part
        type: u1
      - id: event_end
        contents: [0xf7]
  note_off_event:
    seq:
      - id: note
        type: u1
      - id: volume
        type: u1
  note_on_event:
    seq:
      - id: note
        type: u1
      - id: volume
        type: u1
  polyphonic_pressure_event:
    seq:
      - id: volume
        type: u1
  controller_event:
    seq:
      - id: controller
        type: u1
      - id: value
        type: u1
  program_change_event:
    seq:
      - id: program
        type: u1
  channel_pressure_event:
    seq:
      - id: pressure
        type: u1
  pitch_bend_event:
    seq:
      - id: b1
        type: u1
      - id: b2
        type: u1
    instances:
      bend_value:
        value: (b2 << 7) + b1 - 0x4000
      adj_bend_value:
        value: bend_value - 0x4000
  overflow_time:
    # based on the vlq kaitai formats
    seq:
      - id: groups
        type: u1
        repeat: until
        repeat-until: _ != 0xf8
    instances:
      value:
        value: (groups.size - 1) * 240 + groups[-1]
enums:
  record_types:
    1: sprite
    2: font
    3: music
    5: unknown3
