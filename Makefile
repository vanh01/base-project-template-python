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