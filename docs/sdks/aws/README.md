# Aws
(*aws*)

## Overview

APIs used to change  credentials or return details about the  user's AWS environment

### Available Operations

* [get_aws_accounts](#get_aws_accounts) - Get a list of AWS accounts
* [get_aws_roles](#get_aws_roles) - Lists AWS role ARNs for the account
* [get_aws_tags](#get_aws_tags) - Get a list of AWS tag keys
* [get_aws_aws_account_id_regions](#get_aws_aws_account_id_regions) - Get a list of regions for the  AWS account
* [get_aws_aws_account_id_region_id_subnets](#get_aws_aws_account_id_region_id_subnets) - Get a list of AWS subnets for an AWS account and region
* [get_aws_aws_account_id_region_id_vpcs](#get_aws_aws_account_id_region_id_vpcs) - Get a list of VPCs for AWS accounts.
* [post_aws_roles](#post_aws_roles) - Add AWS role to the account
* [put_aws_roles_role_id_](#put_aws_roles_role_id_) - Change AWS role name

## get_aws_accounts

Returns a list of AWS accounts for this Secure Application account.


### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.aws.get_aws_accounts()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetAwsAccountsResponse](../../models/operations/getawsaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_roles

Lists AWS role ARNs for the account

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.aws.get_aws_roles()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetAwsRolesResponse](../../models/operations/getawsrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_tags

Get a list of AWS tag keys

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.aws.get_aws_tags()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetAwsTagsResponse](../../models/operations/getawstagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_aws_account_id_regions

Returns a list of regions for AWS account.


### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAwsAwsAccountIDRegionsRequest(
    aws_account_id='<value>',
)

res = s.aws.get_aws_aws_account_id_regions(req)

if res.strings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetAwsAwsAccountIDRegionsRequest](../../models/operations/getawsawsaccountidregionsrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetAwsAwsAccountIDRegionsResponse](../../models/operations/getawsawsaccountidregionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_aws_account_id_region_id_subnets

Get a list of AWS subnets for an AWS account and region

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAwsAwsAccountIDRegionIDSubnetsRequest(
    aws_account_id='<value>',
    region_id='<value>',
)

res = s.aws.get_aws_aws_account_id_region_id_subnets(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GetAwsAwsAccountIDRegionIDSubnetsRequest](../../models/operations/getawsawsaccountidregionidsubnetsrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.GetAwsAwsAccountIDRegionIDSubnetsResponse](../../models/operations/getawsawsaccountidregionidsubnetsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_aws_aws_account_id_region_id_vpcs

Returns a list of VPCs for an AWS account and region. These values are used to define a Secure Application environment.


### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAwsAwsAccountIDRegionIDVpcsRequest(
    aws_account_id='<value>',
    region_id='<value>',
)

res = s.aws.get_aws_aws_account_id_region_id_vpcs(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetAwsAwsAccountIDRegionIDVpcsRequest](../../models/operations/getawsawsaccountidregionidvpcsrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetAwsAwsAccountIDRegionIDVpcsResponse](../../models/operations/getawsawsaccountidregionidvpcsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_aws_roles

Upload a role ARN, that Secure Application will use to connect to the AWS account.

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.AWSRolePost(
    arn='<value>',
    name='<value>',
)

res = s.aws.post_aws_roles(req)

if res.aws_role is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.AWSRolePost](../../models/shared/awsrolepost.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.PostAwsRolesResponse](../../models/operations/postawsrolesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_aws_roles_role_id_

Change AWS role name

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutAwsRolesRoleIDRequest(
    aws_role_details=shared.AWSRoleDetails(
        name='<value>',
    ),
    role_id='81eef92a-b1e0-45da-ba61-a597d143757f',
)

res = s.aws.put_aws_roles_role_id_(req)

if res.aws_role is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PutAwsRolesRoleIDRequest](../../models/operations/putawsrolesroleidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PutAwsRolesRoleIDResponse](../../models/operations/putawsrolesroleidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
