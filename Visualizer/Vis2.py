__author__ = 'cyberbeast'
import pandas as pd
from bokeh.plotting import figure
from bokeh.charts import Line, show, output_file
from bokeh.models.widgets import Panel, Tabs

# Common settings for all visualizations
output_file("Visualizations.html", title="GSAF 2.0 Results")
vis_common_width = 1024
vis_common_height = 768
vis_common_tab_tools = "pan, wheel_zoom, box_zoom, reset, save, crosshair, tap, poly_select, resize"

# Load data for visualizations
data_collection_vis1 = pd.read_csv(open("real-vs-imaginary.csv"),)
data_collection_vis1_formatted = pd.DataFrame(dict(
    x=data_collection_vis1['Real'],
    y=data_collection_vis1['Imaginary']
))
data_collection_vis2 = pd.read_csv(open("squareroot-of-sum-of-squares-of-real-and-imaginary.csv"),)

# TAB 1 Visualizations
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
p_v1 = figure(title="Real vs Imaginary parts of Eigen Values", width=vis_common_width, height=vis_common_height, tools=vis_common_tab_tools + ",lasso_select")
p_v1.xaxis.axis_label = "Real"
p_v1.yaxis.axis_label = "Imaginary"
p_v1.circle(data_collection_vis1_formatted["x"], data_collection_vis1_formatted["y"], size=10)
tab1 = Panel(child=p_v1, title="Visualization 1 - (x)+(y)j")

# TAB 2 Visualizations
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
p_v2 = Line(data_collection_vis2, title="Magnitude vs. Eigen Position", xlabel='Position in Eigen Value Set', ylabel='Magnitude', width=vis_common_width, height=vis_common_height, legend=True, tools=vis_common_tab_tools + ", hover")
tab2 = Panel(child=p_v2, title="Visualization 2 - sqrt((x)^2+(y)^2)")

tabs = Tabs(tabs=[tab1, tab2])  # Set Tabs
show(tabs)  # Show Visualization Output

