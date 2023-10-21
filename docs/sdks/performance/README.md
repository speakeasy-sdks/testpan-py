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
    spec_path='string',
    spec_path_method=operations.GetAPISecurityAPICatalogIDHitCountGraphSpecPathMethod.CONNECT,
)

res = s.performance.get_api_security_api_catalog_id_hit_count_graph(req)

if res.api_service_spec_path_hit_count_graph is not None:
    # handle response
    pass
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
    protocol='string',
    source_namespace='565fb8ea-d185-4971-9112-61059b89d3b7',
    source_pod_template='dcd1b894-b8a5-4ad8-a111-06ddd9453d84',
    start_time=dateutil.parser.isoparse('2022-01-22T20:26:53.423Z'),
    target_namespace='e92fa045-69a7-47dd-a601-68cf6d7999aa',
    target_pod_template='93b9be30-176b-4a06-8558-1cebc600c70d',
)

res = s.performance.get_performance_metrics(req)

if res.performance_metrics is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetPerformanceMetricsRequest](../../models/operations/getperformancemetricsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetPerformanceMetricsResponse](../../models/operations/getperformancemetricsresponse.md)**

