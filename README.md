# SFIA-2
# Requirements 
* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
* This could also provide a record of any issues or risks that you faced creating your project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a * CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture that has been asked for.
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project you need to create an Ansible Playbook that will provision the environment that your application needs to run.

# Technologies
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
# Docker
* Docker containers allow for easy packing, deploying and management of applications in a clean environment. Containers allow you to package up an app with everything it needs so that any other Linux user can download and distribute it easily. This ensures consistency in development, build, test, and production environments and promotes security as containers are completely segregated from one another. Docker also allows you to version control your images, including rollbacks if you encounter an error with the image. It reduces deployment times as container images do not require an OS to be booted up. They are compatible with Google Cloud Services which is what I used to host my VMs and database. Storing the service images on Dockerhub means that they can be downloaded and utilised anywhere and by anyone which in a real-life setting would reduce the time taken to download and deploy the services whilst ensuring efficiency.
# Ansible
* Ansible is an automation tool that allows you to provision your machines with the set-up they need to run the software. It also assists in deployment and orchestration of software. 
# Designs
## Use Case
![imageofusecase](https://github.com/sophiecosgrove/sfia2/blob/development/images/usecase.png)
## User Stories
![imageofuserstories](https://github.com/sophiecosgrove/sfia2/blob/development/images/userstories.png)
## ERD
![imageoferd](https://github.com/sophiecosgrove/sfia2/blob/development/images/erd.png)
* Once a fortune is generated, it is entered into the database and assigned a unique ID. At the moment this is the only table in the database however should more be added in later stages of development, the primary key in the fortunes table is the fortune ID. 
## Changes
### Python Logic
* Initially both the time and phrase functions just returned a random selection from a single list, however, I wanted to add more variability in the selection of the fortune. I considered implementing a 2D list, with two random numbers being generated to select the position of the fortune in the list, but finally I decided on having two different lists. First a number is generated to select which list to choose from and then a second number is generated to select which string to return. Doing it this way allowed me to account for the different lengths of the lists and also manipulate the odds of the selection. For example, the chances of getting a good fortune compared to a bad fortune is 2:1 due to there being two possible numbers selected from the given range that correspond to the good fortune list and only one for the bad fortune list.
## MySQL
* Initially I had set up a database as a docker container from the first VMs IP address on port 3306. However, after a bit of troubleshooting I decided to instead have it as an instance on GCP. I felt like this was more easily accessible as multiple VMs would need to be accessing it when the containers were hosted across the swarm. 

# Project Tracking
## Trello 
* I used a trello board to track my project and organise my workload. 
![imageoftrello1](https://github.com/sophiecosgrove/sfia2/blob/development/images/sfia2sprint1.png)
![imageoftrello2](https://github.com/sophiecosgrove/sfia2/blob/development/images/sfia2sprint2.png)
![imageoftrello3](https://github.com/sophiecosgrove/sfia2/blob/development/images/sfia2sprint3.png)
# Deployment
## CI Pipeline
![imageofcipipeline](https://github.com/sophiecosgrove/sfia2/blob/development/images/CIPipeline.png)
* In the development stage, I created 4 microservice APIs using Flask and Python for the back end and Bootstrap CSS and HTML for the front end. Service 1 provided the user interface of the app, hosting a website with two pages, home and fortunes. When the home page is refreshed or the 'generate fortune' button is selected by the user, the home route sends a get request to service 4 to receive some data. Service 4 then requests a random time response from service 2 and a random fortune response from service 3. Service 4 then puts these two text responses together and returns it to service 1, where it is finally turned into text, entered into the MySQL database and displayed for the user on the home page and also in a list on the fortunes page. During this stage I tested the app by manually deploying it through docker-compose and then transitioning onto the use of docker stack deploy once I had set up my worker nodes. The app was hosted on port 80 through the use of a reverse-proxy using NGINX. This meant that traffic was redirected from port 80 to the app on port 5000. I also tested the app during this stage. Firstly testing the python logic of the routes on a separate python document and then finally utilising Unittest and Mocking to test the rest of the app and its connections.  
* The VCS service used was GitHub and I utilised a Webhook so that whenever new code was pushed to the development branch, it would trigger Jenkins to build a pipeline. In this pipeline I automated the use of Ansible, which installed Docker on each of the VMs and also set up the Docker Swarm. Finally I automated the builds of the Docker images through Jenkins and then deployed the service stack across the swarm.
![imageofjenkinspipeline](https://github.com/sophiecosgrove/sfia2/blob/development/images/Jenkins.png)
* As demonstrated I have conducted an extensive amount of builds which were triggered after each commit made to github. 
* When I was having problems with my database URIs not exporting across Jenkins, I made use of the replay function which allows you to alter the Jenkins File within Jenkins to re-test the pipeline. This was helpful because it meant I did not have to go through github and made the problem solving much quicker.

# Risk Assessment
![imageofinitialriskassessment](https://github.com/sophiecosgrove/sfia2/blob/development/images/initialriskassessment.png)
![imageofinitialriskmatrix](https://github.com/sophiecosgrove/sfia2/blob/development/images/initialriskmatrix.png)
* My initial risk considerations were mainly theoretical as I had not got to grips with the concepts and technologies we would be using throughout the project. The allocated time for this project was shorter than previously experienced, so I was concerned this would pose a risk to the project being completed. However, some of the concepts I was already familiar with from the last project and there was not as much programming to do for the actual app but instead setting up the services which did not take too long. Therefore, the project was successfully completed on time. 
![imageofongoingriskassessment](https://github.com/sophiecosgrove/sfia2/blob/development/images/ongoingriskassessment.png)
![imageofongoingriskmatrix](https://github.com/sophiecosgrove/sfia2/blob/development/images/ongoingriskmatrix.png)
* In the on-going risk assessment, I logged some of the risks I faced when working on the project, incase they arose again and to document their effect on the project. The biggest problem I faced was with NGINX as the image was missing some important files needed for it to run properly, such as the conf.d directory and default.conf file. I had to download a stable image rather than the latest image from dockerhub. Another issue that arose was when setting up the ability for the manager to SSH into the other VMs to enable Ansible to work, it was important that I only allowed the connection from the IPs of my VMs on port 22 and not have it open to the internet. 
![imageoffinalriskassessment](https://github.com/sophiecosgrove/sfia2/blob/development/images/futurerisks.png)
![imageoffinalriskmatrix](https://github.com/sophiecosgrove/sfia2/blob/development/images/finalriskmatrix.png)
* My final risk assessment is my consideration of risks that may pose a threat to the app in the future. They are mainly considerations of how the app could be improved should it be released for public consumption. Due to the ability to upscale apps in both Docker and Flask, I believe that it would be possible to achieve the improvements stated above to improve the user experience. 
# Testing
## Service 2
![imageofservice2covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service2covdiagram.png)
* Due to the random feature in the route, each time the test was run it would only go through half of the code. This is represented in the stage 1 test coverage where with one test to get the url for the route and return the response code of 200, the coverage was at 92%. In order to get to 100% test coverage, I utilised 'with self.client' and ran the test for the route 3 times. This way the same test would run atleast once through each if statement and all lines of code would be tested.
## Service 3
![imageofservice3covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service3covdiagram.png)
* As service 3 is structured very similarly to service 2, I adopted the same method for testing. With one test to get the route, the coverage was at 77%, I believe this is because in this specific instance the test initiated the if statement with the lesser code between the two. This time I added three more tests because the odds for the if statements were 2:1, with the positive fortunes being favoured. Therefore it was necessary to run the tests 4 times in total to make sure that the negative if statement was triggered at least once, with the positive if statement almost certainly being triggered. This got the test coverage up to 100%.
## Service 1
![imageofservice1covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service1covdiagram.png)
* In stage 1 I conducted a test to set up the app and connection to the database and input an entry. This lead to the overall coverage being at 69%. Stage 2 involved resting the repr function in models, which increased the models coverage to 100%. In stage 3 I implemented mock testing to mimic a response from service 4 whilst it was not running. This allowed me to test the home route for service 1. In order to test the fortunes route I asserted that the text entered into the database in the first test would be shown on the fortunes page. This lead to the test coverage being 100%. 
## Service 4 
![imageofservice4covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service4-100.png)
* To test service 4's route I also used mock testing to mimic the response from services 2 and 3. The test is not exactly the same as the original route as it has two different responses which it puts together whereas in the test it has one response. Nonetheless, the test coverage is 100%.

# Best Practices
* I utilised a venv when installing packages and when making changes to the python code and running pytest.
* I implemented the use of a .gitignore and a .dockerignore to prevent cache files being pushed to github and dockerhub, respectively.
* I made sure that variables were not hardcoded into the files and therefore accessible to anyone on github. I did this using environment variables.
* I made sure that the only VMs that were able to SSH into one another were the ones that I was using and my local machine's IP so that I could SSH into my master VM to work on the app from VSCode.
* Reverse-Proxy

# Bugs and Fixes
* 05/06/20 Website not displaying using docker-compose - I had to clear my docker images and containers up as I had a lot of items saved and Docker didn't have enough space to work. Commands I used for this were: docker stop $(docker ps -q), docker rm $(docker ps -aq), docker rmi $(docker images -q), docker system prune.
* 09/06/20 Website not displaying using docker swarm stack - Firstly I changed the location of my database so that it was not a container and running on my IP on port 3306. Instead I set it up in GCP as an instance, allowing connections from the worker nodes as well as the manager-node. I also had to change the firewall rules for the VMs to make sure they had access to all parts of the application. 
* 09/06/20 Jenkins not running - had to add the private and public to the jenkins ssh directory as well as the config file.
* 10/06/20 Nginx not running, replicas 0/1 - changed the version to stable and added it to the same ingress network as the other containers.
* 11/06/20 Environment variables not exporting through Jenkins - added this line to the code so that the environment variables were included in the docker stack deploy command. env DATABASE_URI="${DATABASE_URI}" env TEST_DB_URI="${TEST_DB_URI} docker stack deploy --compose-file docker-compose.yml sfia2stack

# Future Improvements
## Fortune Aspect
* As mentioned above, I believe that the user experience of the app could be improved by providing more specific fortunes and involving an interactive element. I would like to add comment and like functionality as this would provide elaboration on the fortunes recieved and some detail on if they were accurate to the individual. In addition, a customised fortune generation including forms to personalise the fortune or involving the time of access in the time aspect of the fortune would make the user experience more meaninful. Nonetheless, I do appreciate the simplicity of the app as it provides a simple and fast response. 
## Testing
* I would have liked to implement another form of testing in my app such as selenium to test the front end including links and buttons. In addition, the mock testing does not test the apps integration and functionality in a real-life environment. Despite this, I am happy with my less formal practice of the app's working functionality by running it and checking the website works as well as observing the container logs and service list. 
# Acceptance Criteria
## 4 services
* I have created an app with four interactive services and a further fifth NGINX service. I believe I have met the criteria in this section as my first service hosts the interactive element of the app, using Jinja2 syntax to pass through a layout html for the webpages and it is the service responsible for triggering the other services into action. In addition, this service connects to a MySQL database which persists the created data in order for it to be retrieved on the website. Services 2 and 3 both create a random object as specified and service 4 creates an object based on the text responses received from services 2 and 3.
## Different Implementations 
* In my presentation I will demonstrate how the services can be altered without disrupting the user experience. This is achieved using Docker Swarm's replica functionality which will continue to host the service whilst each replica is being updated.
## MoSCow
* The MoSCow criteria I created at the start of my project is as follows:
* Must have - 4 micro services, a database, 2 implementations
* Should have - best practices
* Could have - a nice front-end website
* Won't have - a complex website
* I feel I have met my must have, should have and could have criteria which ensure the functionability and quality of the project. The won't have criteria is an area that I have discussed above in my risk assessment and future improvements so I am happy that this criteria although not achieved currently, could be achieved in the future.
# Authors
Sophie Cosgrove
# License
MIT License

Copyright (c) 2020 sophiecosgrove

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
