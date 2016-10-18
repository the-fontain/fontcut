.PHONY: setup run

setup:
	@brew install -v fontforge --with-libspiro --enable-pyextension
	@pip install -r test_requirements.txt
	@pip install -r requirements.txt

run:
	PYTHONPATH=$(PYTHONPATH):/usr/local/Cellar/fontforge/20160404/lib/python2.7/site-packages/ python server.py

test:
	PYTHONPATH=$(PYTHONPATH):/usr/local/Cellar/fontforge/20160404/lib/python2.7/site-packages/ coverage run --branch `which nosetests` --with-yanc --logging-clear-handlers -s
	@coverage report -m
