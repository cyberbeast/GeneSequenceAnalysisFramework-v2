__author__ = 'Sandesh'

from celery import Celery
from CustomClasses.ATree import *
from Bio import SeqIO
import os


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
	sequence_record = ""

	# print(os.getcwd())
	for record in SeqIO.parse(filename, "fasta"):
		sequence_record.join(record.seq)

	atree = ATree()
	print(str(len(sequence_record)) + "-->" + str(atree))

	for subsequence_chunks in break_sequence(sequence_record, 4):
		atree.process_subsequence(subsequence_chunks)

	# atree.dump_to_file(filename + "_TREE")
	# print("done")
	# atree.pickle_into_file(str(os.getcwd()) + 'GenomeDataset/Processing/' + filename + "_PICKLE")
