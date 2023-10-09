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
    type=[
        'Bermuda',
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
    app_id='b5ec2f78-8d75-415b-825b-1520f3bb2d0d',
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
        '-cp',
        '-jar',
        './*',
    ],
    cwd='/usr/local/bin/corp',
    executable='java',
    executable_path='/usr/bin',
    labels=[
        shared.Label(
            key='<key>',
            value='becquerel',
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
    '928e88cb-3f2c-4e95-af8f-afbfe2029fce',
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
            '-cp',
            '-jar',
            './*',
        ],
        cwd='/usr/local/bin/corp',
        executable='java',
        executable_path='/usr/bin',
        labels=[
            shared.Label(
                key='<key>',
                value='Mercedes Fluorine',
            ),
        ],
        name='AccountingApp',
        process_name='accounting_app',
        type='frontend',
    ),
    app_id='a3d78ca7-d0e6-48bc-a8a0-d7f811909514',
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

