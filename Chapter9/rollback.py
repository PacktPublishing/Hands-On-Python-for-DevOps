mport boto3 

  

def  lambda_handler(event, context): 

     domain_name = '<your_domain_name_here>' 

    default_endpoint = '<your_endpoint_here>' 

  

    # Initialize the Route 53 client 

    client = boto3.client('route53') 

  

    # Get the hosted zone ID for the domain 

    response = client.list_hosted_zones_by_name(DNSName=domain_name) 

    hosted_zone_id = response['HostedZoneId'] 

  

    # Update the Route 53 record set to point to the default endpoint 

    changes= { 

        'Changes': [ 

            { 

                'Action': 'UPSERT', 

                'ResourceRecordSet': { 

                    'Name': domain_name, 

                    'Type': 'A', 

                    'TTL': 300, 

                    'ResourceRecords': [{'Value': default_endpoint}] 

                } 

            } 

        ] 

    } 

  

       client.change_resource_record_sets( 

        HostedZoneId=hosted_zone_id, 

        ChangeBatch=changes 

    ) 

  

        return { 

        'statusCode': 200, 

        'body': "Nothing, really, no one’s gonna see this}" 

    } 
