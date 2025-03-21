import numpy as np
import ipywidgets
from IPython.display import display
from collections import defaultdict
import PIL.Image as Image
import os

_terrain_attrs = (
    "wall_tiles",
    "wall_corners",
    "floor_tiles",
    "floor_special_tiles",
    "gate_tiles",
    "keys_switches",
    "door_tiles",
    "unk12",
    "big_wooden_thing",
    "big_boulder",
)

_wall_attrs = (
    "wall_decor1",
    "wall_decor2",
    "wall_decor3",
    "wall_overlay_tiles",
)

_tile_conversions = {
    0: b'\xc9',
    1: b'\xcd',
    2: b'\xbb',
    3: b'\xba',
    4: b'\xc8',
    5: b'\xbc',
    6: b'\xcb',
    7: b'\xcc',
    8: b'\xb9',
    9: b'\xca',
    10: b'\xce',
    11: b'\xcd', # bit too thick
    12: b'\xcd',
    13: b'\xba', # bit too thick
    14: b'\xba',
    15: b'\x45',
    16: b'\xb3',
    17: b'\xc4',
    27: b'\xb0',
    28: b'\xb1',
    31: b'\xdf',
    32: b'\xdc',
    33: b'\xe4',
    34: b'\xe5',
    35: b'\xe6',
    36: b'\xf8',
    37: b'\x76',
    53: b'\x41',
    255: b'\x20',
}

_corner_table = [
    (False, False),
    (True, False),
    (True, False),
    (False, True),
    (False, True),
    (True, True),
    (True, False),
    (False, True),
    (True, True),
    (True, True),
    (True, False),
    (False, False),
    (False, True),
    (False, False),
]

def concat_horizontal(im1, im2):
    dst = Image.new('RGBA', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def concat_vertical(im1, im2):
    dst = Image.new('RGBA', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

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
        for attr in _wall_attrs:
            self[attr] = sprites[offset + getattr(props, attr)]

    def get_wall_sprite(self, wall_id, scale = 1, aspect_ratio = 1.0):
        # This returns the full 32x32 sprite of the wall
        # But it also requires that wall_id be between 0 .. 14.
        if wall_id < 0 or wall_id > 14:
            raise KeyError(wall_id)
        # We concatenate the two PIL images
        tile = concat_vertical(
            self["wall_tiles"].frames[wall_id],
            self["wall_tiles"].frames[wall_id + 15]
        )
        blank = Image.new('RGBA', (16, 8))
        left, right = _corner_table[wall_id]
        if left:
            left_tile = self["wall_corners"].frames[0]
        else:
            left_tile = blank
        if right:
            right_tile = self["wall_corners"].frames[1]
        else:
            right_tile = blank
        tile = concat_vertical(
            concat_horizontal(left_tile, right_tile),
            tile
        )
        if scale > 1:
            nw = round(tile.height * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample = Image.NEAREST)
        return tile

    def get_floor_sprite(self, floor_id, scale = 1, aspect_ratio = 1.0):
        # This returns a 32x32 sprite of the floor
        # But it also requires that the floor_id be between 0 .. 3
        if floor_id < 0 or floor_id > 3:
            raise KeyError(floor_id)
        # We concatenate the two PIL images
        tile = concat_vertical(
            self["floor_tiles"].frames[floor_id * 2 + 0],
            self["floor_tiles"].frames[floor_id * 2 + 1],
        )
        if scale > 1:
            nw = round(tile.height * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample = Image.NEAREST)
        return tile

    def _ipython_display_(self):
        children = []
        titles = []
        for attr in _terrain_attrs + _wall_attrs:
            titles.append(attr.replace("_", " ").capitalize())
            o = ipywidgets.Output()
            with o:
                display(self[attr])
            children.append(ipywidgets.HBox([ipywidgets.Label(attr), o]))
        t = ipywidgets.Tab(children)
        for i, title in enumerate(titles):
            t.set_title(i, title)
        display(t)

    def export_all_frames(self, folder_name):
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
            for key in sorted(self):
                for i, frame in enumerate(self[key].frames):
                    frame.save(os.path.join(folder_name, f"{key}-{i:04d}.png"))


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
        if len(self.items) > 0:
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

    def to_cp437(self, overrides = None):
        # This is a pretty simple and straightforward mapping of the tiles to cp437.
        tile_map = defaultdict(lambda: b'\xb1')
        tile_map.update(_tile_conversions)
        if overrides is not None:
            tile_map.update(overrides)
        new_string = b'\n'.join(b''.join(tile_map[_] for _ in row) for row in self.tiles)
        return new_string.decode('cp437')

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
        tile_frame = self.terrain_sprites["floor_tiles"].frames[0]
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
                                "wall_tiles"
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
                        tile_frame = self.terrain_sprites["floor_tiles"].frames[tile_key & 7]
                        # image.alpha_composite(tile_frame, (start_x, start_y + h // 2))
        return image

    def extract_tiles(self):
        # We'll come up with a few layers here.
        # Our first layer will be the floor.
        # We'll make it a 64 bit array
        floor_tiles = np.zeros(self.tiles.shape, dtype="u8")
        has_floor = (self.tiles & 15 << 4) != 0
        floor_tiles[has_floor] = self.tiles[has_floor] & 7
        floor_tiles += 1
        floor_tiles[self.tiles == 255] = 0
        return floor_tiles

    def print_numpy_array(self):
        print("     ", end="")
        for i in range(self.tiles.shape[1]):
            print(f"{i: 4d} ", end="")
        print()
        for row in range(self.tiles.shape[0]):
            print(f"{row: 4d} ", end="")
            for col in range(self.tiles.shape[1]):
                if self.tiles[row, col] == 255:
                    print(" "*5, end="")
                    continue
                print(f"{self.tiles[row, col]: 4d} ", end="")
            print()
