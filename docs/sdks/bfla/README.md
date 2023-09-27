# Bfla
(*bfla*)

### Available Operations

* [delete_api_security_internal_catalog_catalog_id_bfla_detection](#delete_api_security_internal_catalog_catalog_id_bfla_detection) - stop bfla detection phase
* [delete_api_security_internal_catalog_catalog_id_bfla_learning](#delete_api_security_internal_catalog_catalog_id_bfla_learning) - stop bfla learning phase
* [get_api_security_internal_catalog_catalog_id_bfla](#get_api_security_internal_catalog_catalog_id_bfla) - Get bfla info for given catalogId
* [post_api_security_internal_catalog_catalog_id_bfla_detection](#post_api_security_internal_catalog_catalog_id_bfla_detection) - Start new bfla detection phase
* [post_api_security_internal_catalog_catalog_id_bfla_learning](#post_api_security_internal_catalog_catalog_id_bfla_learning) - Start new bfla learning phase
* [post_api_security_internal_catalog_catalog_id_bfla_reset](#post_api_security_internal_catalog_catalog_id_bfla_reset) - Reset bfla model
* [put_api_security_internal_catalog_catalog_id_bfla](#put_api_security_internal_catalog_catalog_id_bfla) - update BFLA info for this catalogId

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
    catalog_id='54c82f16-8a36-43c8-873e-484380b1f6b8',
)

res = s.bfla.delete_api_security_internal_catalog_catalog_id_bfla_detection(req)

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
    catalog_id='ca275a60-a04c-4495-8c69-9171b51c1bdb',
)

res = s.bfla.delete_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.delete_api_security_internal_catalog_catalog_id_bfla_learning_204_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                          | Type                                                                                                                                                               | Required                                                                                                                                                           | Description                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                                          | [operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest](../../models/operations/deleteapisecurityinternalcatalogcatalogidbflalearningrequest.md) | :heavy_check_mark:                                                                                                                                                 | The request object to use for the request.                                                                                                                         |


### Response

**[operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningResponse](../../models/operations/deleteapisecurityinternalcatalogcatalogidbflalearningresponse.md)**


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
    catalog_id='1cf4b888-ebdf-4c4c-8ca9-9bc7fc0b2dce',
)

res = s.bfla.get_api_security_internal_catalog_catalog_id_bfla(req)

if res.api_service_bfla_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/getapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/getapisecurityinternalcatalogcatalogidbflaresponse.md)**


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
        duration='veritatis',
    ),
    catalog_id='0873e42b-006d-4678-878b-a8581a58208c',
)

res = s.bfla.post_api_security_internal_catalog_catalog_id_bfla_detection(req)

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
        duration='enim',
    ),
    catalog_id='4fefa9c9-5f2e-4ac5-965d-307cfee81206',
)

res = s.bfla.post_api_security_internal_catalog_catalog_id_bfla_learning(req)

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
    catalog_id='e2813fa4-a41c-4480-93f2-132af03102d5',
)

res = s.bfla.post_api_security_internal_catalog_catalog_id_bfla_reset(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_reset_201_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest](../../models/operations/postapisecurityinternalcatalogcatalogidbflaresetrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.PostAPISecurityInternalCatalogCatalogIDBflaResetResponse](../../models/operations/postapisecurityinternalcatalogcatalogidbflaresetresponse.md)**


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
        end_time=dateutil.parser.isoparse('2022-09-13T22:56:49.685Z'),
        status=shared.APIServiceBflaInfoStatus.IN_PROGRESS_DETECTION,
        tags=[
            shared.APIServiceBflaTagInfo(
                is_legitimate=False,
                name='Kara Rolfson',
                paths=[
                    shared.APIServiceBflaPathInfo(
                        clients=[
                            shared.APIServiceBflaClientInfo(
                                external=False,
                                identifier='18bf9621-a6a4-4f77-a87e-e3e4be752c65',
                                is_legitimate=False,
                                last_observed=dateutil.parser.isoparse('2022-07-25T18:23:48.906Z'),
                                last_status_code=284885,
                                name='Julie Lakin',
                                namespace='expedita',
                                principles=[
                                    shared.APIServiceBflaPrincipleInfo(
                                        ip='libero',
                                        name='Joshua Schiller',
                                        principle_type='sint',
                                    ),
                                ],
                            ),
                        ],
                        is_legitimate=False,
                        method=shared.HTTPMethod.HEAD,
                        path='enim',
                    ),
                ],
            ),
        ],
    ),
    catalog_id='e0e8419d-8f84-4f14-8f3e-07edcc4aa5f3',
)

res = s.bfla.put_api_security_internal_catalog_catalog_id_bfla(req)

if res.put_api_security_internal_catalog_catalog_id_bfla_200_application_json_uuid_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/putapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/putapisecurityinternalcatalogcatalogidbflaresponse.md)**

