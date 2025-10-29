import requests


# todo: extract more shared logic
def get_dataset_info(api_key: str, datasetid: int) -> requests.Response:
    full_url: str = (
        f"https://services.scicrunch.io/odc/dataset/{datasetid}/info/?api_key={api_key}"
    )
    headers = {"accept": "application/json", "x-auth-token": api_key}
    return requests.get(full_url, headers=headers)


# todo: 403 or 500 error
def get_dataset(api_key: str, datasetid: int) -> requests.Response:
    full_url: str = (
        f"https://services.scicrunch.io/odc/dataset/{datasetid}/?api_key={api_key}"
    )
    headers = {"accept": "application/json", "x-auth-token": api_key}
    return requests.get(full_url, headers=headers)


def get_data_dict(api_key: str, datasetid: int) -> requests.Response:
    full_url: str = f"https://services.scicrunch.io/odc/dataset/{datasetid}/data-dictionary/?api_key={api_key}"
    headers = {"accept": "application/json", "x-auth-token": api_key}
    return requests.get(full_url, headers=headers)
