import csv

from googlescraper import export
from googlescraper.places import Place


def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def test_ensure_csv_extension_does_not_double_it():
    assert export.ensure_csv_extension("out") == "out.csv"
    assert export.ensure_csv_extension("out.csv") == "out.csv"
    assert export.ensure_csv_extension("OUT.CSV") == "OUT.CSV"


def test_save_places(tmp_path):
    path = export.save_places(str(tmp_path / "maps"), "Nike",
                              [Place("Shop, Inc", "1 Main St"), Place("Café", "Quezon City")])

    assert path.endswith("maps.csv")
    assert read_rows(path) == [
        ["Brand", "B&M", "Address", "ContactNo"],
        ["Nike", "Shop, Inc", "1 Main St", ""],
        ["Nike", "Café", "Quezon City", ""],
    ]


def test_save_domains(tmp_path):
    path = export.save_domains(str(tmp_path / "search.csv"), "Nike", ["a.com", "b.ph"])

    assert path == str(tmp_path / "search.csv")
    assert read_rows(path) == [["Brand", "OLRetailer"], ["Nike", "a.com"], ["Nike", "b.ph"]]
