from USPS_scraper import track

if __name__ == '__main__':
	numbers = ["9400110200882950235373", "LN147802515CN"]
	tracking_info = track(numbers)
	print(tracking_info)