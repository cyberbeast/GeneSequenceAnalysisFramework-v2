# Distributed Processing Module
__author__ = 'Sandesh'

from CustomClasses.ATree import *
from celery import Celery
import glob
from itertools import product
import subprocess


def manage_process_task():
    async_result = []
    for name in glob.glob('GenomeDataset/Chromosomes/*.fa'):
        async_result.append(app.send_task("d_process_task.process", args=(name,)))
    # async_result.append(app.send_task("d_process_task.process", args=(name,)))

    total = 0

    for key in async_result:
        if key.ready:
            total += key.get()

    print(total)

    subprocess.call(["ssh", "server_master@192.168.6.4", "./d_sync.sh"])


def manage_unique_pattern_generation_task(depth):
    unique_patterns = []

    range_val = 2 * depth

    for length in range(1, range_val):
        upg_async_result = [app.send_task("d_process_task.unique_pattern_generation", args=(length,))]

    for key in upg_async_result:
        if key.ready:
            unique_patterns.append(key.get())

    print(unique_patterns)


def analysis():
    filelist = []
    for name in glob.glob('GenomeDataset/Processing/*pTree'):
        filelist.append(name)

    pattern_list = ["".join(x) for i in range(1, 9) for x in product(*['ATGC'] * i)]
    pattern_list.sort()
    count_matrix = {}
    result = {pattern: [] for pattern in pattern_list}

    for infile in filelist:
        with open(infile, 'rb') as in_fh:
            new_tree = pickle.load(in_fh)

        for pattern in pattern_list:
            result[pattern].append(new_tree.count(pattern))
            print("-->" + pattern + ": " + new_tree.count(pattern))


if __name__ == '__main__':
    app = Celery('d_process_task', broker='redis://192.168.6.4:6379/0', backend='redis://192.168.6.4:6379/0')

    # manage_unique_pattern_generation_task(4)
    manage_process_task()
