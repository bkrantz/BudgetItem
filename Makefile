SHELL := /bin/bash

PYTHON_EXE := env/bin/python

.PHONY: dependencies install-docker clean install install-dev run build-docker run-docker migrate reset-migration

test:

dependencies:
	@#sripts to install project dependencies
	@#see also Dockerfile
	sudo apt-get update
	sudo apt-get install -y software-properties-common
	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt-get update
	sudo apt-get install -y make \
		python3.7-dev \
		python3.7-venv \
		python3-pip \
		libmysqlclient-dev \
		default-libmysqlclient-dev \
		build-essential \
		mysql-client

install-docker:
	@#scripts to install docker on VM
	sudo apt update
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
	apt-cache policy docker-ce
	sudo apt install docker-ce
	sudo usermod -aG docker ${USER}
	su - ${USER}

clean:
	rm -rf env
	find . -type d -name  "__pycache__" -exec rm -r {} +

install: clean
	python3.7 -m venv env
	${PYTHON_EXE} -m pip install -r requirements.txt

install-dev: clean
	python3.7 -m venv env
	${PYTHON_EXE} -m pip install -r requirements_dev.txt

run:
	source env/bin/activate \
		&& export FLASK_APP=src/app \
		&& flask run --host=0.0.0.0

build-docker:
	docker build . -t budget:0.0.1

run-docker:
	docker run --network=host budget:0.0.1 #-p 5000:5000

migrate:
	source env/bin/activate \
		&& export FLASK_APP=src/app \
		&& (flask db init &> /dev/null || true) \
		&& flask db migrate \
		&& flask db upgrade

reset-migration:
	source env/bin/activate \
		&& export FLASK_APP=src/app \
		&& (flask db downgrade &> /dev/null || true) \
		&& flask db upgrade