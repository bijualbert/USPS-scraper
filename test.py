from USPS_scraper import track
from concurrent.futures import ProcessPoolExecutor, as_completed
import sys

import sqlite3
db = sqlite3.connect('db', isolation_level=None)
tracking_pattern = "LN1478%05dCN"
#real tracking number: LN147802515CN
stride=10

def record_info(numbers, i):
	try:
		tracking_infos = track(numbers)
		if len(tracking_infos)!=stride:
			print("got %d tracking infos, expected %d"%(len(tracking_infos), stride))
		else:
			for j in range(i,i+stride):
				info = tracking_infos[j%stride]
				tracking_info = (tracking_pattern%j, info)
				print(tracking_info)
				db.execute("insert into tracking_infos values (?, ?)", tracking_info)
	except Exception as e:
		print(e)
	sys.stdout.flush()
if __name__ == '__main__':
	executor = ProcessPoolExecutor(max_workers=20)
	futures = []
	tasks = 0
	for i in range(0,100000,stride):
		numbers = [tracking_pattern%j for j in range(i,i+stride)]
		futures.append(executor.submit(record_info, numbers, i))
		tasks+=1
	print("submitted tasks")
	for i, future in enumerate(as_completed(futures)):
		print(r"%d/%d"%(i+1,tasks), future)