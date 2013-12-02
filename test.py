from USPS_scraper import track

tracking_pattern = "LN147802%03dCN"
if __name__ == '__main__':
	#real tracking number: LN147802515CN
	#stride 10
	#
	for i in range(0,1000,10):
		numbers = [tracking_pattern%j for j in range(i,i+10)]
		tracking_info = track(numbers)
		for j in range(i,i+10):
			info = tracking_info[j%10]
			if info!="error":
				print(tracking_pattern%j, info)