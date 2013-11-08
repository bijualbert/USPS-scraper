import requests
from lxml import etree
url = "https://tools.usps.com/go/TrackConfirmAction.action?tRef=fullpage&tLc=2&tLabels="
def track(numbers):
	r = requests.get(url+numbers)
	r.encoding = "CP-1252"
	htmlparser = etree.HTMLParser()
	html_text = r.text
	print(html_text)	
	tree = etree.parse(html_text, htmlparser)
	tree.xpath(r"""//*[@id="results-multi"]/div[1]/div/div[1]/div[2]/div[1]/h2""")