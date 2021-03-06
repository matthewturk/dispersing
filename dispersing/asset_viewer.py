import bqplot
import ipycanvas
import ipywidgets
import traitlets


class ObjectViewer(traitlets.HasTraits):
    obj_id = traitlets.CInt()


class MapViewer(traitlets.HasTraits):
    map_id = traitlets.CInt()
