import pytest

from googlescraper import web_search
from googlescraper.web_search import SearchError


@pytest.mark.parametrize("url, domain", [
    ("https://www.example.com/shoes?id=1", "example.com"),
    ("http://shop.example.co.uk/x", "example.co.uk"),
    ("https://lazada.com.ph", "lazada.com.ph"),
    ("http://localhost:8000/", "localhost"),
])
def test_extract_domain(url, domain):
    assert web_search.extract_domain(url) == domain


def test_search_urls_passes_query_and_caps_results():
    seen = []

    def fake_search(query, num_results):
        seen.append((query, num_results))
        return iter(["https://a.com", "https://b.com", "https://c.com"])

    assert web_search.search_urls("running shoes", 2, search=fake_search) == [
        "https://a.com", "https://b.com"]
    assert seen == [("running shoes", 2)]


def test_search_failure_becomes_search_error():
    def failing_search(query, num_results):
        raise RuntimeError("429 Too Many Requests")

    with pytest.raises(SearchError, match="429"):
        web_search.search_urls("x", 5, search=failing_search)


@pytest.mark.parametrize("query, n", [("", 5), ("x", 0)])
def test_invalid_arguments(query, n):
    with pytest.raises(ValueError):
        web_search.search_urls(query, n, search=lambda q, n: [])
