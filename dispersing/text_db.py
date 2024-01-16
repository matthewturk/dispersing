import ipywidgets
from IPython.display import display


class TextDatabase(dict):
    def __init__(self, game):
        super().__init__()
        self.game = game
        for i, rec in enumerate(game.assets["TEXT"].text):
            self[i] = rec.value

    def _ipython_display_(self):
        record_id = ipywidgets.IntSlider(min=0, max=len(self) - 1, step=1)
        record_id.value = 0
        text_value = ipywidgets.Textarea(disabled=True, value=self[0], rows=10)

        def change_record(event):
            text_value.value = self[event["new"]]

        record_id.observe(change_record, "value")

        display(ipywidgets.VBox([record_id, text_value]))
