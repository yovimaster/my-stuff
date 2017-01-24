# __author__ == 'Yoav T. L'

import boto3
import logging
import sys


logging.basicConfig(stream=sys.stdout,level=logging.INFO)


# AWS info
session = boto3.Session(profile_name='sizewhiz', region_name='eu-west-1')
client = session.client('ecs')

def main():
	logging.info("Starting script")
	cluster = client.describe_clusters(clusters=['prod'])
	if cluster['clusters'][0]['runningTasksCount'] == 1: 
		logging.info("There is one Task running under the service. All good")
		return sys.exit(0)
	elif cluster['clusters'][0]['runningTasksCount'] == 0:
		logging.info("no service is running")
		return sys.exit(2)
	else:
		logging.info("there are more then one service running. please check")
		return sys.exit(2)

if __name__ == "__main__":

	main()