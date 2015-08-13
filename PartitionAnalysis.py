__author__ = 'cyberbeast'
from Bio import SeqIO
from itertools import product
from GeneralModules.GMCount import NumberOf

# Variables & Dictionaries Initialization
# --------------------------------------------------------
depth = 2
UniquePatterns = ["".join(x) for i in range(1, depth + 1) for x in product(*['ATCG'] * 4)]
GDS = {}
GDS_UniqueCount = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns))]))
GDS['GDS_UniqueCount'] = GDS_UniqueCount
GDS['GDS_Links'] = {}
GDS_Links = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns))]))
for l in dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns))])):
    GDS["GDS_Links"][l] = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns))]))

print(GDS)

