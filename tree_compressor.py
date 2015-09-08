__author__ = 'Sandesh'
from CustomClasses.ATree import *
from itertools import product
import pprint
import glob
import numpy as np
import os
import re

_nsre = re.compile('([0-9]+)')

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]


filelist = []
for name in glob.glob('GenomeDataset/Processing/*pTREE'):
    filelist.append(name)
filelist.sort(key=natural_sort_key)
pattern_list = ["".join(x) for i in range(1, 5) for x in product(*['ATGC'] * i)]
pattern_list.sort()
count_matrix = {}
result = {pattern: [] for pattern in pattern_list}

for infile in filelist:
    with open(infile, 'rb') as in_fh:
        new_tree = pickle.load(in_fh)

    for pattern in pattern_list:
        # result[pattern].append(os.path.basename(infile) + "-->" + str(new_tree.count(pattern)))
        result[pattern].append(new_tree.count(pattern))

pprint.pprint(result, width=250)
#
# for keys, values in result:
# 	print(keys, end='')
# 	print(values)

input_str = str(input('PATTERN? \t'))
input_chr = int(input('CHR? \t\t'))

print(str(result[input_str][input_chr - 1]))
