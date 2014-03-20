from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .geom import geom

class geom_vline(geom):
    VALID_AES = ['x', 'ymin', 'ymax', 'color', 'linestyle', 'alpha', 'label']

    def plot_layer(self, data, ax):
        groups = {'color', 'alpha', 'linestyle'}
        groups = groups & set(data.columns)
        if groups:
            for name, _data in data.groupby(list(groups)):
                _data = _data.to_dict('list')
                for ae in groups:
                    _data[ae] = _data[ae][0]
                self._plot(_data, ax)
        else:
            _data = data.to_dict('list')
            self._plot(_data, ax)

    def _plot(self, layer, ax):
        layer = dict((k, v) for k, v in layer.items() if k in self.VALID_AES)
        layer.update(self.manual_aes)
        if 'x' in layer:
            x = layer.pop('x')
        ymin, ymax = None, None
        if 'ymin' in layer:
            ymin = layer.pop('ymin')
        else:
            ymin = 0
        if 'ymax' in layer:
            ymax = layer.pop('ymax')
        else:
            ymax = 0
        if ymin and ymax:
            ax.axvline(x=x, ymin=ymin, ymax=ymax, **layer)
        elif ymin:
            ax.axvline(x=x, ymin=ymin, **layer)
        elif ymax:
            ax.axvline(x=x, ymax=ymax, **layer)
        else:
            ax.axvline(x=x, **layer)


