__author__ = 'Sandesh'

from CustomClasses.Chromosome import *
import glob
from multiprocessing import Pool, Process, Manager

filelist = []
for name in glob.glob('GenomeDataset/Processing/*pTREE'):
    filelist.append(name)

for infile in filelist:
    ch = Chromosome()
    ch.analyze(infile)
