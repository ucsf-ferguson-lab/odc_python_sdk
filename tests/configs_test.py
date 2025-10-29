import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from configs.env_var import init_api_key, import_api_key


if __name__ == "__main__":
    init_api_key()

    api_key: str = import_api_key()
    print(api_key)
