#!/bin/bash
. ~/.bashrc
export DATABASE_URI=${DATABASE_URI}
export SECRET_KEY=${SECRET_KEY}
docker stack deploy --compose-file docker-compose.yml sfia2stack