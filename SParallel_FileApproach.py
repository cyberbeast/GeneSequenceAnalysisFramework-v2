__author__ = 'cyberbeast'
from Bio import SeqIO, Seq
from multiprocessing import Pool, Process, Manager
from py2neo import neo4j, Node, Relationship, watch, authenticate, Graph


def logic(input_f):
    temp = 0
    for seq_records in SeqIO.parse("formatter-o.fa", "fasta"):
        temp += seq_records.seq.count(input_f)
    return [temp, input_f]


def callback(input_c):
    single_char = False
    double_char = False

    in_val, in_pat = input_c
    # print("in callback for " + in_pat + " with count " + str(in_val))

    if len(in_pat) == 1:
        single_char = True
    else:
        if len(in_pat) % 2 == 0:
            double_char = True

    tx = graph.cypher.begin()
    statement_count = "MATCH (n {ID:{id}}) SET n.Count = {VALUE}"
    statement_map = "MATCH (a:Pattern),(b:Pattern) WHERE a.ID = {id1} AND b.ID = {id2} MERGE (a)<-[r:FOLLOWS {follow_count : {VALUE}, chromosome : {CHROMOSOME}}]-(b)"

    tx.append(statement_count, {"id": in_pat, "VALUE": in_val})

    if double_char:
        tx.append(statement_map, {"id1": in_pat[:int(len(in_pat)/2)], "id2": in_pat[int(len(in_pat)/2):], "VALUE": in_val, "CHROMOSOME": 1})
    else:
        tx.append(statement_map, {"id1": in_pat[:int(len(in_pat)/2)], "id2": in_pat[int(len(in_pat)/2):], "VALUE": in_val, "CHROMOSOME": 1})
        tx.append(statement_map, {"id1": in_pat[:1+int(len(in_pat)/2)], "id2": in_pat[1+int(len(in_pat)/2):], "VALUE": in_val, "CHROMOSOME": 1})
    tx.commit()

if __name__ == '__main__':

    watch("httpstream")
    authenticate("192.168.6.74:7474", "neo4j", "trvlr")
    graph = neo4j.Graph("http://192.168.6.64:7474/db/data/")

    print("Scanning Dataset for patterns from Graph database")

    pool = Pool()

    for record in graph.cypher.execute("MATCH (n:Pattern) RETURN n.ID as ID"):
        pool.apply_async(logic, (record.ID,), callback=callback)
    pool.close()
    pool.join()



