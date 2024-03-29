# AuditLogs
(*audit_logs*)

## Overview

APIs used to retrieve  audit logs

### Available Operations

* [get_audit_logs](#get_audit_logs) - Get audit logs
* [get_audit_logs_actions](#get_audit_logs_actions) - Get all the audit logs actions
* [get_audit_logs_kubernetes](#get_audit_logs_kubernetes) - Get audit logs
* [get_audit_logs_kubernetes_actions](#get_audit_logs_kubernetes_actions) - Get all the kubernetes audit logs actions

## get_audit_logs

Get audit logs

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAuditLogsRequest(
    end_time=dateutil.parser.isoparse('2023-10-20T18:04:43.105Z'),
    start_time=dateutil.parser.isoparse('2024-03-18T18:06:48.311Z'),
)

res = s.audit_logs.get_audit_logs(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetAuditLogsRequest](../../models/operations/getauditlogsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetAuditLogsResponse](../../models/operations/getauditlogsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_audit_logs_actions

Get all the audit logs actions

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.audit_logs.get_audit_logs_actions()

if res.strings is not None:
    # handle response
    pass

```


### Response

**[operations.GetAuditLogsActionsResponse](../../models/operations/getauditlogsactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_audit_logs_kubernetes

Get audit logs

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAuditLogsKubernetesRequest(
    end_time=dateutil.parser.isoparse('2024-03-24T14:09:45.265Z'),
    start_time=dateutil.parser.isoparse('2024-07-09T23:49:40.165Z'),
)

res = s.audit_logs.get_audit_logs_kubernetes(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetAuditLogsKubernetesRequest](../../models/operations/getauditlogskubernetesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetAuditLogsKubernetesResponse](../../models/operations/getauditlogskubernetesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_audit_logs_kubernetes_actions

Get all the kubernetes audit logs actions

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.audit_logs.get_audit_logs_kubernetes_actions()

if res.strings is not None:
    # handle response
    pass

```


### Response

**[operations.GetAuditLogsKubernetesActionsResponse](../../models/operations/getauditlogskubernetesactionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
