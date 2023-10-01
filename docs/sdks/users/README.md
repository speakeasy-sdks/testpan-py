# Users
(*users*)

## Overview

APIs used for login and password management

### Available Operations

* [delete_users_user_id_](#delete_users_user_id_) - Delete a user
* [get_operator_credentials](#get_operator_credentials) - get the credentials of the Secure Application Operator service user
* [get_users](#get_users) - List current users
* [get_users_user_id_access_tokens](#get_users_user_id_access_tokens) - Get the  access tokens for the user
* [get_users_user_id_delete_dependencies](#get_users_user_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified user
* [post_account_usage_status](#post_account_usage_status) - an api to get the account usage status
* [post_change_password](#post_change_password) - Change the password for the current user
* [post_login](#post_login) - Login
* [post_logout](#post_logout) - Log out
* [post_me](#post_me) - an api to get current logged in user info
* [post_users](#post_users) - Create a user
* [post_users_accept_eula](#post_users_accept_eula) - Accept the EULA
* [post_users_trial](#post_users_trial) - Create a trail user
* [put_users_user_id_](#put_users_user_id_) - Change user details

## delete_users_user_id_

Delete a user

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

req = operations.DeleteUsersUserIDRequest(
    user_id='2d4aef6d-76db-4c57-a2a3-fe8efd3db6e2',
)

res = s.users.delete_users_user_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteUsersUserIDRequest](../../models/operations/deleteusersuseridrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteUsersUserIDResponse](../../models/operations/deleteusersuseridresponse.md)**


## get_operator_credentials

get the credentials of the Secure Application Operator service user

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


res = s.users.get_operator_credentials()

if res.access_token is not None:
    # handle response
```


### Response

**[operations.GetOperatorCredentialsResponse](../../models/operations/getoperatorcredentialsresponse.md)**


## get_users

List current users

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

req = operations.GetUsersRequest(
    email='Martine_Welch@hotmail.com',
    roles=[
        operations.GetUsersRoles.ACCOUNT_ADMIN,
    ],
    username='Domenick_Schulist87',
)

res = s.users.get_users(req)

if res.user_displays is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUsersRequest](../../models/operations/getusersrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetUsersResponse](../../models/operations/getusersresponse.md)**


## get_users_user_id_access_tokens

Get the access tokens for the user, to access Secure Application

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

req = operations.GetUsersUserIDAccessTokensRequest(
    user_id='d48eca12-2332-4def-a816-08c21f5e1906',
)

res = s.users.get_users_user_id_access_tokens(req)

if res.access_token is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetUsersUserIDAccessTokensRequest](../../models/operations/getusersuseridaccesstokensrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetUsersUserIDAccessTokensResponse](../../models/operations/getusersuseridaccesstokensresponse.md)**


## get_users_user_id_delete_dependencies

get dependencies which need to be handled in order to delete specified user

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

req = operations.GetUsersUserIDDeleteDependenciesRequest(
    user_id='8a75ffe4-62b3-4153-829f-86055d39570f',
)

res = s.users.get_users_user_id_delete_dependencies(req)

if res.delete_dependency_element_user is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetUsersUserIDDeleteDependenciesRequest](../../models/operations/getusersuseriddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetUsersUserIDDeleteDependenciesResponse](../../models/operations/getusersuseriddeletedependenciesresponse.md)**


## post_account_usage_status

an api to get the account usage status

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


res = s.users.post_account_usage_status()

if res.usage_status is not None:
    # handle response
```


### Response

**[operations.PostAccountUsageStatusResponse](../../models/operations/postaccountusagestatusresponse.md)**


## post_change_password

Change the password for the current user

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

req = shared.ChangePasswordInfo(
    new_password='Clifton Tuna invoice',
    old_password='Loan',
)

res = s.users.post_change_password(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.ChangePasswordInfo](../../models/shared/changepasswordinfo.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostChangePasswordResponse](../../models/operations/postchangepasswordresponse.md)**


## post_login

Login

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

req = operations.PostLoginRequest(
    google_id_token='Paradigm Touring enthusiastically',
    token='gray',
)

res = s.users.post_login(req)

if res.user_login_info is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PostLoginRequest](../../models/operations/postloginrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostLoginResponse](../../models/operations/postloginresponse.md)**


## post_logout

Log out

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


res = s.users.post_logout()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostLogoutResponse](../../models/operations/postlogoutresponse.md)**


## post_me

an api to get current logged in user info

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


res = s.users.post_me()

if res.user_login_info is not None:
    # handle response
```


### Response

**[operations.PostMeResponse](../../models/operations/postmeresponse.md)**


## post_users

Create a new user. Must be admin user.


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

req = shared.UserInput(
    description='Cross-group reciprocal toolset',
    email='Erin_Wintheiser@hotmail.com',
    full_name='Mrs. Todd Halvorson',
    id='d86a2273-6c5e-406f-80e1-8a3ed58c3e0d',
    role=shared.Role.PORTSHIFT_AUDITOR,
    status=shared.UserStatus.DISABLED,
)

res = s.users.post_users(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.UserInput](../../models/shared/userinput.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.PostUsersResponse](../../models/operations/postusersresponse.md)**


## post_users_accept_eula

Accept the EULA

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


res = s.users.post_users_accept_eula()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostUsersAcceptEulaResponse](../../models/operations/postusersaccepteularesponse.md)**


## post_users_trial

Create a trail user

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

req = operations.PostUsersTrialRequest(
    trial_user=shared.TrialUser(
        company='Rohan and Sons',
        email='Tremaine.Bashirian@gmail.com',
        first_name='Sim',
        how_did_you_hear_about_us=shared.TrialUserHowDidYouHearAboutUs.ADVERTISING,
        job_title='Human Program Liaison',
        last_name='Kovacek',
        privacy_policy_and_terms_and_conditions_agreement=False,
    ),
    g_recaptcha_response='Automated',
)

res = s.users.post_users_trial(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PostUsersTrialRequest](../../models/operations/postuserstrialrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PostUsersTrialResponse](../../models/operations/postuserstrialresponse.md)**


## put_users_user_id_

Change user details

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

req = operations.PutUsersUserIDRequest(
    edit_user_input=shared.EditUserInput(
        description='Assimilated zero defect moratorium',
        full_name='Ms. Kathy Stanton',
        id='79a1c67b-61ff-41da-8536-101e994c1527',
        role=shared.Role.ACCOUNT_ADMIN,
        status=shared.EditUserStatus.DISABLED,
    ),
    user_id='04672250-5e17-4edb-8b8f-fdfce4dbd0b1',
)

res = s.users.put_users_user_id_(req)

if res.user is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PutUsersUserIDRequest](../../models/operations/putusersuseridrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutUsersUserIDResponse](../../models/operations/putusersuseridresponse.md)**
