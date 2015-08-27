_author__ = 'Sandesh'

from celery import Celery
import glob
# import os

if __name__ == '__main__':
	app = Celery('d_process_task', broker='redis://192.168.6.4:6379/0', backend='redis://192.168.6.4:6379/0')

	async_result = []

	# print(glob.glob(str(os.getcwd() + '/GenomeDataset/Chromosomes/*.fa')))

	for name in glob.glob('GenomeDataset/Chromosomes/*.fa'):
		# print("DoingThis")
		async_result.append(app.send_task("d_process_task.process", args=(name,)))
