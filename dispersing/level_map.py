import numpy as np
import ipywidgets
from IPython.display import display
import PIL.Image as Image

_terrain_attrs = (
    "internal_wall_edges",
    "floor",
    "floor_special_tile",
    "wall_edges",
    "keys_switches",
    "door",
    "unk7",
    "unk8",
    "unk9",
    "unk12",
    "big_wooden_thing",
    "big_boulder",
)


class TerrainSprites(dict):
    def __init__(self, game, level_asset):
        super(dict, self).__init__()
        self.game = game
        self.level_asset = level_asset
        offset = self.game.assets["INIT"].sprite_offsets.terrain
        sprites = self.game.resources.sprites
        props = self.level_asset.properties

        for attr in _terrain_attrs:
            self[attr] = sprites[offset + getattr(props, attr)]
        offset = self.game.assets["INIT"].sprite_offsets.wall_decoration
        self["wall_overlay_tiles"] = sprites[offset + props.wall_overlay_tiles]

    def _ipython_display_(self):
        children = []
        titles = []
        for attr in _terrain_attrs + ("wall_overlay_tiles",):
            titles.append(attr.replace("_", " ").capitalize())
            o = ipywidgets.Output()
            with o:
                display(self[attr])
            children.append(ipywidgets.HBox([ipywidgets.Label(attr), o]))
        t = ipywidgets.Tab(children)
        for i, title in enumerate(titles):
            t.set_title(i, title)
        display(t)


class LevelMap:
    def __init__(self, game, level_number):
        self.game = game
        self.level_asset = game.assets["LEVELS"].levels[level_number]
        self.tiles = np.frombuffer(self.level_asset.map, dtype="u1").reshape(
            (self.level_asset.height, self.level_asset.width)
        )

        self.items = {}
        self.info = {}
        # Always one extra to signal terminus of item list
        for item in self.level_asset.items[:-1]:
            self.items[item.x, item.y] = [game.objects[_] for _ in item.info.items]
            self.info[item.x, item.y] = item.info

        # Setup terrain sprites
        self.terrain_sprites = TerrainSprites(self.game, self.level_asset)

    def create_map(self):
        # OK!  This will be our really hard part.  We have to do an isometric draw.
        # The way this works is that we have a uint8 for each tile.  The values they take on range from 0 .. 53,
        # but with a few missing. (18, 19, 20, 22)
        #
        # Our walls have 15 "upper" sprites and 15 "lower" sprites (in that order)
        # We have 8 floor tiles, 8 "special" floor tiles, and 8 "wall edges". 4 keys.
        # Doors I haven't totally worked out.
        # For a wall edge, the sprites are 32 across, 16 high. But, we end up
        # with 2 to make a wall.  So 32x32 net.  Floor tiles are 16 high, 32 across.
        #
        # We're going to roughly follow
        # https://stackoverflow.com/questions/892811/drawing-isometric-game-worlds
        # and note that our tiles are oriented with our origin in what would be
        # the top of the diamond.
        # How big does our image need to be?
        # Add one on to the height for the top/bottom
        w, h = 32, 16
        image_shape = (
            (self.tiles.shape[0] + self.tiles.shape[1] + 1) * w // 2,
            (self.tiles.shape[0] + self.tiles.shape[1] + 1) * h // 2,
        )
        image = Image.new("RGBA", image_shape)
        tile_frame = self.terrain_sprites["floor"].frames[0]
        offset = (self.tiles.shape[0] - 1) * w // 2
        # i is for y, j for x
        for i in range(self.tiles.shape[0]):
            for j in range(self.tiles.shape[1])[::-1]:
                tile_key = self.tiles[i, j]
                if tile_key == 255:
                    continue
                start_x = j * w // 2 - i * w // 2 + offset
                start_y = i * h // 2 + j * h // 2
                # Figure out the tile type
                if tile_key & (15 << 4) == 0:
                    tile_frame = self.terrain_sprites["internal_wall_edges"].frames[
                        tile_key
                    ]
                else:
                    tile_frame = self.terrain_sprites["floor"].frames[tile_key & 7]
                image.paste(tile_frame, (start_x, start_y))
        return image
