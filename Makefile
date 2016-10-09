.PHONY: setup run

setup:
	@brew install -v fontforge --with-libspiro --enable-pyextension
	@pip install -r requirements.txt

run:
	PYTHONPATH=$(PYTHONPATH):/usr/local/Cellar/fontforge/20160404/lib/python2.7/site-packages/ python server.py

test:
	@python tests/__init__.py
