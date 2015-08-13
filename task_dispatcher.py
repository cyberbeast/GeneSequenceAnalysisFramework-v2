l__author__ = 'Sandesh'
from celery import Celery
import logging as logger
from GeneralModules.file_open import *
from GeneralModules.Breaker8 import *
from GeneralModules.GeneDataStructure import *
import ujson


app = Celery('tasks', broker='redis://192.168.6.78:6379/0', backend='redis://192.168.6.78:6379/0')

# Set Depth
depth = 4

ret=[]   

# open the file
file = file_open("input_smallest.txt")

# reading from the opened file
str_ = file.read().replace('\n', '')
input_list = breaker8(str_, 70)
break_length = len(input_list)
print(break_length)
# set up the dictionary
graph1 = {"nodes": [], "links": []}
CreateGeneDataStructure(graph1, depth)


def manage_analysis_task(in_list):
    # for idx, word in enumerate(in_list):
        # app.send_task('tasks.analysis', args=(word, graph1, 4, idx))
        # analysis.delay(word, graph1, 4, idx)
        # analysis(word, graph1, 4, idx)
    async_result = []
    for word in in_list:
        async_result.append(app.send_task('tasks.analysis', args=(word, graph1, depth)))

    for value in async_result:
        ret.append(value.get())
    print("DONE")

if __name__ == '__main__':
    manage_analysis_task(input_list)
    # Throw the graph at a JSON file

    with open('output1-b.json', 'w') as outfile:
        ujson.dump({"links": ret[len(ret)]['links'], "nodes": ret[len(ret)]['nodes']}, outfile)

    #print(ret[0]['links'][5]['AC']['A'])
    print(ret[12]['links'])

    print("OVER")
