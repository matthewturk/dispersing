import numpy as np
from .fast_utilities import unpack_sprite_algo3
import PIL.Image

class SpriteResource:
    def __init__(self, rec, palettes):
        self.record = rec
        h = rec.header.height
        w = rec.header.width_over_eight * 8
        c = rec.header.count
        self.frames = []
        if c > 1:
            c, h = h, c
        if rec.header.algo == 3:
            rec_data = unpack_sprite_algo3(rec.contents, c * h * w)
        else:
            return
        im = rec_data.reshape((c, h, w))
        im = np.moveaxis(im, 0, -1)
        pal1_id = rec.header.field_4 >> 4
        pal2_id = rec.header.field_4 & 15
        palette = np.concatenate([palettes[pal1_id], palettes[pal2_id]], axis=0)
        for frame in range(im.shape[-1]):
            self.frames.append(PIL.Image.fromarray(palette[im[:, :, frame]]))
