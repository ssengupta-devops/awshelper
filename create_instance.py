import boto.ec2
conn = boto.ec2.connect_to_region("us-west-2")
#conn.run_instances('ami-5189a661')
conn.run_instances(
       'ami-5189a661',
        key_name='key-pair-us-west-2',
        instance_type='t2.micro',
        security_groups=['default'])

