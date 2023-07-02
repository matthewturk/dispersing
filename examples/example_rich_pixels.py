from rich_pixels import Pixels
from rich.console import Console
import dispersing

ts = dispersing.games.TheSummoning("the-summoning")

console = Console()

console.print(Pixels.from_image(ts.npcs[103].images['head'].frames[0]))
