#!/usr/bin/env python3

import os
import os.path
import subprocess
import re
import csv
import datetime

today = datetime.date.today().strftime("%Y-%m-%d")
subdir = os.path.join("images", today)

os.makedirs(subdir, exist_ok=True)

urls = {}


def path(url):
    url = url.replace("://", "_")
    return os.path.join(subdir, re.sub("[^\w\-_\. ]", "_", url) + ".png")


for row in csv.DictReader(
    open("../brownfield-land-collection/dataset/brownfield-land.csv")
):
    url = row["documentation-url"]
    if url and not row["end-date"]:
        urls[url] = path(url)


for url in urls:
    if not os.path.exists(urls[url]):
        print(urls[url])
        # cmd = ["python", "webscreenshot.py", "-o", subdir, url]
        cmd = [
            "phantomjs",
            "--ignore-ssl-errors=true",
            "--ssl-protocol=any",
            "--ssl-ciphers=ALL",
            "webscreenshot.js",
            "url_capture=" + url,
            "output_file=" + urls[url],
            "width=1200",
            "height=800",
            "format=png",
            "quality=75",
        ]
        print(cmd)
        subprocess.call(cmd)
