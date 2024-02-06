import boto3

def stop_ec2():
    ec2_client = boto3.client("ec2")
    print(ec2_client.stop_instances(InstanceIds=["i-02d42ec52027baa08"]))

if __name__ == "__main__":
    stop_ec2()