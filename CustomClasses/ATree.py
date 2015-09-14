# ATree Class Definitions
__author__ = 'Sandesh'
import json
import pickle


class ATree:
    """Aggregator Tree to accumulate subsequence count in a string"""

    def __init__(self):
        self.values_computed = False
        self.value = 0
        self.children = {}

    def process_subsequence(self, subsequence, level=1):
        if len(subsequence) == 1:
            if subsequence not in self.children.keys():
                self.children[subsequence] = ATree()
            self.children[subsequence].value += 1
        else:
            head, tail = subsequence[0], subsequence[1:]
            if head not in self.children.keys():
                self.children[head] = ATree()
            self.children[head].process_subsequence(tail, level + 1)

    def process_subsequence_improved(self, subseqeunce_batch):
        pass

    def compute_values(self):
        if not self.values_computed:
            if self.children != {}:
                for key in self.children.keys():
                    self.value += self.children[key].compute_values()
            self.values_computed = True
            return self.value

    def count(self, subsequence):
        if not self.values_computed:
            self.compute_values()
        if len(subsequence) == 1:
            if subsequence in self.children.keys():
                return self.children[subsequence].value
            else:
                return 0
        else:
            head, tail = subsequence[0], subsequence[1:]
            if head not in self.children.keys():
                return 0
            else:
                return self.children[head].count(tail)

    def node_count(self):
        if self.children == {}:
            return 1
        else:
            return 1 + sum([self.children[key].nodeCount() for key in self.children.keys()])

    @staticmethod
    def load_tree(filename):
        with open(filename, 'r') as infile:
            tree_dictionary = json.load(infile)

        return tree_dictionary

    def to_dictionary(self):
        """Return a dictionary representation of the tree"""
        _dict = {}
        if self.children != {}:
            for key in self.children.keys():
                _dict[key] = [self.children[key].value, self.children[key].to_dictionary()]
            return _dict
        else:
            return {}

    def __repr__(self):
        return json.dumps(self.to_dictionary())

    def __eq__(self, cmp_other):
        if self.value == cmp_other.value:
            for key in self.children.keys():
                if key not in cmp_other.children.keys():
                    return False
                if self.children[key].__eq__(cmp_other.children[key]):
                    return False
            return True
        else:
            return False

    def dump_to_file(self, filename):
        with open(filename, 'w') as outfile:
            if not self.values_computed:
                self.compute_values()
            json.dump(self.to_dictionary(), outfile)

    def pickle_into_file(self, filename):
        with open(filename, 'wb') as picklefile:
            if not self.values_computed:
                self.compute_values()
            pickle.dump(self, picklefile)
