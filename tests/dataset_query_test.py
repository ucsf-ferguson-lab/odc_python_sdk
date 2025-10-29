from typing import Any
import os
import sys
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from configs.env_var import import_api_key
from logic.dataset_query import get_dataset_info, get_data_dict
from logic.shared_logic import unmarshal_json, convert_to_df
from models.dataset.dataset_info import DatasetInfo

if __name__ == "__main__":
    api_key: str = import_api_key(dotenv_filename=".env")
    print(api_key)  # debug
    dataset_id = 1404  # chosen at random

    # dataset info
    data_info_res: Any = get_dataset_info(api_key, dataset_id)
    dataset_info: DatasetInfo = unmarshal_json(data_info_res, DatasetInfo)
    print(
        dataset_info.name, dataset_info.long_name, dataset_info.publications
    )  # print(dataset_info) for all fields

    # data dictionary
    data_dict_res: Any = get_data_dict(api_key, dataset_id)
    data_dict: pd.DataFrame = convert_to_df(data_dict_res)
    print(data_dict.head())
