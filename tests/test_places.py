import io
import json
import urllib.error

import pytest

from googlescraper import places
from googlescraper.places import Place, PlacesError


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def fake_urlopen(payload, calls=None):
    def urlopen(request, timeout):
        if calls is not None:
            calls.append(request)
        return FakeResponse(json.dumps(payload).encode("utf-8"))
    return urlopen


def test_search_places_parses_results_and_sends_key_in_header():
    calls = []
    payload = {"places": [
        {"displayName": {"text": "Shop A"}, "formattedAddress": "1 Main St"},
        {"displayName": {"text": "Shop B"}, "formattedAddress": "2 High St"},
    ]}

    result = places.search_places("nike store manila", "KEY", urlopen=fake_urlopen(payload, calls))

    assert result == [Place("Shop A", "1 Main St"), Place("Shop B", "2 High St")]
    request = calls[0]
    assert request.full_url == places.TEXT_SEARCH_URL
    assert request.get_method() == "POST"
    assert request.get_header("X-goog-api-key") == "KEY"
    assert "KEY" not in request.full_url
    assert json.loads(request.data) == {"textQuery": "nike store manila"}


def test_search_places_with_no_matches_returns_empty_list():
    assert places.search_places("zzz", "KEY", urlopen=fake_urlopen({})) == []


def test_parse_response_tolerates_missing_fields():
    assert places.parse_response({"places": [{}]}) == [Place("", "")]


def test_http_error_surfaces_google_message():
    body = json.dumps({"error": {"message": "API key expired."}}).encode()

    def urlopen(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 400, "Bad", {}, io.BytesIO(body))

    with pytest.raises(PlacesError, match="API key expired"):
        places.search_places("x", "KEY", urlopen=urlopen)


def test_network_error_becomes_places_error():
    def urlopen(request, timeout):
        raise urllib.error.URLError("no route")

    with pytest.raises(PlacesError, match="no route"):
        places.search_places("x", "KEY", urlopen=urlopen)


def test_empty_query_is_rejected():
    with pytest.raises(ValueError):
        places.search_places("  ", "KEY", urlopen=fake_urlopen({}))


def test_get_api_key_reads_environment():
    assert places.get_api_key({places.API_KEY_ENV: " abc "}) == "abc"
    with pytest.raises(PlacesError, match=places.API_KEY_ENV):
        places.get_api_key({})
