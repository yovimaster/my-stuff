# __author__ == 'Yoav T. L'

import boto
import time
import logging
import sys


logging.basicConfig(stream=sys.stdout,level=logging.INFO)

# AWS info
access_key = '???????'
secret_key = '??????????????'
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
staging_ip = '?????????/'
staging_alloc = '?????/'

cron_ip = '????????/'
cron_alloc = '??????//'

production_elb_name = '????????'

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
	# =========== Deploy new version ==========
	logging.info("Deploying new version on production servers")
	
	# Stage 1 - Production servers increase size of desired servers under elb
	instance_to_terminate = get_instances('Ctconnect Nginx servers')
	
	logging.info("Up Scaling the number of instances")
	change_capacity('Ctconnect Nginx servers',4)
	logging.info(len(elb_status(production_elb_name).instances))
	while len(elb_status(production_elb_name).instances) < 4:
		looging.info("The new instance is not up yet")
		time.sleep(10)

	# stage 2 - Terminate the old instances
	logging.info("Terminating the instances with the old version")
	for server in instance_to_terminate:
		ec2_treminate(server)
		time.sleep(10)
		while len(elb_status(production_elb_name).instances) != 4:
			looging.info("The new instance is not up yet")
			time.sleep(10)

	# stage 3 - change the desired number back again to 3
	logging.info("Now decreasing the instances back again")
	change_capacity('Ctconnect Nginx servers',3)
	while len(elb_status(production_elb_name).instances) != 3:
		print "waiting for it to teminate instance"
		logging.info(len(elb_status(production_elb_name).instances))
		time.sleep(10)

	# Stage 4 - Cron server
	logging.info("Deploying Cron server")
	Cron_server = get_instances('Cron server')[0]

	# Stage 5 - Production servers increase size of desired servers under elb
	logging.info("Uploading to 2 instance")
	change_capacity('Cron server',2)
	time.sleep(420)

	# Stage 6- Dissasociate the elastic ip
	associate_ip(Cron_server, cron_ip, cron_alloc)
	disassociate_ip(cron_ip, dissassoction_id)

	# stage 7 - change the desired number back again to 1
	logging.info("now decreasing")
	ec2_treminate(Cron_server)
	change_capacity('Cron server',1)
	time.sleep(180)

	# Stage 8 - assign the staging server elastic ip
	logging.info("Assisgning the ellastic ip")
	Cron_server = get_instances('Cron server')[0]
	associate_ip(Cron_server,cron_ip,cron_alloc)

	logging.info("Deployed successfully")


if __name__ == "__main__":
	main()