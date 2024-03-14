#!/bin/bash

# Build Docker image
docker build -t testing01 .

# Run Docker container
docker run -v ./Users/phil/Documents/Projekte/preisDateien testing01

#-v ./Users/phil/Documents/Projekte/preisDateien -p 8000:5000 
