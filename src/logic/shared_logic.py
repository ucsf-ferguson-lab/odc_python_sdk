import requests
from typing import Type, TypeVar, Any
import pandas as pd
import json

T = TypeVar("T")


# type safe, T is generic defined in models submodule
def unmarshal_json(response: requests.Response, struct_type: Type[T]) -> T | None:
    if response.status_code == 200:
        data_json: Any = response.json()
        return struct_type(**data_json)
    else:
        print(
            f"Failed to retrieve dataset information. Status code: {response.status_code}"
        )
        return None


# data dictionary endpoint returns list (not valid json)
# not type safe, pandas handle all type casting
def convert_to_df(response: requests.Response) -> pd.DataFrame:
    json_str = response.content.decode("utf-8")  # convert to valid json
    return pd.DataFrame(json.loads(json_str))
