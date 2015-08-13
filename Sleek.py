__author__ = 'cyberbeast'
from itertools import product
from GeneralModules.GMCount import NumberOf
from Bio import SeqIO, Seq

UniquePatterns = ["".join(x) for i in range(1, 5) for x in product(*['ATCG'] * i)]

print(len(UniquePatterns))
single_char = False
double_char = False
counter = 0
GDS = {}
GDS_UniqueCount = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)]))
GDS['UniqueCount'] = GDS_UniqueCount
GDS['GDS_Links'] = {}
GDS_links = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)]))

for l in dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)])):
    GDS['GDS_Links'][l] = dict(zip(UniquePatterns, [0 for i in range(1, NumberOf(UniquePatterns)+1)]))

for pat in GDS_UniqueCount:
    counter = 0
    for seq_record in SeqIO.parse("formatter-o.fa", "fasta"):
        counter += int(seq_record.seq.count(pat))

    if len(pat) == 1:
        single_char = True
    else:
        if len(pat) % 2 == 0:
            double_char = True

    if single_char:
        GDS['UniqueCount'][pat] = counter
        # print("single-->" + str(counter))
    else:
        if double_char:
            GDS['UniqueCount'][pat] = counter
            GDS['GDS_Links'][pat[:int(len(pat)/2)]][pat[int(len(pat)/2):]] = counter
            # print("double-->" + str(GDS['GDS_Links'][str(pat[:int(len(pat)/2)])][str(pat[int(len(pat)/2):])]))
        else:
            GDS['UniqueCount'][pat] = counter
            GDS['GDS_Links'][pat[:int(len(pat)/2)]][pat[int(len(pat)/2):]] = counter
            GDS['GDS_Links'][pat[:1+int(len(pat)/2)]][pat[1+int(len(pat)/2):]] = counter
            # print("multi->" + str(GDS['GDS_Links'][pat[:1+int(len(pat)/2)]][pat[1+int(len(pat)/2):]]))
print(GDS)
