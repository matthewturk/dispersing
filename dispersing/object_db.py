from IPython.core.display import display
import ipywidgets


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
        for i, rec in enumerate(game.assets["OBJECTS"].object):
            obj_inst = GameObject(game, rec)
            self[i] = self[obj_inst.name] = obj_inst
