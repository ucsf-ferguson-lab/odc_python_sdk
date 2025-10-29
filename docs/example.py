from logic.stats_logic import (
    get_stats,
    user_stats,
    dataset_stats,
    lab_stats,
    download_stats,
)
from models.endpoints.public_endpoints import init_stat_endpoints
from configs.env_var import init_api_key, import_api_key

# Note: type annotations not included to keep code simple
if __name__ == "__main__":
    # Example code starts below this line
    stat_endpoints = init_stat_endpoints("https://services.scicrunch.io/odc")

    # stats endpoints
    print(user_stats(stat_endpoints))
    print(dataset_stats(stat_endpoints))
    print(lab_stats(stat_endpoints))
    print(download_stats(stat_endpoints))

    # stats endpoints (recommended for advanced users)
    print(get_stats(stat_endpoints, "labs"))

    # setup env file
    init_api_key()

    # import API key, don't need to any arguments if .env file created with init_api_key()
    api_key = import_api_key()
