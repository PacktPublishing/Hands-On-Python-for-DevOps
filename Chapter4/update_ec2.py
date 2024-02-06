import boto3

def update_ec2():
    ec2_client = boto3.client("ec2")
    print(ec2_client.modify_instance_attribute(
        InstanceId="i-02d42ec52027baa08",
        InstanceType={
            'Value': 't2.micro',
        }
    ))

if __name__ == "__main__":
    update_ec2()