import pandas as pd

from Dev.public_endpoints import init_stat_endpoints
from odc_sdk.logic.stats_logic import get_stats

# example code for functional approach (deprecated)
if __name__ == "__main__":
    stat_endpoints = init_stat_endpoints()

    to_download = ["users", "datasets", "labs", "downloads"]
    for item in to_download:
        temp_df = pd.DataFrame(get_stats(stat_endpoints, item))
        temp_df.to_csv(f"./data/{item}.csv")
