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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteTrustedSignersTrustedSignerIDRequest(
    trusted_signer_id='72a0c357-f09f-4b54-84ce-1c9dc40be52b',
)

res = s.trusted_signers.delete_trusted_signers_trusted_signer_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.DeleteTrustedSignersTrustedSignerIDRequest](../../models/operations/deletetrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.DeleteTrustedSignersTrustedSignerIDResponse](../../models/operations/deletetrustedsignerstrustedsigneridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_trusted_signers

Get a list of defined trusted signers

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetTrustedSignersRequest()

res = s.trusted_signers.get_trusted_signers(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetTrustedSignersRequest](../../models/operations/gettrustedsignersrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetTrustedSignersResponse](../../models/operations/gettrustedsignersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_trusted_signers_trusted_signer_id_

get existing trusted signer

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetTrustedSignersTrustedSignerIDRequest(
    trusted_signer_id='3d8f6f9a-2b35-44bb-82c6-f820a67d0e04',
)

res = s.trusted_signers.get_trusted_signers_trusted_signer_id_(req)

if res.trusted_signer is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetTrustedSignersTrustedSignerIDRequest](../../models/operations/gettrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetTrustedSignersTrustedSignerIDResponse](../../models/operations/gettrustedsignerstrustedsigneridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_trusted_signers

Add new trusted signer

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TrustedSignerInput(
    name='<value>',
)

res = s.trusted_signers.post_trusted_signers(req)

if res.trusted_signer is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.TrustedSignerInput](../../models/shared/trustedsignerinput.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostTrustedSignersResponse](../../models/operations/posttrustedsignersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_trusted_signers_trusted_signer_id_

edit existing trusted signer

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutTrustedSignersTrustedSignerIDRequest(
    trusted_signer=shared.TrustedSignerInput(
        name='<value>',
    ),
    trusted_signer_id='8d323c1d-de95-475d-a823-90f3ebb00bb0',
)

res = s.trusted_signers.put_trusted_signers_trusted_signer_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.PutTrustedSignersTrustedSignerIDRequest](../../models/operations/puttrustedsignerstrustedsigneridrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PutTrustedSignersTrustedSignerIDResponse](../../models/operations/puttrustedsignerstrustedsigneridresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
