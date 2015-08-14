__author__ = 'cyberbeast'
import os as os
from Bio import SeqIO
from multiprocessing import Pool
import glob


def clean(fasta_file, min_length=0, rec_n=100):
    # TODO Code to check if file is already clean or not!
    # ---------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------------

    # create our hash table to add the sequences
    sequences = {}

    # Using the biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # Take the current sequence
        sequence = str(seq_record.seq).upper()
        # Check if the current sequence is according to the user parameters
        if len(sequence) >= min_length and (float(sequence.count("N")) / float(len(sequence))) * 100 <= rec_n:
            # If the sequence passed in the test "is It clean?" and It isnt in the hash table , the sequence and Its id are going to be in the hash
            if sequence not in sequences:
                sequences[sequence] = seq_record.id
                # If It is already in the hash table, We're just gonna concatenate the ID of the current sequence to another one that is already in the hash table
            else:
                sequences[sequence] += "_" + seq_record.id

    # Write the clean sequences

    # Create a file in the same directory where you ran this script
    output_file = open("clear_" + fasta_file, "w+")
    # Just Read the Hash Table and write on the file as a fasta format
    for sequence in sequences:
        output_file.write(">" + sequences[sequence] + "\n" + sequence + "\n")
    output_file.close()

    print("CLEAN!!!\nPlease check clear_" + fasta_file)


if __name__ == "__main__":
    filelist = []
    # use glob module
    for name in glob.glob(str(os.getcwd()) + '/GenomeDataset/Chromosomes/*.fa'):
        filelist.append(name)

    # print(filelist)
    pool = Pool()
    for file_l in filelist:
        print(file_l)
        pool.apply_async(clean, (file_l,))

    pool.close()
    pool.join()
