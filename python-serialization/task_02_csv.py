#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        # Read data from CSV file
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize data to JSON and write to data.json
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
