"""CSV export for scrape results."""

import csv

MAP_HEADER = ["Brand", "B&M", "Address", "ContactNo"]
SEARCH_HEADER = ["Brand", "OLRetailer"]


def ensure_csv_extension(path):
    return path if path.lower().endswith(".csv") else path + ".csv"


def _write(path, header, rows):
    path = ensure_csv_extension(path)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    return path


def save_places(path, brand, places):
    """Write Google Maps results; returns the path actually written."""
    return _write(path, MAP_HEADER, [(brand, p.name, p.address, "") for p in places])


def save_domains(path, brand, domains):
    """Write Google Search domains; returns the path actually written."""
    return _write(path, SEARCH_HEADER, [(brand, d) for d in domains])
