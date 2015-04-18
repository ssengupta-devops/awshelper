import boto.ec2
conn = boto.ec2.connect_to_region("us-west-2")
reservations = conn.get_all_reservations()
#print (reservations)
#i-28e50fdf
instances = reservations[0].instances
print(instances)
conn.terminate_instances(instance_ids='i-c8f71d3f')
