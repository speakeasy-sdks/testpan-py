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
        password="",
        username="",
    ),
)

req = operations.DeletePodSecurityPolicyProfilesProfileIDRequest(
    profile_id='bb90cc1f-4444-454a-8574-313c05003108',
)

res = s.psp_profiles.delete_pod_security_policy_profiles_profile_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [operations.DeletePodSecurityPolicyProfilesProfileIDRequest](../../models/operations/deletepodsecuritypolicyprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.DeletePodSecurityPolicyProfilesProfileIDResponse](../../models/operations/deletepodsecuritypolicyprofilesprofileidresponse.md)**


## delete_seccomp_profiles_profile_id_

Delete a seccomp profile

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

req = operations.DeleteSeccompProfilesProfileIDRequest(
    profile_id='4cc0f6a2-ff01-4311-a20d-d6510a1ff69a',
)

res = s.psp_profiles.delete_seccomp_profiles_profile_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteSeccompProfilesProfileIDRequest](../../models/operations/deleteseccompprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteSeccompProfilesProfileIDResponse](../../models/operations/deleteseccompprofilesprofileidresponse.md)**


## get_pod_security_policy_profiles

Get all the pod security standards profiles on the system

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


res = s.psp_profiles.get_pod_security_policy_profiles()

if res.pod_security_policies is not None:
    # handle response
    pass
```


### Response

**[operations.GetPodSecurityPolicyProfilesResponse](../../models/operations/getpodsecuritypolicyprofilesresponse.md)**


## get_seccomp_profiles

Get all the seccomp profiles on the system

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


res = s.psp_profiles.get_seccomp_profiles()

if res.seccomp_profiles is not None:
    # handle response
    pass
```


### Response

**[operations.GetSeccompProfilesResponse](../../models/operations/getseccompprofilesresponse.md)**


## post_pod_security_policy_profiles

Create a new pod security standards

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

req = shared.PodSecurityPolicy(
    allowed_capabilities=[
        'bypass',
    ],
    allowed_host_paths=[
        shared.AllowedHostPath(),
    ],
    allowed_proc_mount_types=[
        shared.AllowedProcMountType.DEFAULT,
    ],
    allowed_unsafe_sysctls=[
        'turquoise',
    ],
    forbidden_sysctls=[
        'moderator',
    ],
    fs_group=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(),
        ],
    ),
    host_ports=[
        shared.HostPortRange(),
    ],
    name='Gloves',
    required_drop_capabilities=[
        'explicit',
    ],
    run_as_group=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(),
        ],
    ),
    run_as_user=shared.RunAsUserStrategyOptions(
        ranges=[
            shared.IDRange(),
        ],
    ),
    supplemental_groups=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(),
        ],
    ),
    volumes=[
        shared.PSPVolumeTypes.HOST_PATH,
    ],
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


## post_pod_security_policy_profiles_batch

Add a number of new Pod Security Standards Profiles.


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

req = [
    shared.PodSecurityPolicy(
        allowed_capabilities=[
            'Copernicium',
        ],
        allowed_host_paths=[
            shared.AllowedHostPath(),
        ],
        allowed_proc_mount_types=[
            shared.AllowedProcMountType.UNMASKED,
        ],
        allowed_unsafe_sysctls=[
            'Northeast',
        ],
        forbidden_sysctls=[
            'Directives',
        ],
        fs_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        host_ports=[
            shared.HostPortRange(),
        ],
        name='mint',
        required_drop_capabilities=[
            'Gasoline',
        ],
        run_as_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        run_as_user=shared.RunAsUserStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        supplemental_groups=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        volumes=[
            shared.PSPVolumeTypes.AZURE_DISK,
        ],
    ),
]

res = s.psp_profiles.post_pod_security_policy_profiles_batch(req)

if res.pod_security_policies is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                           | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `request`                                           | [list[shared.PodSecurityPolicy]](../../models//.md) | :heavy_check_mark:                                  | The request object to use for the request.          |


### Response

**[operations.PostPodSecurityPolicyProfilesBatchResponse](../../models/operations/postpodsecuritypolicyprofilesbatchresponse.md)**


## post_seccomp_profiles

Add seccomp profile

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

req = shared.SeccompProfileInput(
    pod_security_policies=[
        'Cab',
    ],
)

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


## put_pod_security_policy_profiles_profile_id_

Change pod security standards profile

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

req = operations.PutPodSecurityPolicyProfilesProfileIDRequest(
    pod_security_policy=shared.PodSecurityPolicy(
        allowed_capabilities=[
            'North',
        ],
        allowed_host_paths=[
            shared.AllowedHostPath(),
        ],
        allowed_proc_mount_types=[
            shared.AllowedProcMountType.UNMASKED,
        ],
        allowed_unsafe_sysctls=[
            'since',
        ],
        forbidden_sysctls=[
            'DNS',
        ],
        fs_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        host_ports=[
            shared.HostPortRange(),
        ],
        name='Coupe THX',
        required_drop_capabilities=[
            'Dynamic',
        ],
        run_as_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        run_as_user=shared.RunAsUserStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        supplemental_groups=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(),
            ],
        ),
        volumes=[
            shared.PSPVolumeTypes.FLOCKER,
        ],
    ),
    profile_id='04edb379-d9af-4bb9-b687-b2cfe0a637e7',
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


## put_seccomp_profiles_profile_id_

Change seccomp profile

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

req = operations.PutSeccompProfilesProfileIDRequest(
    seccomp_profile_input=shared.SeccompProfileInput(
        pod_security_policies=[
            'payment',
        ],
    ),
    profile_id='689ccbcc-101f-4ed2-936c-76ef44408a69',
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

