# __author__ == 'Yoav T. L'

import boto
import time
import logging
import sys

logging.basicConfig(stream=sys.stdout,level=logging.INFO)


# AWS info
access_key = 'AKIAJB46524P5FUPJ3JQ'
secret_key = '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'
region = 'eu-west-1'

# Connections
autoscale = boto.connect_autoscale(access_key, secret_key)
asg_conn = boto.ec2.autoscale.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
ec2_conn = boto.ec2.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
elb_conn = boto.ec2.elb.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
# IP and info 
staging_ip = '54.229.79.209'
staging_alloc = 'eipalloc-092ae062'

staging_elb_name = 'ct-connect-stage'

dissassoction_id = ''

def get_groups():
	group = asg_conn.get_all_groups()
	return group

def get_instances(group_name):
	group = asg_conn.get_all_groups([group_name])[0]
	instance_ids = [i.instance_id for i in group.instances]
	return instance_ids


def ec2_treminate(instance):
    logging.info("terminating instance...")
    ec2_conn.terminate_instances(instance_ids=[instance])


def associate_ip(instance,ip,allocation):
    addrs = ec2_conn.associate_address_object(instance,ip,allocation)
    global dissassoction_id
    dissassoction_id = addrs.association_id
    logging.info("association done")

def disassociate_ip(ip,assocation):
    addrs = ec2_conn.disassociate_address(ip,assocation)
    logging.info("Dislocated th IP")

def change_capacity(group_name,size):
	asg_conn.set_desired_capacity(group_name,size)

def elb_status(elb_name):
	return elb_conn.get_all_load_balancers([elb_name])[0]

def main():
	# =========== Deploy New Staging version ==========
	logging.info("Deploying new version on Staing servers")

	# Stage 1- Dissasociate the elastic ip
	logging.info("Assisgning the ellastic ip")
	Staging_server= get_instances('Staging server')[0]
	associate_ip(Staging_server,staging_ip,staging_alloc)
	disassociate_ip(staging_ip, dissassoction_id)

	
	# Stage 2 - Production servers increase size of desired servers under elb
	logging.info("Uploading to 2 instance")
	change_capacity('Staging server',2)
	logging.info("the size of instances under ELB")
	logging.info(len(elb_status(staging_elb_name).instances))
	while len(elb_status(staging_elb_name).instances) < 2:
		logging.info("the instance is not up yet...")
		print(len(elb_status(staging_elb_name).instances))
		time.sleep(10)

	# stage 3 - change the desired number back again to 1
	logging.info("now decreasing")
	change_capacity('Staging server',1)
	logging.info((elb_status(staging_elb_name).instances))
	while len(elb_status(staging_elb_name).instances) != 1:
		print "waiting for it to teminate instance"
		logging.info(len(elb_status(staging_elb_name).instances))
		time.sleep(10)


	#wait 3 minute for the changes to take place 
	time.sleep(180)

	# Stage 4 - assign the staging server elastic ip
	logging.info("Assisgning the ellastic ip")
	Staging_server= get_instances('Staging server')[0]
	associate_ip(Staging_server,staging_ip,staging_alloc)

	logging.info("Deployed successfully")


if __name__ == "__main__":
	main()




