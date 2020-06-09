#!/bin/bash
source ~/.bashrc
source ~/.ssh/config
ansible-playbook -i inventory.cfg playbook.yml