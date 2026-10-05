import csv

import pytest

from googlescraper import gui
from googlescraper.places import Place, PlacesError
from googlescraper.web_search import SearchError


@pytest.fixture(autouse=True)
def popups(monkeypatch):
    """Record message boxes instead of blocking on them."""
    shown = []
    monkeypatch.setattr(gui, "_warn", lambda title, text: shown.append((title, text)))
    return shown


def make_map_tab(qtbot, search):
    tab = gui.MapTab(search_places=search, get_api_key=lambda: "KEY")
    qtbot.addWidget(tab)
    return tab


def test_main_window_builds(qtbot):
    window = gui.MainWindow()
    qtbot.addWidget(window)
    assert window.windowTitle() == "Google Scraper"


def test_map_tab_requires_query_and_brand(qtbot, popups):
    calls = []
    tab = make_map_tab(qtbot, lambda q, k: calls.append(q) or [])

    tab.load()
    tab.query.setText("nike store")
    tab.load()

    assert [t for _, t in popups] == ["Please make sure the search box is filled.", "Type in the brand."]
    assert calls == []
    assert not tab.btn_save.isEnabled()


def test_map_tab_load_and_save(qtbot, tmp_path):
    tab = make_map_tab(qtbot, lambda q, k: [Place("Shop A", "1 Main St")])
    tab.query.setText("nike store")
    tab.brand.setText("Nike")

    tab.load()

    assert tab.output.toPlainText() == "Shop A | 1 Main St"
    assert tab.total.text() == "1"
    assert tab.btn_save.isEnabled()

    tab.save(str(tmp_path / "out"))
    with open(tmp_path / "out.csv", newline="") as f:
        assert list(csv.reader(f))[1] == ["Nike", "Shop A", "1 Main St", ""]


def test_map_tab_shows_api_errors(qtbot, popups):
    def failing(q, k):
        raise PlacesError("Places API error: API key expired.")

    tab = make_map_tab(qtbot, failing)
    tab.query.setText("x")
    tab.brand.setText("y")
    tab.load()

    assert popups == [("Google Maps", "Places API error: API key expired.")]
    assert not tab.btn_save.isEnabled()


def test_search_tab_load_clear(qtbot):
    tab = gui.SearchTab(search_urls=lambda q, n: ["https://www.a.com/x", "https://shop.b.co.uk"][:n])
    qtbot.addWidget(tab)
    tab.query.setText("running shoes")
    tab.brand.setText("Nike")
    tab.count.setValue(2)

    tab.load()

    assert tab.raw.toPlainText() == "https://www.a.com/x\nhttps://shop.b.co.uk"
    assert tab.domains == ["a.com", "b.co.uk"]
    assert tab.total.text() == "2"
    assert tab.btn_save.isEnabled()

    tab.clear()
    assert tab.domains == [] and tab.total.text() == "0" and not tab.btn_save.isEnabled()


def test_search_tab_shows_scrape_errors(qtbot, popups):
    def failing(q, n):
        raise SearchError("Google Search failed: 429")

    tab = gui.SearchTab(search_urls=failing)
    qtbot.addWidget(tab)
    tab.query.setText("x")
    tab.brand.setText("y")
    tab.load()

    assert popups == [("Google Search", "Google Search failed: 429")]
