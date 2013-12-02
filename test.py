from USPS_scraper import track

tracking_pattern = "LN1478025%02dCN"
if __name__ == '__main__':
	#numbers = ["9400110200882950235373", "LN147802515CN"]
	for i in range(0,100,10):
		numbers = [tracking_pattern%i for i in range(15+i,25+i)]
		tracking_info = track(numbers)
		for i in range(15+i,25+i):
			info = tracking_info[i%10]
			if info!="error":
				print(tracking_pattern%i, info)