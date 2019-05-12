FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:certbot/certbot && \
    apt-get update && \
    apt-get install -y certbot docker.io
COPY deploy-hook /deploy-hook
RUN chmod +x /deploy-hook
