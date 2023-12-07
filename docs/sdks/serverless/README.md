# Serverless
(*serverless*)

### Available Operations

* [delete_cloud_accounts_cloud_account_id_](#delete_cloud_accounts_cloud_account_id_) - Delete a cloud account
* [get_cloud_accounts](#get_cloud_accounts) - List all the cloud accounts on the system
* [get_cloud_accounts_azure_installation_details](#get_cloud_accounts_azure_installation_details) - Get the Azure installation details
* [get_cloud_accounts_installation_details](#get_cloud_accounts_installation_details) - Get the installation details
* [get_cloud_accounts_regions_aws](#get_cloud_accounts_regions_aws) - List all the possible regions of AWS
* [get_cloud_accounts_regions_azure](#get_cloud_accounts_regions_azure) - List all the possible regions of Azure
* [get_cloud_accounts_cloud_account_id_delete_dependencies](#get_cloud_accounts_cloud_account_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified cloud account
* [get_cloud_accounts_cloud_account_id_download_bundle](#get_cloud_accounts_cloud_account_id_download_bundle) - Get Secure Application installation script
* [get_serverless_functions](#get_serverless_functions) - Get serverless functions
* [get_serverless_functions_arns](#get_serverless_functions_arns) - Get serverless functions names
* [get_serverless_functions_names](#get_serverless_functions_names) - Get serverless functions names
* [get_serverless_functions_function_id_](#get_serverless_functions_function_id_) - Get Serverless Function by ID
* [get_serverless_functions_function_id_secrets](#get_serverless_functions_function_id_secrets) - Get Serverless Function secrets issues
* [get_serverless_functions_function_id_vulnerabilities](#get_serverless_functions_function_id_vulnerabilities) - Get Serverless Function Vulnerabilities by ID
* [get_serverless_zip_files](#get_serverless_zip_files) - Get serverless zip files that was scanned by cli
* [get_serverless_zip_files_zip_id_](#get_serverless_zip_files_zip_id_) - Get specific zip file record
* [get_serverless_zip_files_zip_id_packages](#get_serverless_zip_files_zip_id_packages) - Returns a list of packages for a specific serverless zip
* [get_serverless_zip_files_zip_id_vulnerabilities](#get_serverless_zip_files_zip_id_vulnerabilities) - Returns a list of vulnerabilities detected in the serverless zip
* [post_cloud_accounts_scan](#post_cloud_accounts_scan) - invoke cloud account scan
* [put_cloud_accounts_cloud_account_id_](#put_cloud_accounts_cloud_account_id_) - Edit cloud account definition

## delete_cloud_accounts_cloud_account_id_

Delete a cloud account

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

req = operations.DeleteCloudAccountsCloudAccountIDRequest(
    cloud_account_id='a4061d9a-ae48-48cc-a173-2eca65acca85',
)

res = s.serverless.delete_cloud_accounts_cloud_account_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteCloudAccountsCloudAccountIDRequest](../../models/operations/deletecloudaccountscloudaccountidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.DeleteCloudAccountsCloudAccountIDResponse](../../models/operations/deletecloudaccountscloudaccountidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts

List all the cloud accounts on the system

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

req = operations.GetCloudAccountsRequest(
    sort_key=operations.GetCloudAccountsQueryParamSortKey.LAST_SCANNED,
)

res = s.serverless.get_cloud_accounts(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCloudAccountsRequest](../../models/operations/getcloudaccountsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetCloudAccountsResponse](../../models/operations/getcloudaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts_azure_installation_details

Get the Azure installation details

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


res = s.serverless.get_cloud_accounts_azure_installation_details()

if res.serverless_azure_installation_details is not None:
    # handle response
    pass
```


### Response

**[operations.GetCloudAccountsAzureInstallationDetailsResponse](../../models/operations/getcloudaccountsazureinstallationdetailsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts_installation_details

Get the installation details

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


res = s.serverless.get_cloud_accounts_installation_details()

if res.serverless_installation_details is not None:
    # handle response
    pass
```


### Response

**[operations.GetCloudAccountsInstallationDetailsResponse](../../models/operations/getcloudaccountsinstallationdetailsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts_regions_aws

List all the possible regions of AWS

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


res = s.serverless.get_cloud_accounts_regions_aws()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetCloudAccountsRegionsAWSResponse](../../models/operations/getcloudaccountsregionsawsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts_regions_azure

List all the possible regions of Azure

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


res = s.serverless.get_cloud_accounts_regions_azure()

if res.strings is not None:
    # handle response
    pass
```


### Response

**[operations.GetCloudAccountsRegionsAzureResponse](../../models/operations/getcloudaccountsregionsazureresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts_cloud_account_id_delete_dependencies

get dependencies which need to be handled in order to delete specified cloud account

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

req = operations.GetCloudAccountsCloudAccountIDDeleteDependenciesRequest(
    cloud_account_id='64304886-9365-422a-8282-644a12d7387e',
)

res = s.serverless.get_cloud_accounts_cloud_account_id_delete_dependencies(req)

if res.cloud_account_delete_dependencies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.GetCloudAccountsCloudAccountIDDeleteDependenciesRequest](../../models/operations/getcloudaccountscloudaccountiddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.GetCloudAccountsCloudAccountIDDeleteDependenciesResponse](../../models/operations/getcloudaccountscloudaccountiddeletedependenciesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_cloud_accounts_cloud_account_id_download_bundle

In order to install, extract and run "./install_bundle.sh"

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

req = operations.GetCloudAccountsCloudAccountIDDownloadBundleRequest(
    cloud_account_id='78a9218a-bbdc-48dd-8c99-acaaac2d314e',
)

res = s.serverless.get_cloud_accounts_cloud_account_id_download_bundle(req)

if res.stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetCloudAccountsCloudAccountIDDownloadBundleRequest](../../models/operations/getcloudaccountscloudaccountiddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetCloudAccountsCloudAccountIDDownloadBundleResponse](../../models/operations/getcloudaccountscloudaccountiddownloadbundleresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_functions

Get serverless functions

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

req = operations.GetServerlessFunctionsRequest(
    cloud_accounts_ids_filter=[
        '2d213824-3222-42f0-b89a-c2b1bfba58c4',
    ],
    func_name=[
        'string',
    ],
    policy_risk=[
        operations.PolicyRisk.LOW,
    ],
    result=[
        operations.QueryParamResult.ALLOW,
    ],
    risk=[
        operations.QueryParamRisk.HIGH,
    ],
    secrets_risk=[
        operations.SecretsRisk.RISK_IDENTIFIED,
    ],
)

res = s.serverless.get_serverless_functions(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetServerlessFunctionsRequest](../../models/operations/getserverlessfunctionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetServerlessFunctionsResponse](../../models/operations/getserverlessfunctionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_functions_arns

Get serverless functions names

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

req = operations.GetServerlessFunctionsArnsRequest(
    func_arn=[
        'string',
    ],
)

res = s.serverless.get_serverless_functions_arns(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetServerlessFunctionsArnsRequest](../../models/operations/getserverlessfunctionsarnsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetServerlessFunctionsArnsResponse](../../models/operations/getserverlessfunctionsarnsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_functions_names

Get serverless functions names

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

req = operations.GetServerlessFunctionsNamesRequest(
    func_name=[
        'string',
    ],
)

res = s.serverless.get_serverless_functions_names(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetServerlessFunctionsNamesRequest](../../models/operations/getserverlessfunctionsnamesrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetServerlessFunctionsNamesResponse](../../models/operations/getserverlessfunctionsnamesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_functions_function_id_

Get Serverless Function by ID

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

req = operations.GetServerlessFunctionsFunctionIDRequest(
    function_id='c94885c8-e582-488b-bf74-bf3ac1e10be4',
)

res = s.serverless.get_serverless_functions_function_id_(req)

if res.serverless_function is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetServerlessFunctionsFunctionIDRequest](../../models/operations/getserverlessfunctionsfunctionidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetServerlessFunctionsFunctionIDResponse](../../models/operations/getserverlessfunctionsfunctionidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_functions_function_id_secrets

Get Serverless Function secrets issues

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

req = operations.GetServerlessFunctionsFunctionIDSecretsRequest(
    function_id='1200d55a-1387-4753-ab90-33c09b02720e',
)

res = s.serverless.get_serverless_functions_function_id_secrets(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetServerlessFunctionsFunctionIDSecretsRequest](../../models/operations/getserverlessfunctionsfunctionidsecretsrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetServerlessFunctionsFunctionIDSecretsResponse](../../models/operations/getserverlessfunctionsfunctionidsecretsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_functions_function_id_vulnerabilities

Get Serverless Function Vulnerabilities by ID

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

req = operations.GetServerlessFunctionsFunctionIDVulnerabilitiesRequest(
    function_id='2ad182ca-55b9-436d-935a-2584c6608fc0',
)

res = s.serverless.get_serverless_functions_function_id_vulnerabilities(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetServerlessFunctionsFunctionIDVulnerabilitiesRequest](../../models/operations/getserverlessfunctionsfunctionidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetServerlessFunctionsFunctionIDVulnerabilitiesResponse](../../models/operations/getserverlessfunctionsfunctionidvulnerabilitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_zip_files

Get serverless zip files that was scanned by cli

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

req = operations.GetServerlessZipFilesRequest()

res = s.serverless.get_serverless_zip_files(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetServerlessZipFilesRequest](../../models/operations/getserverlesszipfilesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetServerlessZipFilesResponse](../../models/operations/getserverlesszipfilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_zip_files_zip_id_

Get specific zip file record

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

req = operations.GetServerlessZipFilesZipIDRequest(
    zip_id='47af1679-7e54-41ca-b6c1-2fafc1426c1d',
)

res = s.serverless.get_serverless_zip_files_zip_id_(req)

if res.serverless_zip is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetServerlessZipFilesZipIDRequest](../../models/operations/getserverlesszipfileszipidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetServerlessZipFilesZipIDResponse](../../models/operations/getserverlesszipfileszipidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_zip_files_zip_id_packages

Returns a list of packages for a specific serverless zip

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

req = operations.GetServerlessZipFilesZipIDPackagesRequest(
    zip_id='8930b13e-93d3-4a51-9609-c730ba7092f4',
)

res = s.serverless.get_serverless_zip_files_zip_id_packages(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetServerlessZipFilesZipIDPackagesRequest](../../models/operations/getserverlesszipfileszipidpackagesrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetServerlessZipFilesZipIDPackagesResponse](../../models/operations/getserverlesszipfileszipidpackagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_serverless_zip_files_zip_id_vulnerabilities

Returns a list of vulnerabilities detected in the serverless zip

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

req = operations.GetServerlessZipFilesZipIDVulnerabilitiesRequest(
    zip_id='7d640878-f682-4a69-b4d3-f1a10ecad858',
)

res = s.serverless.get_serverless_zip_files_zip_id_vulnerabilities(req)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetServerlessZipFilesZipIDVulnerabilitiesRequest](../../models/operations/getserverlesszipfileszipidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetServerlessZipFilesZipIDVulnerabilitiesResponse](../../models/operations/getserverlesszipfileszipidvulnerabilitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## post_cloud_accounts_scan

invoke cloud account scan

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

req = shared.ServerlessScanConfig(
    cloud_accounts=[
        '458b5913-dc88-4dbf-ab7f-5674c6953077',
    ],
)

res = s.serverless.post_cloud_accounts_scan(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.ServerlessScanConfig](../../models/shared/serverlessscanconfig.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostCloudAccountsScanResponse](../../models/operations/postcloudaccountsscanresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## put_cloud_accounts_cloud_account_id_

Edit cloud account definition

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

req = operations.PutCloudAccountsCloudAccountIDRequest(
    cloud_account=shared.CloudAccountInput(
        periodic_job_expression=shared.ServerlessPeriodicJobExpression(
            periodic_job_type=shared.ServerlessPeriodicJobExpressionPeriodicJobType.SERVERLESS_BY_HOURS_PERIODIC_JOB_EXPRESSION,
        ),
        regions=[
            'string',
        ],
        security_threats=shared.CloudAccountSecurityThreats(),
        vulnerabilities_summary=shared.VulnerabilitiesSummary(),
    ),
    cloud_account_id='3c18ca7f-b155-4344-88dc-c7697a579ecd',
)

res = s.serverless.put_cloud_accounts_cloud_account_id_(req)

if res.cloud_account is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutCloudAccountsCloudAccountIDRequest](../../models/operations/putcloudaccountscloudaccountidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PutCloudAccountsCloudAccountIDResponse](../../models/operations/putcloudaccountscloudaccountidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
