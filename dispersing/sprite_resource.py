from .fast_utilities import unpack_sprite_algo3
import numpy as np
import PIL.Image
import io
import ipywidgets
from IPython.display import display


class SpriteResource:
    def __init__(self, rec, palettes):
        self.record = rec
        h = rec.header.height
        w = rec.header.width_over_eight * 8
        c = rec.header.count
        self.frames = []
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

    def _ipython_display_(self):
        png_images = []
        for fr in self.frames:
            with io.BytesIO() as output:
                fr.save(output, format="PNG")
                output.seek(0)
                png_images.append(output.read())
        frame_slider = ipywidgets.IntSlider(min=0, max=len(png_images) - 1, step=1)
        im = ipywidgets.Image(value=b"", format="png", height=200)
        html = (
            "<style>.dispersing-pixelated {image-rendering: pixelated;}</style><table>"
        )
        display(ipywidgets.HTML(html))

        def update_image(change):
            im.value = png_images[frame_slider.value]

        im.add_class("dispersing-pixelated")
        im.layout.height = "200px"
        im.layout.object_fit = "contain"
        frame_slider.observe(update_image, "value")
        update_image(None)
        # There's gotta be a better way to do this, but.
        display(ipywidgets.VBox([im, frame_slider]))
