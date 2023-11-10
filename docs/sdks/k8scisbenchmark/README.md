# K8sCisBenchmark
(*k8s_cis_benchmark*)

## Overview

APIs to get the kubernetes cis benchmark data

### Available Operations

* [get_k8s_cis_benchmark](#get_k8s_cis_benchmark) - Get k8s cis benchmark for clusters
* [get_k8s_cis_benchmark_summary](#get_k8s_cis_benchmark_summary) - Get k8s cis benchmark summary of account
* [get_k8s_cis_benchmark_cluster_id_](#get_k8s_cis_benchmark_cluster_id_) - Get k8s cis benchmark for a specific cluster
* [post_k8s_cis_benchmark_cluster_id_](#post_k8s_cis_benchmark_cluster_id_) - initiate k8s cis benchmark scan for a specific cluster
* [put_k8s_cis_benchmark_cluster_id_](#put_k8s_cis_benchmark_cluster_id_) - edit k8s cis benchmark for a specific cluster with test statuses

## get_k8s_cis_benchmark

Get k8s cis benchmark for clusters

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

req = operations.GetK8sCISBenchmarkRequest(
    cluster_ids=[
        'string',
    ],
)

res = s.k8s_cis_benchmark.get_k8s_cis_benchmark(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetK8sCISBenchmarkRequest](../../models/operations/getk8scisbenchmarkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetK8sCISBenchmarkResponse](../../models/operations/getk8scisbenchmarkresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_k8s_cis_benchmark_summary

Get k8s cis benchmark summary of account

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


res = s.k8s_cis_benchmark.get_k8s_cis_benchmark_summary()

if res.k8s_cis_benchmark_account_summary is not None:
    # handle response
    pass
```


### Response

**[operations.GetK8sCISBenchmarkSummaryResponse](../../models/operations/getk8scisbenchmarksummaryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_k8s_cis_benchmark_cluster_id_

Get k8s cis benchmark for a specific cluster

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

req = operations.GetK8sCISBenchmarkClusterIDRequest(
    cluster_id='22b6e2e3-3165-4cce-b4e8-bc9db9f52c45',
)

res = s.k8s_cis_benchmark.get_k8s_cis_benchmark_cluster_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetK8sCISBenchmarkClusterIDRequest](../../models/operations/getk8scisbenchmarkclusteridrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetK8sCISBenchmarkClusterIDResponse](../../models/operations/getk8scisbenchmarkclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_k8s_cis_benchmark_cluster_id_

initiate k8s cis benchmark scan for a specific cluster

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

req = operations.PostK8sCISBenchmarkClusterIDRequest(
    cluster_id='35b87c47-9c94-446b-bd9d-9edabb3c15c6',
)

res = s.k8s_cis_benchmark.post_k8s_cis_benchmark_cluster_id_(req)

if res.k8s_cis_benchmark_clusters_summary is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostK8sCISBenchmarkClusterIDRequest](../../models/operations/postk8scisbenchmarkclusteridrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostK8sCISBenchmarkClusterIDResponse](../../models/operations/postk8scisbenchmarkclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_k8s_cis_benchmark_cluster_id_

edit k8s cis benchmark for a specific cluster with test statuses

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

req = operations.PutK8sCISBenchmarkClusterIDRequest(
    k8s_cis_benchmark_update_nodes=shared.K8sCISBenchmarkUpdateNodes(
        cluster_id='49b403e0-ddc8-4f07-8f6d-7b4806fe4a7b',
        index='string',
        nodes=[
            shared.K8sCISBenchmarkUpdateNode(),
        ],
        status=shared.K8sCISBenchmarkUpdateNodeStatus.PASS,
    ),
    cluster_id='e3c739e9-05f1-44c9-b8f5-5f4602b586f1',
)

res = s.k8s_cis_benchmark.put_k8s_cis_benchmark_cluster_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutK8sCISBenchmarkClusterIDRequest](../../models/operations/putk8scisbenchmarkclusteridrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutK8sCISBenchmarkClusterIDResponse](../../models/operations/putk8scisbenchmarkclusteridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
