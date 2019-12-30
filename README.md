# Digital Land brownfield land screenshots

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/digital-land/brownfield-land/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://black.readthedocs.io/en/stable/)

An experiment to capture the information Local Planning Authorities publish alongside their brownfield land registers.

We did this to see if it's possible to identify when new registers are published, and to assess how we can help people publish other registers, such as developer contributions and local plans.

The script uses phantomJS to take a screenshot of the documentation pages listed in the [brownfield-land-collection](https://github.com/digital-land/brownfield-land-collection)/[dataset/brownfield-land.csv](https://github.com/digital-land/brownfield-land-collection/blob/master/dataset/brownfield-land.csv) and dump the rendered page as HTML.

TBD:

* dismiss cookie and other pop-ups
* reintroduce code to timeout blocking pages
* better handle SSL and other errors
* save image files with a sha256 filename
* experiment with [Wraith](http://bbc-news.github.io/wraith/) and other tools for comparing images
* experiment using lynx, pandoc and other tools to save the HTML as plain text or other easier to compare format
* consider integrating these screenshots into the [dataset] pages

# Updating the screenshots

We recommend working in [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) before installing the python dependencies:

    $ make init
    $ make

# Licence

The software in this project is open source and covered by LICENSE file.

Individual datasets copied into this repository may have specific copyright and licensing, otherwise all content and data in this repository is
[© Crown copyright](http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/copyright-and-re-use/crown-copyright/)
and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
