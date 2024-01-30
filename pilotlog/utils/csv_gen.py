import csv
import json


def generate_csv(data, response):
    json_data = json.loads(data)

    unique_meta_keys = set()
    for item in json_data:
        meta_data = item.get("meta", {})
        unique_meta_keys.update(meta_data.keys())

    writer = csv.writer(response)

    header_row = ["Table Name"] + list(unique_meta_keys)
    writer.writerow(header_row)

    for item in json_data:
        table_name = item.get("table")
        meta_data = item.get("meta", {})

        meta_values = [table_name] + [
            meta_data.get(key, "") for key in unique_meta_keys
        ]
        writer.writerow(meta_values)
