#!/bin/bash

docker build -t devops-dato:latest .

docker run -it devops-dato:latest pytest
