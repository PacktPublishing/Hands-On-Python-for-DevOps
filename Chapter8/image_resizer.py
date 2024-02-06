import os 

import tempfile 

import boto3 

from PIL import Image 

  

s3 = boto3.client('s3') 

  

def lambda_handler(event, context): 

    # Get the name of the bucket and the image name when upload is triggered. 

    bucket = event['Records'][0]['s3']['bucket']['name'] 

    key = event['Records'][0]['s3']['object']['key'] 

     

    new_width = 300 #width of image 

    new_height = 200 #height of image 

     

    with tempfile.TemporaryDirectory() as tmpdir: 

        # Download the original image from S3 into a pre-defined temporary directory 

        download_path = os.path.join(tmpdir, 'original.jpg') 

 

       #download the S3 file into the temporay path 

        s3.download_file(bucket, key, download_path) 

         

        with Image.open(download_path) as image: 

            image = image.resize((new_width, new_height)) 

             

            # Save the resized image in its own path 

            resized_path = os.path.join(tmpdir, 'resized.jpg') 

            image.save(resized_path) 

         

        # Upload the resized image back to the S3 bucket and delete the original 

       s3.delete_object(Bucket=bucket, Key=key) 

       s3.upload_file(resized_path, bucket, key) 

         

  

    return { 

        'statusCode': 200, 

        'body': 'You don’t really need this because its not for people!' 

    } 
