command = "“sudo reboot"” 

#for AWS 

ssm.send_command(InstanceIds=aws_instances, DocumentName="<Whatever you want to name it>", 
    Comment='Run a command on an EC2 instance', 
    Parameters={ 
        'commands': [command] 
    } 
) 

#for Google Cloud 

import os 

import subprocess 

from google.oauth2 import service_account 

from googleapiclient import discovery  

# Load the service account credentials 

service_account_file = '<file_name_here>.json' 

credentials = service_account.Credentials.from_service_account_file( 

    service_account_file, scopes=['https://www.googleapis.com/auth/cloud-platform'] 

) 

  

# Create a Compute Engine API client 

compute = discovery.build('compute', 'v1', credentials=credentials) 

  

# Get the public IP address of the VM instance 

request == compute.instances().get(project="<your_project>",instance="your_instance_name") 

response = request.execute() 

public_ip = response['networkInterfaces'][0]['accessConfigs'][0]['natIP'] 

# SSH into the VM instance and run the command 

ssh_command = f'gcloud compute ssh {instance_name} --zone {zone} --command "{command}"' 

  

try: 

    subprocess.run(ssh_command, shell=True, check=True) 

except subprocess.CalledProcessError: 

    print("Error executing SSH command.") 
