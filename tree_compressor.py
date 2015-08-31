__author__ = 'Sandesh'
from CustomClasses.ATree import *
import json


with open("tree.fa_TREE", "r") as infile:
	tree_dict = json.load(infile)

new_tree = ATree()
new_tree.load_tree("tree.fa_TREE")

print(new_tree)
