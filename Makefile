init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock
watch:
	pipenv run ptw
tests:
	pipenv run pytest

start:
	pipenv run python -m udprelay.server
publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist
	twine upload dist/*
	rm -rf build dist .egg getport.egg-info
