from USPS_scraper import track

import sqlite3
db = sqlite3.connect('db', isolation_level=None)

tracking_pattern = "LN147802%03dCN"
#real tracking number: LN147802515CN
stride=10

def record_info(numbers):
	tracking_infos = track(numbers)
	if len(tracking_infos)!=stride:
		print("got %d tracking infos, expected %d"%(len(tracking_infos), stride))
		return
	for j in range(i,i+stride):
		info = tracking_infos[j%stride]
		tracking_info = (tracking_pattern%j, info)
		print(tracking_info)
		db.execute("insert into tracking_infos values (?, ?)", tracking_info)

if __name__ == '__main__':
	for i in range(0,1000,stride):
		numbers = [tracking_pattern%j for j in range(i,i+stride)]
		record_info(numbers)