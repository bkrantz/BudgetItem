#FROM python:3.7.12-alpine
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y make \
		python3.7-dev \
		python3.7-venv \
		python3-pip \
		libmysqlclient-dev \
		default-libmysqlclient-dev \
		build-essential \
		mysql-client
		
WORKDIR /app
ADD . /app

RUN mv .env.docker .env &> /dev/null | true
RUN make install

EXPOSE 5000

CMD ["make", "run"]