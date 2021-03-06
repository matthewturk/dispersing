import io
import ipywidgets
from IPython.display import display

_display_fields = (
    ("AC Bonus", "ac_bonus"),
    ("col0", "col0"),
    ("weight", "weight"),
    ("Container Flags", "container_flags"),
    ("col4", "col4"),
    ("col5", "col5"),
    ("Action 1 DMG", "act1_dmg"),
    ("Action 1 Flags", "act1_flags"),
    ("Action 2 DMG", "act2_dmg"),
    ("Action 2 Flags", "act2_flags"),
    ("Action 3 DMG", "act3_dmg"),
    ("Action 3 Flags", "act3_flags"),
    ("Charges", "charges"),
    ("col11", "col11"),
    ("Sub", "col12"),
    ("Type", "obj_type"),
    ("col14", "col14"),
)


def _fill_template(record):
    html = "<style>.dispersing-pixelated {image-rendering: pixelated;}</style><table>"
    for title, field in _display_fields:
        html += f"<tr><td><b>{title}</b></td><td>{getattr(record, field)}</td></tr>\n"
    return html + "</table>"


class ObjectDatabase:
    def __init__(self, game):
        self.object_asset = game.assets["OBJECTS"]
        self.objects_by_id = {}
        self.objects_by_name = {}
        self.images_by_id = {}
        self.images_by_name = {}
        self.id_to_name = {}
        text_asset = game.assets["TEXT"]
        for i, obj in enumerate(self.object_asset.object):
            small_id = obj.image_id + 100
            big_id = obj.image_id + 333
            name = text_asset.text[obj.text_record].value.decode("ascii")
            self.id_to_name[i] = name
            self.objects_by_id[i] = obj
            self.objects_by_name[name] = obj
            self.images_by_id[i] = (
                game.resources.sprites[small_id],
                game.resources.sprites[big_id],
            )
            self.images_by_name[name] = self.images_by_id[i]

    def __contains__(self, key):
        return key in self.objects_by_id or key in self.objects_by_name

    def __getitem__(self, item):
        if item in self.objects_by_id:
            return (self.objects_by_id[item], self.images_by_id[item])
        elif item in self.objects_by_name:
            return (self.objects_by_name[item], self.images_by_name[item])
        else:
            raise KeyError(item)

    def _ipython_display_(self):
        n = len(self.objects_by_id)
        png_images = []
        for i in range(n):
            png_images.append([])
            for fr in self[i][1][1].frames:
                with io.BytesIO() as output:
                    fr.save(output, format="PNG")
                    output.seek(0)
                    png_images[-1].append(output.read())
        sprite_slider = ipywidgets.IntSlider(min=0, max=n, step=1)
        frame_slider = ipywidgets.IntSlider(min=0, step=1)
        im = ipywidgets.Image(value=b"", format="png", height=200)
        span = ipywidgets.HTML()

        def update_record(change):
            new_object_record = self.objects_by_id[sprite_slider.value]
            span.value = _fill_template(new_object_record)

        def update_image(change):
            im.value = png_images[sprite_slider.value][frame_slider.value]

        def update_sprite(change):
            frame_slider.max = len(png_images[sprite_slider.value])

        im.add_class("dispersing-pixelated")
        im.layout.height = "200px"
        im.layout.object_fit = "contain"
        sprite_slider.observe(update_record, "value")
        sprite_slider.observe(update_sprite, "value")
        sprite_slider.observe(update_image, "value")
        frame_slider.observe(update_image, "value")
        sprite_slider.value = 0
        display(
            ipywidgets.HBox([ipywidgets.VBox([sprite_slider, frame_slider, span]), im])
        )
