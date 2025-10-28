import requests
from typing import Type, TypeVar, Any

T = TypeVar("T")


def unmarshal_json(response: requests.Response, struct_type: Type[T]) -> T | None:
    if response.status_code == 200:
        data_json: Any = response.json()
        return struct_type(**data_json)
    else:
        print(
            f"Failed to retrieve dataset information. Status code: {response.status_code}"
        )
        return None
