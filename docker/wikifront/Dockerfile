FROM ubuntu:18.04

RUN apt-get update && apt-get -y install git curl
RUN curl -O https://deb.nodesource.com/setup_10.x && chmod +x setup_10.x && ./setup_10.x
RUN apt-get install -y nodejs
RUN curl -O https://wiki.js.org/install.sh && chmod 755 install.sh && ./install.sh
COPY config.yml /config.yml
RUN sed -i 's/XXX_KEY_XXX/'$(dd if=/dev/urandom bs=32 count=1 | sha256sum | cut -f 1 -d ' ')'/' config.yml
ENTRYPOINT node wiki start; tail -Fq /logs/wiki-*-0.log
