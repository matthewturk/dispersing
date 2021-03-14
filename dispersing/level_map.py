import numpy as np
import ipywidgets
from IPython.display import display

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
        for attr in _terrain_attrs + ("wall_overlay_tiles",):
            o = ipywidgets.Output()
            with o:
                display(self[attr])
            children.append(ipywidgets.HBox([ipywidgets.Label(attr), o]))
        display(ipywidgets.VBox(children))


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
        image_shape = (
            (self.tiles.shape[0] + 0) * 32,
            (self.tiles.shape[1] + 1) * 2 * 16,
        )
        image = np.zeros((image_shape) + (4,), dtype="u1")
        tile_image = np.swapaxes(
            np.array(self.terrain_sprites["floor"].frames[0]), 0, 1
        )
        # i is for y, j for x
        for i in range(self.tiles.shape[0]):
            for j in range(self.tiles.shape[1])[::-1]:
                if self.tiles[i, j] == 255:
                    continue
                start_x = (j * 32 // 2) + (i * 32 // 2)
                start_y = (i * 16 // 2) - (j * 16 // 2) + image_shape[1] // 2
                image[start_x : start_x + 32, start_y : start_y + 16] = tile_image
        return image
