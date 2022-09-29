#!/usr/bin/python3

import csv
import gzip
import json
import os
import subprocess
import time

try:
    os.mkdir("ltn_proposals")
except FileExistsError:
    pass

# This'll only work for Dustin or anyone with read permission on the GCS bucket
subprocess.run(
    [
        "gsutil",
        "-m",
        "rsync",
        "gs://aorta-routes.appspot.com/ltn_proposals",
        "ltn_proposals",
    ]
)

with open("summary.csv", "w") as out:
    writer = csv.DictWriter(
        out,
        fieldnames=[
            "datetime_nice",
            # Easier to sort
            "datetime_raw",
            "map_name",
            "proposal_name",
            "url",
            "road_edits",
            "intersection_edits",
            "one_way_edits",
        ],
    )
    writer.writeheader()

    for filename in os.listdir("ltn_proposals"):
        print(f"Reading {filename}")
        path = os.path.join("ltn_proposals", filename)
        # Each proposal file is a gzipped JSON file
        doc = json.load(gzip.open(path))
        map_name = "/".join(
            [
                doc["map"]["city"]["country"],
                doc["map"]["city"]["city"],
                doc["map"]["map"],
            ]
        )

        creation_time = os.path.getmtime(path)
        writer.writerow(
            {
                "datetime_nice": time.ctime(creation_time),
                "datetime_raw": creation_time,
                "map_name": map_name,
                "proposal_name": doc["name"],
                "url": f"http://play.abstreet.org/0.3.33/ltn.html?system/{map_name}.bin&--proposal=remote/{filename}",
                "road_edits": len(doc["edits"]["roads"]),
                "intersection_edits": len(doc["edits"]["intersections"]),
                "one_way_edits": len(doc["edits"]["one_ways"]),
            }
        )
