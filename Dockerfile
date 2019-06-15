FROM ubuntu:18.04
LABEL maintainer="julio@blackdevs.com.br"

ENV DEBIAN_FRONTEND=noninteractive

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -qq && \
    apt-get install -y -qq \
    tzdata \
    apt-transport-https \
    ca-certificates \
    curl apt-utils git wget zip \
    gnupg-agent \
    software-properties-common

RUN apt-get install -y python3.7 python3-pip python-pip

WORKDIR /app
COPY . /app

RUN pip install virtualenv

RUN virtualenv venv -p python3.7

RUN chmod +x ./venv/bin/activate
RUN ./venv/bin/activate

RUN pip install -r requirements.txt

ENTRYPOINT [ "/usr/bin/python", "-u", "app/server.py" ]
