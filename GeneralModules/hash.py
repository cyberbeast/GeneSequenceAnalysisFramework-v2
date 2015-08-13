__author__ = 'cyberbeast'

from itertools import product
from GeneralModules.GMCount import NumberOf

# Variables & Dictionaries Initialization
# --------------------------------------------------------
depth = 4
UniquePatterns = ["".join(x) for i in range(1, 5) for x in product(* ['ATGC']*i)]
GDS = {}
GDS_UniqueCount = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns))]))
GDS['GDS_UniqueCount'] = GDS_UniqueCount
GDS['GDS_Links'] = {}
GDS_Links = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns))]))
for l in dict(zip(UniquePatterns, [0 for o in range(1, NumberOf(UniquePatterns))])):
    GDS['GDS_Links'][l] = dict(zip(UniquePatterns, 0 for u in range(1, NumberOf(UniquePatterns))))
