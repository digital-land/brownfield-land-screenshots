#!/usr/bin/env python3

import re
import os
import os.path
import csv
import datetime
from collections import OrderedDict

dataset = "brownfield-land"
organisation_csv = "../organisation-collection/collection/organisation.csv"
dataset_csv = "../brownfield-land-collection/dataset/brownfield-land.csv"

today = datetime.date.today().strftime("%Y-%m-%d")
subdir = os.path.join("images", today)
os.makedirs(subdir, exist_ok=True)


def path(url):
    url = url.replace("://", "_")
    return os.path.join(subdir, re.sub("[^\w\-_\. ]", "_", url) + ".png")


organisations = OrderedDict()
for o in csv.DictReader(open(organisation_csv)):
    o["path-segments"] = list(filter(None, o["organisation"].split(":")))
    prefix = o["prefix"] = o["path-segments"][0]
    o["id"] = o["path-segments"][1]
    o.setdefault("tags", [])
    o["tags"].append(prefix)
    o["link"] = "/dataset/{dataset}/organisation/{path}".format(dataset=dataset, path="/".join(o["path-segments"]))
    organisations[o["organisation"]] = o


urls = {}
for row in csv.DictReader(open(dataset_csv)):
    url = row["documentation-url"]
    if url:
        urls.setdefault(url, {
            "path": path(url),
            "organisation": {},
        })
        urls[url]["organisation"][row["organisation"]] = True


print(
    """
<style>
img {
  width: 250px;
  border: 1px solid black;
}

article {
  column-width: 250px;
}

figure {
 display: inline-block;
}

figcaption {
    padding-top: 0.5em;
}
</style>
<article>
"""
)


for url, u in urls.items():
    if os.path.exists(u["path"]):
        title = ", ".join([organisations[o]["name"] for o in u["organisation"]])
        caption = ", ".join(['<a href="{link}">{name}</a>'.format(**organisations[o]) for o in u["organisation"]])
        print(
            """
<figure>
  <a href="{url}" title="{title}"><img src="{path}"></a>
  <figcaption>{caption}</figcaption>
</figure>
""".format(url=url, path=u["path"], title=title, caption=caption))


print(
    """
<article>
"""
)
