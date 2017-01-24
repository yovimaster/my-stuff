# __author__ == 'Yoav T. L'

import time
import logging
import sys
import urllib2

logging.basicConfig(stream=sys.stdout,level=logging.INFO)


def main():
	logging.info("Starting script")
	try: 
		urllib2.urlopen('http://api.sizewhiz.com/health-check')
		logging.info("all a-ok")
		return sys.exit(1)
	except urllib2.HTTPError as err:
		if err.code == 401:
 			logging.info("there seem to be a normal response. dont worry")
 			return sys.exit(1)
		else:
			logging.info("there is an error with the site, please check")
			return sys.exit(2)

if __name__ == "__main__":

	main()