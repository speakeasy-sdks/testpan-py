# ImagesAndVulnerabilities
(*images_and_vulnerabilities*)

## Overview

APIs used to define and manage  image hashes

### Available Operations

* [delete_images_id_](#delete_images_id_) - Delete an image hash
* [get_account_vulnerabilities_xlsx](#get_account_vulnerabilities_xlsx) - Returns a xlsx file of images alongside to their vulnerabilities.
* [get_images](#get_images) - Returns a list of images
* [get_images_images_hash](#get_images_images_hash) - search for image hash in the account
* [get_images_vulnerabilities_by_image_name_and_hash](#get_images_vulnerabilities_by_image_name_and_hash) - Returns a list of vulnerabilities detected in the image
* [get_images_id_](#get_images_id_) - get an image
* [get_images_image_id_dockerfile_scan_results](#get_images_image_id_dockerfile_scan_results) - Returns a list of vulnerabilities detected in the  image
* [get_images_image_id_image_layers](#get_images_image_id_image_layers) - Returns a list of image layers
* [get_images_image_id_packages](#get_images_image_id_packages) - Returns a list of packages for a specific image
* [get_images_image_id_sbom_path](#get_images_image_id_sbom_path) - Returns the path to the SBOM in cloud storage
* [get_images_image_id_vulnerabilities](#get_images_image_id_vulnerabilities) - Returns a list of vulnerabilities detected in the image
* [post_images](#post_images) - Define a New image hash
* [post_images_approve](#post_images_approve) - Approve an image hash
* [post_images_image_id_dockerfile_scan_results_ignore](#post_images_image_id_dockerfile_scan_results_ignore) - Add / remove a list of  UUIDs of dockerfileScanResults from ignored list
* [post_images_image_id_vulnerabilities_ignore](#post_images_image_id_vulnerabilities_ignore) - Add / remove a list of  UUIDs of vulnerabilities from ignored list

## delete_images_id_

Delete an image hash

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

req = operations.DeleteImagesIDRequest(
    id='667aaf9b-bad1-485f-a431-d6bf5c838fbb',
)

res = s.images_and_vulnerabilities.delete_images_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteImagesIDRequest](../../models/operations/deleteimagesidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteImagesIDResponse](../../models/operations/deleteimagesidresponse.md)**


## get_account_vulnerabilities_xlsx

Returns a xlsx file of images alongside to their vulnerabilities.

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

req = operations.GetAccountVulnerabilitiesXlsxRequest(
    image_hash=[
        'totam',
    ],
    image_name=[
        'quod',
    ],
    image_tag=[
        'aspernatur',
    ],
    vulnerability_name='eaque',
)

res = s.images_and_vulnerabilities.get_account_vulnerabilities_xlsx(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAccountVulnerabilitiesXlsxRequest](../../models/operations/getaccountvulnerabilitiesxlsxrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAccountVulnerabilitiesXlsxResponse](../../models/operations/getaccountvulnerabilitiesxlsxresponse.md)**


## get_images

Returns a list of images

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

req = operations.GetImagesRequest(
    image_hash=[
        'impedit',
    ],
    image_name=[
        'nam',
    ],
    image_tag=[
        'ex',
    ],
    download_as_xlsx=False,
    max_results=4836.26,
    offset=9630.94,
    sort_dir=operations.GetImagesSortDir.DESC,
    sort_key=operations.GetImagesSortKey.IMAGE_NAME,
    vulnerability_name='distinctio',
)

res = s.images_and_vulnerabilities.get_images(req)

if res.image_def_gets is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetImagesRequest](../../models/operations/getimagesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetImagesResponse](../../models/operations/getimagesresponse.md)**


## get_images_images_hash

search for image hash in the account

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

req = operations.GetImagesImagesHashRequest(
    image_hash='eius',
    max_results=1764.18,
)

res = s.images_and_vulnerabilities.get_images_images_hash(req)

if res.get_images_images_hash_200_application_json_strings is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetImagesImagesHashRequest](../../models/operations/getimagesimageshashrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetImagesImagesHashResponse](../../models/operations/getimagesimageshashresponse.md)**


## get_images_vulnerabilities_by_image_name_and_hash

Returns a list of vulnerabilities detected in the image

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

req = operations.GetImagesVulnerabilitiesByImageNameAndHashRequest(
    image_hash='veniam',
    image_name='repudiandae',
    is_ignored=False,
    layer_id='99e6234c-9f7b-479d-beb7-7a5c38d4baf9',
    max_results=752.03,
    offset=9015.63,
    show_only_vulnerabilities_with_fix=False,
    sort_dir=operations.GetImagesVulnerabilitiesByImageNameAndHashSortDir.ASC,
)

res = s.images_and_vulnerabilities.get_images_vulnerabilities_by_image_name_and_hash(req)

if res.vulnerabilities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetImagesVulnerabilitiesByImageNameAndHashRequest](../../models/operations/getimagesvulnerabilitiesbyimagenameandhashrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetImagesVulnerabilitiesByImageNameAndHashResponse](../../models/operations/getimagesvulnerabilitiesbyimagenameandhashresponse.md)**


## get_images_id_

get an image

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

req = operations.GetImagesIDRequest(
    id='06ef890a-54b4-475f-96f5-6d385a3c4ac6',
)

res = s.images_and_vulnerabilities.get_images_id_(req)

if res.image_def_get is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetImagesIDRequest](../../models/operations/getimagesidrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetImagesIDResponse](../../models/operations/getimagesidresponse.md)**


## get_images_image_id_dockerfile_scan_results

Returns a list of vulnerabilities detected in the  image

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

req = operations.GetImagesImageIDDockerfileScanResultsRequest(
    image_id='31b99e26-ced8-4f9f-9b94-10f63bbf8178',
    is_ignored=False,
    max_results=2439.41,
    offset=4747.74,
    sort_dir=operations.GetImagesImageIDDockerfileScanResultsSortDir.DESC,
)

res = s.images_and_vulnerabilities.get_images_image_id_dockerfile_scan_results(req)

if res.dockerfile_scan_results is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetImagesImageIDDockerfileScanResultsRequest](../../models/operations/getimagesimageiddockerfilescanresultsrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.GetImagesImageIDDockerfileScanResultsResponse](../../models/operations/getimagesimageiddockerfilescanresultsresponse.md)**


## get_images_image_id_image_layers

Returns a list of image layers

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

req = operations.GetImagesImageIDImageLayersRequest(
    image_id='01afdd78-8624-4189-ab44-873f5033f19d',
    is_ignored=False,
    sort_dir=operations.GetImagesImageIDImageLayersSortDir.DESC,
)

res = s.images_and_vulnerabilities.get_images_image_id_image_layers(req)

if res.image_layers is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetImagesImageIDImageLayersRequest](../../models/operations/getimagesimageidimagelayersrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetImagesImageIDImageLayersResponse](../../models/operations/getimagesimageidimagelayersresponse.md)**


## get_images_image_id_packages

Returns a list of packages for a specific image

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

req = operations.GetImagesImageIDPackagesRequest(
    image_id='f125ce41-52ea-4b9c-97e5-224a6a0e123b',
)

res = s.images_and_vulnerabilities.get_images_image_id_packages(req)

if res.image_package_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetImagesImageIDPackagesRequest](../../models/operations/getimagesimageidpackagesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetImagesImageIDPackagesResponse](../../models/operations/getimagesimageidpackagesresponse.md)**


## get_images_image_id_sbom_path

Returns the path to the SBOM in cloud storage

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

req = operations.GetImagesImageIDSbomPathRequest(
    image_id='7847ec59-e1f6-47f3-84cc-e4b6d7696ff3',
)

res = s.images_and_vulnerabilities.get_images_image_id_sbom_path(req)

if res.image_sbom_path_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetImagesImageIDSbomPathRequest](../../models/operations/getimagesimageidsbompathrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetImagesImageIDSbomPathResponse](../../models/operations/getimagesimageidsbompathresponse.md)**


## get_images_image_id_vulnerabilities

Returns a list of vulnerabilities detected in the image

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

req = operations.GetImagesImageIDVulnerabilitiesRequest(
    image_id='c5747501-357e-444f-91f8-b084c3197e19',
    is_ignored=False,
    layer_id='3a245467-f948-474c-ad5c-c4972233e66b',
    max_results=8537.01,
    offset=5265.84,
    show_only_vulnerabilities_with_fix=False,
    sort_dir=operations.GetImagesImageIDVulnerabilitiesSortDir.DESC,
)

res = s.images_and_vulnerabilities.get_images_image_id_vulnerabilities(req)

if res.vulnerabilities is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetImagesImageIDVulnerabilitiesRequest](../../models/operations/getimagesimageidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetImagesImageIDVulnerabilitiesResponse](../../models/operations/getimagesimageidvulnerabilitiesresponse.md)**


## post_images

Define a New image hash

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

req = shared.ImageDefInput(
    image_hash='officiis',
    image_name='corporis',
    image_tags=[
        'repellendus',
    ],
    time_added=dateutil.parser.isoparse('2022-12-20T11:08:09.767Z'),
)

res = s.images_and_vulnerabilities.post_images(req)

if res.image_def_get is not None:
    # handle response
```

### Parameters

| Parameter                                                    | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request`                                                    | [shared.ImageDefInput](../../models/shared/imagedefinput.md) | :heavy_check_mark:                                           | The request object to use for the request.                   |


### Response

**[operations.PostImagesResponse](../../models/operations/postimagesresponse.md)**


## post_images_approve

Approve an image hash

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

req = operations.PostImagesApproveRequest(
    uuid_list=shared.UUIDList(
        uuid_list=[
            'b979ef20-3873-4205-90cc-c1096400313b',
        ],
    ),
    is_image_approved=False,
)

res = s.images_and_vulnerabilities.post_images_approve(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PostImagesApproveRequest](../../models/operations/postimagesapproverequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PostImagesApproveResponse](../../models/operations/postimagesapproveresponse.md)**


## post_images_image_id_dockerfile_scan_results_ignore

Add / remove a list of  UUIDs of dockerfileScanResults from ignored list

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

req = operations.PostImagesImageIDDockerfileScanResultsIgnoreRequest(
    uuid_list=shared.UUIDList(
        uuid_list=[
            '3e5044f6-5fe7-42dc-8077-d0cc3f408efc',
        ],
    ),
    action_type=operations.PostImagesImageIDDockerfileScanResultsIgnoreActionType.ADD,
    image_id='5ceb4d6e-1eae-40f7-9aed-f2acab58b991',
)

res = s.images_and_vulnerabilities.post_images_image_id_dockerfile_scan_results_ignore(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.PostImagesImageIDDockerfileScanResultsIgnoreRequest](../../models/operations/postimagesimageiddockerfilescanresultsignorerequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.PostImagesImageIDDockerfileScanResultsIgnoreResponse](../../models/operations/postimagesimageiddockerfilescanresultsignoreresponse.md)**


## post_images_image_id_vulnerabilities_ignore

Add / remove a list of  UUIDs of vulnerabilities from ignored list

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

req = operations.PostImagesImageIDVulnerabilitiesIgnoreRequest(
    uuid_list=shared.UUIDList(
        uuid_list=[
            'c926ddb5-8946-41e7-821c-be6d9502f0ea',
        ],
    ),
    action_type=operations.PostImagesImageIDVulnerabilitiesIgnoreActionType.REMOVE,
    image_id='30b69f7a-c2f7-42f8-8500-904911608207',
    snooze_time=operations.PostImagesImageIDVulnerabilitiesIgnoreSnoozeTime.MONTH,
)

res = s.images_and_vulnerabilities.post_images_image_id_vulnerabilities_ignore(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PostImagesImageIDVulnerabilitiesIgnoreRequest](../../models/operations/postimagesimageidvulnerabilitiesignorerequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PostImagesImageIDVulnerabilitiesIgnoreResponse](../../models/operations/postimagesimageidvulnerabilitiesignoreresponse.md)**

