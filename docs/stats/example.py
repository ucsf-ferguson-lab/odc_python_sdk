from odc_sdk.endpoints import StatEndpoints
from odc_sdk.client import StatsClient
from odc_sdk.models import stats_responses as stats_models

# example code for OOP approach (current)
if __name__ == "__main__":
    stat_endpoints = StatEndpoints.from_base_url()
    stat_client = StatsClient(stat_endpoints)

    # available methods: user_stats, download_stats, lab_stats, dataset_stats
    user_stats = stat_client.user_stats(stats_models)
    download_stats = stat_client.download_stats(stats_models)

    print(user_stats)
