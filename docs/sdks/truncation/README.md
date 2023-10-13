# Truncation
(*truncation*)

## Overview

APIs to delete workloads

### Available Operations

* [get_truncation_images](#get_truncation_images) - Get workloads truncation time for account
* [get_truncation_workloads](#get_truncation_workloads) - Get workloads truncation time for account
* [post_truncation_images](#post_truncation_images) - Update workloads truncation status for account
* [post_truncation_workloads](#post_truncation_workloads) - Update workloads truncation status for account

## get_truncation_images

Get workloads truncation time for account

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


res = s.truncation.get_truncation_images()

if res.truncation_status is not None:
    # handle response
    pass
```


### Response

**[operations.GetTruncationImagesResponse](../../models/operations/gettruncationimagesresponse.md)**


## get_truncation_workloads

Get workloads truncation time for account

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


res = s.truncation.get_truncation_workloads()

if res.truncation_status is not None:
    # handle response
    pass
```


### Response

**[operations.GetTruncationWorkloadsResponse](../../models/operations/gettruncationworkloadsresponse.md)**


## post_truncation_images

Update workloads truncation status for account

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

req = shared.TruncationStatus(
    is_truncation_enabled=False,
    truncate_time_in_days=271429,
)

res = s.truncation.post_truncation_images(req)

if res.truncation_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.TruncationStatus](../../models/shared/truncationstatus.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostTruncationImagesResponse](../../models/operations/posttruncationimagesresponse.md)**


## post_truncation_workloads

Update workloads truncation status for account

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

req = shared.TruncationStatus(
    is_truncation_enabled=False,
    truncate_time_in_days=519889,
)

res = s.truncation.post_truncation_workloads(req)

if res.truncation_status is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.TruncationStatus](../../models/shared/truncationstatus.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.PostTruncationWorkloadsResponse](../../models/operations/posttruncationworkloadsresponse.md)**

