_author__ = 'Sandesh'

from celery import Celery
import glob
import logging
# import os


def manage_process_task():
	async_result = []
	for name in glob.glob('GenomeDataset/Chromosomes/*.fa'):
		async_result.append(app.send_task("d_process_task.process", args=(name,)))

	total = 0

	for key in async_result:
		if key.ready():
			total += key.get()

	print(total)

if __name__ == '__main__':
	app = Celery('d_process_task', broker='redis://192.168.6.4:6379/0', backend='redis://192.168.6.4:6379/0')

	manage_process_task()

# Thats it