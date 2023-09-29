# Performance
(*performance*)

### Available Operations

* [get_api_security_api_catalog_id_hit_count_graph](#get_api_security_api_catalog_id_hit_count_graph) - Get hit count for specific spec path
* [get_performance_metrics](#get_performance_metrics) - Get performance metrics for a connection between workloads

## get_api_security_api_catalog_id_hit_count_graph

Get hit count for specific spec path

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

req = operations.GetAPISecurityAPICatalogIDHitCountGraphRequest(
    catalog_id='6b535753-b47a-42be-a003-f45375c0bae8',
    hours_interval=654607,
    spec_path='network',
    spec_path_method=operations.GetAPISecurityAPICatalogIDHitCountGraphSpecPathMethod.POST,
)

res = s.performance.get_api_security_api_catalog_id_hit_count_graph(req)

if res.api_service_spec_path_hit_count_graph is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetAPISecurityAPICatalogIDHitCountGraphRequest](../../models/operations/getapisecurityapicatalogidhitcountgraphrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetAPISecurityAPICatalogIDHitCountGraphResponse](../../models/operations/getapisecurityapicatalogidhitcountgraphresponse.md)**


## get_performance_metrics

Get performance metrics for a connection between workloads

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

req = operations.GetPerformanceMetricsRequest(
    end_time=dateutil.parser.isoparse('2023-06-20T17:24:08.589Z'),
    protocol='Account',
    source_namespace='b8ead185-971d-4112-a105-9b89d3b7dcd1',
    source_pod_template='b894b8a5-ad8e-4111-86dd-d9453d845e92',
    start_time=dateutil.parser.isoparse('2023-11-21T23:20:37.062Z'),
    target_namespace='a04569a7-7dda-4601-a8cf-6d7999aa93b9',
    target_pod_template='be30176b-a06c-4558-9ceb-c600c70dc9c6',
)

res = s.performance.get_performance_metrics(req)

if res.performance_metrics is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetPerformanceMetricsRequest](../../models/operations/getperformancemetricsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetPerformanceMetricsResponse](../../models/operations/getperformancemetricsresponse.md)**

