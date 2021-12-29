SHELL := /bin/bash

PYTHON_EXE := env/bin/python

dependencies:
	sudo apt-get install -y make \
		python3.7-dev \
		python3.7-venv \
		python3-pip
	sudo apt update
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
	apt-cache policy docker-ce
	sudo apt install docker-ce
	sudo usermod -aG docker ${USER}
	su - ${USER}
	sudo apt-get install -y \
		libmysqlclient-dev \
		python-mysqldb \
		default-libmysqlclient-dev \
		build-essential

clean:
	rm -rf env
	find . -type d -name  "__pycache__" -exec rm -r {} +

install: clean
	python3.7 -m venv env

install-dev: install
	${PYTHON_EXE} -m pip install -r requirements_dev.txt

run:
	source env/bin/activate \
		&& export FLASK_APP=src/app \
		&& flask run --host=0.0.0.0

build-docker:
	docker build . -t budget:0.0.1

run-docker:
	docker run -p 5000:5000 budget:0.0.1 

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
	
alembic-revision:
	alembic revision --autogenerate -m "commit"

alembic-migrate:
	alembic upgrade head