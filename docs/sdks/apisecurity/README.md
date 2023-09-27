# APISecurity
(*api_security*)

## Overview

APIs used to manage Api Security

### Available Operations

* [delete_api_security_api_catalog_id_](#delete_api_security_api_catalog_id_) - Delete an API
* [delete_api_security_internal_catalog_catalog_id_bfla_detection](#delete_api_security_internal_catalog_catalog_id_bfla_detection) - stop bfla detection phase
* [delete_api_security_internal_catalog_catalog_id_bfla_learning](#delete_api_security_internal_catalog_catalog_id_bfla_learning) - stop bfla learning phase
* [delete_api_security_open_api_specs_catalog_id_](#delete_api_security_open_api_specs_catalog_id_) - delete open api spec include all of it findings and scores
* [delete_gateways_gateway_id_](#delete_gateways_gateway_id_) - Delete gateway
* [get_api_security_external_catalog](#get_api_security_external_catalog) - Get a list of APIs and their compliance
* [get_api_security_external_catalog_count](#get_api_security_external_catalog_count) - Get the number of existing 3rd party APIs in the inventory
* [get_api_security_external_catalog_catalog_id_](#get_api_security_external_catalog_catalog_id_) - Get information about a specific API
* [get_api_security_internal_catalog](#get_api_security_internal_catalog) - Get a list of APIs and their compliance
* [get_api_security_internal_catalog_count](#get_api_security_internal_catalog_count) - Get the number of existing 3rd party APIs in the inventory
* [get_api_security_internal_catalog_catalog_id_](#get_api_security_internal_catalog_catalog_id_) - Get information about a specific API
* [get_api_security_internal_catalog_catalog_id_bfla](#get_api_security_internal_catalog_catalog_id_bfla) - Get bfla info for given catalogId
* [get_api_security_internal_catalog_catalog_id_fuzzing_status](#get_api_security_internal_catalog_catalog_id_fuzzing_status) - Get status of the last/running fuzzing test
* [get_api_security_internal_catalog_catalog_id_fuzzing_tests](#get_api_security_internal_catalog_catalog_id_fuzzing_tests) - Get list of fuzzing tests
* [get_api_security_internal_catalog_catalog_id_trace_analysis](#get_api_security_internal_catalog_catalog_id_trace_analysis) - Get trace analysis details
* [get_api_security_open_api_specs_catalog_id_](#get_api_security_open_api_specs_catalog_id_) - Get provided and reconstructed open api specs for specific API
* [get_api_security_open_api_specs_catalog_id_diff_detection_status](#get_api_security_open_api_specs_catalog_id_diff_detection_status) - Get provided and reconstructed open api specs for specific API
* [get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status](#get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status) - Get open api spec score status
* [get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json](#get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json) - Get provided spec content as json
* [get_api_security_open_api_specs_catalog_id_reconstructed_spec_review](#get_api_security_open_api_specs_catalog_id_reconstructed_spec_review) - Get the suggestions of a spec reconstruction (or previously cached info)
* [get_api_security_open_api_specs_catalog_id_reconstructed_spec_status](#get_api_security_open_api_specs_catalog_id_reconstructed_spec_status) - Get the status of a spec reconstruction
* [get_api_security_open_api_specs_catalog_id_reconstructed_spec_json](#get_api_security_open_api_specs_catalog_id_reconstructed_spec_json) - Get reconstructed open api spec as json for specific API
* [get_api_security_risk_findings](#get_api_security_risk_findings) - Get a list of risk findings
* [get_api_security_risk_findings_categories](#get_api_security_risk_findings_categories) - Get a list of risk findings categories
* [get_api_security_risk_findings_sources](#get_api_security_risk_findings_sources) - Get a list of risk findings sources
* [get_api_security_risk_findings_risk_finding_id_](#get_api_security_risk_findings_risk_finding_id_) - Get a specific risk findings
* [get_api_security_catalog_id_delete_dependencies](#get_api_security_catalog_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified api security service
* [get_api_security_catalog_id_methods](#get_api_security_catalog_id_methods) - Get a list of an API spec methods for a specific API and its spec's tags
* [get_api_security_catalog_id_tags](#get_api_security_catalog_id_tags) - Get a list of an API spec tags or a specific API
* [get_dashboard_apisec_risk_findings](#get_dashboard_apisec_risk_findings) - Get API sec risk findings widget
* [get_dashboard_apisec_risk_findings_trend](#get_dashboard_apisec_risk_findings_trend) - Get API sec risk findings trend graph widget for the last 30 days
* [get_dashboard_apisec_specs_and_operations_diffs](#get_dashboard_apisec_specs_and_operations_diffs) - Get API sec specs and operations diffs widget
* [get_dashboard_apisec_top_risky_apis](#get_dashboard_apisec_top_risky_apis) - Get API sec top risky APIs widget
* [get_dashboard_apisec_top_risky_findings](#get_dashboard_apisec_top_risky_findings) - Get API sec top risky findings widget
* [get_gateways](#get_gateways) - Get gateways
* [get_gateways_clusters](#get_gateways_clusters) - Get clusters info
* [get_gateways_gateway_id_download_bundle](#get_gateways_gateway_id_download_bundle) - Get a GW installation script
* [post_api_security_api](#post_api_security_api) - Register an API for scoring
* [post_api_security_internal_catalog_catalog_id_bfla_detection](#post_api_security_internal_catalog_catalog_id_bfla_detection) - Start new bfla detection phase
* [post_api_security_internal_catalog_catalog_id_bfla_learning](#post_api_security_internal_catalog_catalog_id_bfla_learning) - Start new bfla learning phase
* [post_api_security_internal_catalog_catalog_id_bfla_reset](#post_api_security_internal_catalog_catalog_id_bfla_reset) - Reset bfla model
* [post_api_security_internal_catalog_catalog_id_reset_trace_analysis](#post_api_security_internal_catalog_catalog_id_reset_trace_analysis) - Reset trace analysis
* [post_api_security_internal_catalog_catalog_id_start_fuzzing](#post_api_security_internal_catalog_catalog_id_start_fuzzing) - Start new fuzzing test
* [post_api_security_internal_catalog_catalog_id_start_trace_analysis](#post_api_security_internal_catalog_catalog_id_start_trace_analysis) - Start trace analysis
* [post_api_security_internal_catalog_catalog_id_stop_fuzzing](#post_api_security_internal_catalog_catalog_id_stop_fuzzing) - Stop fuzzing test
* [post_api_security_internal_catalog_catalog_id_stop_trace_analysis](#post_api_security_internal_catalog_catalog_id_stop_trace_analysis) - Stop trace analysis
* [post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort](#post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort) - abort learning and reconstructing an API via API Clarity
* [post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn](#post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn) - Start learning and reconstructing an API via API Clarity
* [post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve](#post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve) - Approve reconstructed spec suggestions (only 1 approval per catalogId)
* [post_api_security_open_api_specs_catalog_id_start_diffs_detection](#post_api_security_open_api_specs_catalog_id_start_diffs_detection) - Start spec diffs detection
* [post_api_security_open_api_specs_catalog_id_stop_diffs_detection](#post_api_security_open_api_specs_catalog_id_stop_diffs_detection) - stop spec diffs detection
* [post_gateways](#post_gateways) - Add new gateway
* [put_api_security_internal_catalog_catalog_id_bfla](#put_api_security_internal_catalog_catalog_id_bfla) - update BFLA info for this catalogId
* [put_api_security_open_api_specs_catalog_id_](#put_api_security_open_api_specs_catalog_id_) - Add or edit a spec about a specific API for the account
* [put_gateways_gateway_id_](#put_gateways_gateway_id_) - Edit gateway

## delete_api_security_api_catalog_id_

Delete an API

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

req = operations.DeleteAPISecurityAPICatalogIDRequest(
    catalog_id='3a8d8f5c-0b2f-42fb-bb19-4a276b26916f',
)

res = s.api_security.delete_api_security_api_catalog_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteAPISecurityAPICatalogIDRequest](../../models/operations/deleteapisecurityapicatalogidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteAPISecurityAPICatalogIDResponse](../../models/operations/deleteapisecurityapicatalogidresponse.md)**


## delete_api_security_internal_catalog_catalog_id_bfla_detection

stop bfla detection phase

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

req = operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest(
    catalog_id='e1f08f42-94e3-4698-b447-f603e8b445e8',
)

res = s.api_security.delete_api_security_internal_catalog_catalog_id_bfla_detection(req)

if res.delete_api_security_internal_catalog_catalog_id_bfla_detection_204_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest](../../models/operations/deleteapisecurityinternalcatalogcatalogidbfladetectionrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionResponse](../../models/operations/deleteapisecurityinternalcatalogcatalogidbfladetectionresponse.md)**


## delete_api_security_internal_catalog_catalog_id_bfla_learning

stop bfla learning phase

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

req = operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest(
    catalog_id='0ca55efd-20e4-457e-9858-b6a89fbe3a5a',
)

res = s.api_security.delete_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.delete_api_security_internal_catalog_catalog_id_bfla_learning_204_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest](../../models/operations/deleteapisecurityinternalcatalogcatalogidbflalearningrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningResponse](../../models/operations/deleteapisecurityinternalcatalogcatalogidbflalearningresponse.md)**


## delete_api_security_open_api_specs_catalog_id_

delete open api spec include all of it findings and scores

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

req = operations.DeleteAPISecurityOpenAPISpecsCatalogIDRequest(
    catalog_id='a8e4824d-0ab4-4075-888e-51862065e904',
)

res = s.api_security.delete_api_security_open_api_specs_catalog_id_(req)

if res.open_api_spec_score_status is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.DeleteAPISecurityOpenAPISpecsCatalogIDRequest](../../models/operations/deleteapisecurityopenapispecscatalogidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.DeleteAPISecurityOpenAPISpecsCatalogIDResponse](../../models/operations/deleteapisecurityopenapispecscatalogidresponse.md)**


## delete_gateways_gateway_id_

Delete gateway

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

req = operations.DeleteGatewaysGatewayIDRequest(
    gateway_id='f3b1194b-8abf-4603-a79f-9dfe0ab7da8a',
)

res = s.api_security.delete_gateways_gateway_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteGatewaysGatewayIDRequest](../../models/operations/deletegatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeleteGatewaysGatewayIDResponse](../../models/operations/deletegatewaysgatewayidresponse.md)**


## get_api_security_external_catalog

Get a list of APIs and their compliance

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

req = operations.GetAPISecurityExternalCatalogRequest(
    api_policy_profiles=[
        'veniam',
    ],
    drill_down_score=False,
    include_service_with_no_spec=False,
    max_results=291,
    name='Phil Boyer',
    no_pagination=False,
    offset=9911.42,
    sort_dir=operations.GetAPISecurityExternalCatalogSortDir.DESC,
    sort_key=operations.GetAPISecurityExternalCatalogSortKey.NAME,
    updated_after=dateutil.parser.isoparse('2021-05-22T03:09:11.884Z'),
)

res = s.api_security.get_api_security_external_catalog(req)

if res.api_service_list_external is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAPISecurityExternalCatalogRequest](../../models/operations/getapisecurityexternalcatalogrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAPISecurityExternalCatalogResponse](../../models/operations/getapisecurityexternalcatalogresponse.md)**


## get_api_security_external_catalog_count

Get the number of existing 3rd party APIs in the inventory

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

req = operations.GetAPISecurityExternalCatalogCountRequest(
    include_service_with_no_spec=False,
    name='Georgia Farrell',
    updated_after=dateutil.parser.isoparse('2021-10-02T23:52:38.012Z'),
)

res = s.api_security.get_api_security_external_catalog_count(req)

if res.get_api_security_external_catalog_count_200_application_json_integer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetAPISecurityExternalCatalogCountRequest](../../models/operations/getapisecurityexternalcatalogcountrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetAPISecurityExternalCatalogCountResponse](../../models/operations/getapisecurityexternalcatalogcountresponse.md)**


## get_api_security_external_catalog_catalog_id_

Get information about a specific API

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

req = operations.GetAPISecurityExternalCatalogCatalogIDRequest(
    api_policy_profiles=[
        'officiis',
    ],
    catalog_id='ee9526f8-d986-4e88-9ead-4f0e1012563f',
    download_as_json=False,
)

res = s.api_security.get_api_security_external_catalog_catalog_id_(req)

if res.api_service_drill_down_external is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetAPISecurityExternalCatalogCatalogIDRequest](../../models/operations/getapisecurityexternalcatalogcatalogidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetAPISecurityExternalCatalogCatalogIDResponse](../../models/operations/getapisecurityexternalcatalogcatalogidresponse.md)**


## get_api_security_internal_catalog

Get a list of APIs and their compliance

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

req = operations.GetAPISecurityInternalCatalogRequest(
    api_policy_profiles=[
        'molestias',
    ],
    drill_down_score=False,
    include_service_with_no_spec=False,
    max_results=3000.29,
    name='Carlos McClure',
    namespaces_filter='in',
    no_pagination=False,
    offset=2380.43,
    sort_dir=operations.GetAPISecurityInternalCatalogSortDir.DESC,
    sort_key=operations.GetAPISecurityInternalCatalogSortKey.RISK,
    updated_after=dateutil.parser.isoparse('2022-11-08T18:10:37.954Z'),
)

res = s.api_security.get_api_security_internal_catalog(req)

if res.api_service_list_internal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAPISecurityInternalCatalogRequest](../../models/operations/getapisecurityinternalcatalogrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAPISecurityInternalCatalogResponse](../../models/operations/getapisecurityinternalcatalogresponse.md)**


## get_api_security_internal_catalog_count

Get the number of existing 3rd party APIs in the inventory

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

req = operations.GetAPISecurityInternalCatalogCountRequest(
    include_service_with_no_spec=False,
    name='Leo Kiehn II',
    namespaces_filter='quidem',
    updated_after=dateutil.parser.isoparse('2022-04-05T02:21:38.050Z'),
)

res = s.api_security.get_api_security_internal_catalog_count(req)

if res.get_api_security_internal_catalog_count_200_application_json_integer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetAPISecurityInternalCatalogCountRequest](../../models/operations/getapisecurityinternalcatalogcountrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCountResponse](../../models/operations/getapisecurityinternalcatalogcountresponse.md)**


## get_api_security_internal_catalog_catalog_id_

Get information about a specific API

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

req = operations.GetAPISecurityInternalCatalogCatalogIDRequest(
    api_policy_profiles=[
        'vero',
    ],
    catalog_id='060807e2-b6e3-4ab8-845f-0597a60ff2a5',
    download_as_json=False,
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_(req)

if res.api_service_drill_down_internal is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetAPISecurityInternalCatalogCatalogIDRequest](../../models/operations/getapisecurityinternalcatalogcatalogidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDResponse](../../models/operations/getapisecurityinternalcatalogcatalogidresponse.md)**


## get_api_security_internal_catalog_catalog_id_bfla

Get bfla info for given catalogId

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

req = operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest(
    catalog_id='4a31e947-64a3-4e86-9e79-56f9251a5a9d',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_bfla(req)

if res.api_service_bfla_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/getapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/getapisecurityinternalcatalogcatalogidbflaresponse.md)**


## get_api_security_internal_catalog_catalog_id_fuzzing_status

Get status of the last/running fuzzing test

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

req = operations.GetAPISecurityInternalCatalogCatalogIDFuzzingStatusRequest(
    catalog_id='a660ff57-bfaa-4d4f-9efc-1b4512c10326',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_fuzzing_status(req)

if res.api_service_fuzzing_progress is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetAPISecurityInternalCatalogCatalogIDFuzzingStatusRequest](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingstatusrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDFuzzingStatusResponse](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingstatusresponse.md)**


## get_api_security_internal_catalog_catalog_id_fuzzing_tests

Get list of fuzzing tests

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

req = operations.GetAPISecurityInternalCatalogCatalogIDFuzzingTestsRequest(
    catalog_id='48dc2f61-5199-4ebf-90e9-fe6c632ca3ae',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_fuzzing_tests(req)

if res.api_service_fuzzing_tests is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetAPISecurityInternalCatalogCatalogIDFuzzingTestsRequest](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingtestsrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDFuzzingTestsResponse](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingtestsresponse.md)**


## get_api_security_internal_catalog_catalog_id_trace_analysis

Get trace analysis details

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

req = operations.GetAPISecurityInternalCatalogCatalogIDTraceAnalysisRequest(
    catalog_id='d0117996-312f-4de0-8771-778ff61d0174',
    max_results=4582.59,
    offset=4037.93,
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_trace_analysis(req)

if res.trace_analysis_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetAPISecurityInternalCatalogCatalogIDTraceAnalysisRequest](../../models/operations/getapisecurityinternalcatalogcatalogidtraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDTraceAnalysisResponse](../../models/operations/getapisecurityinternalcatalogcatalogidtraceanalysisresponse.md)**


## get_api_security_open_api_specs_catalog_id_

Get provided and reconstructed open api specs for specific API

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDRequest(
    catalog_id='360a15db-6a66-4065-9a1a-deaab5851d6c',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_(req)

if res.open_api_spec is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetAPISecurityOpenAPISpecsCatalogIDRequest](../../models/operations/getapisecurityopenapispecscatalogidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDResponse](../../models/operations/getapisecurityopenapispecscatalogidresponse.md)**


## get_api_security_open_api_specs_catalog_id_diff_detection_status

Get provided and reconstructed open api specs for specific API

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDDiffDetectionStatusRequest(
    catalog_id='645b08b6-1891-4baa-8fe1-ade008e6f8c5',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_diff_detection_status(req)

if res.diff_detection_status is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.GetAPISecurityOpenAPISpecsCatalogIDDiffDetectionStatusRequest](../../models/operations/getapisecurityopenapispecscatalogiddiffdetectionstatusrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDDiffDetectionStatusResponse](../../models/operations/getapisecurityopenapispecscatalogiddiffdetectionstatusresponse.md)**


## get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status

Get open api spec score status

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusRequest(
    catalog_id='f350d8cd-b5a3-4418-9430-10421813d520',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status(req)

if res.open_api_spec_score_status is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusRequest](../../models/operations/getapisecurityopenapispecscatalogidgetopenapispecscorestatusrequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusResponse](../../models/operations/getapisecurityopenapispecscatalogidgetopenapispecscorestatusresponse.md)**


## get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json

Get provided spec content as json

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDOpenAPISpecSwaggerJSONRequest(
    catalog_id='8ece7e25-3b66-4845-9c6c-6e205e16deab',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json(req)

if res.get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.GetAPISecurityOpenAPISpecsCatalogIDOpenAPISpecSwaggerJSONRequest](../../models/operations/getapisecurityopenapispecscatalogidopenapispecswaggerjsonrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDOpenAPISpecSwaggerJSONResponse](../../models/operations/getapisecurityopenapispecscatalogidopenapispecswaggerjsonresponse.md)**


## get_api_security_open_api_specs_catalog_id_reconstructed_spec_review

Get the suggestions of a spec reconstruction (or previously cached info)

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewRequest(
    catalog_id='3fec9578-a645-4842-b3a8-418d162309fb',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_reconstructed_spec_review(req)

if res.api_reconstructed_spec is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewRequest](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecreviewrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewResponse](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecreviewresponse.md)**


## get_api_security_open_api_specs_catalog_id_reconstructed_spec_status

Get the status of a spec reconstruction

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecStatusRequest(
    catalog_id='0929921a-efb9-4f58-84d8-6e68e4be0560',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_reconstructed_spec_status(req)

if res.api_reconstruction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecStatusRequest](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecstatusrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecStatusResponse](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecstatusresponse.md)**


## get_api_security_open_api_specs_catalog_id_reconstructed_spec_json

Get reconstructed open api spec as json for specific API

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

req = operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONRequest(
    catalog_id='13f59da7-57a5-49ec-bef6-6ef1caa3383c',
    download_as_json=False,
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_reconstructed_spec_json(req)

if res.get_api_security_open_api_specs_catalog_id_reconstructed_spec_json_200_application_json_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONRequest](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecjsonrequest.md) | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONResponse](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecjsonresponse.md)**


## get_api_security_risk_findings

Get a list of risk findings

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

req = operations.GetAPISecurityRiskFindingsRequest(
    api_sec_source=operations.GetAPISecurityRiskFindingsAPISecSource.INTERNAL,
    category='soluta',
    detected=False,
    element='repudiandae',
    max_results=7214.3,
    name='Glenda Kling',
    offset=2055.66,
    risks=[
        operations.GetAPISecurityRiskFindingsRisks.CRITICAL,
    ],
    sort_dir=operations.GetAPISecurityRiskFindingsSortDir.DESC,
    sort_key=operations.GetAPISecurityRiskFindingsSortKey.RISK,
    source='iure',
)

res = s.api_security.get_api_security_risk_findings(req)

if res.risk_findings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAPISecurityRiskFindingsRequest](../../models/operations/getapisecurityriskfindingsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetAPISecurityRiskFindingsResponse](../../models/operations/getapisecurityriskfindingsresponse.md)**


## get_api_security_risk_findings_categories

Get a list of risk findings categories

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


res = s.api_security.get_api_security_risk_findings_categories()

if res.get_api_security_risk_findings_categories_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetAPISecurityRiskFindingsCategoriesResponse](../../models/operations/getapisecurityriskfindingscategoriesresponse.md)**


## get_api_security_risk_findings_sources

Get a list of risk findings sources

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


res = s.api_security.get_api_security_risk_findings_sources()

if res.get_api_security_risk_findings_sources_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetAPISecurityRiskFindingsSourcesResponse](../../models/operations/getapisecurityriskfindingssourcesresponse.md)**


## get_api_security_risk_findings_risk_finding_id_

Get a specific risk findings

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

req = operations.GetAPISecurityRiskFindingsRiskFindingIDRequest(
    risk_finding_id='2f64d1db-1f2c-4431-8661-e96349e1cf9e',
)

res = s.api_security.get_api_security_risk_findings_risk_finding_id_(req)

if res.risk_finding is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetAPISecurityRiskFindingsRiskFindingIDRequest](../../models/operations/getapisecurityriskfindingsriskfindingidrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetAPISecurityRiskFindingsRiskFindingIDResponse](../../models/operations/getapisecurityriskfindingsriskfindingidresponse.md)**


## get_api_security_catalog_id_delete_dependencies

get dependencies which need to be handled in order to delete specified api security service

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

req = operations.GetAPISecurityCatalogIDDeleteDependenciesRequest(
    catalog_id='06e3a437-000a-4e6b-abc9-b8f759eac55a',
)

res = s.api_security.get_api_security_catalog_id_delete_dependencies(req)

if res.api_service_delete_dependencies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetAPISecurityCatalogIDDeleteDependenciesRequest](../../models/operations/getapisecuritycatalogiddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetAPISecurityCatalogIDDeleteDependenciesResponse](../../models/operations/getapisecuritycatalogiddeletedependenciesresponse.md)**


## get_api_security_catalog_id_methods

Get a list of an API spec methods for a specific API and its spec's tags

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

req = operations.GetAPISecurityCatalogIDMethodsRequest(
    catalog_id='9741d311-3529-465b-b8a7-202611435e13',
    tags=[
        'unde',
    ],
)

res = s.api_security.get_api_security_catalog_id_methods(req)

if res.api_service_methods is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAPISecurityCatalogIDMethodsRequest](../../models/operations/getapisecuritycatalogidmethodsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetAPISecurityCatalogIDMethodsResponse](../../models/operations/getapisecuritycatalogidmethodsresponse.md)**


## get_api_security_catalog_id_tags

Get a list of an API spec tags or a specific API

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

req = operations.GetAPISecurityCatalogIDTagsRequest(
    catalog_id='dbc2259b-1abd-4a8c-870e-1084cb0672d1',
)

res = s.api_security.get_api_security_catalog_id_tags(req)

if res.api_service_tags is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAPISecurityCatalogIDTagsRequest](../../models/operations/getapisecuritycatalogidtagsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetAPISecurityCatalogIDTagsResponse](../../models/operations/getapisecuritycatalogidtagsresponse.md)**


## get_dashboard_apisec_risk_findings

Get API sec risk findings widget

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

req = operations.GetDashboardApisecRiskFindingsRequest(
    api_sec_source=operations.GetDashboardApisecRiskFindingsAPISecSource.EXTERNAL,
)

res = s.api_security.get_dashboard_apisec_risk_findings(req)

if res.api_sec_risk_findings_widget is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetDashboardApisecRiskFindingsRequest](../../models/operations/getdashboardapisecriskfindingsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetDashboardApisecRiskFindingsResponse](../../models/operations/getdashboardapisecriskfindingsresponse.md)**


## get_dashboard_apisec_risk_findings_trend

Get API sec risk findings trend graph widget for the last 30 days

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

req = operations.GetDashboardApisecRiskFindingsTrendRequest(
    api_sec_source=operations.GetDashboardApisecRiskFindingsTrendAPISecSource.EXTERNAL,
    num_of_days=545918,
)

res = s.api_security.get_dashboard_apisec_risk_findings_trend(req)

if res.api_sec_risk_findings_trend_widget is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetDashboardApisecRiskFindingsTrendRequest](../../models/operations/getdashboardapisecriskfindingstrendrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetDashboardApisecRiskFindingsTrendResponse](../../models/operations/getdashboardapisecriskfindingstrendresponse.md)**


## get_dashboard_apisec_specs_and_operations_diffs

Get API sec specs and operations diffs widget

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

req = operations.GetDashboardApisecSpecsAndOperationsDiffsRequest(
    api_sec_source=operations.GetDashboardApisecSpecsAndOperationsDiffsAPISecSource.INTERNAL,
)

res = s.api_security.get_dashboard_apisec_specs_and_operations_diffs(req)

if res.specs_and_operations_diffs_widget is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetDashboardApisecSpecsAndOperationsDiffsRequest](../../models/operations/getdashboardapisecspecsandoperationsdiffsrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetDashboardApisecSpecsAndOperationsDiffsResponse](../../models/operations/getdashboardapisecspecsandoperationsdiffsresponse.md)**


## get_dashboard_apisec_top_risky_apis

Get API sec top risky APIs widget

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

req = operations.GetDashboardApisecTopRiskyApisRequest(
    api_sec_source=operations.GetDashboardApisecTopRiskyApisAPISecSource.EXTERNAL,
    max_results=8822.84,
)

res = s.api_security.get_dashboard_apisec_top_risky_apis(req)

if res.api_sec_top_risky_apis_widget is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetDashboardApisecTopRiskyApisRequest](../../models/operations/getdashboardapisectopriskyapisrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetDashboardApisecTopRiskyApisResponse](../../models/operations/getdashboardapisectopriskyapisresponse.md)**


## get_dashboard_apisec_top_risky_findings

Get API sec top risky findings widget

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

req = operations.GetDashboardApisecTopRiskyFindingsRequest(
    api_sec_source=operations.GetDashboardApisecTopRiskyFindingsAPISecSource.EXTERNAL,
    max_results=7332.89,
)

res = s.api_security.get_dashboard_apisec_top_risky_findings(req)

if res.api_sec_top_risky_findings_widget is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetDashboardApisecTopRiskyFindingsRequest](../../models/operations/getdashboardapisectopriskyfindingsrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetDashboardApisecTopRiskyFindingsResponse](../../models/operations/getdashboardapisectopriskyfindingsresponse.md)**


## get_gateways

Get gateways

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

req = operations.GetGatewaysRequest(
    max_results=5750.78,
    name='Stacey Hintz',
    no_pagination=False,
    offset=3572.07,
    sort_dir=operations.GetGatewaysSortDir.DESC,
)

res = s.api_security.get_gateways(req)

if res.gateways is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetGatewaysRequest](../../models/operations/getgatewaysrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetGatewaysResponse](../../models/operations/getgatewaysresponse.md)**


## get_gateways_clusters

Get clusters info

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

req = operations.GetGatewaysClustersRequest(
    gateway_type=operations.GetGatewaysClustersGatewayType.F5_BIG_IP,
)

res = s.api_security.get_gateways_clusters(req)

if res.gateway_cluster_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetGatewaysClustersRequest](../../models/operations/getgatewaysclustersrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetGatewaysClustersResponse](../../models/operations/getgatewaysclustersresponse.md)**


## get_gateways_gateway_id_download_bundle

In order to install,  extract and run "./install_bundle.sh"

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

req = operations.GetGatewaysGatewayIDDownloadBundleRequest(
    gateway_id='bd02bae0-be2d-4782-a59e-3ea4b5197f92',
)

res = s.api_security.get_gateways_gateway_id_download_bundle(req)

if res.get_gateways_gateway_id_download_bundle_200_application_json_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetGatewaysGatewayIDDownloadBundleRequest](../../models/operations/getgatewaysgatewayiddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetGatewaysGatewayIDDownloadBundleResponse](../../models/operations/getgatewaysgatewayiddownloadbundleresponse.md)**


## post_api_security_api

Register an API for scoring

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

req = shared.APISecurityAPI(
    name='Carrie Douglas',
)

res = s.api_security.post_api_security_api(req)

if res.post_api_security_api_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.APISecurityAPI](../../models/shared/apisecurityapi.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostAPISecurityAPIResponse](../../models/operations/postapisecurityapiresponse.md)**


## post_api_security_internal_catalog_catalog_id_bfla_detection

Start new bfla detection phase

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

req = operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionRequest(
    bfla_duration_configuration=shared.BflaDurationConfiguration(
        duration='dignissimos',
    ),
    catalog_id='ce52b895-c537-4c64-94ef-b0b34896c3ca',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_bfla_detection(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_detection_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbfladetectionrequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbfladetectionresponse.md)**


## post_api_security_internal_catalog_catalog_id_bfla_learning

Start new bfla learning phase

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

req = operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningRequest(
    bfla_duration_configuration=shared.BflaDurationConfiguration(
        duration='nostrum',
    ),
    catalog_id='acfbe2fd-5707-4577-9291-77deac646ecb',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_learning_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbflalearningrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbflalearningresponse.md)**


## post_api_security_internal_catalog_catalog_id_bfla_reset

Reset bfla model

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

req = operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest(
    catalog_id='573409e3-eb1e-45a2-b12e-b07f116db995',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_bfla_reset(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_reset_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbflaresetrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaResetResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbflaresetresponse.md)**


## post_api_security_internal_catalog_catalog_id_reset_trace_analysis

Reset trace analysis

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

req = operations.PostAPISecurityInternalCatalogCatalogIDResetTraceAnalysisRequest(
    catalog_id='45fc95fa-8897-40e1-89db-b30fcb33ea05',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_reset_trace_analysis(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.PostAPISecurityInternalCatalogCatalogIDResetTraceAnalysisRequest](../../models/operations/postapisecurityinternalcatalogcatalogidresettraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDResetTraceAnalysisResponse](../../models/operations/postapisecurityinternalcatalogcatalogidresettraceanalysisresponse.md)**


## post_api_security_internal_catalog_catalog_id_start_fuzzing

Start new fuzzing test

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

req = operations.PostAPISecurityInternalCatalogCatalogIDStartFuzzingRequest(
    api_fuzzing_test_configuration=shared.APIFuzzingTestConfiguration(
        auth=shared.AuthorizationScheme(
            authorization_scheme_type=shared.AuthorizationSchemeAuthorizationSchemeType.AUTHORIZATION_SCHEME_API_TOKEN,
        ),
        depth=shared.TestInputDepthEnum.DEEP,
    ),
    catalog_id='197cd44e-2f52-4d82-9351-3bb6f48b656b',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_start_fuzzing(req)

if res.api_service_fuzzing_test is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.PostAPISecurityInternalCatalogCatalogIDStartFuzzingRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstartfuzzingrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStartFuzzingResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstartfuzzingresponse.md)**


## post_api_security_internal_catalog_catalog_id_start_trace_analysis

Start trace analysis

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

req = operations.PostAPISecurityInternalCatalogCatalogIDStartTraceAnalysisRequest(
    trace_analysis_configuration=shared.TraceAnalysisConfiguration(
        duration=794507,
        time_unit=shared.TraceAnalysisConfigurationTimeUnit.DAYS,
    ),
    catalog_id='b35ff2e4-b275-437a-8cd9-e7319c177d52',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_start_trace_analysis(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.PostAPISecurityInternalCatalogCatalogIDStartTraceAnalysisRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstarttraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStartTraceAnalysisResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstarttraceanalysisresponse.md)**


## post_api_security_internal_catalog_catalog_id_stop_fuzzing

Stop fuzzing test

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

req = operations.PostAPISecurityInternalCatalogCatalogIDStopFuzzingRequest(
    catalog_id='5f77b114-eeb5-42ff-b85f-c37814d4c98e',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_stop_fuzzing(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.PostAPISecurityInternalCatalogCatalogIDStopFuzzingRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstopfuzzingrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStopFuzzingResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstopfuzzingresponse.md)**


## post_api_security_internal_catalog_catalog_id_stop_trace_analysis

Stop trace analysis

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

req = operations.PostAPISecurityInternalCatalogCatalogIDStopTraceAnalysisRequest(
    catalog_id='0c2bb89e-b75d-4ad6-b6c6-00503d8bb311',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_stop_trace_analysis(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.PostAPISecurityInternalCatalogCatalogIDStopTraceAnalysisRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstoptraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStopTraceAnalysisResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstoptraceanalysisresponse.md)**


## post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort

abort learning and reconstructing an API via API Clarity

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

req = operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecAbortRequest(
    catalog_id='80f739ae-9e05-47eb-809e-2810331f3981',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecAbortRequest](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecabortrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecAbortResponse](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecabortresponse.md)**


## post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn

Start learning and reconstructing an API via API Clarity

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

req = operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecLearnRequest(
    api_reconstruction_request=shared.APIReconstructionRequest(
        cluster_id='d4c700b6-07f3-4c93-873b-9da3f2ceda7e',
        learning_duration='qui',
    ),
    catalog_id='3f225741-1faf-44b7-944e-472e802857a5',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecLearnRequest](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspeclearnrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecLearnResponse](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspeclearnresponse.md)**


## post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve

Approve reconstructed spec suggestions (only 1 approval per catalogId)

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

req = operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveRequest(
    api_reconstructed_spec_input=shared.APIReconstructedSpecInput(
        oas_version=shared.OASVersion.OA_SV3_0,
        review_path_items=[
            shared.ReviewPathItem(
                api_events_paths=[
                    shared.APIEventPathAndMethods(
                        methods=[
                            shared.HTTPMethod.PUT,
                        ],
                        path='sit',
                    ),
                ],
                suggested_path='modi',
            ),
        ],
    ),
    catalog_id='63a7d575-f140-40e7-a4ad-7334ec1b781b',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                    | [operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveRequest](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecreviewapproverequest.md) | :heavy_check_mark:                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                   |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveResponse](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecreviewapproveresponse.md)**


## post_api_security_open_api_specs_catalog_id_start_diffs_detection

Start spec diffs detection

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

req = operations.PostAPISecurityOpenAPISpecsCatalogIDStartDiffsDetectionRequest(
    action_duration=shared.ActionDuration(
        duration=229276,
        time_unit=shared.ActionDurationTimeUnit.HOURS,
    ),
    catalog_id='a08088d1-00ef-4ada-a00e-f0422eb2164c',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_start_diffs_detection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.PostAPISecurityOpenAPISpecsCatalogIDStartDiffsDetectionRequest](../../models/operations/postapisecurityopenapispecscatalogidstartdiffsdetectionrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDStartDiffsDetectionResponse](../../models/operations/postapisecurityopenapispecscatalogidstartdiffsdetectionresponse.md)**


## post_api_security_open_api_specs_catalog_id_stop_diffs_detection

stop spec diffs detection

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

req = operations.PostAPISecurityOpenAPISpecsCatalogIDStopDiffsDetectionRequest(
    catalog_id='f9ab8366-c723-4ffd-a9e0-6bee4825c1fc',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_stop_diffs_detection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.PostAPISecurityOpenAPISpecsCatalogIDStopDiffsDetectionRequest](../../models/operations/postapisecurityopenapispecscatalogidstopdiffsdetectionrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDStopDiffsDetectionResponse](../../models/operations/postapisecurityopenapispecscatalogidstopdiffsdetectionresponse.md)**


## post_gateways

Add new gateway

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

req = shared.Gateway(
    cluster_name='quae',
    description='officiis',
    id='115c80bf-f918-4544-ac42-defcce8f1977',
    name='Lydia Douglas',
    type=shared.GatewayType.APIGEE_X,
)

res = s.api_security.post_gateways(req)

if res.gateway is not None:
    # handle response
```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [shared.Gateway](../../models/shared/gateway.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.PostGatewaysResponse](../../models/operations/postgatewaysresponse.md)**


## put_api_security_internal_catalog_catalog_id_bfla

update BFLA info for this catalogId

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

req = operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest(
    api_service_bfla_info=shared.APIServiceBflaInfo(
        end_time=dateutil.parser.isoparse('2022-08-16T23:55:48.181Z'),
        status=shared.APIServiceBflaInfoStatus.NO_SPEC,
        tags=[
            shared.APIServiceBflaTagInfo(
                is_legitimate=False,
                name='Ron Rau IV',
                paths=[
                    shared.APIServiceBflaPathInfo(
                        clients=[
                            shared.APIServiceBflaClientInfo(
                                external=False,
                                identifier='f05e3d48-fdaf-4313-a1f5-fd94259c0b36',
                                is_legitimate=False,
                                last_observed=dateutil.parser.isoparse('2022-07-05T01:41:17.302Z'),
                                last_status_code=330440,
                                name='Luke Mayer',
                                namespace='tenetur',
                                principles=[
                                    shared.APIServiceBflaPrincipleInfo(
                                        ip='adipisci',
                                        name='Harvey Harber',
                                        principle_type='ab',
                                    ),
                                ],
                            ),
                        ],
                        is_legitimate=False,
                        method=shared.HTTPMethod.GET,
                        path='hic',
                    ),
                ],
            ),
        ],
    ),
    catalog_id='6c37a512-6243-4835-bbc0-5a23a45cefc5',
)

res = s.api_security.put_api_security_internal_catalog_catalog_id_bfla(req)

if res.put_api_security_internal_catalog_catalog_id_bfla_200_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/putapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/putapisecurityinternalcatalogcatalogidbflaresponse.md)**


## put_api_security_open_api_specs_catalog_id_

Add or edit a spec about a specific API for the account

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

req = operations.PutAPISecurityOpenAPISpecsCatalogIDRequest(
    request_body='doloribus',
    catalog_id='de10a0ce-2169-4e51-8019-c6dc5e347627',
)

res = s.api_security.put_api_security_open_api_specs_catalog_id_(req)

if res.open_api_spec is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PutAPISecurityOpenAPISpecsCatalogIDRequest](../../models/operations/putapisecurityopenapispecscatalogidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PutAPISecurityOpenAPISpecsCatalogIDResponse](../../models/operations/putapisecurityopenapispecscatalogidresponse.md)**


## put_gateways_gateway_id_

Edit gateway

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

req = operations.PutGatewaysGatewayIDRequest(
    gateway=shared.Gateway(
        cluster_name='natus',
        description='provident',
        id='bfbbe694-9fb2-4bb4-acae-6c3d5db3adeb',
        name='Leon Schumm',
        type=shared.GatewayType.TYK_INTERNAL,
    ),
    gateway_id='4c506a8a-a94c-4026-84cf-5e9d9a4578ad',
)

res = s.api_security.put_gateways_gateway_id_(req)

if res.gateway is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PutGatewaysGatewayIDRequest](../../models/operations/putgatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PutGatewaysGatewayIDResponse](../../models/operations/putgatewaysgatewayidresponse.md)**

