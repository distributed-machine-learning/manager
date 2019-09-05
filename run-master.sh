#!/usr/bin/bash

# build image for 
docker build -t app .
docker tag app:latest app:staging

# Run the compose file
docker-compose up