import os

from .resource_files import \
        resource_registry

class Game:
    name = None
    path = None
    asset_files = None
    assets = None

    def __init__(self, path):
        self.path = path
        self.assets = {}
        for asset_file in self.asset_files:
            if isinstance(asset_file, tuple):
                asset_type, asset_filename = asset_file
            else:
                asset_type = asset_filename = asset_file
            args = ()
            if isinstance(asset_type, tuple):
                asset_type, *args = asset_type
            fn = os.path.join(self.path, asset_filename.upper())
            self.assets[asset_filename] = resource_registry[asset_type](fn,
                    *args)

class TheSummoning(Game):
    name = "The Summoning"
    asset_files = (
            "interact",
            "resource",
            "objects",
            "colors",
            "interact",
            "text",
            "keywords",
            "levels")
