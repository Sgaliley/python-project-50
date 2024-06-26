install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

check:
	poetry check

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: 
	python3 -m pip install dist/*.whl --force-reinstall

start:
	poetry run gendiff