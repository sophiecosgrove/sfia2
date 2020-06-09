#!/bin/bash

sudo apt install -y python 

sudo apt install -y python-pip

sudo mkdir -p ~/.local/bin
sudo touch ~/.bashrc
sudo echo 'PATH=$PATH:~/.local/bin' > ~/.bashrc

sudo chown -R $(whoami):$(whoami) ~/*
sudo source ~/.bashrc

sudo pip3 install --user ansible

ansible --version