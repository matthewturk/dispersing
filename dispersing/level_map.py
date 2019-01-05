import numpy as np

class LevelMap:
    def __init__(self, game, level_number):
        self.game = game
        self.level_asset = game.assets["LEVELS"].levels[level_number]
        self.level_tiles = np.frombuffer(self.level_asset.map,
                dtype="u1").reshape((self.level_asset.height,
                                    self.level_asset.width))

        self.items = {}
        self.info = {}
        # Always one extra to signal terminus of item list
        for item in self.level_asset.items[:-1]:
            self.items[item.x, item.y] = [game.objects[_] for _ in
                    item.info.items]
            self.info[item.x, item.y] = item.info

    def __getitem__(self, item):
        return self.items.get(item, []), self.info.get(item, None)
