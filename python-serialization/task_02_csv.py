#!/usr/bin/env python3
"""Convert CSV data to JSON using serialization."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to data.json."""
    try:
        data = []
        with open(csv_filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except Exception:
        return False
