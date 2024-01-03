Infrastructure for the application

Here I used aws instance for the implementation of the application. I have selected basic general purpose instance T2micro.and the linux 64bit ami . configured 3 instances one for master and other two for worker node. 

Installation of Docker and creation swarm

I logged in to the master through the mobaxtream
Then i updated the os 
#Sudo Yum update

Then i install the docker 
	# Sudo yum install -y docker

Started the docker
	# sudo systemctl start docker

I got an error of permission denied in this step
#Sudo user -aG docker ec2-user

This grant permission to linux to interact with the docker deamon

Then i changed the name of the server host names as master and node 1 ,2
#sudo -i hostnamectl set -hostname master

To create cluster

#docker swarm init

Then i got a link with token  
	# docker swarm join token manager ip : 2377
I copied the link to the two nodes


Docker image

I have a basic python flask which is integrated with the db

Created the docker image 

#docker build -t project-ps

Deployment

Then mention the project-ps image and the official latest image of db service in the compose file

Deployed the stack to the docker swarm

#docker stack deploy -c docker-compose.yml  pythnprjct

Then the app will be available in the port   #node ip:5000


Installation of Traefik

I have to install the traefik service in the cluster and then specify the port used for communication by using the  label

#traefik.http.services.project-ps.loadbalancer.port=5000

 So  to add the label and the one external network section in the compose file

Then deploy the stack in to cluster

#docker stack deploy -c docker-compose.yml  pythnprjct

