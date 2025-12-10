import requests
import pandas as pd
import json
from typing import Type, TypeVar, Any

T = TypeVar("T")


class RequestHandler:
    """Http requests"""

    @staticmethod
    def get_response(url: str) -> requests.Response:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
        return response

    @staticmethod
    def unmarshal_json(response: requests.Response, struct_type: Type[T]) -> T | None:
        if response.status_code == 200:
            data_json: Any = response.json()
            return struct_type(**data_json)
        return None

    @staticmethod
    def convert_to_df(response: requests.Response) -> pd.DataFrame:
        """Convert List[Any] to pandas dataframe"""
        json_str = response.content.decode("utf-8")
        return pd.DataFrame(json.loads(json_str))
