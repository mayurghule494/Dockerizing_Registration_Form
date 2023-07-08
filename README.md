✅ 
# Dockerizing_Registration_Form



# Project Overview

🚀 In this project we are Dockerizing Simple Registration Form.<br>
🚀 Here We are using **Index.html and css** to create frontend.<br>
🚀 Here We are using **Python** to create backend.<br>
🚀 And to store the users registration details we are going to use **MySql Database** as a backend.<br>
➡️ **We are going to create :-** <br>
   - Ubuntu based **EC2 Instance**. <br>
   - 3 Docker container using **docker-compose**. <br>
     - Frontend with **html and css**. <br>
     - Backend with **app.py** python based <br>
     - Backend for **Mysql Database** to store users information after registration. <br>     

## Getting Started

✅ Steps
- Launch EC2 Instance with Ubuntu OS.<br>
- Connect to the instance with SSH.<br>
- Update the packeages using below command. <br>
  ##### $ sudo apt-get update -y <br>
- Now Install Docker on the server using below command. <br>
  ##### $ sudo apt-get install docker.io -y <br>
- Now use below commands to Install docker-compose as we are usining docker compose to create containers at one go.<br>
  ##### $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose <br>
  ##### $ sudo chmod +x /usr/local/bin/docker-compose <br>
- Use the below command to check the docker-compose version.<br>
  ##### $ docker-compose --version <br>
- clone this repo to your ubuntu machine to get the source code for this project. <br>
  ##### $ git clone https://github.com/mayurghule494/Dockerizing_Registration_Form.git <br>
    You can also Fork this repo to get the code in your github repository. <br>
- Go to the Dockerizing_Registration_Form directory.<br>
  ##### $ cd Dockerizing_Registration_Form <br>
- Now use below command to create the all 3 containers <br>
  ##### $ sudo docker-compose up -d <br>
   You will get the output as shown in below image. <br>
      ![docker-compose](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/b3513111-0e1e-48ba-bdcb-32ea54f05c7c)

- You have to open following Ports in security group. <br>
    update 8000 to access frontend webpage. <br>
    update 3306 to access Mysql Database. <br>
    update 8080 to access Mysql Database with GUI interface. <br>

- Now you can access the frontend web page on your browser as shown in below screenshots. <br>
    ##### http://13.59.222.100:8000/ <br>        
    ##### Here we are using public-ip:8000 <br>

  ![form-op](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/9929e7f1-f875-4bda-b986-8dc64490da1a)


  ![form-op-2](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/531a8379-d47e-4a64-b466-38044e92dd32)

  ![form-op-3](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/aac91e7b-5894-4bc5-aa87-871157652c37)


- If you want to check the entry after submitting the form, You can use Mysql phpmyadmin login page as shown in below screenshots. <br>
    ##### http://13.59.222.100:8080/ <br>
    ##### Here we are using public-ip:8080 <br>
    ##### use user: admin password: admin <br>
  ![form-phpmyadmin-1](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/d4ccf713-c536-4fd8-8849-6af867cc4890) 

- Now add you Database user credential which is admin - admin <br>

  ![form-phpmyadmin-2](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/ff5be567-fadd-438d-aef0-f5a2314b1a0b) 

- Now open registration_db databse and there click on users table to see your entry. <br>

  ![form-phpmyadmin-3](https://github.com/mayurghule494/Dockerizing_Registration_Form/assets/54388290/3a1e0a30-2aa7-4dfe-9731-d486be987bdf) 



