try:
    import pretty_midi
except ImportError:
    pass

_drum_names = ("Bass drum", "Snare drum", "Tom tom", "Top cymbal", "Hi-hat cymbal")

_instrument_types = {
    0: [(f"Instrument{i+1}", False) for i in range(9)],
    1: [(f"Instrument{i+1}", False) for i in range(6)]
    + [(_, True) for _ in _drum_names],
}


class MusicResource:
    def __init__(self, rec):
        # This has the instruments and the actual music tracks.
        # Note that we aren't going to attempt to do individual instruments yet.
        self.record = rec
        self.instruments = [_ for _ in rec.contents.instruments]
        self.num_channels = len(_instrument_types[rec.header.sound_mode])

    def convert_to_midi(self, factor=1):
        dest_midi = pretty_midi.PrettyMIDI(initial_tempo=self.record.header.basic_tempo)

        # Note!  We are not using the instruments from the music resource,
        # because they are meant to be used in an SND bank.
        instruments = _instrument_types[self.record.header.sound_mode]
        for i, (n, d) in enumerate(instruments):
            dest_midi.instruments.append(pretty_midi.Instrument(i, is_drum=d, name=n))
        # Now let's figure out our note durations!
        for channel, _ in enumerate(self.instruments):
            events = self.events_by_channel(channel)
            # We need to figure out the note durations.
            start_times = []
            stop_times = []
            notes = []
            volumes = []
            current_time = 0
            for event in events:
                current_time += event.v_time.value
                if event.event_type == 0x90:
                    if event.event_body.volume > 0:
                        volumes.append(event.event_body.volume)
                        start_times.append(current_time)
                        notes.append(event.event_body.note)
                    else:
                        stop_times.append(current_time)
                elif event.event_type == 0xF0 and event.channel == 0:
                    # This is where we'd do tempo change
                    pass
                elif event.event_type == 0x80:
                    stop_times.append(current_time)
                elif event.event_type == 0xE0:
                    v = (event.event_body.b2 << 8) | (event.event_body.b1) - 8192
                    print(current_time, v)
                    dest_midi.instruments[channel].pitch_bends.append(
                        pretty_midi.PitchBend(v, current_time)
                    )
            for n, v, t0, t1 in zip(notes, volumes, start_times, stop_times):
                note = pretty_midi.Note(v, n, t0 / (240 * factor), t1 / (240 * factor))
                dest_midi.instruments[channel].notes.append(note)
        return dest_midi

    def events_by_channel(self, channel):
        events = []
        for event in self.record.contents.music_commands:
            if event.channel != channel:
                continue
            events.append(event)
        return events
