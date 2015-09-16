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
import numpy
import pandas as pd

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

df1 = pd.DataFrame()

i = 1
with open('Visualizer/output-file.txt', 'w') as outf:
    for infile in filelist:
        if "pChromosome" not in infile:
            ch = Chromosome()
            ch.analyze(infile)
        else:
            with open(infile, 'rb') as in_fh:
                ch = Chromosome()
                ch = pickle.load(in_fh)

        y_val = ch.calculate_eigen_values()
        y_val_real.append(y_val.real)
        y_val_imag.append(y_val.imag)
        x_val.append([i for _ in range(len(y_val))])

        y_r = [y.real for y in y_val.tolist()]
        y_i = [y.imag for y in y_val.tolist()]

        for rr, ri in zip(y_r, y_i):
            outf.write(str(rr) + "," + str(ri) + '\n')

        y_r_square = [real**2 for real in y_r]
        y_i_square = [imag**2 for imag in y_i]

        y_sqrt_of_sum_of_R_I_list = []

        for rr2, ri2 in zip(y_r_square, y_i_square):
            y_sqrt_of_sum_of_R_I_list.append(np.sqrt(rr2 + ri2))

        df1["C" + str(i)] = y_sqrt_of_sum_of_R_I_list

        i += 1

df1.to_csv('Visualizer/squareroot-of-sum-of-squares-of-real-and-imaginary.csv')
plot1()


