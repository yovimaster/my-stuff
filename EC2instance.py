import boto.ec2

access_key = 'AKIAJB46524P5FUPJ3JQ'
secret_key = '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'

def get_ec2_instances(region):
    ec2_conn = boto.ec2.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
    reservations = ec2_conn.get_all_reservations()
    for reservation in reservations:    
        print region+':',reservation.instances

    for vol in ec2_conn.get_all_volumes():
        print region+':',vol.id

def ec2_treminate(instance_id):
    ec2_conn = boto.ec2.connect_to_region('eu-west-1',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
    
    print "terminating instance..."
    ec2_conn.terminate_instances(instance_ids=[instance_id])


def main():
    ec2_treminate('i-8cce2706')


if  __name__ =='__main__':main()