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
        'quibusdam',
    ],
    download_as_xlsx=False,
    end_time=dateutil.parser.isoparse('2022-08-14T06:59:07.022Z'),
    max_results=8664.59,
    object_type='sit',
    offset=6947.28,
    sort_dir=operations.GetAuditLogsSortDir.DESC,
    sort_key=operations.GetAuditLogsSortKey.TIME,
    start_time=dateutil.parser.isoparse('2021-01-31T13:17:13.329Z'),
    user='sed',
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
    cluster_name='possimus',
    download_as_xlsx=False,
    end_time=dateutil.parser.isoparse('2020-03-28T10:33:13.519Z'),
    kubernetes_audit_action=[
        'architecto',
    ],
    max_results=2406.96,
    namespace_name='pariatur',
    no_pagination=False,
    offset=6884.63,
    resource_kind='dolore',
    resource_name='voluptatibus',
    result=[
        operations.GetAuditLogsKubernetesResult.DETECT,
    ],
    sort_dir=operations.GetAuditLogsKubernetesSortDir.ASC,
    sort_key=operations.GetAuditLogsKubernetesSortKey.USER,
    start_time=dateutil.parser.isoparse('2021-08-24T10:03:12.351Z'),
    user='velit',
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

