"""Look up brick-and-mortar retailers with the Google Places API (New)."""

import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass

TEXT_SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"
FIELD_MASK = "places.displayName,places.formattedAddress"
API_KEY_ENV = "GOOGLE_MAPS_API_KEY"


class PlacesError(Exception):
    """Raised when the Places API can't be reached or rejects the request."""


@dataclass(frozen=True)
class Place:
    name: str
    address: str


def get_api_key(environ=os.environ):
    key = environ.get(API_KEY_ENV, "").strip()
    if not key:
        raise PlacesError(
            f"Set the {API_KEY_ENV} environment variable to a Google Maps API key "
            "with the Places API (New) enabled.")
    return key


def build_request(query, api_key):
    body = json.dumps({"textQuery": query}).encode("utf-8")
    return urllib.request.Request(
        TEXT_SEARCH_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": FIELD_MASK,
        },
    )


def parse_response(payload):
    """Turn a searchText JSON payload into a list of Place."""
    places = []
    for item in payload.get("places", []):
        name = item.get("displayName", {}).get("text", "")
        places.append(Place(name=name, address=item.get("formattedAddress", "")))
    return places


def _error_message(http_error):
    try:
        payload = json.loads(http_error.read().decode("utf-8"))
        return payload["error"]["message"]
    except (ValueError, KeyError, TypeError):
        return f"HTTP {http_error.code}"


def search_places(query, api_key, urlopen=urllib.request.urlopen, timeout=30):
    """Return the places Google Maps finds for a free-text query."""
    if not query.strip():
        raise ValueError("query must not be empty")
    try:
        with urlopen(build_request(query, api_key), timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise PlacesError(f"Places API error: {_error_message(e)}") from e
    except urllib.error.URLError as e:
        raise PlacesError(f"Could not reach the Places API: {e.reason}") from e
    return parse_response(payload)
