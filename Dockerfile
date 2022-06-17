# start from base

FROM ubuntu:20.04

LABEL maintainer="bharadwajr07"
WORKDIR /app

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y python3.9 python3.9-dev python3-pip python3-wheel build-essential

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "app.py" ]