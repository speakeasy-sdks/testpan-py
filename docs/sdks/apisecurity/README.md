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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteAPISecurityAPICatalogIDRequest(
    catalog_id='842f34dd-ffa1-41b2-85e1-21c9635c9fcb',
)

res = s.api_security.delete_api_security_api_catalog_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.DeleteAPISecurityAPICatalogIDRequest](../../models/operations/deleteapisecurityapicatalogidrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.DeleteAPISecurityAPICatalogIDResponse](../../models/operations/deleteapisecurityapicatalogidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_security_internal_catalog_catalog_id_bfla_detection

stop bfla detection phase

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest(
    catalog_id='3d2f6c1c-29ba-4502-9cb8-4666b2e993b7',
)

res = s.api_security.delete_api_security_internal_catalog_catalog_id_bfla_detection(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest](../../models/operations/deleteapisecurityinternalcatalogcatalogidbfladetectionrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionResponse](../../models/operations/deleteapisecurityinternalcatalogcatalogidbfladetectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_security_internal_catalog_catalog_id_bfla_learning

stop bfla learning phase

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest(
    catalog_id='3ba770da-4891-4357-a360-0c0e060f5b0f',
)

res = s.api_security.delete_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest](../../models/operations/deleteapisecurityinternalcatalogcatalogidbflalearningrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningResponse](../../models/operations/deleteapisecurityinternalcatalogcatalogidbflalearningresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_security_open_api_specs_catalog_id_

delete open api spec include all of it findings and scores

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteAPISecurityOpenAPISpecsCatalogIDRequest(
    catalog_id='95e2243c-a46e-4f56-870a-883817cd0574',
)

res = s.api_security.delete_api_security_open_api_specs_catalog_id_(req)

if res.open_api_spec_score_status is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.DeleteAPISecurityOpenAPISpecsCatalogIDRequest](../../models/operations/deleteapisecurityopenapispecscatalogidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.DeleteAPISecurityOpenAPISpecsCatalogIDResponse](../../models/operations/deleteapisecurityopenapispecscatalogidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_gateways_gateway_id_

Delete gateway

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteGatewaysGatewayIDRequest(
    gateway_id='0059ee9e-2eb4-40ca-97cc-9e2e4879b4b7',
)

res = s.api_security.delete_gateways_gateway_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.DeleteGatewaysGatewayIDRequest](../../models/operations/deletegatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeleteGatewaysGatewayIDResponse](../../models/operations/deletegatewaysgatewayidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_external_catalog

Get a list of APIs and their compliance

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityExternalCatalogRequest()

res = s.api_security.get_api_security_external_catalog(req)

if res.api_service_list_external is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAPISecurityExternalCatalogRequest](../../models/operations/getapisecurityexternalcatalogrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAPISecurityExternalCatalogResponse](../../models/operations/getapisecurityexternalcatalogresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_external_catalog_count

Get the number of existing 3rd party APIs in the inventory

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityExternalCatalogCountRequest()

res = s.api_security.get_api_security_external_catalog_count(req)

if res.integer is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetAPISecurityExternalCatalogCountRequest](../../models/operations/getapisecurityexternalcatalogcountrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetAPISecurityExternalCatalogCountResponse](../../models/operations/getapisecurityexternalcatalogcountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_external_catalog_catalog_id_

Get information about a specific API

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityExternalCatalogCatalogIDRequest(
    catalog_id='2d833a13-8a8e-436d-b01d-d86e879c6858',
)

res = s.api_security.get_api_security_external_catalog_catalog_id_(req)

if res.api_service_drill_down_external is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetAPISecurityExternalCatalogCatalogIDRequest](../../models/operations/getapisecurityexternalcatalogcatalogidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetAPISecurityExternalCatalogCatalogIDResponse](../../models/operations/getapisecurityexternalcatalogcatalogidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog

Get a list of APIs and their compliance

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogRequest()

res = s.api_security.get_api_security_internal_catalog(req)

if res.api_service_list_internal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAPISecurityInternalCatalogRequest](../../models/operations/getapisecurityinternalcatalogrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAPISecurityInternalCatalogResponse](../../models/operations/getapisecurityinternalcatalogresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog_count

Get the number of existing 3rd party APIs in the inventory

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogCountRequest()

res = s.api_security.get_api_security_internal_catalog_count(req)

if res.integer is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetAPISecurityInternalCatalogCountRequest](../../models/operations/getapisecurityinternalcatalogcountrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCountResponse](../../models/operations/getapisecurityinternalcatalogcountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog_catalog_id_

Get information about a specific API

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogCatalogIDRequest(
    catalog_id='a4b30b16-7e21-4dd4-bc5f-718b9d308613',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_(req)

if res.api_service_drill_down_internal is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.GetAPISecurityInternalCatalogCatalogIDRequest](../../models/operations/getapisecurityinternalcatalogcatalogidrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDResponse](../../models/operations/getapisecurityinternalcatalogcatalogidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog_catalog_id_bfla

Get bfla info for given catalogId

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest(
    catalog_id='74e0c81f-ef10-4f23-b74f-8447d1953ccf',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_bfla(req)

if res.api_service_bfla_info is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/getapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/getapisecurityinternalcatalogcatalogidbflaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog_catalog_id_fuzzing_status

Get status of the last/running fuzzing test

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogCatalogIDFuzzingStatusRequest(
    catalog_id='b8ae405f-27d4-4986-b826-818df6837b3d',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_fuzzing_status(req)

if res.api_service_fuzzing_progress is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetAPISecurityInternalCatalogCatalogIDFuzzingStatusRequest](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingstatusrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDFuzzingStatusResponse](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog_catalog_id_fuzzing_tests

Get list of fuzzing tests

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogCatalogIDFuzzingTestsRequest(
    catalog_id='03b031d5-bcbe-4041-865f-3cf281949555',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_fuzzing_tests(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.GetAPISecurityInternalCatalogCatalogIDFuzzingTestsRequest](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingtestsrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDFuzzingTestsResponse](../../models/operations/getapisecurityinternalcatalogcatalogidfuzzingtestsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_internal_catalog_catalog_id_trace_analysis

Get trace analysis details

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityInternalCatalogCatalogIDTraceAnalysisRequest(
    catalog_id='14f8fff8-1410-462d-9de3-1aa0e5094377',
)

res = s.api_security.get_api_security_internal_catalog_catalog_id_trace_analysis(req)

if res.trace_analysis_details is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.GetAPISecurityInternalCatalogCatalogIDTraceAnalysisRequest](../../models/operations/getapisecurityinternalcatalogcatalogidtraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDTraceAnalysisResponse](../../models/operations/getapisecurityinternalcatalogcatalogidtraceanalysisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_

Get provided and reconstructed open api specs for specific API

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDRequest(
    catalog_id='9766bdb5-2002-47a6-9ab1-0c9e7ba174e7',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_(req)

if res.open_api_spec is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetAPISecurityOpenAPISpecsCatalogIDRequest](../../models/operations/getapisecurityopenapispecscatalogidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDResponse](../../models/operations/getapisecurityopenapispecscatalogidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_diff_detection_status

Get provided and reconstructed open api specs for specific API

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDDiffDetectionStatusRequest(
    catalog_id='89ba7d71-938d-4e0d-ae77-2227f0233a60',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_diff_detection_status(req)

if res.diff_detection_status is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.GetAPISecurityOpenAPISpecsCatalogIDDiffDetectionStatusRequest](../../models/operations/getapisecurityopenapispecscatalogiddiffdetectionstatusrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDDiffDetectionStatusResponse](../../models/operations/getapisecurityopenapispecscatalogiddiffdetectionstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status

Get open api spec score status

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusRequest(
    catalog_id='e844ac3e-b37a-4e44-810c-fb03dafad57b',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status(req)

if res.open_api_spec_score_status is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                        | [operations.GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusRequest](../../models/operations/getapisecurityopenapispecscatalogidgetopenapispecscorestatusrequest.md) | :heavy_check_mark:                                                                                                                                                               | The request object to use for the request.                                                                                                                                       |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDGetOpenAPISpecScoreStatusResponse](../../models/operations/getapisecurityopenapispecscatalogidgetopenapispecscorestatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json

Get provided spec content as json

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDOpenAPISpecSwaggerJSONRequest(
    catalog_id='c1e78882-5e52-4c34-a91e-a88ab3af7faf',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.GetAPISecurityOpenAPISpecsCatalogIDOpenAPISpecSwaggerJSONRequest](../../models/operations/getapisecurityopenapispecscatalogidopenapispecswaggerjsonrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDOpenAPISpecSwaggerJSONResponse](../../models/operations/getapisecurityopenapispecscatalogidopenapispecswaggerjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_reconstructed_spec_review

Get the suggestions of a spec reconstruction (or previously cached info)

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewRequest(
    catalog_id='96eed0ac-9db4-4a1c-babc-e6affa5427c5',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_reconstructed_spec_review(req)

if res.api_reconstructed_spec is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewRequest](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecreviewrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewResponse](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecreviewresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_reconstructed_spec_status

Get the status of a spec reconstruction

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecStatusRequest(
    catalog_id='0bfa0230-126d-4965-9d51-cb2d6c612293',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_reconstructed_spec_status(req)

if res.api_reconstruction_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecStatusRequest](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecstatusrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecStatusResponse](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_open_api_specs_catalog_id_reconstructed_spec_json

Get reconstructed open api spec as json for specific API

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONRequest(
    catalog_id='4022b3ba-9ecc-4767-9469-71ea890137cd',
)

res = s.api_security.get_api_security_open_api_specs_catalog_id_reconstructed_spec_json(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONRequest](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecjsonrequest.md) | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |


### Response

**[operations.GetAPISecurityOpenAPISpecsCatalogIDReconstructedSpecJSONResponse](../../models/operations/getapisecurityopenapispecscatalogidreconstructedspecjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_risk_findings

Get a list of risk findings

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityRiskFindingsRequest(
    api_sec_source=operations.APISecSource.INTERNAL,
    sort_key=operations.GetAPISecurityRiskFindingsQueryParamSortKey.RISK,
)

res = s.api_security.get_api_security_risk_findings(req)

if res.risk_findings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetAPISecurityRiskFindingsRequest](../../models/operations/getapisecurityriskfindingsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetAPISecurityRiskFindingsResponse](../../models/operations/getapisecurityriskfindingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_risk_findings_categories

Get a list of risk findings categories

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.api_security.get_api_security_risk_findings_categories()

if res.strings is not None:
    # handle response
    pass

```


### Response

**[operations.GetAPISecurityRiskFindingsCategoriesResponse](../../models/operations/getapisecurityriskfindingscategoriesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_risk_findings_sources

Get a list of risk findings sources

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.api_security.get_api_security_risk_findings_sources()

if res.strings is not None:
    # handle response
    pass

```


### Response

**[operations.GetAPISecurityRiskFindingsSourcesResponse](../../models/operations/getapisecurityriskfindingssourcesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_risk_findings_risk_finding_id_

Get a specific risk findings

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityRiskFindingsRiskFindingIDRequest(
    risk_finding_id='a6f70519-fb6c-4b3a-af18-7a0de05d5783',
)

res = s.api_security.get_api_security_risk_findings_risk_finding_id_(req)

if res.risk_finding is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetAPISecurityRiskFindingsRiskFindingIDRequest](../../models/operations/getapisecurityriskfindingsriskfindingidrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetAPISecurityRiskFindingsRiskFindingIDResponse](../../models/operations/getapisecurityriskfindingsriskfindingidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_catalog_id_delete_dependencies

get dependencies which need to be handled in order to delete specified api security service

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityCatalogIDDeleteDependenciesRequest(
    catalog_id='a8274b04-711c-4a08-ae55-c1ca905077f8',
)

res = s.api_security.get_api_security_catalog_id_delete_dependencies(req)

if res.api_service_delete_dependencies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetAPISecurityCatalogIDDeleteDependenciesRequest](../../models/operations/getapisecuritycatalogiddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetAPISecurityCatalogIDDeleteDependenciesResponse](../../models/operations/getapisecuritycatalogiddeletedependenciesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_catalog_id_methods

Get a list of an API spec methods for a specific API and its spec's tags

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityCatalogIDMethodsRequest(
    catalog_id='bc418193-54db-45b9-831c-a3b7fcd92288',
    tags=[
        '<value>',
    ],
)

res = s.api_security.get_api_security_catalog_id_methods(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAPISecurityCatalogIDMethodsRequest](../../models/operations/getapisecuritycatalogidmethodsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetAPISecurityCatalogIDMethodsResponse](../../models/operations/getapisecuritycatalogidmethodsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_security_catalog_id_tags

Get a list of an API spec tags or a specific API

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAPISecurityCatalogIDTagsRequest(
    catalog_id='3f2d279c-52dc-45ca-8a35-0c4c47a5deff',
)

res = s.api_security.get_api_security_catalog_id_tags(req)

if res.api_service_tags is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetAPISecurityCatalogIDTagsRequest](../../models/operations/getapisecuritycatalogidtagsrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetAPISecurityCatalogIDTagsResponse](../../models/operations/getapisecuritycatalogidtagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dashboard_apisec_risk_findings

Get API sec risk findings widget

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetDashboardApisecRiskFindingsRequest(
    api_sec_source=operations.QueryParamAPISecSource.INTERNAL,
)

res = s.api_security.get_dashboard_apisec_risk_findings(req)

if res.api_sec_risk_findings_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetDashboardApisecRiskFindingsRequest](../../models/operations/getdashboardapisecriskfindingsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetDashboardApisecRiskFindingsResponse](../../models/operations/getdashboardapisecriskfindingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dashboard_apisec_risk_findings_trend

Get API sec risk findings trend graph widget for the last 30 days

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetDashboardApisecRiskFindingsTrendRequest(
    api_sec_source=operations.GetDashboardApisecRiskFindingsTrendQueryParamAPISecSource.INTERNAL,
)

res = s.api_security.get_dashboard_apisec_risk_findings_trend(req)

if res.api_sec_risk_findings_trend_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetDashboardApisecRiskFindingsTrendRequest](../../models/operations/getdashboardapisecriskfindingstrendrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetDashboardApisecRiskFindingsTrendResponse](../../models/operations/getdashboardapisecriskfindingstrendresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dashboard_apisec_specs_and_operations_diffs

Get API sec specs and operations diffs widget

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetDashboardApisecSpecsAndOperationsDiffsRequest(
    api_sec_source=operations.GetDashboardApisecSpecsAndOperationsDiffsQueryParamAPISecSource.INTERNAL,
)

res = s.api_security.get_dashboard_apisec_specs_and_operations_diffs(req)

if res.specs_and_operations_diffs_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetDashboardApisecSpecsAndOperationsDiffsRequest](../../models/operations/getdashboardapisecspecsandoperationsdiffsrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetDashboardApisecSpecsAndOperationsDiffsResponse](../../models/operations/getdashboardapisecspecsandoperationsdiffsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dashboard_apisec_top_risky_apis

Get API sec top risky APIs widget

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetDashboardApisecTopRiskyApisRequest(
    api_sec_source=operations.GetDashboardApisecTopRiskyApisQueryParamAPISecSource.INTERNAL,
)

res = s.api_security.get_dashboard_apisec_top_risky_apis(req)

if res.api_sec_top_risky_apis_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetDashboardApisecTopRiskyApisRequest](../../models/operations/getdashboardapisectopriskyapisrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetDashboardApisecTopRiskyApisResponse](../../models/operations/getdashboardapisectopriskyapisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dashboard_apisec_top_risky_findings

Get API sec top risky findings widget

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetDashboardApisecTopRiskyFindingsRequest(
    api_sec_source=operations.GetDashboardApisecTopRiskyFindingsQueryParamAPISecSource.INTERNAL,
)

res = s.api_security.get_dashboard_apisec_top_risky_findings(req)

if res.api_sec_top_risky_findings_widget is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetDashboardApisecTopRiskyFindingsRequest](../../models/operations/getdashboardapisectopriskyfindingsrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetDashboardApisecTopRiskyFindingsResponse](../../models/operations/getdashboardapisectopriskyfindingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_gateways

Get gateways

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetGatewaysRequest()

res = s.api_security.get_gateways(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetGatewaysRequest](../../models/operations/getgatewaysrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetGatewaysResponse](../../models/operations/getgatewaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_gateways_clusters

Get clusters info

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetGatewaysClustersRequest(
    gateway_type=operations.GatewayType.TYK_INTERNAL,
)

res = s.api_security.get_gateways_clusters(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetGatewaysClustersRequest](../../models/operations/getgatewaysclustersrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetGatewaysClustersResponse](../../models/operations/getgatewaysclustersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_gateways_gateway_id_download_bundle

In order to install,  extract and run "./install_bundle.sh"

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetGatewaysGatewayIDDownloadBundleRequest(
    gateway_id='d7df551a-98f0-4f5b-9bdc-d69676cf90f0',
)

res = s.api_security.get_gateways_gateway_id_download_bundle(req)

if res.stream is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetGatewaysGatewayIDDownloadBundleRequest](../../models/operations/getgatewaysgatewayiddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetGatewaysGatewayIDDownloadBundleResponse](../../models/operations/getgatewaysgatewayiddownloadbundleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_api

Register an API for scoring

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.APISecurityAPI(
    name='<value>',
)

res = s.api_security.post_api_security_api(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                      | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `request`                                                      | [shared.APISecurityAPI](../../models/shared/apisecurityapi.md) | :heavy_check_mark:                                             | The request object to use for the request.                     |


### Response

**[operations.PostAPISecurityAPIResponse](../../models/operations/postapisecurityapiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_bfla_detection

Start new bfla detection phase

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionRequest(
    bfla_duration_configuration=shared.BflaDurationConfiguration(
        duration='<value>',
    ),
    catalog_id='35e94464-b0ff-40e6-be14-ca29162fc277',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_bfla_detection(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                        | [operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbfladetectionrequest.md) | :heavy_check_mark:                                                                                                                                               | The request object to use for the request.                                                                                                                       |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbfladetectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_bfla_learning

Start new bfla learning phase

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningRequest(
    bfla_duration_configuration=shared.BflaDurationConfiguration(
        duration='<value>',
    ),
    catalog_id='08fbc82f-2c9e-4a85-a326-b52d888f26e1',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbflalearningrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbflalearningresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_bfla_reset

Reset bfla model

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest(
    catalog_id='2682814f-440b-4991-ae68-e4a1209728f3',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_bfla_reset(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbflaresetrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaResetResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbflaresetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_reset_trace_analysis

Reset trace analysis

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDResetTraceAnalysisRequest(
    catalog_id='3e5cd1f7-bf20-45d2-aba9-73c37afbfaa8',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_reset_trace_analysis(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.PostAPISecurityInternalCatalogCatalogIDResetTraceAnalysisRequest](../../models/operations/postapisecurityinternalcatalogcatalogidresettraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDResetTraceAnalysisResponse](../../models/operations/postapisecurityinternalcatalogcatalogidresettraceanalysisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_start_fuzzing

Start new fuzzing test

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDStartFuzzingRequest(
    api_fuzzing_test_configuration=shared.APIFuzzingTestConfiguration(
        auth=shared.AuthorizationScheme(
            authorization_scheme_type=shared.AuthorizationSchemeType.AUTHORIZATION_SCHEME_API_TOKEN,
        ),
        depth=shared.TestInputDepthEnum.DEEP,
    ),
    catalog_id='312eede1-be03-42b8-bb19-27700a035c99',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_start_fuzzing(req)

if res.api_service_fuzzing_test is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                      | [operations.PostAPISecurityInternalCatalogCatalogIDStartFuzzingRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstartfuzzingrequest.md) | :heavy_check_mark:                                                                                                                                             | The request object to use for the request.                                                                                                                     |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStartFuzzingResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstartfuzzingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_start_trace_analysis

Start trace analysis

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDStartTraceAnalysisRequest(
    trace_analysis_configuration=shared.TraceAnalysisConfiguration(
        duration=916267,
        time_unit=shared.TraceAnalysisConfigurationTimeUnit.DAYS,
    ),
    catalog_id='815f76cb-d054-45bf-9982-26857956700d',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_start_trace_analysis(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                  | Type                                                                                                                                                                       | Required                                                                                                                                                                   | Description                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                  | [operations.PostAPISecurityInternalCatalogCatalogIDStartTraceAnalysisRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstarttraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                                         | The request object to use for the request.                                                                                                                                 |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStartTraceAnalysisResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstarttraceanalysisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_stop_fuzzing

Stop fuzzing test

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDStopFuzzingRequest(
    catalog_id='c198f457-4849-4dd7-8320-e57f81ab2f63',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_stop_fuzzing(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                    | Type                                                                                                                                                         | Required                                                                                                                                                     | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                    | [operations.PostAPISecurityInternalCatalogCatalogIDStopFuzzingRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstopfuzzingrequest.md) | :heavy_check_mark:                                                                                                                                           | The request object to use for the request.                                                                                                                   |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStopFuzzingResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstopfuzzingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_internal_catalog_catalog_id_stop_trace_analysis

Stop trace analysis

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityInternalCatalogCatalogIDStopTraceAnalysisRequest(
    catalog_id='a026be33-c18b-419f-9481-083f4a844dc4',
)

res = s.api_security.post_api_security_internal_catalog_catalog_id_stop_trace_analysis(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                | Type                                                                                                                                                                     | Required                                                                                                                                                                 | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                                | [operations.PostAPISecurityInternalCatalogCatalogIDStopTraceAnalysisRequest](../../models/operations/postapisecurityinternalcatalogcatalogidstoptraceanalysisrequest.md) | :heavy_check_mark:                                                                                                                                                       | The request object to use for the request.                                                                                                                               |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDStopTraceAnalysisResponse](../../models/operations/postapisecurityinternalcatalogcatalogidstoptraceanalysisresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort

abort learning and reconstructing an API via API Clarity

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecAbortRequest(
    catalog_id='c8574da1-a228-4204-81bd-8ea8316c46d5',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecAbortRequest](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecabortrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecAbortResponse](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecabortresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn

Start learning and reconstructing an API via API Clarity

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecLearnRequest(
    catalog_id='4fd7941d-9d44-44e5-b609-cdd9605335d7',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecLearnRequest](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspeclearnrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecLearnResponse](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspeclearnresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve

Approve reconstructed spec suggestions (only 1 approval per catalogId)

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveRequest(
    api_reconstructed_spec=shared.APIReconstructedSpecInput(
        oas_version=shared.OASVersion.OA_SV3_0,
        review_path_items=[
            shared.ReviewPathItem(),
        ],
    ),
    catalog_id='33273b3e-10c3-43f3-8cf1-fe2c5b724ecc',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                    | Type                                                                                                                                                                                         | Required                                                                                                                                                                                     | Description                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                                    | [operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveRequest](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecreviewapproverequest.md) | :heavy_check_mark:                                                                                                                                                                           | The request object to use for the request.                                                                                                                                                   |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDReconstructedSpecReviewApproveResponse](../../models/operations/postapisecurityopenapispecscatalogidreconstructedspecreviewapproveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_open_api_specs_catalog_id_start_diffs_detection

Start spec diffs detection

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityOpenAPISpecsCatalogIDStartDiffsDetectionRequest(
    action_duration=shared.ActionDuration(
        duration=672614,
        time_unit=shared.TimeUnit.HOURS,
    ),
    catalog_id='84658317-7e1f-4e27-b84c-670056ef2d95',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_start_diffs_detection(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.PostAPISecurityOpenAPISpecsCatalogIDStartDiffsDetectionRequest](../../models/operations/postapisecurityopenapispecscatalogidstartdiffsdetectionrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDStartDiffsDetectionResponse](../../models/operations/postapisecurityopenapispecscatalogidstartdiffsdetectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_api_security_open_api_specs_catalog_id_stop_diffs_detection

stop spec diffs detection

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostAPISecurityOpenAPISpecsCatalogIDStopDiffsDetectionRequest(
    catalog_id='733d2638-f8e8-462b-aa51-67f9d1bf9b92',
)

res = s.api_security.post_api_security_open_api_specs_catalog_id_stop_diffs_detection(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                            | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                            | [operations.PostAPISecurityOpenAPISpecsCatalogIDStopDiffsDetectionRequest](../../models/operations/postapisecurityopenapispecscatalogidstopdiffsdetectionrequest.md) | :heavy_check_mark:                                                                                                                                                   | The request object to use for the request.                                                                                                                           |


### Response

**[operations.PostAPISecurityOpenAPISpecsCatalogIDStopDiffsDetectionResponse](../../models/operations/postapisecurityopenapispecscatalogidstopdiffsdetectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_gateways

Add new gateway

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.Gateway(
    cluster_name='<value>',
    name='<value>',
    type=shared.GatewayType.APIGEE_X,
)

res = s.api_security.post_gateways(req)

if res.gateway is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [shared.Gateway](../../models/shared/gateway.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.PostGatewaysResponse](../../models/operations/postgatewaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_security_internal_catalog_catalog_id_bfla

update BFLA info for this catalogId

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest(
    api_service_bfla_info=shared.APIServiceBflaInfo(
        status=shared.APIServiceBflaInfoStatus.NO_SPEC,
    ),
    catalog_id='aab64aef-3b3f-4caa-9d44-2012ad1459f8',
)

res = s.api_security.put_api_security_internal_catalog_catalog_id_bfla(req)

if res.string is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/putapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/putapisecurityinternalcatalogcatalogidbflaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_security_open_api_specs_catalog_id_

Add or edit a spec about a specific API for the account

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutAPISecurityOpenAPISpecsCatalogIDRequest(
    request_body='<value>',
    catalog_id='39b6c1e7-d209-4d8c-b8d6-6907b8b2d3e4',
)

res = s.api_security.put_api_security_open_api_specs_catalog_id_(req)

if res.open_api_spec is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.PutAPISecurityOpenAPISpecsCatalogIDRequest](../../models/operations/putapisecurityopenapispecscatalogidrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PutAPISecurityOpenAPISpecsCatalogIDResponse](../../models/operations/putapisecurityopenapispecscatalogidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_gateways_gateway_id_

Edit gateway

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutGatewaysGatewayIDRequest(
    gateway=shared.Gateway(
        cluster_name='<value>',
        name='<value>',
        type=shared.GatewayType.F5_BIG_IP,
    ),
    gateway_id='b1d9c87e-1369-4f02-8e6c-75779c9c8e93',
)

res = s.api_security.put_gateways_gateway_id_(req)

if res.gateway is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.PutGatewaysGatewayIDRequest](../../models/operations/putgatewaysgatewayidrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PutGatewaysGatewayIDResponse](../../models/operations/putgatewaysgatewayidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
