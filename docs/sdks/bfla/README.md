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
    catalog_id='3d2f6c1c-29ba-4502-9cb8-4666b2e993b7',
)

res = s.bfla.delete_api_security_internal_catalog_catalog_id_bfla_detection(req)

if res.delete_api_security_internal_catalog_catalog_id_bfla_detection_204_application_json_uuid_string is not None:
    # handle response
    pass
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
    catalog_id='3ba770da-4891-4357-a360-0c0e060f5b0f',
)

res = s.bfla.delete_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.delete_api_security_internal_catalog_catalog_id_bfla_learning_204_application_json_uuid_string is not None:
    # handle response
    pass
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
    catalog_id='74e0c81f-ef10-4f23-b74f-8447d1953ccf',
)

res = s.bfla.get_api_security_internal_catalog_catalog_id_bfla(req)

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
        duration='Garden',
    ),
    catalog_id='e94464b0-ff0e-46fe-94ca-29162fc27770',
)

res = s.bfla.post_api_security_internal_catalog_catalog_id_bfla_detection(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_detection_201_application_json_uuid_string is not None:
    # handle response
    pass
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
        duration='South',
    ),
    catalog_id='fbc82f2c-9ea8-45a3-a6b5-2d888f26e15a',
)

res = s.bfla.post_api_security_internal_catalog_catalog_id_bfla_learning(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_learning_201_application_json_uuid_string is not None:
    # handle response
    pass
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
    catalog_id='2682814f-440b-4991-ae68-e4a1209728f3',
)

res = s.bfla.post_api_security_internal_catalog_catalog_id_bfla_reset(req)

if res.post_api_security_internal_catalog_catalog_id_bfla_reset_201_application_json_uuid_string is not None:
    # handle response
    pass
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
        status=shared.APIServiceBflaInfoStatus.NO_SPEC,
        tags=[
            shared.APIServiceBflaTagInfo(
                name='International',
                paths=[
                    shared.APIServiceBflaPathInfo(
                        clients=[
                            shared.APIServiceBflaClientInfo(
                                name='Human',
                                principles=[
                                    shared.APIServiceBflaPrincipleInfo(
                                        ip='252.50.185.52',
                                        name='sherbet',
                                        principle_type='Technician',
                                    ),
                                ],
                            ),
                        ],
                        method=shared.HTTPMethod.TRACE,
                        path='/usr/sbin',
                    ),
                ],
            ),
        ],
    ),
    catalog_id='442012ad-1459-4f87-a9c2-0110831cf060',
)

res = s.bfla.put_api_security_internal_catalog_catalog_id_bfla(req)

if res.put_api_security_internal_catalog_catalog_id_bfla_200_application_json_uuid_string is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest](../../models/operations/putapisecurityinternalcatalogcatalogidbflarequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.PutAPISecurityInternalCatalogCatalogIDBflaResponse](../../models/operations/putapisecurityinternalcatalogcatalogidbflaresponse.md)**

