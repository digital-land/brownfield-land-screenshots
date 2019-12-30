.PHONY: init c text images index clobber black clean prune
.SECONDARY:
.DELETE_ON_ERROR:

all: text images index.html

index.html:	index.py
	python3 index.py > $@

images:
	python3 images.py

black:
	black .

init::
	pip install -r requirements.txt
