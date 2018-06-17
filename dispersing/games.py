import pandas as pd
import os

from .kaitai_parsers import summoning
from . import kaitai_utilities as ku

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
            self.records[asset_filename] = make_df(getattr(d, attr))

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
                ("LEVELS", "levels")
            )
