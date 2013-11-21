import requests
import lxml.html
from lxml import etree
from itertools import chain

removeNonAscii = lambda s: "".join(i for i in s if ord(i)<128)

url = "https://tools.usps.com/go/TrackConfirmAction.action"
_params = dict(tRef="fullpage", tLc="2")

def track(numbers):
	params = dict(chain( _params.items(), {"tLabels" : ','.join(numbers)}.items() ))
	r = requests.get(url, params=params)
	html_text = removeNonAscii(r.text)
	print(r.url)
	tree = lxml.html.fromstring(html_text)
	#print(tree)
	status = tree.xpath(r"""/html/body""")
	#print(etree)
	#print(etree.tostring(tree, pretty_print=True).strip())
	return status