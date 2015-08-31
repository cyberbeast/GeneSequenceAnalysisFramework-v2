# Distributed Processing Module Worker Task
__author__ = 'Sandesh'

from celery import Celery
from CustomClasses.ATree import *
from Bio import SeqIO, Seq
import os
from itertools import product


def break_sequence(sequence, depth):
	length = len(sequence)
	for i in range(length):
		if i + depth <= length:
			yield sequence[i:i + depth]
		else:
			yield sequence[i:]


app = Celery('tasks', broker='redis://192.168.6.4:6379/0', backend='redis://192.168.6.4:6379/0')


@app.task
def process(filename):
	print(filename)
	sequence_record_list = []

	# print(os.getcwd())
	for record in SeqIO.parse(filename, "fasta"):
		sequence_record_list.append(record.seq)

	sequence_record = ''.join(str(e) for e in sequence_record_list)
	atree = ATree()
	print(str(len(sequence_record)) + "-->" + str(atree))

	for subsequence_chunks in break_sequence(sequence_record, 4):
		atree.process_subsequence(subsequence_chunks)

	atree.dump_to_file(filename + "_TREE")
	atree.pickle_into_file(filename + "_pTREE")
	return len(sequence_record)


@app.task
def unique_pattern_generation(depth):
	print("I am doing - " + str(depth))
	temp_result = [''.join(x) for x in (product(*['ACGT'] * depth))]
	return temp_result
