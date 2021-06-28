# A Digit Recognition Project
A full feature web app using MLP for digit recognition
<hr>

## Connect to EC2 instance
1. Navigate to the folder where you keep your .pem file as the ec2 key pair
2. type `chmod 400 ` command in your terminal and drag your .pem file to the terminal. it should look like something lile this.\
 `chmod 400 /Users/yipengjiang/Learn/SFL\ demo/num_recog.pem`
3. Go to your ec2 terminal and click connect, copy the ssh clinet command and run it in your local terminal, then you can control your sever using ssh client. 

<span style="color:red">Attention: </span> When you stop and restart a instance, the public ip address and dns will change, so make sure you change your database configuration and whitelist.


## PostgresSQL container
1. To start your postgres docker container, make sure your have docker installed on your server, if not please refer to [docker offical documentation](https://www.walmart.com/registry/baby/c5dbbe58-62cc-4eed-b872-696496ac10ff).

2. In order to start your docker container, you have two options.
    1. Run this command in your terminal\
    `docker run -d --name <container_name> -p 5432:5432 -e POSTGRES_PASSWORD=1234 postgres`
    2. If you have install docker-compose on your EC2 instance, there is a yaml file which is a docker compose file. you can start your container simply by runing:\
    `docker-compose -f docker_compose.yaml up -d`
    
    *Remember* if there are multiple containers to run, it is easier to use docker-compose instead of writing individual running command on your terminal.
2. In order for local pgadmin to connect to the postgresSQL container on the cloud, we need to add a new security rule in the security group to enable postgresSQL TCP request.

<img src="https://i.stack.imgur.com/GLWwb.png" alt="illustration" width="400"/>

3. Go to your pgadmin, click on create server
4. Fill your public EC2 instance address and your database password in the following window. 

<img src="readme_img/2021-06-27-20-21-32.png" alt="illustration" width="300"/>

## MongoDB Atlas

In order for the ec2 instance to connect to the mongoDB Atlas we need to whitelist our ec2 ip address in the mongodb terminal.

1. Go to cloud.mongodb.com to login in to your cluster
2. Navigate to *Network Acess* and click on <span style="background-color: #32a852">ADD IP ADDRESS</span>.
3. Go to your ec2 control panel, click on the instance and find your public Ip address. Remember the mongodb atlas free tier can not set up peering connection using private ip address. 
 

## TensorFlow2 on AWS DLAMI 
To activate TensorFlow 2, open an Amazon Elastic Compute Cloud (Amazon EC2) instance of the DLAMI with Conda.

1. For TensorFlow 2 and Keras 2 on Python 3 with CUDA 10.1 and MKL-DNN, run this command:\
`source activate tensorflow2_p36`

2. To Check virtual environments run:\
`conda info --envs`

