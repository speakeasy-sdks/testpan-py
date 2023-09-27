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
    profile_id='3b084da9-9257-4d04-b408-47a742d84496',
)

res = s.psp_profiles.delete_pod_security_policy_profiles_profile_id_(req)

if res.status_code == 200:
    # handle response
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
    profile_id='cbdeecf6-b99b-4c63-962e-bfdf55c294c0',
)

res = s.psp_profiles.delete_seccomp_profiles_profile_id_(req)

if res.status_code == 200:
    # handle response
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
    allow_privilege_escalation=False,
    allowed_capabilities=[
        'ea',
    ],
    allowed_host_paths=[
        shared.AllowedHostPath(
            path_prefix='consequatur',
            read_only=False,
        ),
    ],
    allowed_proc_mount_types=[
        shared.AllowedProcMountType.UNMASKED,
    ],
    allowed_unsafe_sysctls=[
        'accusantium',
    ],
    default_allow_privilege_escalation=False,
    description='ea',
    forbidden_sysctls=[
        'laborum',
    ],
    fs_group=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(
                max=88758,
                min=144856,
            ),
        ],
        rule=shared.RunAsGroupStrategy.MAY_RUN_AS,
    ),
    host_ipc=False,
    host_network=False,
    host_pid=False,
    host_ports=[
        shared.HostPortRange(
            max=476770,
            min=454329,
        ),
    ],
    id='64eef6d0-c6d6-4ed9-873d-d634571509a8',
    is_securecn_default_profile=False,
    name='Dr. Jaime Kunde',
    privileged=False,
    read_only_root_file_system=False,
    required_drop_capabilities=[
        'minus',
    ],
    run_as_group=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(
                max=330908,
                min=664679,
            ),
        ],
        rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
    ),
    run_as_user=shared.RunAsUserStrategyOptions(
        ranges=[
            shared.IDRange(
                max=978229,
                min=598497,
            ),
        ],
        rule=shared.RunAsUserStrategy.RUN_AS_ANY,
    ),
    seccomp_profile='242c7b66-a1f3-40c7-bdf5-b6719890f42a',
    supplemental_groups=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(
                max=272396,
                min=749863,
            ),
        ],
        rule=shared.RunAsGroupStrategy.RUN_AS_ANY,
    ),
    volumes=[
        shared.PSPVolumeTypes.DOWNWARD_API,
    ],
)

res = s.psp_profiles.post_pod_security_policy_profiles(req)

if res.pod_security_policy is not None:
    # handle response
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
        allow_privilege_escalation=False,
        allowed_capabilities=[
            'adipisci',
        ],
        allowed_host_paths=[
            shared.AllowedHostPath(
                path_prefix='atque',
                read_only=False,
            ),
        ],
        allowed_proc_mount_types=[
            shared.AllowedProcMountType.UNMASKED,
        ],
        allowed_unsafe_sysctls=[
            'rem',
        ],
        default_allow_privilege_escalation=False,
        description='exercitationem',
        forbidden_sysctls=[
            'tempore',
        ],
        fs_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=180839,
                    min=389585,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
        ),
        host_ipc=False,
        host_network=False,
        host_pid=False,
        host_ports=[
            shared.HostPortRange(
                max=326894,
                min=595595,
            ),
        ],
        id='1d745e3c-2059-4c9c-bf56-7e0e252765b1',
        is_securecn_default_profile=False,
        name='Reginald Cruickshank',
        privileged=False,
        read_only_root_file_system=False,
        required_drop_capabilities=[
            'possimus',
        ],
        run_as_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=670710,
                    min=761835,
                ),
            ],
            rule=shared.RunAsGroupStrategy.RUN_AS_ANY,
        ),
        run_as_user=shared.RunAsUserStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=100926,
                    min=968792,
                ),
            ],
            rule=shared.RunAsUserStrategy.MUST_RUN_AS,
        ),
        seccomp_profile='1216ce22-39e8-4f25-8d0d-19d959f439e3',
        supplemental_groups=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=573816,
                    min=177632,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MAY_RUN_AS,
        ),
        volumes=[
            shared.PSPVolumeTypes.FLOCKER,
        ],
    ),
]

res = s.psp_profiles.post_pod_security_policy_profiles_batch(req)

if res.pod_security_policies is not None:
    # handle response
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
    data='{"foo":"boZ>zM]_.a","bar":30034,"bike":9270,"a":39110,"b":"An)tEFVT}l","name":">?XG1+Mk1U","prop":47319}',
    name='Allison Kemmer',
    pod_security_policies=[
        'tempora',
    ],
)

res = s.psp_profiles.post_seccomp_profiles(req)

if res.seccomp_profile is not None:
    # handle response
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
        allow_privilege_escalation=False,
        allowed_capabilities=[
            'aspernatur',
        ],
        allowed_host_paths=[
            shared.AllowedHostPath(
                path_prefix='ad',
                read_only=False,
            ),
        ],
        allowed_proc_mount_types=[
            shared.AllowedProcMountType.DEFAULT,
        ],
        allowed_unsafe_sysctls=[
            'alias',
        ],
        default_allow_privilege_escalation=False,
        description='adipisci',
        forbidden_sysctls=[
            'atque',
        ],
        fs_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=734296,
                    min=989913,
                ),
            ],
            rule=shared.RunAsGroupStrategy.RUN_AS_ANY,
        ),
        host_ipc=False,
        host_network=False,
        host_pid=False,
        host_ports=[
            shared.HostPortRange(
                max=328217,
                min=584483,
            ),
        ],
        id='71e98190-5573-489c-adba-c7fda39594d6',
        is_securecn_default_profile=False,
        name='Patty Schinner',
        privileged=False,
        read_only_root_file_system=False,
        required_drop_capabilities=[
            'officiis',
        ],
        run_as_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=304571,
                    min=559392,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
        ),
        run_as_user=shared.RunAsUserStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=422215,
                    min=209920,
                ),
            ],
            rule=shared.RunAsUserStrategy.MUST_RUN_AS,
        ),
        seccomp_profile='b9954b6f-a220-4636-9828-553cb10006be',
        supplemental_groups=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=968591,
                    min=277569,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MAY_RUN_AS,
        ),
        volumes=[
            shared.PSPVolumeTypes.CINDER,
        ],
    ),
    profile_id='1ec2053b-7493-466a-88ee-0f2bf19588d4',
)

res = s.psp_profiles.put_pod_security_policy_profiles_profile_id_(req)

if res.pod_security_policy is not None:
    # handle response
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
        data='{"foo":87372,"bar":19647,"bike":"4nuf_/ZMbx","a":93359,"b":"!af8!o|TGO","name":"qC2<\">hd53","prop":86405}',
        name='Ramona Crona',
        pod_security_policies=[
            'doloribus',
        ],
    ),
    profile_id='127fb0e0-bf1f-4821-b978-d0acca77aeb7',
)

res = s.psp_profiles.put_seccomp_profiles_profile_id_(req)

if res.seccomp_profile is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutSeccompProfilesProfileIDRequest](../../models/operations/putseccompprofilesprofileidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutSeccompProfilesProfileIDResponse](../../models/operations/putseccompprofilesprofileidresponse.md)**

