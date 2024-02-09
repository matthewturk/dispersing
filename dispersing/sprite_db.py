import ipywidgets

class SpriteDatabase(dict):
    def __init__(self, game):
        super(dict, self).__init__()
        self.game = game
        for k, sprite in sorted(game.resources.sprites.items()):
            self[k] = sprite

    def _ipython_display_(self):
        sprite_id = ipywidgets.SelectionSlider(options = self.keys(), index = 0)
        out = ipywidgets.Output()

        def change_sprite(event):
            with out:
                out.clear_output(wait=True)
                display(self[event["new"]])

        sprite_id.observe(change_sprite, "value")

        display(ipywidgets.VBox([sprite_id, out]))
