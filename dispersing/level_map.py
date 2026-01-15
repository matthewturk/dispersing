import numpy as np
import ipywidgets
from IPython.display import display
from collections import defaultdict
import PIL.Image as Image
import os
import xml.etree.ElementTree as ET

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
    0: b"\xc9",
    1: b"\xcd",
    2: b"\xbb",
    3: b"\xba",
    4: b"\xc8",
    5: b"\xbc",
    6: b"\xcb",
    7: b"\xcc",
    8: b"\xb9",
    9: b"\xca",
    10: b"\xce",
    11: b"\xcd",  # bit too thick
    12: b"\xcd",
    13: b"\xba",  # bit too thick
    14: b"\xba",
    15: b"\x45",
    16: b"\xb3",
    17: b"\xc4",
    27: b"\xb0",
    28: b"\xb1",
    31: b"\xdf",
    32: b"\xdc",
    33: b"\xe4",
    34: b"\xe5",
    35: b"\xe6",
    36: b"\xf8",
    37: b"\x76",
    53: b"\x41",
    255: b"\x20",
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
    (False, False),
    (False, False),
]


def concat_horizontal(im1, im2):
    dst = Image.new("RGBA", (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


def concat_vertical(im1, im2):
    dst = Image.new("RGBA", (im1.width, im1.height + im2.height))
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

    def get_wall_sprite(self, wall_id, scale=1, aspect_ratio=1.0):
        # This returns the full 32x32 sprite of the wall
        # But it also requires that wall_id be between 0 .. 14.
        if wall_id < 0 or wall_id >= len(_corner_table):
            raise KeyError(wall_id)

        frames = self["wall_tiles"].frames
        tile = frames[wall_id]
        # Try to append the bottom part of the wall if it exists
        if len(frames) > wall_id + 15:
            tile = concat_vertical(tile, frames[wall_id + 15])

        blank = Image.new("RGBA", (16, 8))
        left, right = _corner_table[wall_id]
        if left:
            left_tile = self["wall_corners"].frames[0]
        else:
            left_tile = blank
        if right:
            right_tile = self["wall_corners"].frames[1]
        else:
            right_tile = blank
        tile = concat_vertical(concat_horizontal(left_tile, right_tile), tile)
        if scale > 1:
            nw = round(tile.width * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample=Image.NEAREST)
        return tile

    def get_floor_sprite(self, floor_id, scale=1, aspect_ratio=1.0):
        if floor_id < 0 or floor_id > 7:
            raise KeyError(floor_id)

        frames = self["floor_tiles"].frames
        tile = frames[floor_id * 2]
        if len(frames) > floor_id * 2 + 1:
            tile = concat_vertical(tile, frames[floor_id * 2 + 1])

        if scale > 1:
            nw = round(tile.width * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample=Image.NEAREST)
        return tile

    def get_special_floor_sprite(self, floor_id, scale=1, aspect_ratio=1.0):
        if floor_id < 0 or floor_id > 7:
            raise KeyError(floor_id)
        tile = self["floor_special_tiles"].frames[floor_id]
        if scale > 1:
            nw = round(tile.width * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample=Image.NEAREST)
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

    def to_cp437(self, overrides=None):
        # This is a pretty simple and straightforward mapping of the tiles to cp437.
        tile_map = defaultdict(lambda: b"\xb1")
        tile_map.update(_tile_conversions)
        if overrides is not None:
            tile_map.update(overrides)
        new_string = b"\n".join(
            b"".join(tile_map[_] for _ in row) for row in self.tiles
        )
        return new_string.decode("cp437")

    def _create_map(self):
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
                            tile_frame = self.terrain_sprites["wall_tiles"].frames[
                                tile_key + foff
                            ]
                            if r:
                                tile_frame = tile_frame.transpose(method=r)
                            image.alpha_composite(
                                tile_frame,
                                (start_x + int(w * xoff), start_y + int(h * yoff)),
                            )
                    else:
                        if p == 0:
                            continue
                        tile_frame = self.terrain_sprites["floor_tiles"].frames[
                            tile_key & 7
                        ]
                        # image.alpha_composite(tile_frame, (start_x, start_y + h // 2))
        return image

    def create_map(self):
        w, h = 32, 16
        image_shape = (
            (self.tiles.shape[0] + self.tiles.shape[1] + 1) * w,
            (self.tiles.shape[0] + self.tiles.shape[1] + 1) * h,
        )
        image = Image.new("RGBA", image_shape)
        for i in range(self.tiles.shape[0]):
            for j in range(self.tiles.shape[1])[::-1]:
                tile_key = self.tiles[i, j]
                if tile_key == 255:
                    continue
                start_x = j * w - i * w + offset
                start_y = i * h + j * h
                if tile_key & (15 << 4) == 0:
                    # Floor tile?
                    tile_frame = self.terrain_sprites.get_floor_sprite
                image.alpha_composite(
                    tile_frame,
                    (start_x + int(w * xoff), start_y + int(h * yoff)),
                )

    def export_to_tmx(self, filename):
        # Ensure directory exists
        base_dir = os.path.dirname(os.path.abspath(filename))
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        images_dir = os.path.join(base_dir, "images")
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        tile_mapping = {}
        next_local_id = 0

        tileset_elem = ET.Element("tileset")
        tileset_elem.set("name", "level_tiles")
        tileset_elem.set("tilewidth", "32")
        tileset_elem.set("tileheight", "32")
        tileset_elem.set("tilecount", "0")
        tileset_elem.set("columns", "0")

        def add_tile(category, index, sprite):
            nonlocal next_local_id
            img_name = f"{category}_{index}.png"
            sprite.save(os.path.join(images_dir, img_name))

            tile_elem = ET.SubElement(tileset_elem, "tile")
            tile_elem.set("id", str(next_local_id))
            img_elem = ET.SubElement(tile_elem, "image")
            img_elem.set("source", f"images/{img_name}")
            img_elem.set("width", str(sprite.width))
            img_elem.set("height", str(sprite.height))

            tile_mapping[(category, index)] = next_local_id + 1
            next_local_id += 1

        for i in range(16):
            try:
                sprite = self.terrain_sprites.get_wall_sprite(i)
                add_tile("wall", i, sprite)
            except Exception:
                pass

        for i in range(8):
            try:
                sprite = self.terrain_sprites.get_floor_sprite(i)
                add_tile("floor", i, sprite)
            except Exception:
                pass

        for i in range(8):
            try:
                sprite = self.terrain_sprites.get_special_floor_sprite(i)
                add_tile("floor_special", i, sprite)
            except Exception:
                pass

        tileset_elem.set("tilecount", str(next_local_id))

        map_elem = ET.Element("map")
        map_elem.set("version", "1.0")
        map_elem.set("tiledversion", "1.0.0")
        map_elem.set("orientation", "orthogonal")
        map_elem.set("renderorder", "right-down")
        map_elem.set("width", str(self.level_asset.width))
        map_elem.set("height", str(self.level_asset.height))
        map_elem.set("tilewidth", "32")
        map_elem.set("tileheight", "32")

        tileset_elem.set("firstgid", "1")
        map_elem.append(tileset_elem)

        layer_elem = ET.SubElement(map_elem, "layer")
        layer_elem.set("name", "Tile Layer 1")
        layer_elem.set("width", str(self.level_asset.width))
        layer_elem.set("height", str(self.level_asset.height))

        data_elem = ET.SubElement(layer_elem, "data")
        data_elem.set("encoding", "csv")

        data_csv = []
        for row in self.tiles:
            row_data = []
            for tile_val in row:
                gid = 0
                if tile_val == 255:
                    gid = 0
                elif (tile_val & (15 << 4)) == 0:
                    gid = tile_mapping.get(("wall", tile_val), 0)
                else:
                    f_idx = tile_val & 7
                    if tile_val & 8:
                        gid = tile_mapping.get(("floor_special", f_idx), 0)
                    else:
                        gid = tile_mapping.get(("floor", f_idx), 0)
                row_data.append(str(gid))
            data_csv.append(",".join(row_data))

        data_elem.text = "\n" + ",\n".join(data_csv) + "\n"

        tree = ET.ElementTree(map_elem)
        tree.write(filename, encoding="UTF-8", xml_declaration=True)

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
                    print(" " * 5, end="")
                    continue
                print(f"{self.tiles[row, col]: 4d} ", end="")
            print()

    def render_to_png(self, filename):
        # Standard isometric tile dimensions
        scale = 1
        tile_w = 32 * scale
        tile_h = 16 * scale

        rows, cols = self.tiles.shape

        # Calculate canvas dimensions based on isometric projection
        # x = (col - row) * (tile_w / 2)
        # y = (col + row) * (tile_h / 2)

        # Min x is at (row=max, col=0)
        min_x = (0 - (rows - 1)) * (tile_w // 2)
        # Max x is at (row=0, col=max)
        max_x = (cols - 1) * (tile_w // 2)

        # Max y is at (row=max, col=max)
        max_y = (rows + cols - 2) * (tile_h // 2)

        # Margins to accommodate sprite height (walls extend upwards)
        margin_x = 32 * scale
        margin_y = 64 * scale

        width = max_x - min_x + tile_w + margin_x
        height = max_y + tile_h + margin_y

        image = Image.new("RGBA", (int(width), int(height)))

        # Offsets to center the map in the image
        offset_x = -min_x + margin_x // 2
        offset_y = margin_y

        for row in range(rows):
            for col in range(cols):
                tile_val = self.tiles[row, col]
                if tile_val == 255:
                    continue

                sprite = None
                # Determine if wall or floor
                if (tile_val & (15 << 4)) == 0:
                    # Wall
                    try:
                        sprite = self.terrain_sprites.get_wall_sprite(
                            tile_val, scale=scale
                        )
                    except (KeyError, IndexError):
                        continue
                else:
                    # Floor
                    floor_idx = tile_val & 7
                    is_special = (tile_val & 8) != 0
                    try:
                        if is_special:
                            sprite = self.terrain_sprites.get_special_floor_sprite(
                                floor_idx, scale=scale
                            )
                        else:
                            sprite = self.terrain_sprites.get_floor_sprite(
                                floor_idx, scale=scale
                            )
                    except (KeyError, IndexError):
                        continue

                if sprite:
                    # Calculate screen position for the tile footprint (top-left)
                    screen_x = (col - row) * (tile_w // 2) + offset_x
                    screen_y = (col + row) * (tile_h // 2) + offset_y

                    # Center horizontally based on sprite width vs tile width
                    draw_x = screen_x + (tile_w - sprite.width) // 2

                    # Align the bottom of the sprite to the bottom of the tile footprint
                    # Tile footprint bottom is at screen_y + tile_h
                    draw_y = screen_y + tile_h - sprite.height

                    image.alpha_composite(sprite, (int(draw_x), int(draw_y)))

        image.save(filename)
