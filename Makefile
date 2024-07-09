init:
	python -m venv venv
.PHONY: init

zipp:
	pip freeze > requirements.txt
.PHONY: zipp

unzipp:
	pip install -r requirements.txt
.PHONY: unzipp

migrate:
	python migrate.py
.PHONY: migrate

run:
	flask run
.PHONY: run

test:
	flask run
.PHONY: test

enable-service:
	sudo cp app.service /etc/systemd/system/
	sudo systemctl enable app.service
.PHONY: enable-service

start-service:
	sudo systemctl start app.service
.PHONY: start-service

config-nginx:
	sudo cp nginx.conf /etc/nginx/nginx.conf
.PHONY: config-nginx