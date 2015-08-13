__author__ = 'cyberbeast'

from itertools import product, chain
from multiprocessing import Pool
from py2neo import neo4j, Node, Relationship, watch, authenticate, Graph

if __name__ == '__main__':
    watch("httpstream")
    # watch("py2neo.cypher")
    authenticate("192.168.6.74:7474", "neo4j", "trvlr")
    graph = neo4j.Graph("http://192.168.6.64:7474/db/data/")

    record = graph.cypher.execute("MATCH (n:DataFile) WHERE n.ID = {name} RETURN n.SequenceCount")
    if record is None:
        print("None")
    else:
        print("Huh?")

    print(record.one)