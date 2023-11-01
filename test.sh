#!/bin/bash

docker run -it \
    -v "$(pwd):/app/" \
    -w /app/ \
    python:3.12 \
    /bin/bash -c \
    "pip install -r /app/requirements.txt && \
    pytest"
