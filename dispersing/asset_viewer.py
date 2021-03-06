import ipywidgets
import traitlets
import ipycanvas
import bqplot


class ObjectViewer(traitlets.HasTraits):
    obj_id = traitlets.CInt()


class MapViewer(traitlets.HasTraits):
    map_id = traitlets.CInt()
