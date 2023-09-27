# Apps
(*apps*)

## Overview

APIs used to define apps

### Available Operations

* [get_apps](#get_apps) - Returns a list of defined Apps
* [get_apps_app_id_](#get_apps_app_id_) - Returns an App by its ID
* [post_apps](#post_apps) - Define a New App
* [post_apps_delete](#post_apps_delete) - Delete several Apps
* [put_apps_app_id_](#put_apps_app_id_) - Edit the existing App

## get_apps

Returns a list of defined Apps

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetAppsRequest(
    download_as_xlsx=False,
    name='Roger O'Connell',
    no_pagination=False,
    sort_dir=operations.GetAppsSortDir.ASC,
    sort_key=operations.GetAppsSortKey.NAME,
    type=[
        'facere',
    ],
)

res = s.apps.get_apps(req)

if res.apps is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetAppsRequest](../../models/operations/getappsrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetAppsResponse](../../models/operations/getappsresponse.md)**


## get_apps_app_id_

Returns an App by its ID

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetAppsAppIDRequest(
    app_id='ec001ac8-02e2-4ec0-9ff8-f0f816ff3477',
)

res = s.apps.get_apps_app_id_(req)

if res.app is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetAppsAppIDRequest](../../models/operations/getappsappidrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetAppsAppIDResponse](../../models/operations/getappsappidresponse.md)**


## post_apps

Define a New App

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.App(
    args=[
        'eligendi',
    ],
    cwd='/usr/local/bin/corp',
    executable='java',
    executable_path='/usr/bin',
    id='13e902c1-4125-4b09-a0a6-68151a472af9',
    labels=[
        shared.Label(
            key='sed',
            value='nesciunt',
        ),
    ],
    name='AccountingApp',
    process_name='accounting_app',
    type='frontend',
)

res = s.apps.post_apps(req)

if res.app is not None:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [shared.App](../../models/shared/app.md)   | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostAppsResponse](../../models/operations/postappsresponse.md)**


## post_apps_delete

Delete several apps.


### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = [
    'c5949f83-f350-4cf8-b6ff-b901c6ecbb4e',
]

res = s.apps.post_apps_delete(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [list[str]](../../models//.md)             | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PostAppsDeleteResponse](../../models/operations/postappsdeleteresponse.md)**


## put_apps_app_id_

Edit the existing App

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.PutAppsAppIDRequest(
    app=shared.App(
        args=[
            'fugit',
        ],
        cwd='/usr/local/bin/corp',
        executable='java',
        executable_path='/usr/bin',
        id='43cf789f-fafe-4da5-be5a-e6e0ac184c2b',
        labels=[
            shared.Label(
                key='natus',
                value='minus',
            ),
        ],
        name='AccountingApp',
        process_name='accounting_app',
        type='frontend',
    ),
    app_id='247c8837-3a40-4e19-82f3-2e55055756f5',
)

res = s.apps.put_apps_app_id_(req)

if res.app is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PutAppsAppIDRequest](../../models/operations/putappsappidrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PutAppsAppIDResponse](../../models/operations/putappsappidresponse.md)**

