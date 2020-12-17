FROM python:3.8-slim

USER root
WORKDIR /root

COPY requirements.txt requirements.txt

RUN  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && pip install -U pip \  
    && pip install --no-cache-dir -r requirements.txt \ 
    && rm -rf /var/lib/apt/lists/* \ 