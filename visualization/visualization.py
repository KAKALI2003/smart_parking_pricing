from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from datetime import datetime
from bokeh.layouts import column

source = ColumnDataSource(data = dict(time =[], price = []))

p = figure(title = "Real-Time parking price", x_axis_type = "datetime", height = 300)
p.line(x = "time", y = "price", source = source)

def update_plot(price):
    new_data = dict(time=[datetime.now()], price=[price])
    source.stream(new_data, rollover=100)       # .stream() insert the new_data into the source
                                                # rollover = 100: the graph will retain a maximum of 100 data points — if new data arrives beyond that, the oldest points will be removed to maintain performance and prevent the graph from becoming cluttered.
def get_layout():
    return column(p)