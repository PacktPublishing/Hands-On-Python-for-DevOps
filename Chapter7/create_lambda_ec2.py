import boto3 

  

ec2 = boto3.client('ec2') 

  

def lambda_handler(event, context): 

    instance_size = event['instance_size'] 

  

    response = ec2.run_instances( 

        ImageId='<INSERT_AMI_HERE>', 

        InstanceType=instance_size, 

        MinCount=1, 

        MaxCount=1, 

        SecurityGroupIds=['<INSERT_SECURITY_GROUP_HERE'], 

        SubnetId='<INSERT_SUBNET_HERE>' 

    ) 

  

    return response 
