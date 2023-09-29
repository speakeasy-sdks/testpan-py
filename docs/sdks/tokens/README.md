# Tokens
(*tokens*)

### Available Operations

* [delete_tokens_token_id_](#delete_tokens_token_id_) - Delete token
* [get_tokens](#get_tokens) - Get tokens
* [get_tokens_info](#get_tokens_info) - Get tokens by Ids
* [get_tokens_token_id_delete_dependencies](#get_tokens_token_id_delete_dependencies) - get dependancies which need to be handled in order to delete specified token
* [post_tokens](#post_tokens) - Add new token
* [put_tokens_token_id_](#put_tokens_token_id_) - Edit token

## delete_tokens_token_id_

Delete token

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

req = operations.DeleteTokensTokenIDRequest(
    token_id='b10248b8-2d53-4623-885c-a738cc4f3785',
)

res = s.tokens.delete_tokens_token_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteTokensTokenIDRequest](../../models/operations/deletetokenstokenidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.DeleteTokensTokenIDResponse](../../models/operations/deletetokenstokenidresponse.md)**


## get_tokens

Get tokens

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

req = operations.GetTokensRequest(
    max_results=681.78,
    no_pagination=False,
    offset=7366.65,
    sort_dir=operations.GetTokensSortDir.ASC,
    sort_key='what',
    token_name='policy Rustic',
)

res = s.tokens.get_tokens(req)

if res.tokens is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetTokensRequest](../../models/operations/gettokensrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetTokensResponse](../../models/operations/gettokensresponse.md)**


## get_tokens_info

Get tokens by Ids

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

req = operations.GetTokensInfoRequest(
    tokens_ids=[
        '17c3fed3-a3bf-4acc-82ca-e618f8f9bdf3',
    ],
)

res = s.tokens.get_tokens_info(req)

if res.api_token_infos is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetTokensInfoRequest](../../models/operations/gettokensinforequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetTokensInfoResponse](../../models/operations/gettokensinforesponse.md)**


## get_tokens_token_id_delete_dependencies

get dependancies which need to be handled in order to delete specified token

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

req = operations.GetTokensTokenIDDeleteDependenciesRequest(
    token_id='8e7108bc-33f0-4915-b49d-5a4a26ffa567',
)

res = s.tokens.get_tokens_token_id_delete_dependencies(req)

if res.token_delete_dependencies is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetTokensTokenIDDeleteDependenciesRequest](../../models/operations/gettokenstokeniddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetTokensTokenIDDeleteDependenciesResponse](../../models/operations/gettokenstokeniddeletedependenciesresponse.md)**


## post_tokens

Add new token

### Example Usage

```python
import pan
import dateutil.parser
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = shared.Token(
    apis=[
        '06eb110c-ef48-45c9-b334-9ef284ebe70b',
    ],
    attribute_name='offensive flexibility Gate',
    attribute_type=shared.TokenAttributeType.REQUEST_HEADER,
    expiration_date=dateutil.parser.isoparse('2022-12-06T03:02:47.254Z'),
    http_path='Gasoline Bicycle',
    id='15c6181f-23a7-44d2-945a-aec34929a503',
    name='Cyclocross',
    vault_secret_path='intermediate array',
)

res = s.tokens.post_tokens(req)

if res.token is not None:
    # handle response
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `request`                                    | [shared.Token](../../models/shared/token.md) | :heavy_check_mark:                           | The request object to use for the request.   |


### Response

**[operations.PostTokensResponse](../../models/operations/posttokensresponse.md)**


## put_tokens_token_id_

Edit token

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

req = operations.PutTokensTokenIDRequest(
    token=shared.Token(
        apis=[
            '92f997c4-3e7b-4827-80b5-81f98e4dc9a1',
        ],
        attribute_name='ah card Mercedes',
        attribute_type=shared.TokenAttributeType.REQUEST_HEADER,
        expiration_date=dateutil.parser.isoparse('2023-05-19T15:11:35.927Z'),
        http_path='Ball',
        id='6d3d22b8-df11-4333-9e59-e4bbc71d1a3f',
        name='deposit Checking Rap',
        vault_secret_path='Chevrolet error',
    ),
    token_id='650a257d-f5fe-417c-b321-bf84e462e505',
)

res = s.tokens.put_tokens_token_id_(req)

if res.token is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PutTokensTokenIDRequest](../../models/operations/puttokenstokenidrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PutTokensTokenIDResponse](../../models/operations/puttokenstokenidresponse.md)**

