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
    cloud_account_name='quam Legacy',
    max_results=1307.16,
    no_pagination=False,
    offset=8371.14,
    region='Wagon Arlington',
    sort_dir=operations.GetCloudAccountsSortDir.ASC,
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
    cloud_account_name='coordinated',
    cloud_accounts_ids_filter=[
        '13824322-22f0-4b89-ac2b-1bfba58c422a',
    ],
    download_as_xlsx=False,
    func_name=[
        'synthesizing',
    ],
    max_results=9594.89,
    offset=7413.73,
    policy_risk=[
        operations.GetServerlessFunctionsPolicyRisk.MEDIUM,
    ],
    region='transmit',
    result=[
        operations.GetServerlessFunctionsResult.DETECT,
    ],
    risk=[
        operations.GetServerlessFunctionsRisk.HIGH,
    ],
    secrets_risk=[
        operations.GetServerlessFunctionsSecretsRisk.RISK_IDENTIFIED,
    ],
    sort_dir=operations.GetServerlessFunctionsSortDir.ASC,
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
    cloud_account_name='Northwest',
    func_arn=[
        'South',
    ],
    region='Kia righteously Bronze',
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
    cloud_account_name='withdrawal Human',
    func_name=[
        'whiteboard',
    ],
    region='Avon gosh',
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
    max_results=8248.92,
    offset=7517.01,
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
    max_results=5376.87,
    offset=8734.72,
    sort_dir=operations.GetServerlessZipFilesSortDir.ASC,
    sort_key=operations.GetServerlessZipFilesSortKey.TIME,
    zip_name_filter='Gasoline',
    zip_sha256_filter='calm executive implement',
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
    max_results=4757.97,
    offset=8704.31,
    sort_dir=operations.GetServerlessZipFilesZipIDVulnerabilitiesSortDir.ASC,
    zip_id='40878f68-2a69-434d-bf1a-10ecad858b07',
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
        cloud_provider=shared.CloudProviderType.AWS,
        install_vulnerability_scanner=False,
        name='Bicycle',
        periodic_job_expression=shared.ServerlessPeriodicJobExpression(
            periodic_job_type=shared.ServerlessPeriodicJobExpressionPeriodicJobType.SERVERLESS_BY_DAYS_PERIODIC_JOB_EXPRESSION,
        ),
        regions=[
            'Division',
        ],
        security_threats=shared.CloudAccountSecurityThreats(
            data_access_risk=shared.ServerlessDataAccessRisk.MEDIUM,
            data_access_risk_count=719927,
            is_unused_function=False,
            policy_risk=shared.ServerlessPolicyRisk.NO_RISK,
            policy_risk_count=327969,
            publicly_accessible_risk=shared.ServerlessPubliclyAccessibleRisk.NO_RISK,
            publicly_accessible_risk_count=212197,
            secrets_risk=shared.ServerlessSecretsRisk.NO_KNOWN_RISK,
            secrets_risk_count=276225,
            unused_function_count=505048,
        ),
        validate_function=shared.CloudAccountValidateFunction.SIGNATURE_VALIDATION,
        vulnerabilities_summary=shared.VulnerabilitiesSummary(
            critical=866582,
            high=785242,
            low=794613,
            medium=453950,
            total=407496,
            unknown=594287,
        ),
    ),
    cloud_account_id='7a579ecd-c3c3-4cb0-b74b-a26ecaa06648',
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

