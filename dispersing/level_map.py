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


class TileInfo:
    def __init__(self, game, tile_item_record):
        # Note that we will not have coordinate info
        self.tile_info_record = tile_item_record.info
        self.x = tile_item_record.x
        self.y = tile_item_record.y
        self.items = [game.objects[_] for _ in tile_item_record.info.items]
        self.wall_flags = tile_item_record.info.wall_flags
        self.wall_args = getattr(tile_item_record.info, "wall_args", None)
        self.floor_flags = tile_item_record.info.floor_flags
        self.floor_args = getattr(tile_item_record.info, "floor_args", None)

    def _ipython_display_(self):
        output = []
        if (self.items) > 0:
            children = []
            names = []
            for item in self.items:
                o = ipywidgets.Output()
                with o:
                    display(item)
                children.append(o)
                names.append(item.name)
            items = ipywidgets.Tab(children)
            for i, n in enumerate(names):
                items.set_title(i, n)
            output.append(items)
        display(ipywidgets.VBox(output))


class LevelMap:
    def __init__(self, game, level_number):
        self.game = game
        self.level_asset = game.assets["LEVELS"].levels[level_number]
        self.tiles = np.frombuffer(self.level_asset.map, dtype="u1").reshape(
            (self.level_asset.height, self.level_asset.width)
        )

        self.info = {}
        # Always one extra to signal terminus of item list
        for item in self.level_asset.items[:-1]:
            self.info[item.x, item.y] = TileInfo(game, item)

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
        #
        #   0       corner - top
        #   1       edge - left/up to right/down
        #   2       corner - right
        #   3       edge - left/down to right/up
        #   4       corner - left
        #   5       corner - bottom
        w, h = 32, 16
        image_shape = (
            (self.tiles.shape[0] + self.tiles.shape[1] + 1) * w,
            (self.tiles.shape[0] + self.tiles.shape[1] + 1) * h,
        )
        image = Image.new("RGBA", image_shape)
        tile_frame = self.terrain_sprites["floor"].frames[0]
        offset = (self.tiles.shape[0] - 1) * w
        # I feel confident there's a single-pass method that I just haven't
        # figured out yet.
        for p in [0, 1]:
            # i is for y, j for x
            for i in range(self.tiles.shape[0]):
                for j in range(self.tiles.shape[1])[::-1]:
                    tile_key = self.tiles[i, j]
                    if tile_key == 255:
                        continue
                    start_x = j * w - i * w + offset
                    start_y = i * h + j * h
                    # Figure out the tile type
                    if tile_key & (15 << 4) == 0:
                        if p == 1:
                            continue
                        # We have to paste twice here
                        tile_offsets = [
                            (0, (0, 0, None)),
                            (15, (0, 1, None)),
                            (11, (1, 0.0, None)),
                            # (15, (0, -1.5, Image.ROTATE_180)),
                            # (8, (1, 0, None)),
                            # (7, (-1, 0, None)),
                            # (7, (1, 1, None)),
                        ]
                        # if tile_key & 1 == 1:
                        #    tile_offsets.append((-1, (-1, 0, None)))
                        for foff, (xoff, yoff, r) in tile_offsets:
                            tile_frame = self.terrain_sprites[
                                "internal_wall_edges"
                            ].frames[tile_key + foff]
                            if r:
                                tile_frame = tile_frame.transpose(method=r)
                            image.alpha_composite(
                                tile_frame,
                                (start_x + int(w * xoff), start_y + int(h * yoff)),
                            )
                    else:
                        if p == 0:
                            continue
                        tile_frame = self.terrain_sprites["floor"].frames[tile_key & 7]
                        # image.alpha_composite(tile_frame, (start_x, start_y + h // 2))
        return image
