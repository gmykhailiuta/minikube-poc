APP_NAME=app_one
CHART_NAME=app-one
GUNICORN_PORT=8001

.PHONY: initenv inittestenv clean rundev rungunicorn test build release deploy undeploy

initenv:
	python3 -m venv .venv
	.venv/bin/pip3 install -r requirements/runtime.txt

inittestenv:
	python3 -m venv .venv
	.venv/bin/pip3 install -r requirements/test.txt

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo\$$)" | xargs rm -rf 
	rm -rf .pytest_cache

rundev:
	.venv/bin/python3 main.py

rungunicorn:
	.venv/bin/gunicorn --workers 1 \
	--bind 0.0.0.0:$(GUNICORN_PORT) \
	--access-logfile=- \
	--error-logfile=- \
	main:$(APP_NAME)

test:
	.venv/bin/pytest

build:
	$(MAKE) clean && \
	docker build -t $(APP_NAME) .

release:
ifndef VERSION
	$(error VERSION is undefined)
endif
	sed -i "s/appVersion.*/appVersion: ${VERSION}/" helm/$(CHART_NAME)/Chart.yaml
	$(MAKE) build && \
	docker tag $(APP_NAME):latest $(APP_NAME):${VERSION}

deploy:
	cd helm && \
	helm upgrade $(CHART_NAME) $(CHART_NAME) --install

undeploy:
	cd helm && \
	helm delete $(CHART_NAME)
