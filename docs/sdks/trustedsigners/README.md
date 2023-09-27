# TrustedSigners
(*trusted_signers*)

## Overview

APIs used to  define and manage trusted signers

### Available Operations

* [delete_trusted_signers_trusted_signer_id_](#delete_trusted_signers_trusted_signer_id_) - Delete a trusted signer
* [get_trusted_signers](#get_trusted_signers) - Get a list of defined trusted signers
* [get_trusted_signers_trusted_signer_id_](#get_trusted_signers_trusted_signer_id_) - get existing trusted signer
* [post_trusted_signers](#post_trusted_signers) - Add new trusted signer
* [put_trusted_signers_trusted_signer_id_](#put_trusted_signers_trusted_signer_id_) - edit existing trusted signer

## delete_trusted_signers_trusted_signer_id_

Delete a trusted signer

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

req = operations.DeleteTrustedSignersTrustedSignerIDRequest(
    trusted_signer_id='b99a550a-656e-4d33-bbb0-ce8aa65432a9',
)

res = s.trusted_signers.delete_trusted_signers_trusted_signer_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTrustedSignersTrustedSignerIDRequest](../../models/operations/deletetrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeleteTrustedSignersTrustedSignerIDResponse](../../models/operations/deletetrustedsignerstrustedsigneridresponse.md)**


## get_trusted_signers

Get a list of defined trusted signers

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

req = operations.GetTrustedSignersRequest(
    sort_dir=operations.GetTrustedSignersSortDir.DESC,
    sort_key=operations.GetTrustedSignersSortKey.NAME,
)

res = s.trusted_signers.get_trusted_signers(req)

if res.trusted_signers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetTrustedSignersRequest](../../models/operations/gettrustedsignersrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetTrustedSignersResponse](../../models/operations/gettrustedsignersresponse.md)**


## get_trusted_signers_trusted_signer_id_

get existing trusted signer

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

req = operations.GetTrustedSignersTrustedSignerIDRequest(
    trusted_signer_id='6eb7e14c-a564-4089-9500-97019a48f88e',
)

res = s.trusted_signers.get_trusted_signers_trusted_signer_id_(req)

if res.trusted_signer is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTrustedSignersTrustedSignerIDRequest](../../models/operations/gettrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTrustedSignersTrustedSignerIDResponse](../../models/operations/gettrustedsignerstrustedsigneridresponse.md)**


## post_trusted_signers

Add new trusted signer

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

req = shared.TrustedSignerInput(
    keys=[
        shared.TrustedSignerKey(
            key='impedit',
            name='Ron Ratke',
        ),
    ],
    name='Mr. Elaine Turcotte Jr.',
    trusted_signer_cloud_accounts=[
        shared.TrustedSignerCloudAccountInput(
            id='5d389081-62c6-4beb-a8a0-f657b7d03a14',
            status=shared.TrustedSignerClusterStatus.WARNING,
            validation=shared.TrustedSignerClusterValidation.SIGNATURE,
        ),
    ],
    trusted_signer_clusters=[
        shared.TrustedSignerClusterInput(
            id='f8de30f0-69d8-4106-98d9-7e152297510d',
            status=shared.TrustedSignerClusterStatus.WARNING,
            validation=shared.TrustedSignerClusterValidation.HASH,
        ),
    ],
)

res = s.trusted_signers.post_trusted_signers(req)

if res.trusted_signer is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.TrustedSignerInput](../../models/shared/trustedsignerinput.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostTrustedSignersResponse](../../models/operations/posttrustedsignersresponse.md)**


## put_trusted_signers_trusted_signer_id_

edit existing trusted signer

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

req = operations.PutTrustedSignersTrustedSignerIDRequest(
    trusted_signer_input=shared.TrustedSignerInput(
        keys=[
            shared.TrustedSignerKey(
                key='voluptatem',
                name='Gloria Christiansen',
            ),
        ],
        name='Della Ruecker DDS',
        trusted_signer_cloud_accounts=[
            shared.TrustedSignerCloudAccountInput(
                id='2a702bb9-7ee1-402d-a2de-35f8e01bf33e',
                status=shared.TrustedSignerClusterStatus.WARNING,
                validation=shared.TrustedSignerClusterValidation.HASH,
            ),
        ],
        trusted_signer_clusters=[
            shared.TrustedSignerClusterInput(
                id='b45402ac-1704-4bf1-8c9f-c61aae5eb5f0',
                status=shared.TrustedSignerClusterStatus.WARNING,
                validation=shared.TrustedSignerClusterValidation.SIGNATURE,
            ),
        ],
    ),
    trusted_signer_id='92b5744d-08a2-4267-aaee-79e3c71ad31b',
)

res = s.trusted_signers.put_trusted_signers_trusted_signer_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTrustedSignersTrustedSignerIDRequest](../../models/operations/puttrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PutTrustedSignersTrustedSignerIDResponse](../../models/operations/puttrustedsignerstrustedsigneridresponse.md)**

