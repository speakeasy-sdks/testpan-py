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
    catalog_id='ca4d456e-f103-41e6-899f-0c2001e22cd5',
    hours_interval=351035,
    spec_path='quod',
    spec_path_method=operations.GetAPISecurityAPICatalogIDHitCountGraphSpecPathMethod.TRACE,
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
    end_time=dateutil.parser.isoparse('2022-08-20T18:13:06.023Z'),
    protocol='molestias',
    source_namespace='4a184d76-d971-4fc8-a0c6-5b037bb8e0cc',
    source_pod_template='885187e4-de04-4af2-8c5d-ddb46aa1cfd6',
    start_time=dateutil.parser.isoparse('2021-05-14T04:58:39.138Z'),
    target_namespace='28da0131-9112-4964-a645-c1d81f29042f',
    target_pod_template='569b7aff-0ea2-4216-8be0-71bc163e279a',
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

