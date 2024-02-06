import docker

def docker_sample():
    client = docker.from_env()

    # Define the image name and tag
    image_name = 'python:latest'

    # Pull the image
    client.images.pull(image_name)

    # Create and run a container based on the pulled image
    container = client.containers.create(image_name)
    container.start()
    print(client.containers.list())

if __name__ == "__main__":
    docker_sample()