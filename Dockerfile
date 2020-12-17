FROM python:3.8-slim

USER root
WORKDIR /root
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt requirements.txt

RUN  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && pip install -U pip \  
    && pip install --no-cache-dir -r requirements.txt \ 
    && rm -rf /var/lib/apt/lists/* \ 