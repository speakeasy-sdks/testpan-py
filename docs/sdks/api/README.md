# API
(*api*)

## Overview

APIs to get the Secure Application API specification file

### Available Operations

* [get_api](#get_api) - Get Secure Application API as a Swagger file

## get_api

Get Secure Application API as a Swagger file

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


res = s.api.get_api()

if res.get_api_200_application_json_string is not None:
    # handle response
```


### Response

**[operations.GetAPIResponse](../../models/operations/getapiresponse.md)**
