__author__ = 'cyberbeast'
import pandas as pd
from bokeh.plotting import figure
from bokeh.charts import Line, show, output_file
from bokeh.models.widgets import Panel, Tabs
import numpy.polynomial.polynomial as poly
import numpy as np
from operator import sub

print("Initializing Settings")
# Common settings for all visualizations
output_file("Visualizations.html", title="GSAF 2.0 Results")
vis_common_width = 1376
vis_common_height = 768
vis_common_tab_tools = "pan, wheel_zoom, box_zoom, reset, save, crosshair, tap, poly_select, resize"

print("Loading Data")
# Load data for visualizations
data_collection_vis1 = pd.read_csv(open("real-vs-imaginary.csv"),)
data_collection_vis1_formatted = pd.DataFrame(dict(
    x=data_collection_vis1['Real'],
    y=data_collection_vis1['Imaginary']
))
data_collection_vis2 = pd.read_csv(open("squareroot-of-sum-of-squares-of-real-and-imaginary.csv"), index_col=0)

print("Building Visualizations")
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

# TAB 3 Visualizations
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
data_collection_vis2 = pd.read_csv(open("squareroot-of-sum-of-squares-of-real-and-imaginary.csv"), )
clm_list = list(data_collection_vis2)

y = data_collection_vis2[clm_list[1:len(clm_list)]].values
x = np.array([val1 for val1 in range(0, 340)])

coefs50 = poly.polyfit(x, y, 50)
coefs100 = poly.polyfit(x, y, 120)

xp = [i for i in range(0, 340)]

ffit50 = poly.polyval(xp, coefs50)
ffit100 = poly.polyval(xp, coefs100)

list_obs = [data_collection_vis2[clm_list[countt]].tolist() for countt in range(1, 23)]
list_exp = [list(ffit100[stuff]) for stuff in range(0, 22)]
print(len(list_obs))
print(len(list_exp))
print(len(list_obs) == len(list_exp))

error_list = []
for something in range(0, 22):
    list_diff = [a - b for a, b in zip(list_obs[something], list_exp[something])]
    error_list.append(np.mean(list_diff))
print(np.mean(error_list))
data_collection_vis3 = pd.DataFrame(dict(
    index_x=xp,
    C1=ffit100[0].transpose()
    C2=ffit100[1].transpose(),
    C3=ffit100[2].transpose(),
    C4=ffit100[3].transpose(),
    C5=ffit100[4].transpose(),
    C6=ffit100[5].transpose(),
    C7=ffit100[6].transpose(),
    C8=ffit100[7].transpose(),
    C9=ffit100[8].transpose(),
    C10=ffit100[9].transpose(),
    C11=ffit100[10].transpose(),
    C12=ffit100[11].transpose(),
    C13=ffit100[12].transpose(),
    C14=ffit100[13].transpose(),
    C15=ffit100[14].transpose(),
    C16=ffit100[15].transpose(),
    C17=ffit100[16].transpose(),
    C18=ffit100[17].transpose(),
    C19=ffit100[18].transpose(),
    C20=ffit100[19].transpose(),
    C21=ffit100[20].transpose(),
    C22=ffit100[21].transpose(),
))
p_v3 = Line(data_collection_vis3, index='index_x', title="Polynomial Regression Model for fitting Human Genome Data analyzed using GSAF 2.0", xlabel='Position in Eigen Value Set', ylabel='Magnitude', width=vis_common_width, height=vis_common_height, legend=True, tools=vis_common_tab_tools)
tab3 = Panel(child=p_v3, title="Visualization 3 - Polynomial Regression")

tabs = Tabs(tabs=[tab1, tab2, tab3])  # Set Tabs
# show(tabs)  # Show Visualization Output

