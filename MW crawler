import urllib2
import urllib
import os

with open('MWwords.txt', 'r') as ls:
	content = ls.read().lower().splitlines()

f = open('MWoutput.txt', 'w') 
f.write('URL 				Result\n')
for i in content :
	BasicURL='http://www.merriam-webster.com/dictionary/%s'%i
	print BasicURL
	f.write(i)
	try:
		response = urllib2.urlopen(BasicURL)
		html = response.read().decode("utf-8")
		if 'class="au"' in html:
				f.write('			Sound\n')
		else: 
				f.write('			No sound\n')
	except urllib2.URLError as e:
		f.write('			%s\n'%e.reason) 
		
f.close()
