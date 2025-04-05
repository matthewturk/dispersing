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
        if rec.header.algo == 1:
            # This is definitely not as fast or efficient as it could be, but
            # I wanted to translate precisely as-is before going further.
            contents = np.frombuffer(rec.contents, dtype='i1').tolist()
            buff = []
            values = []
            next_run_length = 0
            for i in range(rec.header.height * rec.header.width):
                if next_run_length == 0:
                    v = contents.pop(0)
                    if v < 0:
                        next_run_length = 1 - v
                        v0 = contents.pop(0)
                        buff.extend([v0 for _ in range(next_run_length)])
                    else:
                        next_run_length = v + 1
                        buff.extend([contents.pop(0) for _ in range(next_run_length)])
                next_run_length -= 1
                values.append(buff.pop(0))
            rec_data = np.array(values, dtype='i1').view('u1')
        elif rec.header.algo == 3:
            rec_data = unpack_sprite_algo3(rec.contents, c * h * w)
        else:
            return
        im = rec_data.reshape((c, h, w))
        im = np.moveaxis(im, 0, -1)
        self.im = im
        sprite_id = getattr(rec, 'i', -1)
        # This is currently hardcoded for the summoning's palimpsest
        if sprite_id >= 0x4b and sprite_id <= 0x51:
            pal1_id = 2
            pal2_id = 3
        else:
            pal1_id = 0
            pal2_id = 1
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
            "<style>.dispersing-pixelated {image-rendering: pixelated;} img.vga-aspect-ratio {aspect-ratio: 4/3;}</style><table>"
        )
        display(ipywidgets.HTML(html))

        def update_image(change):
            im.value = png_images[frame_slider.value]

        im.add_class("dispersing-pixelated")
        im.add_class("vga-aspect-ratio")
        im.layout.height = "200px"
        im.layout.object_fit = "contain"
        frame_slider.observe(update_image, "value")
        update_image(None)
        # There's gotta be a better way to do this, but.
        display(ipywidgets.VBox([im, frame_slider]))
