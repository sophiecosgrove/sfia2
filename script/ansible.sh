#!/bin/bash

sudo source ~/.bashrc
sudo source ~/.ssh/config
ansible-playbook -i inventory.cfg playbook.yml