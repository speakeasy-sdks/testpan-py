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
    token_id='2fc9f484-4225-4e75-b796-065c0efa6f93',
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
    max_results=7302.83,
    no_pagination=False,
    offset=5639.37,
    sort_dir=operations.GetTokensSortDir.ASC,
    sort_key=operations.GetTokensSortKey.EXPIRATION_DATE,
    token_name='fuga',
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
        '1b8c95be-1254-4b73-9f4f-e77210d1f655',
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
    token_id='8c99c722-d2bc-40f9-8087-d9caae042dd7',
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
        'caac9b4c-aa1c-4fe9-a15d-f903907f3783',
    ],
    attribute_name='ab',
    attribute_type=shared.TokenAttributeType.QUERY_PARAM,
    expiration_date=dateutil.parser.isoparse('2022-08-12T23:07:32.354Z'),
    http_path='fugiat',
    id='42e54a85-4665-497c-9023-3c1471d51aaa',
    name='Desiree Swaniawski',
    vault_secret_path='laborum',
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
            'bd6487c5-fc2b-4862-a00b-ef69e1001576',
        ],
        attribute_name='dolor',
        attribute_type=shared.TokenAttributeType.REQUEST_HEADER,
        expiration_date=dateutil.parser.isoparse('2021-04-25T20:11:43.979Z'),
        http_path='fuga',
        id='7afded84-a35a-4412-b8e1-a735ac26ae33',
        name='Dexter Wunsch',
        vault_secret_path='dicta',
    ),
    token_id='a8f46bca-1106-4fe9-a5b7-11d08cf88ec9',
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

