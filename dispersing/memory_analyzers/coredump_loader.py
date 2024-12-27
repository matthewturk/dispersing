import traitlets
import ipywidgets
import IPython.display
import struct

try:
    from jupyterlab_kaitai import HexViewer
except ImportError:
    HexViewer = None


class MemoryLocation(traitlets.HasTraits):
    name = traitlets.Unicode("Unknown")
    address = traitlets.Int()
    display_address = traitlets.Unicode()
    data = traitlets.Bytes()
    value = traitlets.Any()
    display_value = traitlets.Unicode()
    data_type = traitlets.Unicode()

    @traitlets.observe("data", "data_type")
    def _data_changed(self, change):
        if self.data is None or len(self.data) == 0:
            return
        size = struct.calcsize(self.data_type)
        self.value = struct.unpack(
            self.data_type, self.data[self.address : self.address + size]
        )

    @traitlets.observe("address")
    def _address_changed(self, change):
        # Would be better to use a formatter in the traits display, but I like
        # the iteration there too much.
        self.display_address = hex(self.address)

    @traitlets.observe("value")
    def _value_changed(self, change):
        if len(self.value) == 1:
            (value,) = self.value
        else:
            value = "; ".join(str(_) for _ in self.value)
        self.display_value = str(value)


class Coredump(traitlets.HasTraits):
    filename = traitlets.Unicode()
    data = traitlets.Bytes()
    labels = traitlets.List(trait=traitlets.Instance(MemoryLocation))

    def __getitem__(self, item):
        v = {_.name: _.value for _ in self.labels}
        return v[item]

    def __iter__(self, item):
        return {_.name: _.value for _ in self.labels}

    def keys(self):
        return [_.name for _ in self.labels]

    @traitlets.observe("filename")
    def _filename_changed(self, change):
        self.data = open(self.filename, "rb").read()

    @traitlets.observe("data")
    def _data_changed(self, change):
        for label in self.labels:
            label.data = self.data

    def _ipython_display_(self):
        children = []
        if HexViewer is not None:
            children.append(HexViewer(self.data))

        if len(self.labels) > 0:
            rows = []
            attrs = ("name", "display_address", "data_type", "display_value")
            gs = ipywidgets.GridspecLayout(
                n_rows=len(self.labels), n_columns=len(attrs)
            )
            for i, mem_label in enumerate(self.labels):
                for j, attr in enumerate(attrs):
                    l = ipywidgets.Label()
                    traitlets.link(
                        (mem_label, attr),
                        (l, "value"),
                        (lambda a: str(a), lambda a: str(a)),
                    )
                    gs[i, j] = l
            children.append(gs)

        IPython.display.display(ipywidgets.VBox(children))
