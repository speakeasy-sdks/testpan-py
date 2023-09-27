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
    cloud_account_id='650edf22-a94d-420e-890e-a41d1f465e85',
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
    cloud_account_name='ab',
    max_results=3246,
    no_pagination=False,
    offset=3916.67,
    region='repellat',
    sort_dir=operations.GetCloudAccountsSortDir.DESC,
    sort_key=operations.GetCloudAccountsSortKey.NAME,
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
    cloud_account_id='73fdf54f-dd5e-4a95-8339-8dafb42a8d63',
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
    cloud_account_id='388e4d80-39ea-45f9-b18a-244fd619039d',
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
    cloud_account_name='dolorum',
    cloud_accounts_ids_filter=[
        'cd38ed0d-c671-4dc7-b1e3-af15920c90d1',
    ],
    download_as_xlsx=False,
    func_name=[
        'cum',
    ],
    max_results=2975.19,
    offset=6156.98,
    policy_risk=[
        operations.GetServerlessFunctionsPolicyRisk.LOW,
    ],
    region='dicta',
    result=[
        operations.GetServerlessFunctionsResult.BLOCK,
    ],
    risk=[
        operations.GetServerlessFunctionsRisk.LOW,
    ],
    secrets_risk=[
        operations.GetServerlessFunctionsSecretsRisk.RISK_IDENTIFIED,
    ],
    sort_dir=operations.GetServerlessFunctionsSortDir.DESC,
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
    cloud_account_name='totam',
    func_arn=[
        'provident',
    ],
    region='maxime',
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
    cloud_account_name='totam',
    func_name=[
        'id',
    ],
    region='neque',
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
    function_id='2639da5b-7b69-402b-881a-94f643664a8f',
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
    function_id='0af8c691-d732-4d9f-baf9-476a2ae8dcc5',
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
    function_id='0c8a3512-c737-4848-9307-50a00e966ec7',
    max_results=2124.05,
    offset=4311.08,
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

req = operations.GetServerlessZipFilesRequest(
    max_results=8215.79,
    offset=2959.12,
    sort_dir=operations.GetServerlessZipFilesSortDir.ASC,
    sort_key=operations.GetServerlessZipFilesSortKey.TIME,
    zip_name_filter='omnis',
    zip_sha256_filter='quaerat',
)

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
    zip_id='398c783c-9239-48ed-bd3a-b7ca3c5ca864',
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
    zip_id='9a70cfd5-d698-49b7-a064-51077d19ea83',
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
    max_results=8178.07,
    offset=2619.53,
    sort_dir=operations.GetServerlessZipFilesZipIDVulnerabilitiesSortDir.DESC,
    zip_id='2ed14b8a-2c19-4545-85e9-55dcc185ea49',
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
        '01c7c43a-d2da-4a78-8aba-3d230edf7381',
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
        cloud_provider=shared.CloudProviderType.AWS,
        install_vulnerability_scanner=False,
        name='Albert Bruen',
        periodic_job_expression=shared.ServerlessPeriodicJobExpression(
            periodic_job_type=shared.ServerlessPeriodicJobExpressionPeriodicJobType.SERVERLESS_BY_DAYS_PERIODIC_JOB_EXPRESSION,
        ),
        regions=[
            'consequuntur',
        ],
        security_threats=shared.CloudAccountSecurityThreats(
            data_access_risk=shared.ServerlessDataAccessRisk.MEDIUM,
            data_access_risk_count=858317,
            is_unused_function=False,
            policy_risk=shared.ServerlessPolicyRisk.MEDIUM,
            policy_risk_count=908916,
            publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.MEDIUM,
            publicly_accessible_risk_count=313305,
            secrets_risk=shared.ServerlessSecretsRisk.NO_KNOWN_RISK,
            secrets_risk_count=331703,
            unused_function_count=28088,
        ),
        validate_function=shared.CloudAccountValidateFunction.SIGNATURE_VALIDATION,
        vulnerabilities_summary=shared.VulnerabilitiesSummary(
            critical=426152,
            high=136036,
            low=85002,
            medium=781003,
            total=322054,
            unknown=533096,
        ),
    ),
    cloud_account_id='f4d73965-64c2-40a0-b11a-961d24a7dbb8',
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

