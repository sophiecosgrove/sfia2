#!/bin/bash
. ~/.bashrc
cp ~/.bashrc .
docker stack deploy --compose-file docker-compose.yml sfia2stack

echo ${DATABASE_URI} 