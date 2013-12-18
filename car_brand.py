import urllib2
import json

url_base = 'http://app.api.autohome.com.cn/autov3.1/cars/'
car_array = {}

for i in range(0, 10000):
	url_tail = 'seriesprice-a2-pm1-v3.1.1-b%d-t1.html' % i
	url = url_base + url_tail
	try:
		print i
		response = urllib2.urlopen(url)
		html = response.read()
		dict = json.loads(html)
		fctlist = dict['result']
		print '%s - %s' % (fctlist['fctlist'][0]['name'], url_tail)
		car_array[fctlist['fctlist'][0]['name']] = url_tail
	except:
		continue


print len(car_array), 'cars'
