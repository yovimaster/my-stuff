import urllib2
import urllib
import os

f = open('url.txt', 'w')

BasicURL='http://qriv1.ucoz.com/2v.html'
print BasicURL
response = urllib2.urlopen(BasicURL)
html = response.read()
f.write(html)		
f.close()


