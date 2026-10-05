# googleScraper
A school project

![image](https://user-images.githubusercontent.com/32888004/48517409-1d288500-e8cb-11e8-92e7-b4a8d248856f.png)

A small PyQt5 app with two tabs:

- **Google Map** looks up brick-and-mortar retailers for a search (e.g. `nike store manila`) with the Google Places API and saves them as CSV (`Brand, B&M, Address, ContactNo`).
- **Google Search** collects the result URLs for a keyword, reduces them to domains, and saves them as CSV (`Brand, OLRetailer`).

## Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The Google Map tab needs a Google Maps API key with **Places API (New)** enabled:

```sh
export GOOGLE_MAPS_API_KEY=your-key
```

## Run

```sh
python -m googlescraper   # or: python scraperv3.py
```

The Google Search tab scrapes google.com through `googlesearch-python`. Google may rate-limit or block it; when that happens the app shows the error instead of crashing.

## Tests

```sh
pip install -r requirements-dev.txt
pytest
```

The tests never touch the network: the Places API and Google Search are replaced with fakes.

## Layout

| Module | What it does |
| --- | --- |
| `googlescraper/places.py` | Places API (New) text search |
| `googlescraper/web_search.py` | Google Search scraping and domain extraction |
| `googlescraper/export.py` | CSV export |
| `googlescraper/gui.py` | The PyQt5 window |
