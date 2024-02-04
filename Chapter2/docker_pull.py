import docker

def pull_docker_images():
	client = docker.from_env()
	image_list = ["redis:latest", "nginx:latest"]
	for image in image_list:
		print("Pulling image {}".format(image))
		client.images.pull(image)

if __name__ == "__main__":
	pull_docker_images()
