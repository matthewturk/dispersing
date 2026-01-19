import os

import numpy as np
import pandas as pd

from . import kaitai_utilities as ku
from .kaitai_parsers import summoning
from .level_map import LevelMap
from .object_db import ObjectDatabase
from .npc_db import NPCDatabase
from .resource_files import ResourceMap


def make_df(l):
    cattr = ku.common_attributes(l)
    flattened = ku.collect_attributes(l, cattr)
    return pd.DataFrame(flattened)


class Game:
    name = None
    path = None
    asset_files = None
    assets = None

    def __init__(self, path):
        self.path = path
        self.assets = {}
        self.records = {}
        for asset_filename, attr in self.asset_files:
            fn = os.path.join(self.path, asset_filename)
            cls = getattr(self.base_mod, asset_filename)
            d = self.assets[asset_filename] = cls.from_file(fn)
            if attr is not None:
                self.records[asset_filename] = make_df(getattr(d, attr))

        self.setup_resources()

    def export_world_to_tmx(self, output_dir):
        import os
        import math
        import xml.etree.ElementTree as ET
        from PIL import Image

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        unique_sprites = {}

        # Helper to get sprite set ID
        def get_set_id(level, attr):
            props = level.level_asset.properties
            return getattr(props, attr, 0)

        decor_indices = {
            0: "wall_decor1",
            1: "wall_decor2",
            2: "wall_decor3",
            3: "wall_overlay_tiles",
        }

        print("Collecting sprites from all levels...")
        for level in self.levels:
            ts = level.terrain_sprites

            # Walls
            sid = get_set_id(level, "wall_tiles")
            for i in range(16):
                key = ("wall", sid, i, None)
                if key not in unique_sprites:
                    try:
                        unique_sprites[key] = ts.get_sprite("wall_tiles", i)
                    except Exception:
                        pass

            # Floors
            sid = get_set_id(level, "floor_tiles")
            for i in range(8):
                key = ("floor", sid, i, None)
                if key not in unique_sprites:
                    try:
                        unique_sprites[key] = ts.get_sprite("floor_tiles", i)
                    except Exception:
                        pass
            for crop in ["top", "bottom"]:
                key = ("floor", sid, 0, crop)
                if key not in unique_sprites:
                    try:
                        unique_sprites[key] = ts.get_sprite("floor_tiles", 0, crop=crop)
                    except Exception:
                        pass

            # Floor Special
            sid = get_set_id(level, "floor_special_tiles")
            for i in range(8):
                key = ("floor_special", sid, i, None)
                if key not in unique_sprites:
                    try:
                        unique_sprites[key] = ts.get_sprite("floor_special_tiles", i)
                    except Exception:
                        pass

            # Keys/Switches
            sid = get_set_id(level, "keys_switches")
            if "keys_switches" in ts:
                count = len(ts["keys_switches"].frames)
                for i in range(count):
                    key = ("keys_switches", sid, i, None)
                    if key not in unique_sprites:
                        try:
                            s = ts.get_sprite("keys_switches", i)
                            # Bake offset (0, -12) -> pad bottom 12
                            w, h = s.size
                            padded = Image.new("RGBA", (w, h + 12))
                            padded.paste(s, (0, 0))
                            unique_sprites[key] = padded
                        except Exception:
                            pass

            # Decorations
            for cat in decor_indices.values():
                if cat not in ts:
                    continue
                sid = get_set_id(level, cat)
                count = len(ts[cat].frames)
                for i in range(count):
                    key = (cat, sid, i, None)
                    if key not in unique_sprites:
                        try:
                            sprite = ts.get_sprite(cat, i)
                            w, h = sprite.width, sprite.height
                            W = max(64, w + 64)
                            if W % 2 != 0:
                                W += 1
                            H = max(64, h + 64)
                            px = int(W / 2 + w / 2 - 32)
                            py = int(H - h / 2 - 32)
                            padded = Image.new("RGBA", (W, H))
                            padded.paste(sprite, (px, py))
                            unique_sprites[key] = padded
                        except Exception:
                            pass

        print(f"Packing {len(unique_sprites)} sprites into atlas...")
        sorted_keys = sorted(
            unique_sprites.keys(),
            key=lambda x: (x[0], x[1], x[2], x[3] if x[3] is not None else ""),
        )

        max_w = 0
        max_h = 0
        for img in unique_sprites.values():
            max_w = max(max_w, img.width)
            max_h = max(max_h, img.height)

        n_sprites = len(sorted_keys)
        cols = int(math.ceil(math.sqrt(n_sprites)))
        rows = int(math.ceil(n_sprites / cols)) if cols > 0 else 0

        atlas_w = cols * max_w
        atlas_h = rows * max_h

        atlas_img = Image.new("RGBA", (atlas_w, atlas_h))
        gid_map = {}

        for idx, key in enumerate(sorted_keys):
            img = unique_sprites[key]
            r = idx // cols
            c = idx % cols
            x = c * max_w
            y = r * max_h

            # Align bottom-center
            dest_x = x + (max_w - img.width) // 2
            dest_y = y + (max_h - img.height)

            atlas_img.paste(img, (dest_x, dest_y))
            gid_map[key] = idx + 1

        atlas_filename = "world_atlas.png"
        atlas_img.save(os.path.join(output_dir, atlas_filename))

        tsx_filename = "world_atlas.tsx"
        tsx_root = ET.Element("tileset")
        tsx_root.set("version", "1.0")
        tsx_root.set("tiledversion", "1.0.0")
        tsx_root.set("name", "world_atlas")
        tsx_root.set("tilewidth", str(max_w))
        tsx_root.set("tileheight", str(max_h))
        tsx_root.set("tilecount", str(n_sprites))
        tsx_root.set("columns", str(cols))

        image_elem = ET.SubElement(tsx_root, "image")
        image_elem.set("source", atlas_filename)
        image_elem.set("width", str(atlas_w))
        image_elem.set("height", str(atlas_h))

        ET.ElementTree(tsx_root).write(
            os.path.join(output_dir, tsx_filename),
            encoding="UTF-8",
            xml_declaration=True,
        )

        print("Generating TMX files...")
        for level_idx, level in enumerate(self.levels):
            map_elem = ET.Element("map")
            map_elem.set("version", "1.0")
            map_elem.set("tiledversion", "1.0.0")
            map_elem.set("orientation", "isometric")
            map_elem.set("renderorder", "right-down")
            map_elem.set("width", str(level.level_asset.width))
            map_elem.set("height", str(level.level_asset.height))
            map_elem.set("tilewidth", "64")
            map_elem.set("tileheight", "32")

            tileset_elem = ET.SubElement(map_elem, "tileset")
            tileset_elem.set("firstgid", "1")
            tileset_elem.set("source", tsx_filename)

            layers = [
                ("Floor Layer", []),
                ("Floor Detail Layer", []),
                ("Wall Layer", []),
                ("Decor 1 Layer", []),
                ("Decor 2 Layer", []),
                ("Decor 3 Layer", []),
                ("Overlay Tiles Layer", []),
            ]

            height = level.level_asset.height
            width = level.level_asset.width

            layer_grids = [
                [[0 for _ in range(width)] for _ in range(height)] for _ in layers
            ]

            # Cache set IDs for this level
            sid_wall = get_set_id(level, "wall_tiles")
            sid_floor = get_set_id(level, "floor_tiles")
            sid_special = get_set_id(level, "floor_special_tiles")
            sid_keys = get_set_id(level, "keys_switches")

            for row in range(height):
                for col in range(width):
                    tile_val = level.tiles[row, col]

                    gid_floor = 0
                    gid_detail = 0
                    gid_wall = 0

                    if tile_val == 255:
                        pass
                    elif (tile_val & 0xF0) == 0:
                        # Wall logic
                        void_above = (row - 1 < 0) or (level.tiles[row - 1, col] == 255)
                        void_left = (col - 1 < 0) or (level.tiles[row, col - 1] == 255)
                        void_below = (row + 1 >= height) or (
                            level.tiles[row + 1, col] == 255
                        )
                        void_right = (col + 1 >= width) or (
                            level.tiles[row, col + 1] == 255
                        )
                        down_corner = (
                            (row + 1 < height)
                            and (col + 1 < width)
                            and (level.tiles[row + 1, col + 1] == 255)
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
                            gid_floor = gid_map.get(("floor", sid_floor, 0, crop), 0)
                        gid_wall = gid_map.get(("wall", sid_wall, tile_val, None), 0)
                    else:
                        if 31 <= tile_val <= 40:
                            floor_idx = (tile_val + 1) & 0x07
                            gid_floor = gid_map.get(("floor", sid_floor, 0, None), 0)
                            gid_detail = gid_map.get(
                                ("floor_special", sid_special, floor_idx, None), 0
                            )
                        elif tile_val & 0x10:
                            if 27 <= tile_val <= 30:
                                floor_idx = (tile_val + 5) & 0x07
                                gid_floor = gid_map.get(
                                    ("floor", sid_floor, floor_idx, None), 0
                                )
                            elif 23 <= tile_val <= 26:
                                floor_idx = (tile_val + 1) & 0x07
                                gid_floor = gid_map.get(
                                    ("floor", sid_floor, 0, None), 0
                                )
                                gid_detail = gid_map.get(
                                    ("keys_switches", sid_keys, floor_idx, None), 0
                                )
                            else:
                                floor_idx = tile_val & 0x03
                                gid_floor = gid_map.get(
                                    ("floor", sid_floor, floor_idx, None), 0
                                )

                    layer_grids[0][row][col] = gid_floor
                    layer_grids[1][row][col] = gid_detail
                    layer_grids[2][row][col] = gid_wall

                    if (row, col) in level.info:
                        info = level.info[row, col]
                        if info.overlay_flags.name == "decoration":
                            cat_idx = info.overlay_args // 10
                            frame_idx = info.overlay_args % 10
                            if 0 <= cat_idx <= 3:
                                cat_name = decor_indices[cat_idx]
                                sid_decor = get_set_id(level, cat_name)
                                gid = gid_map.get(
                                    (cat_name, sid_decor, frame_idx, None), 0
                                )
                                layer_grids[3 + cat_idx][row][col] = gid

            for (layer_name, _), grid in zip(layers, layer_grids):
                layer_elem = ET.SubElement(map_elem, "layer")
                layer_elem.set("name", layer_name)
                layer_elem.set("width", str(width))
                layer_elem.set("height", str(height))
                if layer_name in (
                    "Decor 1 Layer",
                    "Decor 2 Layer",
                    "Decor 3 Layer",
                    "Overlay Tiles Layer",
                ):
                    layer_elem.set("offsetx", "-8")
                    layer_elem.set("offsety", "16")

                data_elem = ET.SubElement(layer_elem, "data")
                data_elem.set("encoding", "csv")
                csv_lines = [",".join(map(str, r)) for r in grid]
                data_elem.text = "\n" + ",\n".join(csv_lines) + "\n"

            ET.ElementTree(map_elem).write(
                os.path.join(output_dir, f"level_{level_idx:02d}.tmx"),
                encoding="UTF-8",
                xml_declaration=True,
            )


class TheSummoning(Game):
    name = "The Summoning"
    base_mod = summoning
    asset_files = (
        ("INTERACT", "npc_interactions"),
        ("RESOURCE", "records"),
        ("OBJECTS", "object"),
        ("COLORS", "palettes"),
        ("TEXT", "text"),
        ("KEYWORDS", "keyword"),
        ("LEVELS", "levels"),
        ("NPC", "npcs"),
        ("INIT", None),
    )

    def setup_resources(self):
        self.palettes = []
        for i, palette in enumerate(self.assets["COLORS"].palettes):
            rgba = np.array(
                [(_.red * 4, _.green * 4, _.blue * 4, 255) for _ in palette.colors],
                dtype="u1",
            )
            rgba[(rgba == [252, 252, 252, 255]).all(axis=1)] = [0, 0, 0, 0]
            self.palettes.append(rgba)

        self.resources = ResourceMap(self)
        self.objects = ObjectDatabase(self)
        self.npcs = NPCDatabase(self)

        self.levels = [
            LevelMap(self, i) for i in range(len(self.assets["LEVELS"].levels))
        ]
