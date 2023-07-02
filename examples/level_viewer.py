from rich.segment import Segment
from rich.style import Style
from collections import defaultdict
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.coordinate import Coordinate
from textual.geometry import Region
from textual.strip import Strip
from textual.widget import Widget
from textual.widgets import Header, Footer, DataTable, Static
import dispersing
ts = dispersing.games.TheSummoning("the-summoning/")
from dispersing.level_map import _tile_conversions
tile_map = defaultdict(lambda: '\u2592')
tile_map.update({k: v.decode('cp437').encode('utf-8').decode('utf-8') for
                    k, v in _tile_conversions.items()})

class LevelViewer(Widget):

    level_id: int = reactive(0)
    coord: Coordinate = reactive(Coordinate(0,0))

    COMPONENT_CLASSES = {
        "level-viewer--wall",
        "level-viewer--floor",
        "level-viewer--unknown",
        "level-viewer--empty",
        "level-viewer--highlighted",
    }

    def watch_level_id(self, level_id: int) -> None:
        self.coord = Coordinate(0,0)
        self.render()

    def render_line(self, y: int) -> Strip:
        def colorize(tile_id):
            if tile_id <= 17:
                style = self.get_component_rich_style("level-viewer--wall")
            elif tile_id < 31:
                style = self.get_component_rich_style("level-viewer--floor")
            elif tile_id == 255:
                style = self.get_component_rich_style("level-viewer--empty")
            else:
                style = self.get_component_rich_style("level-viewer--unknown")
            return f"{tile_map[tile_id]}", style

        tiles = ts.levels[self.level_id].tiles
        if y >= tiles.shape[0]: return Strip([])
        segments = [Segment(*colorize(_)) for _ in tiles[y, :]]
        if self.coord.row == y:
            highlighted = self.get_component_rich_style("level-viewer--highlighted")
            seg = segments[self.coord.column]
            segments[self.coord.column] = Segment(seg.text, highlighted)
        return Strip(segments)

    def watch_coord(self, coord: Coordinate) -> None:
        reg = Region(coord.column - 1, coord.row - 1, 3, 3)
        self.refresh(reg)

    def validate_coord(self, coord: Coordinate) -> Coordinate:
        tiles = ts.levels[self.level_id].tiles
        column = max(min(coord.column, tiles.shape[1] - 1), 0)
        row = max(min(coord.row, tiles.shape[0] - 1), 0)
        return Coordinate(row = row, column = column)

class LevelViewerApp(App):
    BINDINGS = [("j", "next_level", "Go to next level"),
                ("k", "prev_level", "Go to previous level"),
                ("up", "move_up", ""),
                ("down", "move_down", ""),
                ("left", "move_left", ""),
                ("right", "move_right", "")]
    CSS_PATH = "level_viewer.css"

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield LevelViewer()
        yield Footer()

    def action_next_level(self) -> None:
        lv = self.query_one(LevelViewer)
        lv.level_id = min(lv.level_id + 1, len(ts.levels) - 1)

    def action_prev_level(self) -> None:
        lv = self.query_one(LevelViewer)
        lv.level_id = max(lv.level_id - 1, 0)

    def action_move_up(self) -> None:
        lv = self.query_one(LevelViewer)
        lv.coord = Coordinate(column = lv.coord.column, row = lv.coord.row - 1)

    def action_move_down(self) -> None:
        lv = self.query_one(LevelViewer)
        lv.coord = Coordinate(column = lv.coord.column, row = lv.coord.row + 1)

    def action_move_left(self) -> None:
        lv = self.query_one(LevelViewer)
        lv.coord = Coordinate(column = lv.coord.column - 1, row = lv.coord.row)

    def action_move_right(self) -> None:
        lv = self.query_one(LevelViewer)
        lv.coord = Coordinate(column = lv.coord.column + 1, row = lv.coord.row)

if __name__ == "__main__":
    app = LevelViewerApp()
    app.run()
