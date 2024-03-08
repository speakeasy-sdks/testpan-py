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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteImagesIDRequest(
    id='1532f8e0-5c4e-41fa-a5bc-5aa03e071f17',
)

res = s.images_and_vulnerabilities.delete_images_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DeleteImagesIDRequest](../../models/operations/deleteimagesidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DeleteImagesIDResponse](../../models/operations/deleteimagesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_account_vulnerabilities_xlsx

Returns a xlsx file of images alongside to their vulnerabilities.

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetAccountVulnerabilitiesXlsxRequest()

res = s.images_and_vulnerabilities.get_account_vulnerabilities_xlsx(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetAccountVulnerabilitiesXlsxRequest](../../models/operations/getaccountvulnerabilitiesxlsxrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetAccountVulnerabilitiesXlsxResponse](../../models/operations/getaccountvulnerabilitiesxlsxresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images

Returns a list of images

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesRequest(
    sort_key=operations.GetImagesQueryParamSortKey.RISK,
)

res = s.images_and_vulnerabilities.get_images(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetImagesRequest](../../models/operations/getimagesrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetImagesResponse](../../models/operations/getimagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_images_hash

search for image hash in the account

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesImagesHashRequest()

res = s.images_and_vulnerabilities.get_images_images_hash(req)

if res.strings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetImagesImagesHashRequest](../../models/operations/getimagesimageshashrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetImagesImagesHashResponse](../../models/operations/getimagesimageshashresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_vulnerabilities_by_image_name_and_hash

Returns a list of vulnerabilities detected in the image

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesVulnerabilitiesByImageNameAndHashRequest(
    image_hash='<value>',
    image_name='<value>',
)

res = s.images_and_vulnerabilities.get_images_vulnerabilities_by_image_name_and_hash(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                    | [operations.GetImagesVulnerabilitiesByImageNameAndHashRequest](../../models/operations/getimagesvulnerabilitiesbyimagenameandhashrequest.md) | :heavy_check_mark:                                                                                                                           | The request object to use for the request.                                                                                                   |


### Response

**[operations.GetImagesVulnerabilitiesByImageNameAndHashResponse](../../models/operations/getimagesvulnerabilitiesbyimagenameandhashresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_id_

get an image

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesIDRequest(
    id='d118d3e1-8466-490a-a3b5-54afae983ffe',
)

res = s.images_and_vulnerabilities.get_images_id_(req)

if res.image_def_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetImagesIDRequest](../../models/operations/getimagesidrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetImagesIDResponse](../../models/operations/getimagesidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_image_id_dockerfile_scan_results

Returns a list of vulnerabilities detected in the  image

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesImageIDDockerfileScanResultsRequest(
    image_id='da882664-c35f-4933-94c4-06103746e14d',
)

res = s.images_and_vulnerabilities.get_images_image_id_dockerfile_scan_results(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.GetImagesImageIDDockerfileScanResultsRequest](../../models/operations/getimagesimageiddockerfilescanresultsrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.GetImagesImageIDDockerfileScanResultsResponse](../../models/operations/getimagesimageiddockerfilescanresultsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_image_id_image_layers

Returns a list of image layers

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesImageIDImageLayersRequest(
    image_id='15439eb8-81bd-4ffd-8863-3eb436058a37',
)

res = s.images_and_vulnerabilities.get_images_image_id_image_layers(req)

if res.image_layers is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetImagesImageIDImageLayersRequest](../../models/operations/getimagesimageidimagelayersrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetImagesImageIDImageLayersResponse](../../models/operations/getimagesimageidimagelayersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_image_id_packages

Returns a list of packages for a specific image

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesImageIDPackagesRequest(
    image_id='c2ee574a-71ae-4a8b-a2ff-c4930d365b60',
)

res = s.images_and_vulnerabilities.get_images_image_id_packages(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetImagesImageIDPackagesRequest](../../models/operations/getimagesimageidpackagesrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetImagesImageIDPackagesResponse](../../models/operations/getimagesimageidpackagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_image_id_sbom_path

Returns the path to the SBOM in cloud storage

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesImageIDSbomPathRequest(
    image_id='32f4442d-9f10-4117-a8a5-a2e7f00c922a',
)

res = s.images_and_vulnerabilities.get_images_image_id_sbom_path(req)

if res.image_sbom_path_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetImagesImageIDSbomPathRequest](../../models/operations/getimagesimageidsbompathrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.GetImagesImageIDSbomPathResponse](../../models/operations/getimagesimageidsbompathresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_images_image_id_vulnerabilities

Returns a list of vulnerabilities detected in the image

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.GetImagesImageIDVulnerabilitiesRequest(
    image_id='d0043143-505e-42fc-aacc-aa87ecde910e',
)

res = s.images_and_vulnerabilities.get_images_image_id_vulnerabilities(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetImagesImageIDVulnerabilitiesRequest](../../models/operations/getimagesimageidvulnerabilitiesrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetImagesImageIDVulnerabilitiesResponse](../../models/operations/getimagesimageidvulnerabilitiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_images

Define a New image hash

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.ImageDef()

res = s.images_and_vulnerabilities.post_images(req)

if res.image_def_get is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [shared.ImageDef](../../models/shared/imagedef.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.PostImagesResponse](../../models/operations/postimagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_images_approve

Approve an image hash

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostImagesApproveRequest(
    uuid_list=shared.UUIDList(),
    is_image_approved=False,
)

res = s.images_and_vulnerabilities.post_images_approve(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.PostImagesApproveRequest](../../models/operations/postimagesapproverequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PostImagesApproveResponse](../../models/operations/postimagesapproveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_images_image_id_dockerfile_scan_results_ignore

Add / remove a list of  UUIDs of dockerfileScanResults from ignored list

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostImagesImageIDDockerfileScanResultsIgnoreRequest(
    uuid_list=shared.UUIDList(),
    action_type=operations.ActionType.ADD,
    image_id='d411c9e4-3ee5-4293-ae87-474b2c192fe7',
)

res = s.images_and_vulnerabilities.post_images_image_id_dockerfile_scan_results_ignore(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                        | Type                                                                                                                                             | Required                                                                                                                                         | Description                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                                        | [operations.PostImagesImageIDDockerfileScanResultsIgnoreRequest](../../models/operations/postimagesimageiddockerfilescanresultsignorerequest.md) | :heavy_check_mark:                                                                                                                               | The request object to use for the request.                                                                                                       |


### Response

**[operations.PostImagesImageIDDockerfileScanResultsIgnoreResponse](../../models/operations/postimagesimageiddockerfilescanresultsignoreresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_images_image_id_vulnerabilities_ignore

Add / remove a list of  UUIDs of vulnerabilities from ignored list

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostImagesImageIDVulnerabilitiesIgnoreRequest(
    uuid_list=shared.UUIDList(),
    action_type=operations.QueryParamActionType.ADD,
    image_id='f4573288-079e-4a1b-a4ed-7631fc85bb9b',
)

res = s.images_and_vulnerabilities.post_images_image_id_vulnerabilities_ignore(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [operations.PostImagesImageIDVulnerabilitiesIgnoreRequest](../../models/operations/postimagesimageidvulnerabilitiesignorerequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PostImagesImageIDVulnerabilitiesIgnoreResponse](../../models/operations/postimagesimageidvulnerabilitiesignoreresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
