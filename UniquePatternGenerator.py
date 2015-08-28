__author__ = 'cyberbeast'

from itertools import product, chain
from multiprocessing import Pool
from py2neo import neo4j, Node, Relationship, watch, authenticate, Graph


def logic_patterncounting(inp1):
    count = 0
    tx = graph.cypher.begin()
    statement = "MERGE (:Pattern {ID:{WORD}})"
    for word in product(*['ATCG'] * inp1):
        tx.append(statement, {"WORD": ''.join(word)})
        count += 1
    tx.commit()
    print(count)


if __name__ == '__main__':
    watch("httpstream")
    # watch("py2neo.cypher")
    authenticate("192.168.6.74:7474", "neo4j", "trvlr")
    graph = neo4j.Graph("http://192.168.6.64:7474/db/data/")

    for record in graph.cypher.execute("MATCH (n:Info) RETURN n.LastDepth as LastDepth"):
        depth = int(record.LastDepth)

    depth += 1
    print(depth)

    UniquePatterns = []
    GDS = {}
    pool = Pool()

    pool.map(logic_patterncounting, range(depth, depth + 2))

    pool.close()
    pool.join()

    statement_state = "MATCH (n:Info) SET n.LastDepth={d_val}"
    tx_new = graph.cypher.begin()
    tx_new.append(statement_state, {"d_val": int(depth + 2)})
    tx_new.commit()
