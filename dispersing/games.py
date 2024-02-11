import os

import numpy as np
import pandas as pd
import IPython
from IPython.display import display
import ipywidgets

from . import kaitai_utilities as ku
from .kaitai_parsers import summoning
from .level_map import LevelMap
from .object_db import ObjectDatabase
from .npc_db import NPCDatabase, ConversationDatabase
from .resource_files import ResourceMap
from .text_db import TextDatabase
from .sprite_db import SpriteDatabase


def make_df(l):
    cattr = ku.common_attributes(l)
    flattened = ku.collect_attributes(l, cattr)
    return pd.DataFrame(flattened)


class Game:
    name = None
    path = None
    asset_files = None
    assets = None

    def __init__(self, path):
        self.path = path
        self.assets = {}
        self.records = {}
        for asset_filename, attr in self.asset_files:
            fn = os.path.join(self.path, asset_filename)
            cls = getattr(self.base_mod, asset_filename)
            d = self.assets[asset_filename] = cls.from_file(fn)
            if attr is not None:
                self.records[asset_filename] = make_df(getattr(d, attr))

        self.setup_resources()


class TheSummoning(Game):
    name = "The Summoning"
    base_mod = summoning
    asset_files = (
        ("INTERACT", "npc_interactions"),
        ("RESOURCE", "records"),
        ("OBJECTS", "object"),
        ("COLORS", "palettes"),
        ("TEXT", "text"),
        ("KEYWORDS", "keyword"),
        ("LEVELS", "levels"),
        ("NPC", "npcs"),
        ("INIT", None),
    )

    def setup_resources(self):
        self.palettes = []
        for i, palette in enumerate(self.assets["COLORS"].palettes[::-1]):
            rgba = np.array(
                [(_.red * 4, _.green * 4, _.blue * 4, 255) for _ in palette.colors],
                dtype="u1",
            )
            rgba[(rgba == [252, 252, 252, 255]).all(axis=1)] = [0, 0, 0, 0]
            self.palettes.append(rgba)

        self.resources = ResourceMap(self)
        self.objects = ObjectDatabase(self)
        self.npcs = NPCDatabase(self)
        self.text = TextDatabase(self)
        self.sprites = SpriteDatabase(self)
        self.conversations = ConversationDatabase(self)

        self.levels = [
            LevelMap(self, i) for i in range(len(self.assets["LEVELS"].levels))
        ]

    def _ipython_display_(self):
        def get_level_widget(event):
            level = int(event["new"])
            level_widget.children = [level_id, get_output(self.levels[level])]

        def get_output(w):
            o = ipywidgets.Output()
            with o:
                display(w)
            return o

        level_id = ipywidgets.IntSlider(min=0, max=len(self.levels), step=1)
        level_id.observe(get_level_widget, "value")
        level_widget = ipywidgets.VBox([level_id])
        v = ipywidgets.Tab(
            children=[
                ipywidgets.HBox(),  # Music
                ipywidgets.HBox(),  # Fonts
                level_widget,
                ipywidgets.HBox(),  # Color Palettes
                ipywidgets.HBox(),  # Interactions
                get_output(self.npcs),
                ipywidgets.HBox(),  # Sprites
                get_output(self.objects),
                get_output(self.text),
            ],
            titles=[
                "Music",
                "Fonts",
                "Levels",
                "Color Palettes",
                "Interactions",
                "NPCs",
                "Sprites",
                "Objects",
                "Text",
            ],
        )
        display(v)
