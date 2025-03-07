"""# use_cross_filter"""

import plotly

import solara
import solara.lab
from solara.website.utils import apidoc

title = "use_cross_filter"


df = plotly.data.gapminder()


@solara.component
def Page():
    solara.provide_cross_filter()
    solara.CrossFilterReport(df, classes=["py-2"])
    solara.CrossFilterSelect(df, "continent")
    solara.CrossFilterSlider(df, "gdpPercap", mode=">")


__doc__ += apidoc(solara.use_cross_filter)  # type: ignore
