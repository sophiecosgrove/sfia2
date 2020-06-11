#!/bin/bash
sudo source ~/.bashrc

sudo docker stack deploy --compose-file docker-compose.yml sfia2stack

echo ${DATABASE_URI} > ~/image.log