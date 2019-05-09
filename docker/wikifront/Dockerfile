FROM ubuntu:18.04

RUN apt-get update && apt-get -y install git curl
RUN curl -O https://deb.nodesource.com/setup_10.x && chmod +x setup_10.x && ./setup_10.x
RUN apt-get install -y nodejs
COPY config.yml /wiki/config.yml
RUN sed -i 's/XXX_KEY_XXX/'$(dd if=/dev/urandom bs=32 count=1 | sha256sum | cut -f 1 -d ' ')'/' /wiki/config.yml
RUN groupadd wiki-js && useradd -m -g wiki-js wiki-js
RUN chown wiki-js:wiki-js /wiki
USER wiki-js
RUN curl -o /wiki/install.sh https://wiki.js.org/install.sh && chmod 755 /wiki/install.sh && cd /wiki && ./install.sh
ENTRYPOINT cd /wiki && node wiki start; tail -Fq /wiki/logs/wiki-*-0.log
