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
# Designs
## Use Case
![imageofusecase](https://github.com/sophiecosgrove/sfia2/blob/development/images/usecase.png)
## User Stories
![imageofuserstories](https://github.com/sophiecosgrove/sfia2/blob/development/images/userstories.png)
## ERD
![imageoferd](https://github.com/sophiecosgrove/sfia2/blob/development/images/erd.png)
# Deployment
## CI Pipeline
![imageofcipipeline](https://github.com/sophiecosgrove/sfia2/blob/development/images/CIPipeline.png)
* In the development stage, I create 4 microservice APIs using Flask and Python for the back end and Bootstrap CSS and HTML for the front end. Service 1 provided the user interface with the app, hosting a website with two pages, home and fortunes. When the home page is refreshed or the 'generate fortune' button is selected by the user, the home route sends a request to service 4 to receive some data. Service 4 then requests a random time response from service 2 and a random fortune response from service 3. Service 4 then puts these two text responses together and returns it to service 1, where it is finally turned into text, entered into the MySQL database and displayed for the user on the home page and also in a list on the fortunes page. During this stage I tested the app by manually deploying it through docker-compose and then transitioning onto the use of docker stack deploy once I had set up my worker nodes. The app was hosted on port 80 through the use of a reverse-proxy using NGINX. This meant that traffic was redirected from port 80 to the app on port 5000. I also tested the app during this stage. Firstly testing the python logic of the routes on a separate python document and then finally utilising Unittest and Mocking to test the rest of the app and its connections.  
* The VCS service user was GitHub and I utilised a Webhook so that whenever new code was pushed to github, it would trigger Jenkins to build a pipeline. In this pipeline I automated the use of Ansible, which installed Docker on each of the VMs and also set up the Docker Swarm. Finally I automated the builds of the Docker images through Jenkins and then deployed the service stack across the swarm.

# Risk Assessment
![imageofinitialriskassessment](https://github.com/sophiecosgrove/sfia2/blob/development/images/initialriskassessment.png)
# Testing
## Service 2
![imageofservice2covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service2covdiagram.png)
* Due to the random feature in the route, each time the test was run it would only go through half of the code. This is represented in the stage 1 test coverage where with one test to get the url for the route and return the response code of 200, the coverage was at 92%. In order to get to 100% test coverage, I utilised 'with self.client' and ran the test for the route 3 times. This way the same test would run atleast once through each if statement and all lines of code would be tested.
## Service 3
![imageofservice3covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service3covdiagram.png)
* As service 3 is structured very similarly to service 2, I adopted the same method for testing. With one test to get the route, the coverage was at 77%, I believe this is because in this specific instance the test initiated the if statement with the lesser code between the two. This time I added three more tests because the odds for the if statements were 2:1, with the positive fortunes being favoured. Therefore it was necessary to run the tests 4 times in total to make sure that the negative if statement was triggered at least once, with the positive if statement almost certainly being triggered. This got the test coverage up to 100%.
## Service 1
![imageofservice1covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service1covdiagram.png)
## Service 4 
![imageofservice4covdiagram](https://github.com/sophiecosgrove/sfia2/blob/development/images/service4-100.png)

# Bugs and Fixes
* 05/06/20 Website not displaying using docker-compose - I had to clear my docker images and containers up as I had a lot of items saved and Docker didn't have enough space to work. Commands I used for this were: docker stop $(docker ps -q), docker rm $(docker ps -aq), docker rmi $(docker images -q), docker system prune.
* 09/06/20 Website not displaying using docker swarm stack - Firstly I changed the location of my database so that it was not a container and running on my IP on port 3306. Instead I set it up in GCP as an instance, allowing connections from the worker nodes as well as the manager-node. I also had to change the firewall rules for the VMs to make sure they had access to all parts of the application. 
* 09/06/20 Jenkins not running - had to add the private and public to the jenkins ssh directory as well as the config file.
* 10/06/20 Nginx not running, replicas 0/1 - changed the version to stable and added it to the same ingress network as the other containers.
* 11/06/20 Environment variables not exporting through Jenkins - added this line to the code so that the environment variables were included in the docker stack deploy command. env DATABASE_URI="${DATABASE_URI}" env TEST_DB_URI="${TEST_DB_URI} docker stack deploy --compose-file docker-compose.yml sfia2stack

# SSH
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
