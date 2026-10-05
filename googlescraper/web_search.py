"""Find online retailers for a keyword by scraping Google Search results."""

import tldextract


class SearchError(Exception):
    """Raised when Google Search can't be scraped."""


# Use the public suffix list bundled with tldextract instead of downloading it at runtime.
_extract = tldextract.TLDExtract(suffix_list_urls=())


def extract_domain(url):
    """Return the registered domain of a URL, e.g. 'shop.example.co.uk/x' -> 'example.co.uk'."""
    parts = _extract(url)
    return parts.top_domain_under_public_suffix or parts.domain


def _default_search(query, num_results):
    # Imported lazily so the rest of the app (and the tests) work without it.
    from googlesearch import search
    return search(query, num_results=num_results, lang="en", sleep_interval=2)


def search_urls(query, num_results, search=_default_search):
    """Return up to num_results result URLs for a Google Search query."""
    if not query.strip():
        raise ValueError("query must not be empty")
    if num_results < 1:
        raise ValueError("num_results must be at least 1")
    try:
        return list(search(query, num_results))[:num_results]
    except Exception as e:  # the scraper library raises bare requests/HTTP errors
        raise SearchError(f"Google Search failed: {e}") from e
