# PspProfiles
(*psp_profiles*)

## Overview

APIs used to manage pod security standards profiles on Secure Application

### Available Operations

* [delete_pod_security_policy_profiles_profile_id_](#delete_pod_security_policy_profiles_profile_id_) - Delete a pod security policy standards
* [delete_seccomp_profiles_profile_id_](#delete_seccomp_profiles_profile_id_) - Delete a seccomp profile
* [get_pod_security_policy_profiles](#get_pod_security_policy_profiles) - Get all the pod security standards profiles on the system
* [get_seccomp_profiles](#get_seccomp_profiles) - Get all the seccomp profiles on the system
* [post_pod_security_policy_profiles](#post_pod_security_policy_profiles) - Create a new pod security standards
* [post_pod_security_policy_profiles_batch](#post_pod_security_policy_profiles_batch) - Add a number of Pod Security Standards
* [post_seccomp_profiles](#post_seccomp_profiles) - Add seccomp profile
* [put_pod_security_policy_profiles_profile_id_](#put_pod_security_policy_profiles_profile_id_) - Change pod security standards profile
* [put_seccomp_profiles_profile_id_](#put_seccomp_profiles_profile_id_) - Change seccomp profile

## delete_pod_security_policy_profiles_profile_id_

Delete a pod security policy standards

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeletePodSecurityPolicyProfilesProfileIDRequest(
    profile_id='bb90cc1f-4444-454a-8574-313c05003108',
)

res = s.psp_profiles.delete_pod_security_policy_profiles_profile_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.DeletePodSecurityPolicyProfilesProfileIDRequest](../../models/operations/deletepodsecuritypolicyprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.DeletePodSecurityPolicyProfilesProfileIDResponse](../../models/operations/deletepodsecuritypolicyprofilesprofileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_seccomp_profiles_profile_id_

Delete a seccomp profile

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteSeccompProfilesProfileIDRequest(
    profile_id='4cc0f6a2-ff01-4311-a20d-d6510a1ff69a',
)

res = s.psp_profiles.delete_seccomp_profiles_profile_id_(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteSeccompProfilesProfileIDRequest](../../models/operations/deleteseccompprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteSeccompProfilesProfileIDResponse](../../models/operations/deleteseccompprofilesprofileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_pod_security_policy_profiles

Get all the pod security standards profiles on the system

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.psp_profiles.get_pod_security_policy_profiles()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetPodSecurityPolicyProfilesResponse](../../models/operations/getpodsecuritypolicyprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_seccomp_profiles

Get all the seccomp profiles on the system

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.psp_profiles.get_seccomp_profiles()

if res.classes is not None:
    # handle response
    pass

```


### Response

**[operations.GetSeccompProfilesResponse](../../models/operations/getseccompprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_pod_security_policy_profiles

Create a new pod security standards

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.PodSecurityPolicy(
    fs_group=shared.RunAsGroupStrategyOptions(),
    name='<value>',
    run_as_user=shared.RunAsUserStrategyOptions(),
    supplemental_groups=shared.RunAsGroupStrategyOptions(),
)

res = s.psp_profiles.post_pod_security_policy_profiles(req)

if res.pod_security_policy is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.PodSecurityPolicy](../../models/shared/podsecuritypolicy.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.PostPodSecurityPolicyProfilesResponse](../../models/operations/postpodsecuritypolicyprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_pod_security_policy_profiles_batch

Add a number of new Pod Security Standards Profiles.


### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = [
    shared.PodSecurityPolicy(
        fs_group=shared.RunAsGroupStrategyOptions(),
        name='<value>',
        run_as_user=shared.RunAsUserStrategyOptions(),
        supplemental_groups=shared.RunAsGroupStrategyOptions(),
    ),
]

res = s.psp_profiles.post_pod_security_policy_profiles_batch(req)

if res.classes is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `request`                                          | [List[shared.PodSecurityPolicy]](../../models/.md) | :heavy_check_mark:                                 | The request object to use for the request.         |


### Response

**[operations.PostPodSecurityPolicyProfilesBatchResponse](../../models/operations/postpodsecuritypolicyprofilesbatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_seccomp_profiles

Add seccomp profile

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.SeccompProfileInput()

res = s.psp_profiles.post_seccomp_profiles(req)

if res.seccomp_profile is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SeccompProfileInput](../../models/shared/seccompprofileinput.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.PostSeccompProfilesResponse](../../models/operations/postseccompprofilesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_pod_security_policy_profiles_profile_id_

Change pod security standards profile

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutPodSecurityPolicyProfilesProfileIDRequest(
    pod_security_policy=shared.PodSecurityPolicy(
        fs_group=shared.RunAsGroupStrategyOptions(),
        name='<value>',
        run_as_user=shared.RunAsUserStrategyOptions(),
        supplemental_groups=shared.RunAsGroupStrategyOptions(),
    ),
    profile_id='10ce973a-74d3-47da-b254-604edb379d9a',
)

res = s.psp_profiles.put_pod_security_policy_profiles_profile_id_(req)

if res.pod_security_policy is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [operations.PutPodSecurityPolicyProfilesProfileIDRequest](../../models/operations/putpodsecuritypolicyprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.PutPodSecurityPolicyProfilesProfileIDResponse](../../models/operations/putpodsecuritypolicyprofilesprofileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_seccomp_profiles_profile_id_

Change seccomp profile

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutSeccompProfilesProfileIDRequest(
    seccomp_profile=shared.SeccompProfileInput(),
    profile_id='7a689ccb-cc10-41fe-9293-6c76ef44408a',
)

res = s.psp_profiles.put_seccomp_profiles_profile_id_(req)

if res.seccomp_profile is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutSeccompProfilesProfileIDRequest](../../models/operations/putseccompprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutSeccompProfilesProfileIDResponse](../../models/operations/putseccompprofilesprofileidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
