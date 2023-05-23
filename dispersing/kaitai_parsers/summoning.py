from .summoning_colors import SummoningColors as COLORS
from .summoning_init import SummoningInit as INIT
from .summoning_interact import SummoningInteract as INTERACT
from .summoning_keywords import SummoningKeywords as KEYWORDS
from .summoning_levels import SummoningLevels as LEVELS
from .summoning_npc import SummoningNpc as NPC
from .summoning_object import SummoningObject as OBJECTS
from .summoning_resources import SummoningResources as RESOURCE
from .summoning_text import SummoningText as TEXT

# Files still to address:
#   * JAZ
#   * TAGS
#   * V

try:
    from IPython.display import display
    import ipywidgets
except ImportError:
    pass  # Things just won't work

# We monkeypatch some stuff here so that we can have vanilla compilation for the
# ksy files.


def _COLORS_ipython_display(self):
    display(ipywidgets.Label("Colors"))


COLORS._ipython_display_ = _COLORS_ipython_display
