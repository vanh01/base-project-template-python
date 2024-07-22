init:
	test -d venv || virtualenv venv
.PHONY: init

zipp:
	. ${CURDIR}/venv/bin/activate; pip freeze > requirements.txt
.PHONY: zipp

unzipp: init
	. ${CURDIR}/venv/bin/activate; pip install -r requirements.txt
.PHONY: unzipp

migrate:
	python3 migrate.py
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

stop-service:
	sudo systemctl stop app.service
.PHONY: stop-service

restart-service:
	sudo systemctl restart app.service
.PHONY: restart-service

config-nginx:
	sudo cp nginx.conf /etc/nginx/nginx.conf
.PHONY: config-nginx

restart-nginx:
	sudo systemctl restart nginx
.PHONY: restart-nginx

build-run: unzipp
	python3 gen.py gen-service
	make enable-service
	sudo systemctl is-active --quiet app.service && sudo systemctl restart app.service || sudo systemctl start app.service
	# make config-nginx
	# make restart-nginx

.PHONY: build-run