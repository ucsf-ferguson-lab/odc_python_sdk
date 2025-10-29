import requests


# todo: 403 or 500 error
def get_user_info(api_key: str) -> requests.Response:
    full_url: str = f"https://services.scicrunch.io/odc/user/info/?api_key={api_key}"
    headers = {"accept": "application/json", "x-auth-token": api_key}
    return requests.get(full_url, headers=headers)
