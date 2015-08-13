# __author__ = 'cyberbeast'
# import os as os
# from Bio import SeqIO, Seq
# from multiprocessing import Pool, Process, Manager
# from py2neo import neo4j, Node, Relationship, watch, authenticate, Graph
# import glob
# import subprocess
#
#
# def clean(file_name):
#     # print(str(os.getcwd()) + '/GenomeDataset/Chromosomes/' + file_name)
#     # print(os.path.basename(file_name))
#     # p = subprocess.Popen(["echo", str(os.getcwd())])
#     p = subprocess.Popen(["fasta_formatter", "-i", file_name, "-o", os.path.basename(file_name) + str("_TEST")], stdout=subprocess.PIPE)
#     (output, err) = p.communicate()
#     print(output)
#
# if __name__ == "__main__":
#
#     filelist = []
#     # use glob module
#     for name in glob.glob(str(os.getcwd()) + '/GenomeDataset/Chromosomes/*.fa'):
#         filelist.append(name)
#
#     clean(filelist[0])

import sys
from Bio import SeqIO

def sequence_cleaner(fasta_file,min_length=0,por_n=100):
    #create our hash table to add the sequences
    sequences={}

    #Using the biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        #Take the current sequence
        sequence=str(seq_record.seq).upper()
        #Check if the current sequence is according to the user parameters
        if (len(sequence)>=min_length and (float(sequence.count("N"))/float(len(sequence)))*100<=por_n):
       # If the sequence passed in the test "is It clean?" and It isnt in the hash table , the sequence and Its id are going to be in the hash
            if sequence not in sequences:
                sequences[sequence]=seq_record.id
       #If It is already in the hash table, We're just gonna concatenate the ID of the current sequence to another one that is already in the hash table
            else:
                sequences[sequence]+="_"+seq_record.id


    #Write the clean sequences

    #Create a file in the same directory where you ran this script
    output_file=open("clear_"+fasta_file,"w+")
    #Just Read the Hash Table and write on the file as a fasta format
    for sequence in sequences:
            output_file.write(">"+sequences[sequence]+"\n"+sequence+"\n")
    output_file.close()

    print("CLEAN!!!\nPlease check clear_"+fasta_file)


sequence_cleaner("hs_ref_GRCh38_chr1.fa")
 
