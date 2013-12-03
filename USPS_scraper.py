import socks
s = socks.socksocket()
socks.set_default_proxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9150, True)
import socket
socket.socket = socks.socksocket

# import urllib.request
# print(urllib.request.urlopen("http://www.sourceforge.net/"))
# print(urllib.request.urlopen("https://www.sourceforge.net/"))
# quit()

import requests
import lxml.html
from lxml import etree
from itertools import chain

removeNonAscii = lambda s: "".join(i for i in s if ord(i)<128)

url = "https://tools.usps.com/go/TrackConfirmAction.action"
#url = "https://google.com"
_params = dict(tRef="fullpage", tLc="2")
_headers = {'User-Agent' : r"""Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36"""}

def track(numbers):
	params = dict(chain( _params.items(), {"tLabels" : ','.join(numbers)}.items() ))
	r = requests.get(url, params=params, headers=_headers)
	html_text = removeNonAscii(r.text)
	tree = lxml.html.fromstring(html_text)
	#print(tree)
	status_list = []
	i=1
	while True:
		try:
			status_list.append(tree.xpath(r"""//*[@id="results-multi"]/div[%d]/div/div[1]/div[2]/div[1]/h2/text()"""%i)[0])
		except IndexError:
			break
		i+=1
	#print(etree)
	#print(etree.tostring(tree, pretty_print=True).strip())
	return status_list