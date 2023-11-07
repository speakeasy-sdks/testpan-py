# AuditLogs
(*.audit_logs*)

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
        password="",
        username="",
    ),
)

req = operations.GetAuditLogsRequest(
    actions=[
        'string',
    ],
    end_time=dateutil.parser.isoparse('2022-10-20T03:40:31.022Z'),
    start_time=dateutil.parser.isoparse('2023-03-19T00:25:31.296Z'),
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


## get_audit_logs_actions

Get all the audit logs actions

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


res = s.audit_logs.get_audit_logs_actions()

if res.strings is not None:
    # handle response
    pass
```


### Response

**[operations.GetAuditLogsActionsResponse](../../models/operations/getauditlogsactionsresponse.md)**


## get_audit_logs_kubernetes

Get audit logs

### Example Usage

```python
import dateutil.parser
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetAuditLogsKubernetesRequest(
    end_time=dateutil.parser.isoparse('2023-03-24T20:20:48.235Z'),
    kubernetes_audit_action=[
        'string',
    ],
    result=[
        operations.Result.RISKY,
    ],
    start_time=dateutil.parser.isoparse('2021-10-10T01:17:52.269Z'),
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


## get_audit_logs_kubernetes_actions

Get all the kubernetes audit logs actions

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


res = s.audit_logs.get_audit_logs_kubernetes_actions()

if res.strings is not None:
    # handle response
    pass
```


### Response

**[operations.GetAuditLogsKubernetesActionsResponse](../../models/operations/getauditlogskubernetesactionsresponse.md)**

