#!/bin/bash

apt install -y python 

apt install -y python-pip

mkdir -p ~/.local/bin
touch ~/.bashrc
echo 'PATH=$PATH:~/.local/bin' > ~/.bashrc

sudo chown -R $(whoami):$(whoami) ~/*
source ~/.bashrc

pip3 install --user ansible

ansible --version