# Chromosome Class Definitions
__author__ = 'cyberbeast'

import numpy
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
        self.statistical_inferences = {}

        self.has_been_analyzed = False

        self.gmap_exists = False
        self.gmap = numpy.zeros((340, 340), dtype=numpy.int)

        self.lookup_table = []

        self.new_tree = ATree()

    def load_chromosome_tree(self, filename):
        with open(filename, 'rb') as in_fh:
            self.new_tree = pickle.load(in_fh)

    def analyze(self, chromosome_file):
        self.load_chromosome_tree(chromosome_file)
        self.map() if not self.gmap_exists else print('Chromosome is mapped!')
        # self.calculate_eigen_values() if not self.eigen_exists else print('EV(s) exist!')

        # Update has_been_analyzed attribute
        self.has_been_analyzed = True

    def map(self):
        # Mapping Logic Code
        for pattern in self._pattern_list:
            if len(pattern) > 1:
                if len(pattern) == 2:
                    self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][
                        self._pattern_list_half.index(pattern[int(len(pattern) / 2):])] = self.new_tree.count(pattern)
                    print(pattern[:int(len(pattern) / 2)] + "-->" + pattern[int(len(pattern) / 2):] + ":::" + str(
                        self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][
                            self._pattern_list_half.index(pattern[int(len(pattern) / 2):])]))
                else:
                    if 1 + len(pattern)/2 <= 4:
                        self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][
                            self._pattern_list_half.index(pattern[int(len(pattern) / 2):])] = self.new_tree.count(pattern)
                        print(pattern[:int(len(pattern) / 2)] + "-->" + pattern[int(len(pattern) / 2):] + ":::" + str(
                            self.gmap[self._pattern_list_half.index(pattern[:int(len(pattern) / 2)])][
                                self._pattern_list_half.index(pattern[int(len(pattern) / 2):])]))
                        self.gmap[self._pattern_list_half.index(pattern[:1 + int(len(pattern) / 2)])][
                            self._pattern_list_half.index(pattern[1 + int(len(pattern) / 2):])] = self.new_tree.count(
                            pattern)
                        print(
                            pattern[:1 + int(len(pattern) / 2)] + "-->" + pattern[1 + int(len(pattern) / 2):] + ":::" + str(
                                self.gmap[self._pattern_list_half.index(pattern[:1 + int(len(pattern) / 2)])][
                                    self._pattern_list_half.index(pattern[1 + int(len(pattern) / 2):])]))

        self.gmap_exists = True
        print("Mapped Successfully!")
        # print(self.gmap)

        with open('op', 'w') as outfile:
            outfile.write(str(self.gmap))

        print(self.gmap[self._pattern_list_half.index('A')][self._pattern_list_half.index('AA')])
        print(self.gmap[self._pattern_list_half.index('AA')][self._pattern_list_half.index('A')])

    def store_to_file(self, filename):
        with open(filename, 'w') as picklefile:
            if not self.has_been_analyzed:
                self.analyze()
            pickle.dump(self, picklefile)
        print("Stored to " + filename + " successfully!")

        # def calculate_eigen_values(self, matrix):
        #     # Eigen Value Calculation and Output Code
