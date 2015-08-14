_author__ = 'cyberbeast'

from celery import Celery
import glob
import os

if __name__ == '__main__':
    app = Celery('tasks', broker='redis://192.168.6.64:6379/0', backend='redis://192.168.6.64:6379/0')

    async_result = []
    # use glob module
    for name in glob.glob(str(os.getcwd()) + '/GenomeDataset/Chromosomes/clear_?.fa'):
        async_result.append(app.send_task("tasks.analysis", args=name))
