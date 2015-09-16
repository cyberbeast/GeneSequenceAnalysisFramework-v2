# Chromosome Class Definitions
__author__ = 'cyberbeast'

import numpy as np
from numpy import linalg as LA
from CustomClasses.ATree import *
from itertools import product
import pprint
import json


class Chromosome:
    """Chromosome class to handle analysis modules"""

    _pattern_list = ["".join(x) for i in range(1, 9) for x in product(*['ACGT'] * i)]
    _pattern_list.sort()
    _pattern_list_half = ["".join(x) for i in range(1, 5) for x in product(*['ACGT'] * i)]
    _pattern_list_half.sort()

    def __init__(self):
        self.eigen_exists = False
        self.eigen_values = []

        # statistical_inferences attribute used for storing mean, mode, median, min, max, average
        self.statistical_inferences_exist = False
        self.statistical_inferences = {"mean": 0, "mode": 0, 'median': 0, 'min': 0, 'max': 0, 'range': 0}

        self.has_been_analyzed = False

        self.gmap_exists = False
        self.gmap = np.zeros((340, 340), dtype=np.int)

        self.lookup_table = []

        self.new_tree = ATree()

    def load_chromosome_tree(self, filename):
        with open(filename, 'rb') as in_fh:
            self.new_tree = pickle.load(in_fh)

    def analyze(self, chromosome_file):
        if not self.has_been_analyzed:
            self.load_chromosome_tree(chromosome_file)
            self.map(chromosome_file) if not self.gmap_exists else print('Chromosome is mapped!')
            self.calculate_eigen_values() if not self.eigen_exists else print('EV(s) exist!')

            # Dump pickled data
            self.store_to_file(chromosome_file + "_pChromosome", filealso=False)

            # Update has_been_analyzed attribute
            self.has_been_analyzed = True

    def map(self, chromosome_file):
        # Mapping Logic Code
        for pattern in self._pattern_list:
            if len(pattern) > 1:
                if len(pattern) == 2:
                    self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][
                        self._pattern_list_half.index(pattern[int(len(pattern) / 2):])] = self.new_tree.count(pattern)
                    # print(pattern[:int(len(pattern) / 2)] + "-->" + pattern[int(len(pattern) / 2):] + ":::" + str(self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][self._pattern_list_half.index(pattern[int(len(pattern) / 2):])]))
                else:
                    if 1 + len(pattern) / 2 <= 4:
                        self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][
                            self._pattern_list_half.index(pattern[int(len(pattern) / 2):])] = self.new_tree.count(
                            pattern)
                        # print(pattern[:int(len(pattern) / 2)] + "-->" + pattern[int(len(pattern) / 2):] + ":::" + str(self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][self._pattern_list_half.index(pattern[int(len(pattern) / 2):])]))
                        self.gmap[self._pattern_list_half.index(pattern[:1 + int(len(pattern) / 2)])][
                            self._pattern_list_half.index(pattern[1 + int(len(pattern) / 2):])] = self.new_tree.count(
                            pattern)
                        # print(pattern[:1 + int(len(pattern) / 2)] + "-->" + pattern[1 + int(len(pattern) / 2):] + ":::" + str(self.gmap[self._pattern_list_half.index(pattern[:1 + int(len(pattern) / 2)])][self._pattern_list_half.index(pattern[1 + int(len(pattern) / 2):])]))

        self.gmap_exists = True
        print(str(chromosome_file) + " mapped successfully!")
        # print(self.gmap)

        with open('op', 'w') as outfile:
            outfile.write(str(self.gmap))

            # This is to check if the mapping is indeed correct. If correct, both the print statements will print the same numerical value.
            # print(self.gmap[self._pattern_list_half.index('A')][self._pattern_list_half.index('AA')])
            # print(self.gmap[self._pattern_list_half.index('AA')][self._pattern_list_half.index('A')])

    def store_to_file(self, filename, filealso=False):
        with open(filename, 'wb') as picklefile:
            pickle.dump(self, picklefile)
        print("Stored to " + filename + " successfully!")

        if filealso:
            self.gmap.tofile(filename + "MAP_MATRIX_")

    def calculate_eigen_values(self):
        # Eigen Value Calculation and Output Code
        w, v = LA.eig(self.gmap)
        # print(len(w))
        # Populate statistical inferences
        self.statistical_inferences['mean'] = np.mean(self.gmap)
        # self.statistical_inferences['mode'] =
        self.statistical_inferences['median'] = np.median(self.gmap)
        self.statistical_inferences['min'] = np.amin(self.gmap)
        self.statistical_inferences['max'] = np.amax(self.gmap)
        self.statistical_inferences['range'] = np.ptp(self.gmap)
        self.statistical_inferences_exist = True
        # print(self.statistical_inferences)

        # with open("map" + )

        return w
