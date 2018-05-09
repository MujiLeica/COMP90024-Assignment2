import boto
import time
import os

from boto.ec2.regioninfo import RegionInfo

ACCESS_KEY = '96a0a56c6d15488bbe702b86867adce4'
SECRET_KEY = 'b990527477ba49fbb102a887b80ea886'
IMAGE_ID = 'ami-da0a99ba' #NeCTAR Ubuntu 16.04 LTS (Xenial) amd64

region = RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
ec2_conn = boto.connect_ec2(aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY,
                            is_secure=True,
                            region=region,
                            port=8773,
                            path='/services/Cloud',
                            validate_certs=False)

reservation = ec2_conn.run_instances(IMAGE_ID,
                       key_name='nectarkey',
                       instance_type='m2.medium',
                       security_groups=['default', 'login'],
                       placement='melbourne-np')

instance = reservation.instances[0]

vol_req = ec2_conn.create_volume(30, 'melbourne-np')


def wait(instance_id, count=20):
    loop = 0

    while loop < count:
        time.sleep(15)
        if ec2_conn.get_all_instances(instance_id)[0].instances[0].state == "running":
            return True
        loop += 1

    return False


if wait(instance.id):
    ec2_conn.attach_volume(vol_req.id, instance.id, '/dev/vdc')


direc = os.path.dirname(__file__)
filename = os.path.join(direc, 'inventory', 'newhosts.ini')

f = open(filename, "w+")
f.write("[harvesterserver]\n")
f.write(ec2_conn.get_all_instances(instance.id)[0].instances[0].private_ip_address)

f.close()