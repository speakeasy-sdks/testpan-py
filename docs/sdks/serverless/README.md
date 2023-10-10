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
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.DeleteCloudAccountsCloudAccountIDRequest](../../models/operations/deletecloudaccountscloudaccountidrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.DeleteCloudAccountsCloudAccountIDResponse](../../models/operations/deletecloudaccountscloudaccountidresponse.md)**


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
    sort_key=operations.GetCloudAccountsSortKey.LAST_SCANNED,
)

res = s.serverless.get_cloud_accounts(req)

if res.cloud_accounts is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetCloudAccountsRequest](../../models/operations/getcloudaccountsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetCloudAccountsResponse](../../models/operations/getcloudaccountsresponse.md)**


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
```


### Response

**[operations.GetCloudAccountsAzureInstallationDetailsResponse](../../models/operations/getcloudaccountsazureinstallationdetailsresponse.md)**


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
```


### Response

**[operations.GetCloudAccountsInstallationDetailsResponse](../../models/operations/getcloudaccountsinstallationdetailsresponse.md)**


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

if res.aws_regions is not None:
    # handle response
```


### Response

**[operations.GetCloudAccountsRegionsAWSResponse](../../models/operations/getcloudaccountsregionsawsresponse.md)**


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

if res.get_cloud_accounts_regions_azure_200_application_json_strings is not None:
    # handle response
```


### Response

**[operations.GetCloudAccountsRegionsAzureResponse](../../models/operations/getcloudaccountsregionsazureresponse.md)**


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
```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                | [operations.GetCloudAccountsCloudAccountIDDeleteDependenciesRequest](../../models/operations/getcloudaccountscloudaccountiddeletedependenciesrequest.md) | :heavy_check_mark:                                                                                                                                       | The request object to use for the request.                                                                                                               |


### Response

**[operations.GetCloudAccountsCloudAccountIDDeleteDependenciesResponse](../../models/operations/getcloudaccountscloudaccountiddeletedependenciesresponse.md)**


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

if res.get_cloud_accounts_cloud_account_id_download_bundle_200_application_json_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.GetCloudAccountsCloudAccountIDDownloadBundleRequest](../../models/operations/getcloudaccountscloudaccountiddownloadbundlerequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.GetCloudAccountsCloudAccountIDDownloadBundleResponse](../../models/operations/getcloudaccountscloudaccountiddownloadbundleresponse.md)**


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
        'Electronics',
    ],
    policy_risk=[
        operations.GetServerlessFunctionsPolicyRisk.HIGH,
    ],
    result=[
        operations.GetServerlessFunctionsResult.DETECT,
    ],
    risk=[
        operations.GetServerlessFunctionsRisk.CRITICAL,
    ],
    secrets_risk=[
        operations.GetServerlessFunctionsSecretsRisk.RISK_IDENTIFIED,
    ],
)

res = s.serverless.get_serverless_functions(req)

if res.serverless_functions is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetServerlessFunctionsRequest](../../models/operations/getserverlessfunctionsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetServerlessFunctionsResponse](../../models/operations/getserverlessfunctionsresponse.md)**


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
        'Northeast',
    ],
)

res = s.serverless.get_serverless_functions_arns(req)

if res.serverless_function_arns is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetServerlessFunctionsArnsRequest](../../models/operations/getserverlessfunctionsarnsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetServerlessFunctionsArnsResponse](../../models/operations/getserverlessfunctionsarnsresponse.md)**


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
        'Hermaphrodite',
    ],
)

res = s.serverless.get_serverless_functions_names(req)

if res.serverless_function_names is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetServerlessFunctionsNamesRequest](../../models/operations/getserverlessfunctionsnamesrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetServerlessFunctionsNamesResponse](../../models/operations/getserverlessfunctionsnamesresponse.md)**


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
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetServerlessFunctionsFunctionIDRequest](../../models/operations/getserverlessfunctionsfunctionidrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetServerlessFunctionsFunctionIDResponse](../../models/operations/getserverlessfunctionsfunctionidresponse.md)**


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

if res.serverless_function_secret_issues is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GetServerlessFunctionsFunctionIDSecretsRequest](../../models/operations/getserverlessfunctionsfunctionidsecretsrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GetServerlessFunctionsFunctionIDSecretsResponse](../../models/operations/getserverlessfunctionsfunctionidsecretsresponse.md)**


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

if res.vulnerabilities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                              | Type                                                                                                                                                   | Required                                                                                                                                               | Description                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                              | [operations.GetServerlessFunctionsFunctionIDVulnerabilitiesRequest](../../models/operations/getserverlessfunctionsfunctionidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                                                     | The request object to use for the request.                                                                                                             |


### Response

**[operations.GetServerlessFunctionsFunctionIDVulnerabilitiesResponse](../../models/operations/getserverlessfunctionsfunctionidvulnerabilitiesresponse.md)**


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

if res.serverless_zips is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetServerlessZipFilesRequest](../../models/operations/getserverlesszipfilesrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetServerlessZipFilesResponse](../../models/operations/getserverlesszipfilesresponse.md)**


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
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetServerlessZipFilesZipIDRequest](../../models/operations/getserverlesszipfileszipidrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetServerlessZipFilesZipIDResponse](../../models/operations/getserverlesszipfileszipidresponse.md)**


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

if res.image_package_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetServerlessZipFilesZipIDPackagesRequest](../../models/operations/getserverlesszipfileszipidpackagesrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetServerlessZipFilesZipIDPackagesResponse](../../models/operations/getserverlesszipfileszipidpackagesresponse.md)**


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

if res.vulnerabilities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                  | Type                                                                                                                                       | Required                                                                                                                                   | Description                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                  | [operations.GetServerlessZipFilesZipIDVulnerabilitiesRequest](../../models/operations/getserverlesszipfileszipidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                                         | The request object to use for the request.                                                                                                 |


### Response

**[operations.GetServerlessZipFilesZipIDVulnerabilitiesResponse](../../models/operations/getserverlesszipfileszipidvulnerabilitiesresponse.md)**


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
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.ServerlessScanConfig](../../models/shared/serverlessscanconfig.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostCloudAccountsScanResponse](../../models/operations/postcloudaccountsscanresponse.md)**


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
    cloud_account_input=shared.CloudAccountInput(
        periodic_job_expression=shared.ServerlessPeriodicJobExpression(
            periodic_job_type=shared.ServerlessPeriodicJobExpressionPeriodicJobType.SERVERLESS_BY_HOURS_PERIODIC_JOB_EXPRESSION,
        ),
        regions=[
            'Cheese',
        ],
        security_threats=shared.CloudAccountSecurityThreats(),
        vulnerabilities_summary=shared.VulnerabilitiesSummary(),
    ),
    cloud_account_id='18ca7fb1-5534-4488-9cc7-697a579ecdc3',
)

res = s.serverless.put_cloud_accounts_cloud_account_id_(req)

if res.cloud_account is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.PutCloudAccountsCloudAccountIDRequest](../../models/operations/putcloudaccountscloudaccountidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PutCloudAccountsCloudAccountIDResponse](../../models/operations/putcloudaccountscloudaccountidresponse.md)**

