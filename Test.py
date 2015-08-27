from Bio import SeqIO, Seq
sequence_record = ""

# print(os.getcwd())
for record in SeqIO.parse("form.fa", "fasta"):
	print(record.seq)
