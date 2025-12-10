import pytest
from odc_sdk.endpoints import StatEndpoints


# default
def test_from_base_url_default():
    endpoints = StatEndpoints.from_base_url()

    assert isinstance(endpoints, StatEndpoints)
    assert (
        endpoints.datasets_stats == "https://services.scicrunch.io/odc/stats/datasets"
    )
    assert endpoints.users_stats == "https://services.scicrunch.io/odc/stats/users"
    assert endpoints.labs_stats == "https://services.scicrunch.io/odc/stats/labs"
    assert (
        endpoints.downloads_stats == "https://services.scicrunch.io/odc/stats/downloads"
    )


# overwrite routes directly
def test_direct_initialization():
    endpoints = StatEndpoints(
        datasets_stats="https://example.com/stats/datasets",
        users_stats="https://example.com/stats/users",
        labs_stats="https://example.com/stats/labs",
        downloads_stats="https://example.com/stats/downloads",
    )

    assert endpoints.datasets_stats.endswith("/stats/datasets")
    assert endpoints.users_stats.endswith("/stats/users")
    assert endpoints.labs_stats.endswith("/stats/labs")
    assert endpoints.downloads_stats.endswith("/stats/downloads")


# overwrite base route
@pytest.mark.parametrize("base_url", ["https://api.server", "http://localhost:8080"])
def test_from_base_url_custom(base_url):
    endpoints = StatEndpoints.from_base_url(base_url)

    assert endpoints.datasets_stats == f"{base_url}/stats/datasets"
    assert endpoints.users_stats == f"{base_url}/stats/users"
    assert endpoints.labs_stats == f"{base_url}/stats/labs"
    assert endpoints.downloads_stats == f"{base_url}/stats/downloads"


# show field names for debugging
def test_repr_contains_field_names():
    endpoints = StatEndpoints.from_base_url("https://api.service")
    text = repr(endpoints)
    for attr in ["datasets_stats", "users_stats", "labs_stats", "downloads_stats"]:
        assert attr in text
