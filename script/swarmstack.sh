#!/bin/bash
. ~/.bashrc
cp ~/.bashrc .
env DATABASE_URI="${DATABASE_URI}" docker stack deploy --compose-file docker-compose.yml sfia2stack

echo ${DATABASE_URI} 