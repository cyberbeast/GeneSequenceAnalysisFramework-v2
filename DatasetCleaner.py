__author__ = 'cyberbeast'
import os
from Bio import SeqIO, Seq
from multiprocessing import Pool, Process, Manager
from py2neo import neo4j, Node, Relationship, watch, authenticate, Graph
import glob


def clean(file_name):
    seqcount = SeqIO.convert(file_name, "fasta", file_name + str("_FORMATTED"), "fasta")
    return [file_name, seqcount]


def CreateDataFileNode_callback(files):
    file_name, file_sequence_count = files
    tx = graph.cypher.begin()
    c_pre = 'MATCH (n:DataFile) WHERE n.ID = {name} RETURN n.SequenceCount'
    tx.append(c_pre, {'name':file_name})
    results = tx.commit()

    if results == file_sequence_count:
        print("Sequence Counts are the same. No changes made in the database for: " + str(file_name))
    else:
        if results[0] is None:
            ty = graph.cypher.begin()
            statement = "MERGE (:DataFile {ID:{NAME}, SequenceCount: {SEQCOUNT}})"
            ty.append(statement, {"NAME": file_name, "SEQCOUNT": file_sequence_count})
            ty.commit()
        else:
            tz = graph.cypher.begin()
            statement = "MATCH (a:DataFile) WHERE a.ID = {name} SET a.SequenceCount: {SEQCOUNT}"
            tz.append(statement, {"name": file_name, "SEQCOUNT": file_sequence_count})
            tz.commit()


if __name__ == "__main__":
    watch("httpstream")
    SEQCOUNT = 0

    authenticate("192.168.6.74:7474", "neo4j", "trvlr")
    graph = neo4j.Graph("http://192.168.6.74:7474/db/data/")

    filelist = []
    # use glob module
    for name in glob.glob('Genome Dataset/Chromosomes/hs_ref_GRCh38?.fa'):
        filelist.append(name)

    pool = Pool()
    pool.apply_async(clean, (filelist,), CreateDataFileNode_callback)
    pool.close()
    pool.join()



