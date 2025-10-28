from dataclasses import dataclass


# stats endpoints don't require auth
@dataclass
class StatEndpoints:
    datasets_stats: str
    users_stats: str
    labs_stats: str
    downloads_stats: str


def init_stat_endpoints(base_url: str) -> StatEndpoints:
    return StatEndpoints(
        datasets_stats=f"{base_url}/stats/datasets",
        users_stats=f"{base_url}/stats/users",
        labs_stats=f"{base_url}/stats/labs",
        downloads_stats=f"{base_url}/stats/downloads",
    )
