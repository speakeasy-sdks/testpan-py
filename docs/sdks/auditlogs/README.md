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
import pan
import dateutil.parser
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetAuditLogsRequest(
    actions=[
        'male',
    ],
    download_as_xlsx=False,
    end_time=dateutil.parser.isoparse('2022-01-24T02:40:28.078Z'),
    max_results=5619.36,
    object_type='GB grey Folding',
    offset=2262.25,
    sort_dir=operations.GetAuditLogsSortDir.DESC,
    sort_key=operations.GetAuditLogsSortKey.TIME,
    start_time=dateutil.parser.isoparse('2022-05-15T07:17:17.108Z'),
    user='Lennie.Torphy0',
)

res = s.audit_logs.get_audit_logs(req)

if res.audit_logs is not None:
    # handle response
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

if res.get_audit_logs_actions_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetAuditLogsActionsResponse](../../models/operations/getauditlogsactionsresponse.md)**


## get_audit_logs_kubernetes

Get audit logs

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.GetAuditLogsKubernetesRequest(
    cluster_name='Coupe Southeast Southeast',
    download_as_xlsx=False,
    end_time=dateutil.parser.isoparse('2022-08-15T09:50:37.531Z'),
    kubernetes_audit_action=[
        'online',
    ],
    max_results=3231.79,
    namespace_name='Cadillac',
    no_pagination=False,
    offset=5266.56,
    resource_kind='Island SSL',
    resource_name='South vaguely',
    result=[
        operations.GetAuditLogsKubernetesResult.BLOCK,
    ],
    sort_dir=operations.GetAuditLogsKubernetesSortDir.DESC,
    sort_key=operations.GetAuditLogsKubernetesSortKey.ACTION,
    start_time=dateutil.parser.isoparse('2022-02-10T19:51:08.510Z'),
    user='Rebekah66',
)

res = s.audit_logs.get_audit_logs_kubernetes(req)

if res.kubernetes_audit_logs is not None:
    # handle response
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

if res.get_audit_logs_kubernetes_actions_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetAuditLogsKubernetesActionsResponse](../../models/operations/getauditlogskubernetesactionsresponse.md)**

