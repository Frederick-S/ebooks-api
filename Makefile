run:
	python app.py

test:
	python setup.py test

coverage:
	coverage run --source=ebooks setup.py test

lint:
	pycodestyle . --exclude=venv
