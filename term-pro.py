import boto.ec2
conn = boto.ec2.connect_to_region("us-west-2")
reservations = conn.get_all_reservations()
#print (reservations)
#i-28e50fdf
instances = reservations[0].instances, reservations[1].instances
print(instances)
#inst = instances[0]
#print (inst)
conn.terminate_instances(instance_ids=reservations[0].instances)
#print "list1[0]: ", list1[0]









