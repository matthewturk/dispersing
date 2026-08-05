from rich.console import Console
from rich_pixels import Pixels

import dispersing

ts = dispersing.games.TheSummoning("the-summoning")

console = Console()

console.print(Pixels.from_image(ts.npcs[103].images["head"].frames[0]))
