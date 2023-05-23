from .sprite_resource import SpriteResource
import numpy as np


class ResourceMap:
    # This one uses kaitai and will replace the others
    def __init__(self, game):
        self.game = game
        self.records = []
        self.sprites = {}
        self.palette_sprites = {}
        palettes = game.palettes
        for i, rec in enumerate(game.assets["RESOURCE"].records):
            self.records.append(rec)
            if rec.type.name == "sprite":
                self.sprites[i] = SpriteResource(rec, palettes)

    def palettes_to_array(self):
        # Note that these run 0 .. 63, not 0 .. 255.
        colors = []
        for palette in self.game.assets["COLORS"].palettes:
            p = []
            colors.append(p)
            for color in palette.colors:
                p.append([color.red, color.green, color.blue])

        colors = np.array(colors)
        return colors