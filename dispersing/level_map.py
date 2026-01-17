import numpy as np
import ipywidgets
from IPython.display import display
from collections import defaultdict
import PIL.Image as Image
from PIL import ImageDraw
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
    (False, False),  # 0
    (True, False),  # 1
    (True, False),  # 2
    (False, True),  # 3
    (False, True),  # 4
    (True, True),  # 5
    (True, False),  # 6
    (False, True),  # 7
    (True, True),  # 8
    (True, True),  # 9
    (True, True),  # 10
    (True, False),  # 11
    (False, False),  # 12
    (False, True),  # 13
    (False, False),  # 14
    (False, False),  # 15
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

    def get_floor_sprite(self, floor_id, scale=1, aspect_ratio=1.0, crop=None):
        if floor_id < 0 or floor_id > 7:
            raise KeyError(floor_id)

        frames = self["floor_tiles"].frames
        tile = frames[floor_id * 2]
        tile = concat_vertical(tile, frames[floor_id * 2 + 1])
        arr = np.array(tile)
        half = tile.width // 2
        if crop == "top":
            arr[:half, :, :] = 0
        elif crop == "bottom":
            arr[half:, :, :] = 0

        mask = (arr[:, :, 0] >= 250) & (arr[:, :, 1] >= 250) & (arr[:, :, 2] >= 250)
        arr[mask] = [0, 0, 0, 0]
        tile = Image.fromarray(arr)

        if scale > 1:
            nw = round(tile.width * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample=Image.NEAREST)
        return tile

    def get_special_floor_sprite(self, floor_id, scale=1, aspect_ratio=1.0):
        if floor_id < 0 or floor_id > 7:
            raise KeyError(floor_id)
        tile = self["floor_special_tiles"].frames[floor_id]

        arr = np.array(tile)
        mask = (arr[:, :, 0] >= 250) & (arr[:, :, 1] >= 250) & (arr[:, :, 2] >= 250)
        arr[mask] = [0, 0, 0, 0]
        tile = Image.fromarray(arr)

        if scale > 1:
            nw = round(tile.width * scale)
            nh = round(tile.height * scale * aspect_ratio)
            tile = tile.resize((nw, nh), resample=Image.NEAREST)
        return tile

    def get_sprite(self, category, index, scale=1, aspect_ratio=1.0):
        if category not in self:
            raise KeyError(category)
        frames = self[category].frames
        if index >= len(frames):
            raise IndexError(f"Index {index} out of range for category {category}")
        tile = frames[index]
        if scale != 1 or aspect_ratio != 1.0:
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
        self.temporary_overlay = tile_item_record.info.temporary_overlay
        self.overlay_flags = tile_item_record.info.overlay_flags
        self.overlay_args = getattr(tile_item_record.info, "overlay_args", None)

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
        map_elem.set("orientation", "isometric")
        map_elem.set("renderorder", "right-down")
        map_elem.set("width", str(self.level_asset.width))
        map_elem.set("height", str(self.level_asset.height))
        map_elem.set("tilewidth", "64")
        map_elem.set("tileheight", "32")

        tileset_elem.set("firstgid", "1")
        map_elem.append(tileset_elem)

        # Layer 1: Base
        layer1_elem = ET.SubElement(map_elem, "layer")
        layer1_elem.set("name", "Base Layer")
        layer1_elem.set("width", str(self.level_asset.width))
        layer1_elem.set("height", str(self.level_asset.height))

        data1_elem = ET.SubElement(layer1_elem, "data")
        data1_elem.set("encoding", "csv")

        # Layer 2: Overlay
        layer2_elem = ET.SubElement(map_elem, "layer")
        layer2_elem.set("name", "Overlay Layer")
        layer2_elem.set("width", str(self.level_asset.width))
        layer2_elem.set("height", str(self.level_asset.height))

        data2_elem = ET.SubElement(layer2_elem, "data")
        data2_elem.set("encoding", "csv")

        data1_csv = []
        data2_csv = []

        for row in self.tiles:
            row_data1 = []
            row_data2 = []
            for tile_val in row:
                gid1 = 0
                gid2 = 0

                if tile_val == 255:
                    pass
                elif (tile_val & 0xF0) == 0:
                    gid1 = tile_mapping.get(("floor", 0), 0)
                    gid2 = tile_mapping.get(("wall", tile_val), 0)
                else:
                    if 31 <= tile_val <= 40:
                        floor_idx = (tile_val + 1) & 0x07
                        gid1 = tile_mapping.get(("floor", 0), 0)
                        gid2 = tile_mapping.get(("floor_special", floor_idx), 0)
                    elif tile_val & 0x10:
                        if 27 <= tile_val <= 30:
                            floor_idx = (tile_val + 5) & 0x07
                            gid1 = tile_mapping.get(("floor", floor_idx), 0)
                        elif tile_val == 25:
                            floor_idx = (tile_val + 1) & 0x07
                            gid1 = tile_mapping.get(("floor", 0), 0)
                            gid2 = tile_mapping.get(("floor_special", floor_idx), 0)
                        else:
                            floor_idx = tile_val & 0x03
                            gid1 = tile_mapping.get(("floor", floor_idx), 0)

                row_data1.append(str(gid1))
                row_data2.append(str(gid2))

            data1_csv.append(",".join(row_data1))
            data2_csv.append(",".join(row_data2))

        data1_elem.text = "\n" + ",\n".join(data1_csv) + "\n"
        data2_elem.text = "\n" + ",\n".join(data2_csv) + "\n"

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

    def _retrieve_overlay(self, tile_info, bounds, coords):
        # For now, we only support wall decorations
        return None, (0, 0)
        for i, flag in enumerate(tile_info.wall_flags):
            if flag.startswith("wall_decor"):
                sprite = self.terrain_sprites["wall_decor" + str(i + 1)]
                return sprite, (0, -sprite.height // 2)

    def render(self, scale=1, include_floor=True, debug_text=None):
        width = self.level_asset.width
        height = self.level_asset.height

        tile_w = 32 * scale
        tile_h = 16 * scale

        min_x = -(height - 1) * tile_w
        max_x = (width - 1) * tile_w
        max_y = (width + height - 2) * tile_h

        top_margin = 40 * scale
        side_margin = 32 * scale

        canvas_width = (max_x - min_x) + tile_w + side_margin * 2
        canvas_height = max_y + tile_h + top_margin * 2

        img = Image.new("RGBA", (int(canvas_width), int(canvas_height)))

        draw = None
        if debug_text:
            draw = ImageDraw.Draw(img)

        offset_x = -min_x + side_margin
        offset_y = top_margin

        for row in range(height):
            for col in range(width):
                tile_val = self.tiles[row, col]
                if tile_val == 255:
                    continue

                # Calculate screen position for the tile footprint (top-left)
                screen_x = (col - row) * tile_w + offset_x
                screen_y = (col + row) * tile_h + offset_y

                sprites = []
                # Determine if wall or floor
                if (tile_val & 0xF0) == 0:
                    if include_floor:
                        # We first check the axis.
                        # Wall
                        vertical = (tile_val & 0x02) == 0
                        void_above = (row - 1 < 0) or (self.tiles[row - 1, col] == 255)
                        void_left = (col - 1 < 0) or (self.tiles[row, col - 1] == 255)
                        void_below = (row + 1 >= height) or (
                            self.tiles[row + 1, col] == 255
                        )
                        void_right = (col + 1 >= width) or (
                            self.tiles[row, col + 1] == 255
                        )
                        down_corner = (
                            (row + 1 < height)
                            and (col + 1 < width)
                            and (self.tiles[row + 1, col + 1] == 255)
                        )
                        should_render = True
                        crop = None
                        if tile_val in (0, 6, 7, 10) and down_corner:
                            crop = "bottom"
                        elif void_below and void_left:
                            should_render = False
                        elif void_above and void_right:
                            should_render = False
                        elif void_below or void_right:
                            crop = "bottom"
                        elif void_above or void_left:
                            crop = "top"
                        if should_render:
                            sprites.append(
                                (
                                    self.terrain_sprites.get_floor_sprite(
                                        0, scale=scale, crop=crop
                                    ),
                                    0,
                                )
                            )
                    sprites.append(
                        (self.terrain_sprites.get_wall_sprite(tile_val, scale=scale), 0)
                    )
                else:
                    if include_floor:
                        # Floor
                        if 31 <= tile_val <= 40:
                            floor_idx = (tile_val + 1) & 0x07
                            sprites.append(
                                (
                                    self.terrain_sprites.get_floor_sprite(
                                        0, scale=scale
                                    ),
                                    0,
                                )
                            )
                            sprites.append(
                                (
                                    self.terrain_sprites.get_special_floor_sprite(
                                        floor_idx, scale=scale
                                    ),
                                    8 * scale,
                                )
                            )
                        elif tile_val & 0x10:
                            if 27 <= tile_val <= 30:
                                floor_idx = (tile_val + 5) & 0x07
                                sprites.append(
                                    (
                                        self.terrain_sprites.get_floor_sprite(
                                            floor_idx, scale=scale
                                        ),
                                        0,
                                    )
                                )
                            elif 23 <= tile_val <= 26:
                                floor_idx = (tile_val + 1) & 0x07
                                sprites.append(
                                    (
                                        self.terrain_sprites.get_floor_sprite(
                                            0, scale=scale
                                        ),
                                        0,
                                    )
                                )
                                sprites.append(
                                    (
                                        self.terrain_sprites.get_special_floor_sprite(
                                            floor_idx, scale=scale
                                        ),
                                        16 * scale,
                                    )
                                )
                            else:
                                floor_idx = tile_val & 0x03
                                sprites.append(
                                    (
                                        self.terrain_sprites.get_floor_sprite(
                                            floor_idx, scale=scale
                                        ),
                                        0,
                                    )
                                )

                for sprite, y_off in sprites:
                    # Center horizontally based on sprite width vs tile width
                    draw_x = screen_x + (tile_w - sprite.width) // 2

                    # Align the bottom of the sprite to the bottom of the tile footprint
                    # Tile footprint bottom is at screen_y + tile_h
                    draw_y = screen_y + tile_h - sprite.height + y_off

                    img.alpha_composite(sprite, (int(draw_x), int(draw_y)))

                if (col, row) in self.info:
                    overlay_img, overlay_offset = self._retrieve_overlay(
                        self.info[col, row], (canvas_width, canvas_height), (col, row)
                    )
                    if overlay_img:
                        img.alpha_composite(
                            overlay_img,
                            (
                                int(screen_x + overlay_offset[0]),
                                int(screen_y + overlay_offset[1]),
                            ),
                        )

                if debug_text:
                    text = ""
                    if debug_text == "type":
                        text = str(tile_val)
                    elif debug_text == "coords":
                        text = f"{col},{row}"
                    if text:
                        draw.text(
                            (screen_x + tile_w // 2, screen_y + tile_h // 2),
                            text,
                            fill="white",
                            anchor="mm",
                        )

        return img

    def render_to_png(self, filename):
        self.render().save(filename)
