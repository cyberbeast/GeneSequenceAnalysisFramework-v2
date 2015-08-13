__author__ = 'cyberbeast'
from itertools import product
from GeneralModules.GMCount import NumberOf
from Bio import SeqIO, Seq
from multiprocessing import Pool, Process, Manager
import ujson
import sys


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

    if single_char:
        GDS['UniqueCount'][in_pat] = in_val
    else:
        if double_char:
            GDS['UniqueCount'][in_pat] = in_val
            GDS_Links[in_pat[:int(len(in_pat)/2)]][in_pat[int(len(in_pat)/2):]] = in_val
        else:
            GDS['UniqueCount'][in_pat] = in_val
            GDS_Links[in_pat[:int(len(in_pat)/2)]][in_pat[int(len(in_pat)/2):]] = in_val
            GDS_Links[in_pat[:1+int(len(in_pat)/2)]][in_pat[1+int(len(in_pat)/2):]] = in_val


if __name__ == '__main__':

    depth = 2
    # depth = int(sys.argv[1])
    UniquePatterns = ["".join(x) for i in range(1, depth + 1) for x in product(*['ATCG'] * i)]
    print("Scanning dataset for counts of " + str(len(UniquePatterns)) + " unique patterns!")

    UniqueCountPatterns = UniquePatterns
    GDS = {}
    GDS_UniqueCount = dict(zip(UniqueCountPatterns, [0 for i in range(1, NumberOf(UniqueCountPatterns)+1)]))
    GDS['UniqueCount'] = GDS_UniqueCount

    mngr = Manager()
    GDS_Links = mngr.dict()
    GDS_Links = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)]))
    for l in dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)])):
        GDS_Links[l] = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)]))

    pool = Pool()
    for pat in GDS_UniqueCount:
        pool.apply_async(logic, (pat,), callback=callback)
    pool.close()
    pool.join()

    GDS['GDS_Links'] = GDS_Links.copy()
    with open('output1_p.json', 'w') as outfile:
        ujson.dump(GDS, outfile)



