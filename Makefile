lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

install:
	poetry install

gendiff:
	poetry run python -m gendiff.scripts.script