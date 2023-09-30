# Vulnerabilities
(*vulnerabilities*)

### Available Operations

* [get_vulnerabilities](#get_vulnerabilities) - search for vulnerability names in the account

## get_vulnerabilities

search for vulnerability names in the account

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

req = operations.GetVulnerabilitiesRequest(
    max_results=6542.3,
    vul_name='Vivienne repudiandae Venezuela',
)

res = s.vulnerabilities.get_vulnerabilities(req)

if res.get_vulnerabilities_200_application_json_strings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetVulnerabilitiesRequest](../../models/operations/getvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetVulnerabilitiesResponse](../../models/operations/getvulnerabilitiesresponse.md)**

