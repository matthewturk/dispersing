import numpy as np
from .sprite_resource import SpriteResource
from .fast_utilities import unpack_sprite_algo3
from dataclasses import dataclass
from typing import Any


@dataclass
class GlyphSpriteStore:
    header: Any
    contents: Any


class FontResource(SpriteResource):
    def __init__(self, rec, palettes):
        self.clip_info = np.frombuffer(rec.header.clip_info, dtype="u1")
        super().__init__(
            rec=GlyphSpriteStore(
                header=rec.header.font_sprite_header, contents=rec.contents
            ),
            palettes=palettes,
        )

    def display_text(self, text):
        pass
