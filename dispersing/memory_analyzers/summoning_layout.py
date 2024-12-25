from .coredump_loader import Coredump, MemoryLocation

# These are some best guesses at locations, if we assume that the data segment
# (DS) is at 0x0000 in the file.

_variables = (
    ("character_name", 0x6D29, "26s"),
    ("magic_levels", 0x6D47, "4B"),
    ("weapon_levels", 0x6D4B, "4B"),
    ("character_level", 0x6D4F, "B"),
    ("current_magic_level_exp", 0x6D50, "4H"),
    ("next_magic_level_exp", 0x6D58, "4H"),
    ("current_weapon_level_exp", 0x6D60, "4H"),
    ("next_weapon_level_exp", 0x6D68, "4H"),
    ("maybe_current_experience", 0x6D70, "H"),
    ("maybe_next_experience", 0x6D72, "H"),
    ("maybe_next_level_experience", 0x6D74, "H"),
    ("DAT_3226_6d76", 0x6D76, "H"),
    ("hp_cur", 0x6D78, "H"),
    ("hp_max", 0x6D7A, "H"),
    ("mp_cur", 0x6D7C, "H"),
    ("mp_max", 0x6D7E, "H"),
    ("armor_class", 0x6D80, "H"),
    ("current_strength", 0x6D82, "B"),
    ("current_agility", 0x6D83, "B"),
    ("current_endurance", 0x6D84, "B"),
    ("current_accuracy", 0x6D85, "B"),
    ("current_talent", 0x6D86, "B"),
    ("current_power", 0x6D87, "B"),
    ("max_strength", 0x6D88, "B"),
    ("max_agility", 0x6D89, "B"),
    ("max_endurance", 0x6D8A, "B"),
    ("max_accuracy", 0x6D8B, "B"),
    ("max_talent", 0x6D8C, "B"),
    ("max_power", 0x6D8D, "B"),
    ("unknown2", 0x6D8E, "B"),
    ("maybe_agility_modifier", 0x6D8F, "B"),
    ("maybe_fatigue", 0x6D90, "B"),
    ("maybe_endurance_modifier", 0x6D94, "B"),
    # This is actually 40 in a row, but not sure yet how to represent this without going full Kaitai.
    # Which, of course, is the ultimate destination here anyway.
    ("spell_table", 0x6D95, "5B9s"),
    ("current_memorized", 0x6FC5, "4B"),
    ("inventory_occupancy_map", 0x7AAC, "41B"),
    ("maybe_inventory_1", 0x7AD7, "40B"),
    ("maybe_inventory_2", 0x7AFF, "40B"),
    ("maybe_inventory_3", 0x7B27, "41B"),
)


def load_summoning_coredump(filename):
    labels = []
    for name, address, data_type in _variables:
        labels.append(MemoryLocation(name=name, address=address, data_type=data_type))
    return Coredump(filename=filename, labels=labels)
