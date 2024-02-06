import docker 

 

#Step 1: Intialize and run a container  

client = docker.from_env() 

container = client.containers.run('ubuntu:latest', detach=True, command='/bin/bash') 

container_id = container.id 

print("Container ID:" + container_id) 

#Step 2: Add a layer 

#you can put in any command you want as long as it works 

new_command = "ls"

new_image = client.containers.get(container_id).commit() 

new_image_tag = "<whatever_you_want>:latest" 

new_container = client.containers.run(new_image_tag, detach=True, command=new_command) 

#Step 3: Export layered container as an image 

image = client.images.get("<whatever_you_want>:latest") 

image.save("<insert_file_path_here>") 
