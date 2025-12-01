# ODC SDK for Python

For optimal support, I recommend using latest Python versions (3.13.x or 3.14.x at the time of writing). Prior Python versions should work but not guaranteed.

See `requirements.txt` file for all required dependencies.

## Quick start

### Stats routes

Stats endpoints don't require authentication.

After installing package, create a script called `main.py` in your project folder and paste following code inside

```python
from logic.stats_logic import *

user_statistics = user_stats()
dataset_statistics = dataset_stats()
lab_statistics = lab_stats()
download_statistics = download_stats()
```

Delete any unused lines.

#### Advanced users

For cleaner code, I recommend using `get_stats()`.

```python
from logic.stats_logic import get_stats

#single category
user_statistics = get_stats("users")

#select multiple categories
categories = ["users", "labs", "downloads"]
for category in categories:
    result = get_stats(category)
    #...
```

### Authentication required routes

After installing package, navigate to your project folder and run.

```python
from configs.env_var import init_api_key

init_api_key()
```

Enter the API key you obtained from ODC website when prompted.

By default, this creates a hidden file called `odc_sdk_generated.env` in current folder. Inspect the contents of this file by enable "show hidden files" (different for each operating system) and open in any text editor.

You should see where PLACEHOLDER is API key you entered

```odc_sdk_generated.env
ODC_API_KEY="PLACEHOLDER"
```

Create a script called `main.py` and paste following code inside

```python
from configs.env_var import import_api_key
from logic.dataset_query import get_dataset_info
from logic.shared_logic import unmarshal_json
from models.dataset.dataset_info import DatasetInfo

api_key = import_api_key()
dataset_id = DATASET_ID

dataset_info_raw = get_dataset_info(api_key,dataset_id)
dataset_info = unmarshal_json(dataset_info_raw,DatasetInfo)

#print select fields
print(dataset_info.name,dataset_info.long_name)

#print all fields
print(dataset_info)
```

View `tests` folder for more examples.

## Package structure

Submodules

- configs: setup environment variables, local setup...
- logic: core functions including wrappers
- models: custom data structures to marshal/unmarshal requests/responses (bytes to json and vice-versa)

## Design decisions

1. Reduced number of 3rd party to bare-minimum. For example, used dataclasses (included with python install) over pydantic.
1. Multiple layers of abstraction. The target audience has beginner to intermediate Python knowledge. Very likely uncomfortable with reading self-documenting code or functions with many arguments.
1. Type annotations. These are included even if target audience not required to use it. Note Python is not a type-safe language: type checks not performed at runtime. Intend to be paired with linter.
1. Convert some responses to dataframe and keeping others as json. Data originally in tabular format (tidy format, .csv files) are converted to pandas dataframe to match original representation. Other data not easily represented in tabular format are kept as json. Converting non-tabular data to tabular format is possible but not best use of limited manpower (I'm the only developer working on this package).
