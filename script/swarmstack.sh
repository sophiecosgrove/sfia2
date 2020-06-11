#!/bin/bash
. ~/.bashrc
cp ~/.bashrc .
docker login
cd service1
docker build -t sophiec0s/service1:latest .
docker push sophiec0s/service1:latest
cd ../service2
docker build -t sophiec0s/service2:latest .
docker push sophiec0s/service2:latest
cd ../service3
docker build -t sophiec0s/service3:latest .
docker push sophiec0s/service3:latest
cd ../service4
docker build -t sophiec0s/service4:latest .
docker push sophiec0s/service4:latest
cd ../nginx
docker build -t sophiec0s/service4:latest .
docker push sophiec0s/service4:latest

env DATABASE_URI="${DATABASE_URI}" env TEST_DB_URI="${TEST_DB_URI}" docker stack deploy --compose-file docker-compose.yml sfia2stack

echo ${DATABASE_URI} 