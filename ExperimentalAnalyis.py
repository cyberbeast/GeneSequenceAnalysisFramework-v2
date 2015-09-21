__author__ = 'cyberbeast'

from CustomClasses.Chromosome import *
import glob
from bokeh.plotting import figure, output_file, show
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import rand
from multiprocessing import Pool, Process, Manager
import numpy
import numpy.polynomial.polynomial as poly
import pandas as pd
import pprint

data_collection_vis2 = pd.read_csv(open("Visualizer/squareroot-of-sum-of-squares-of-real-and-imaginary.csv"), )
# pprint.pprint(data_collection_vis2.values)

clm_list = list(data_collection_vis2)

y = data_collection_vis2[clm_list[1:len(clm_list)]].values
x = np.array([val1 for val1 in range(0, 340)])

coefs50 = poly.polyfit(x, y, 50)
coefs100 = poly.polyfit(x, y, 121)

xp = [i for i in range(0, 340)]

ffit50 = poly.polyval(xp, coefs50)
ffit100 = poly.polyval(xp, coefs100)

_ = plt.plot(x, y, '.', xp, ffit50.transpose(), '-', xp, ffit100.transpose(), '--')
plt.show()
