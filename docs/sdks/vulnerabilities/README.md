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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetVulnerabilitiesRequest()

res = s.vulnerabilities.get_vulnerabilities(req)

if res.strings is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetVulnerabilitiesRequest](../../models/operations/getvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetVulnerabilitiesResponse](../../models/operations/getvulnerabilitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
