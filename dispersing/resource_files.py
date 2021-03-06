from .sprite_resource import SpriteResource


class ResourceMap:
    # This one uses kaitai and will replace the others
    def __init__(self, game):
        self.records = []
        self.sprites = {}
        self.palette_sprites = {}
        palettes = game.palettes
        for i, rec in enumerate(game.assets["RESOURCE"].records):
            self.records.append(rec)
            if rec.type.name == "sprite":
                self.sprites[i] = SpriteResource(rec, palettes)
