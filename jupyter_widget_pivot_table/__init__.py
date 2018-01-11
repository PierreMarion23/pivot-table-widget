
from .__meta__ import __version__

from ._widget_pivot import Pivot
from ._widget_pivotui import PivotUI
from ._options import Pivot_Options, PivotUI_Options
from ._sample import samples


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-widget-pivot-table',
        'require': 'jupyter-widget-pivot-table/extension'
    }]
