from odc_sdk.configs.env_var import init_api_key, import_api_key


if __name__ == "__main__":
    init_api_key()

    api_key: str = import_api_key()
    print(api_key)
