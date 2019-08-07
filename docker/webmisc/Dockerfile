FROM python:3.7
RUN groupadd webmisc && useradd -g webmisc webmisc

USER webmisc
CMD cd /var/tmp/serve && python -m http.server 8000
