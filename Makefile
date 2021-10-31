PACKAGE_DIR=ml_api

format:
	@poetry run isort .
	@poetry run black .

lint:
	@poetry run pylint -d C,R,fixme $(PACKAGE_DIR)