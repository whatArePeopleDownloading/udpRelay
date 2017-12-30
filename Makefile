init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock
watch:
	pipenv run ptw
tests:
	pipenv run pytest
clean:
	rm -rf build dist .egg *.egg-info
start:
	pipenv run python -m udprelay.server
publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist
	twine upload dist/*
	make clean

