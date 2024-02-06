import boto3

def create_ec2():
    ec2_client = boto3.resource("ec2")
    print(ec2_client.create_instances(ImageId="ami-051f7e7f6c2f40dc1", 
                                      InstanceType="t2.nano", MaxCount=1, MinCount=1))

if __name__ == "__main__":
    create_ec2()