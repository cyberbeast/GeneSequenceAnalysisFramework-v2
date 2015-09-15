__author__ = 'cyberbeast'
__author__ = 'Sandesh'

from CustomClasses.Chromosome import *
import glob
from bokeh.plotting import figure, output_file, show
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy.random import rand
from multiprocessing import Pool, Process, Manager

filelist = []

y_val_imag = []
y_val_real = []
y_val = []
x_val = []
x1_val = [x for x in range(22)]


def plot1():
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(y_val_real, y_val_imag, x_val, c='r', marker='o')

    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("Chromosome")

    ax.set_zlim3d(1, 22)

    s = 50
    fig, ax = plt.subplots()
    ax.scatter(y_val_real, y_val_imag, s, 'r', marker='o')
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    plt.show()


for name in glob.glob('GenomeDataset/Processing/*pChromosome'):
    filelist.append(name)

if len(filelist) == 0:
    for name in glob.glob('GenomeDataset/Processing/*pTREE'):
        filelist.append(name)

i = 1
for infile in filelist:
    if "pChromosome" not in infile:
        ch = Chromosome()
        ch.analyze(infile)
    else:
        with open(infile, 'rb') as in_fh:
            ch = Chromosome()
            ch = pickle.load(in_fh)

    y_val = ch.calculate_eigen_values()
    y_val_real.append(list(y_val.real))
    y_val_imag.append(list(y_val.imag))
    x_val.append([i for _ in range(len(y_val))])
    i += 1

plot1()


