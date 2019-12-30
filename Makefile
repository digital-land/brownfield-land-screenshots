.PHONY: init c text images second-pass index clobber black clean prune
.SECONDARY:
.DELETE_ON_ERROR:

IMAGE_FILES:=$(wildcard images/*/*.png)
CSV_FILES=\
	../organisation-collection/collection/organisation.csv\
	../brownfield-land-collection/dataset/brownfield-land.csv


all: text images second-pass

second-pass:
	@make --no-print-directory index

index:	index.html
	@:

index.html:	index.py $(IMAGE_FILES) $(CSV_FILES)
	python3 index.py > $@

images:
	python3 images.py

black:
	black .

init::
	pip install -r requirements.txt
