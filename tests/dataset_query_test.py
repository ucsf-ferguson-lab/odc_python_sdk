from typing import Any
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from configs.env_var import import_api_key
from logic.dataset_query import get_dataset_info
from logic.shared_logic import unmarshal_json
from models.dataset_info import DatasetInfo

if __name__ == "__main__":
    api_key: str = import_api_key(dotenv_filename=".env")
    print(api_key)

    response: Any = get_dataset_info(api_key, 26)
    dataset_info: DatasetInfo = unmarshal_json(response, DatasetInfo)

    print(dataset_info.name, dataset_info.long_name, dataset_info.publications)
