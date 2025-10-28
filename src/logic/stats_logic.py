from typing import List, Type, TypeVar
import requests

from models.endpoints.public_endpoints import StatEndpoints
from models.stats.stats_responses import UserStat, DatasetStat, LabStat, DownloadStat


T = TypeVar("T")  # create generic for stats_wrapper


# see models.stats.stats_responses for available types
# Note: types in python are only a suggestion
def stats_wrapper(endpoint: str, response_type: Type[T]) -> List[T]:
    response = requests.get(endpoint)
    if response.status_code == 200:
        data: T = response.json()
        return [response_type(**item) for item in data]
    else:
        print(f"Status code {response.status_code} received")
        return []


# simplify repeated code with hashmap (recommended)
def get_stats(stat_endpoints, stat_type: str):
    mapping = {
        "users": (stat_endpoints.users_stats, UserStat),
        "datasets": (stat_endpoints.datasets_stats, DatasetStat),
        "labs": (stat_endpoints.labs_stats, LabStat),
        "downloads": (stat_endpoints.downloads_stats, DownloadStat),
    }

    if stat_type not in mapping:
        raise ValueError(f"Unknown stat type: {stat_type}")

    endpoint, response_cls = mapping[stat_type]
    return stats_wrapper(endpoint, response_cls)


# alternative (for intended audience)
def user_stats(stat_endpoints: StatEndpoints) -> List[UserStat]:
    return stats_wrapper(stat_endpoints.users_stats, UserStat)


def dataset_stats(stat_endpoints: StatEndpoints) -> List[DatasetStat]:
    return stats_wrapper(stat_endpoints.datasets_stats, DatasetStat)


def lab_stats(stat_endpoints: StatEndpoints) -> List[LabStat]:
    return stats_wrapper(stat_endpoints.labs_stats, LabStat)


def download_stats(stat_endpoints: StatEndpoints) -> List[DownloadStat]:
    return stats_wrapper(stat_endpoints.downloads_stats, DownloadStat)
