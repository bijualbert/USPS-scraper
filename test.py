from USPS_scraper import track
from concurrent.futures import ProcessPoolExecutor, as_completed
import sys
import traceback

import sqlite3
db = sqlite3.connect('db', isolation_level=None)
db.execute("DROP TABLE IF EXISTS tracking_infos")
db.execute("CREATE TABLE IF NOT EXISTS tracking_infos(number text, status text)")


tracking_pattern = "LN1478%05dCN"
#real tracking number: LN147802515CN
stride=10

def record_info(numbers, i):
	try:
		tracking_infos = track(numbers, stride)
		if len(tracking_infos)!=stride:
			print("got %d tracking infos, expected %d"%(len(tracking_infos), stride))
		else:
			for j in range(i,i+stride):
				info = tracking_infos[j%stride]
				info["number"] = tracking_pattern%j
				print(info)
				db.execute("insert into tracking_infos values (?, ?)", (info["number"], info["current_status"]))
	except Exception as e:
		print(e)
		#traceback.print_exc()
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