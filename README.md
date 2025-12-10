# ODC SDK, Python version

Software Development Kit (SDK) to work with ODC platform. https://services.scicrunch.io/odc/docs

Note: package name is `odc_sdk`

## Install

Production

```shell
python3 -m pip install git+https://github.com/ucsf-ferguson-lab/odc_python_sdk
```

Note: Unix systems might require `--break-system-packages` flag

```shell
python3 -m pip install git+https://github.com/ucsf-ferguson-lab/odc_python_sdk --break-system-packages
```

Dev

```shell
python3 -m pip install git+https://github.com/ucsf-ferguson-lab/odc_python_sdk.git@dev
```

### Uninstall

```shell
python3 -m pip uninstall odc_sdk
```

## Quick start

See code examples in `/docs`. Code below copied from `/docs/stats/example.py`.

```python
from odc_sdk.endpoints import StatEndpoints
from odc_sdk.client import StatsClient
from odc_sdk.models import stats_responses as stats_models

if __name__ == "__main__":
    stat_endpoints = StatEndpoints.from_base_url()
    stat_client = StatsClient(stat_endpoints)

    # available methods: user_stats, download_stats, lab_stats, dataset_stats
    user_stats = stat_client.user_stats(stats_models)

    print(user_stats)
```
