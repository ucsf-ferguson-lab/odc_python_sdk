from dataclasses import dataclass


@dataclass
class AuthReqEndpoints:
    user_info: str
    dataset_info: str
    dataset: str
    dataset_dict: str
    create_dataset: str
    upload_dataset: str
    delete_dataset: str
    upload_data_dictionary: str


# todo: subject to change, api key req in query param + json header
def init_auth_req_endpoints(base_url: str, dataset_id: int) -> AuthReqEndpoints:
    return AuthReqEndpoints(
        user_info=f"{base_url}/user/info",
        dataset_info=f"{base_url}/dataset/{dataset_id}/info",
        dataset=f"{base_url}/dataset/{dataset_id}/",
        dataset_dict=f"{base_url}/dataset/dict/{dataset_id}/",
        create_dataset=f"{base_url}/dataset/create",
        upload_dataset=f"{base_url}/dataset/upload",
        delete_dataset=f"{base_url}/dataset/delete",
        upload_data_dictionary=f"{base_url}/dataset/{dataset_id}/upload_data_dictionary",
    )
