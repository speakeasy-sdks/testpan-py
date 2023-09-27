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
        'blanditiis',
    ],
    max_results=5112.03,
    no_pagination=False,
    offset=9152.67,
)

res = s.k8s_cis_benchmark.get_k8s_cis_benchmark(req)

if res.k8s_cis_benchmark_clusters_summaries is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetK8sCISBenchmarkRequest](../../models/operations/getk8scisbenchmarkrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetK8sCISBenchmarkResponse](../../models/operations/getk8scisbenchmarkresponse.md)**


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
```


### Response

**[operations.GetK8sCISBenchmarkSummaryResponse](../../models/operations/getk8scisbenchmarksummaryresponse.md)**


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
    cluster_id='c66183bf-e965-49eb-80ec-16faf75b0b53',
)

res = s.k8s_cis_benchmark.get_k8s_cis_benchmark_cluster_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetK8sCISBenchmarkClusterIDRequest](../../models/operations/getk8scisbenchmarkclusteridrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetK8sCISBenchmarkClusterIDResponse](../../models/operations/getk8scisbenchmarkclusteridresponse.md)**


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
    cluster_id='2a4da37c-baaf-4445-ac48-42c9b2ad32da',
)

res = s.k8s_cis_benchmark.post_k8s_cis_benchmark_cluster_id_(req)

if res.k8s_cis_benchmark_clusters_summary is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostK8sCISBenchmarkClusterIDRequest](../../models/operations/postk8scisbenchmarkclusteridrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostK8sCISBenchmarkClusterIDResponse](../../models/operations/postk8scisbenchmarkclusteridresponse.md)**


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
        cluster_id='fe81a88f-4444-4573-becd-47353f63c820',
        index='natus',
        nodes=[
            shared.K8sCISBenchmarkUpdateNode(
                id='379aa69c-d5fb-4cf7-9da1-8a7822bf9589',
            ),
        ],
        status=shared.K8sCISBenchmarkUpdateNodeStatus.FAIL,
    ),
    cluster_id='e6861adb-55f9-4e5d-b51c-9fe8f7502bfd',
)

res = s.k8s_cis_benchmark.put_k8s_cis_benchmark_cluster_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutK8sCISBenchmarkClusterIDRequest](../../models/operations/putk8scisbenchmarkclusteridrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutK8sCISBenchmarkClusterIDResponse](../../models/operations/putk8scisbenchmarkclusteridresponse.md)**

