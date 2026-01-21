from typing import List, Type, Any
from .request_handler import RequestHandler
from .endpoints import StatEndpoints


class StatsClient:
    """
    Client to handle all public stats endpoints
    available methods: user_stats, dataset_stats, lab_stats, download_stats
    """

    def __init__(self, endpoints: StatEndpoints):
        self.endpoints = endpoints
        self.handler = RequestHandler()

    def _fetch_stats(
        self,
        endpoint: str,
        response_type: Type[Any],
        retries: int = 3,
        delay: int = 10,
    ) -> List[Any]:
        """Generic fetch helper to retrieve stats and return as list"""
        response = self.handler.get_response(endpoint, retries=retries, delay=delay)
        if response.status_code == 200:
            data = response.json()
            return [response_type(**item) for item in data]

        print(f"Status code {response.status_code} received for {endpoint}")
        return []

    def get_stats(
        self,
        stat_type: str,
        models_module,
        retries: int = 3,
        delay: int = 10,
    ) -> List[Any]:
        """Retrieve stats by name"""
        mapping = {
            "users": (self.endpoints.users_stats, models_module.UserStat),
            "datasets": (self.endpoints.datasets_stats, models_module.DatasetStat),
            "labs": (self.endpoints.labs_stats, models_module.LabStat),
            "downloads": (self.endpoints.downloads_stats, models_module.DownloadStat),
        }

        if stat_type not in mapping:
            raise ValueError(f"Unknown stat type: {stat_type}")

        endpoint, model_cls = mapping[stat_type]
        return self._fetch_stats(endpoint, model_cls, retries=retries, delay=delay)

    # wrappers
    def user_stats(self, models_module, retries: int = 3, delay: int = 10) -> List[Any]:
        return self.get_stats("users", models_module, retries=retries, delay=delay)

    def dataset_stats(
        self, models_module, retries: int = 3, delay: int = 10
    ) -> List[Any]:
        return self.get_stats("datasets", models_module, retries=retries, delay=delay)

    def lab_stats(self, models_module, retries: int = 3, delay: int = 10) -> List[Any]:
        return self.get_stats("labs", models_module, retries=retries, delay=delay)

    def download_stats(
        self, models_module, retries: int = 3, delay: int = 10
    ) -> List[Any]:
        return self.get_stats("downloads", models_module, retries=retries, delay=delay)
