__author__ = 'Sandesh'

from celery import Celery
from CustomClasses import ATree
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
	for record in SeqIO.parse(filename, "fasta"):
		sequence_record.join(record)

	atree = ATree.ATree()

	for subsequence_chunks in break_sequence(sequence_record, 4):
		atree.process_subsequence(subsequence_chunks)

	atree.dump_to_file(str(os.getcwd()) + '/' + filename + "_TREE")
	# atree.pickle_into_file(str(os.getcwd()) + 'GenomeDataset/Processing/' + filename + "_PICKLE")
