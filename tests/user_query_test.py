from typing import Any
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from configs.env_var import import_api_key
from logic.user_logic import get_user_info

if __name__ == "__main__":
    api_key: str = import_api_key(dotenv_filename=".env")
    print(api_key)

    response: Any = get_user_info(api_key)
    print(response, response.content)
