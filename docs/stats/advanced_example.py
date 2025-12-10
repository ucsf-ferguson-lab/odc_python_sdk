from odc_sdk.endpoints import StatEndpoints
from odc_sdk.client import StatsClient
from odc_sdk.models import stats_responses as stats_models

# for advanced users
if __name__ == "__main__":
    stat_endpoints = StatEndpoints.from_base_url()
    stat_client = StatsClient(stat_endpoints)

    method_names = ["user_stats", "download_stats", "lab_stats", "dataset_stats"]
    results = {}

    for name in method_names:
        method = getattr(stat_client, name)
        results[name] = method(stats_models)

    print(results["user_stats"])
    print(results["download_stats"])
