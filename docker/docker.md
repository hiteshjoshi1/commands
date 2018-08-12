# Docker commands:
This command will list all running containers, showing information on them including their ID, name, base image name, and port forwarding-> <br>
<b><code>docker ps</code> </b>

This command is used to define a container — it processes the Dockerfile and creates a new container definition. We’ll use this to define our microservice containers-> <br>
<b><code> docker build</code> </b>


This command pulls the container image from the remote repository and stores the definition locally-> <br>

<b><code>docker pull [image name]</code> </b>

This command starts a container based on a local or remote (e.g. DockerHub) container definition. We’ll go into this one quite a bit-> <br>

<b><code>docker run</code></b>

# See all images 
docker images ps

# See Running container
docker container ps

# See running and stopped containers
docker container ps -a

# Remove all containers
docker container prune

# Remove an Image
docker image rm <Image id>

### Publishing a container to docker hub
- docker login             # Log in this CLI session using your Docker credentials
- docker tag <image> username/repository:tag  # Tag <image> for upload to registry
- docker push username/repository:tag            # Upload tagged image to registry
- docker run username/repository:tag                   # Run image from a registry



#Dockerfile
### Sample DockerFile - which needs an argument called JAR_FILE

FROM openjdk:8-jdk-alpine
VOLUME /tmp
ARG JAR_FILE
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"] 



### Building an Image from a Docker file
docker build --build-arg JAR_FILE=/target/your-spring-project-1.0-SNAPSHOT.jar -t your/image/name .

### Running the image
See if image is created
docker image ls

Run it 
docker run -p 8080:8081 your/image/name 

-------------------------------------------------------------------------------------------------------------------------------
## Login to bash in any container
Lets use mysql as an example
- docker exec -it container_name bash

### Finally Log to Mysql client
mysql -u user_anme -p

example
mysql -u root -p test

In my sql you can now run any db commands.

------------------------------------------------------------------------------------------------------------------------------

## Container-specific commands
These commands take either a container ID or container Name as a parameter:<br>

### This command will show the current load on each container specified – it will show CPU%, memory usage, and network traffic
<b><code>docker stats [container name/ID] [container name/ID]</code></b>

### This command shows the latest output from the container. The -f option “follows” the output, much like a console “tail-f” command would.
<b><code>docker logs [-f] [container name/ID]</code></b>

### This command dumps all of the configuration information on the container in JSON format
<b><code>docker inspect [container name/ID]</code></b>


### This command shows all of the port forwarding between the container host and the container.
<b><code>docker port [container name/ID]</code></b>


### Command to execute a command on target container, where i indicates to run interactively and t is pseudo tty  
<b><code>docker exec -it [container name/ID] sh</code></b>

-----------------------------------------------------------------------------------------------------------------------------


Runnig up a Mongodb instance - This will download the Mongodb Image
<b><code>docker run -P -d --name mongodb mongo</code></b>
Some explanation:
the -P tells Docker to expose any container-declared port in the ephemeral range
the -d says to run the container as a daemon (e.g. in the background)
the –name mongodb says what name to assign to the container instance (names must be unique across all running container instances. If you don’t supply one, you will get a random semi-friendly name like: modest_poitras)
the mongo at the end indicates which image definition to use


Downloading and runnig a SQL instance 
[--name  ->of the image, root password ,  -d -> RUN it as daemon, -P -> Any port in the epheremeral range 
mysql:tag -> if you do not specify tag it will take latest]

Command- <br>
<b><code>docker run --name docker-mysql -e MYSQL_ROOT_PASSWORD=test -P -d mysql</code></b>

To Connect via command line -<br>
<b><code>docker run -it --link docker-mysql:mysql --rm mysql sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'</code></b>

Ideally you would connect with the docker instance with MySql workbench with the exposed port
<b><code>docker ps</code></b>  - will give you the exposed port

---------------------------------------------------------------------------------------------------------------------------------------------------------

To Build the image from Docker File - Custom image as specified in the Dockerfile ---> (Note the .) <br>
<b><code>docker build -t microservice/customer . </code></b>

To Run the  Custom Image---><br>
<b><code>docker run --name docker-customer --link docker-mysql:mysql -P -d microservice/customer</code></b>

The logical link we created with --link links the containers. In my use case the docker file is bringing up a spring boot application, 
and it should specify how the spring boot connects to mysql usinng the logical link.

------------------------------------------------------------------------------------------------------------------------------------------------------
To debug a docker events->

First start docker events in the background to see whats going on.<br>
<b><code>docker events&</code></b>

Then run your Docker run command -> <br>
<b><code>docker run -P -d --name docker-customer --link docker-mysql microservice/customer</code></b> 

Output -> <br>
2017-11-26T11:09:17.025465400+05:30 container die 412d1025b8d5abf9878cdca015b01b691edc3adc7ababda889d1b16f729fe37b (exitCode=1, image=microservice/customer, name=docker-customer)

Use the Hash to find the log - <br>

<b><code>docker logs 412d1025b8d5abf9878cdca015b01b691edc3adc7ababda889d1b16f729fe37b</code></b>

--------------------------------------------------------------------------------------------------------------------------------------------------------





