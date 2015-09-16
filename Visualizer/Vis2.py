__author__ = 'cyberbeast'
import pandas as pd
from bokeh.charts import Line, show, output_file
from bokeh.models.widgets import Panel, Tabs

data_coll = pd.read_csv(open("squareroot-of-sum-of-squares-of-real-and-imaginary.csv"),)
data = pd.DataFrame(dict(
    p=data_coll['C1']
))
output_file("Visualizations.html")
tab1_tools = "pan, wheel_zoom, box_zoom, reset, save, hover, crosshair, tap, poly_select, lasso_select, resize"
p = Line(data_coll, title="Magnitude vs. Eigen Position", xlabel='Position in Eigen Value Set', ylabel='Magnitude', width=1500, height=850, legend=True, tools=tab1_tools)
tab1 = Panel(child=p, title="sqrt(x^2+y^2)")

tabs = Tabs(tabs=[tab1])
show(tabs)