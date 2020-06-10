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

# Risk Assessment
# Testing
# Authors
Sophie Cosgrove

# Bugs and Fixes
* 05/06/20 Website not displaying using docker-compose - I had to clear my docker images and containers up as I had a lot of items saved and Docker didn't have enough space to work.
* 09/06/20 Website not displaying using docker swarm stack - Firstly I changed the location of my database so that it was not a container and running on my IP on port 3306. Instead I set it up in GCP as an instance, allowing connections from the worker nodes as well as the manager-node. I also had to change the firewall rules for the VMs to make sure they had access to all parts of the application. 
* 09/06/20 - Jenkins not running - had to add the private and public to the jenkins ssh directory as well as the config file.
* 10/06/20 Nginx not working. It didn't have a conf.d directory so re-installed and then it was missing an nginx.conf.

# SSH
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
