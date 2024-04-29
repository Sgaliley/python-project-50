install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: 
	python3 -m pip install --user dist/*.whl --force-reinstall

start:
	poetry run gendiff