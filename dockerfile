FROM jenkins/agent:latest

USER root

RUN apt-get update && \
    apt-get install -y python3.10