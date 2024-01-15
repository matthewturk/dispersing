import io
import ipywidgets
from IPython.display import display
import pandas as pd

_display_fields = (
    ("Name", "name"),
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


class GameObject:
    def __init__(self, game, record):
        self.game = game  # Enables us to look things up more easily
        self.record = record
        offsets = game.assets["INIT"].sprite_offsets
        self.images = {}
        for img_type in ("small", "worn", "tiny"):
            self.images[img_type] = game.resources.sprites[
                getattr(offsets, img_type + "_object") + record.image_id
            ]
        for _, k in _display_fields:
            setattr(self, k, getattr(record, k, ""))
        self.name = game.assets["TEXT"].text[record.text_record].value.decode("ascii")

    def _ipython_display_(self):
        outputs = {}
        for t, i in self.images.items():
            outputs[t] = ipywidgets.Output()
            with outputs[t]:
                display(i.frames[0])
        vb = ipywidgets.VBox(
            [ipywidgets.HBox([outputs["small"], outputs["tiny"]]), outputs["worn"]]
        )
        display(vb)


class ObjectDatabase(dict):
    def __init__(self, game):
        super(dict, self).__init__()
        self.game = game
        self.n_objs = len(game.assets["OBJECTS"].object)
        for i, rec in enumerate(game.assets["OBJECTS"].object):
            obj_inst = GameObject(game, rec)
            self[i] = self[obj_inst.name] = obj_inst

    def to_df(self):
        obj = self[0]
        fields = [
            _
            for _ in dir(obj)
            if not _.startswith("_")
            and _ not in ("close", "from_file", "from_io", "from_bytes")
        ]
        fields.sort()
        records = []
        for n, orec in sorted(self.items()):
            rec = {_: getattr(orec, _) for _ in fields}
            rec["obj_type"] = orec.obj_type.name
            records.append(rec)
        df = pd.DataFrame(records)
        return df

    def _ipython_display_(self):
        n = self.n_objs
        png_images = []
        for i in range(n):
            png_images.append([])
            for fr in self[i].images["small"].frames:
                with io.BytesIO() as output:
                    fr.save(output, format="PNG")
                    output.seek(0)
                    png_images[-1].append(output.read())
        sprite_slider = ipywidgets.IntSlider(min=0, max=n - 1, step=1)
        frame_slider = ipywidgets.IntSlider(min=0, step=1)
        frame_label = ipywidgets.Label(value="")
        im = ipywidgets.Image(value=b"", format="png", height=200)
        span = ipywidgets.HTML()

        def update_record(change):
            new_object_record = self[sprite_slider.value]
            span.value = _fill_template(new_object_record)

        def update_image(change):
            im.value = png_images[sprite_slider.value][frame_slider.value]

        def update_sprite(change):
            nf = len(png_images[sprite_slider.value])
            frame_label.value = f"({nf})"
            frame_slider.max = nf - 1

        im.add_class("dispersing-pixelated")
        im.layout.height = "200px"
        im.layout.object_fit = "contain"
        sprite_slider.observe(update_record, "value")
        sprite_slider.observe(update_sprite, "value")
        sprite_slider.observe(update_image, "value")
        frame_slider.observe(update_image, "value")
        # There's gotta be a better way to do this, but.
        sprite_slider.value = 1
        sprite_slider.value = 0
        display(
            ipywidgets.HBox(
                [
                    ipywidgets.VBox(
                        [
                            sprite_slider,
                            ipywidgets.HBox([frame_slider, frame_label]),
                            span,
                        ]
                    ),
                    im,
                ]
            )
        )
