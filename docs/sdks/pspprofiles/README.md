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
        'bypass',
    ],
    allowed_host_paths=[
        shared.AllowedHostPath(
            path_prefix='turquoise',
            read_only=False,
        ),
    ],
    allowed_proc_mount_types=[
        shared.AllowedProcMountType.DEFAULT,
    ],
    allowed_unsafe_sysctls=[
        'Product',
    ],
    default_allow_privilege_escalation=False,
    description='Down-sized empowering frame',
    forbidden_sysctls=[
        'incremental',
    ],
    fs_group=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(
                max=247342,
                min=407317,
            ),
        ],
        rule=shared.RunAsGroupStrategy.MAY_RUN_AS,
    ),
    host_ipc=False,
    host_network=False,
    host_pid=False,
    host_ports=[
        shared.HostPortRange(
            max=80641,
            min=34868,
        ),
    ],
    id='142085d7-d484-444d-9348-fb70a8e37e62',
    is_securecn_default_profile=False,
    name='Wooden repudiandae Paradigm',
    privileged=False,
    read_only_root_file_system=False,
    required_drop_capabilities=[
        'clearly',
    ],
    run_as_group=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(
                max=307575,
                min=822060,
            ),
        ],
        rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
    ),
    run_as_user=shared.RunAsUserStrategyOptions(
        ranges=[
            shared.IDRange(
                max=177881,
                min=417586,
            ),
        ],
        rule=shared.RunAsUserStrategy.MUST_RUN_AS,
    ),
    seccomp_profile='e80dd252-3540-4eb3-996a-05613aad0af4',
    supplemental_groups=shared.RunAsGroupStrategyOptions(
        ranges=[
            shared.IDRange(
                max=169335,
                min=820289,
            ),
        ],
        rule=shared.RunAsGroupStrategy.RUN_AS_ANY,
    ),
    volumes=[
        shared.PSPVolumeTypes.STORAGEOS,
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
            'Copernicium',
        ],
        allowed_host_paths=[
            shared.AllowedHostPath(
                path_prefix='Northeast Directives',
                read_only=False,
            ),
        ],
        allowed_proc_mount_types=[
            shared.AllowedProcMountType.DEFAULT,
        ],
        allowed_unsafe_sysctls=[
            'mint',
        ],
        default_allow_privilege_escalation=False,
        description='Self-enabling national application',
        forbidden_sysctls=[
            'THX',
        ],
        fs_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=581609,
                    min=807880,
                ),
            ],
            rule=shared.RunAsGroupStrategy.RUN_AS_ANY,
        ),
        host_ipc=False,
        host_network=False,
        host_pid=False,
        host_ports=[
            shared.HostPortRange(
                max=693689,
                min=305839,
            ),
        ],
        id='ccbec10a-9bc5-4ecc-aa49-c56c0e0d8163',
        is_securecn_default_profile=False,
        name='Bicycle synthesize',
        privileged=False,
        read_only_root_file_system=False,
        required_drop_capabilities=[
            'Cyclocross',
        ],
        run_as_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=978567,
                    min=527502,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MAY_RUN_AS,
        ),
        run_as_user=shared.RunAsUserStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=393434,
                    min=336870,
                ),
            ],
            rule=shared.RunAsUserStrategy.MUST_RUN_AS,
        ),
        seccomp_profile='33ebfbb0-cc93-4268-acf5-38bb5e43e0cc',
        supplemental_groups=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=259664,
                    min=329554,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
        ),
        volumes=[
            shared.PSPVolumeTypes.VSPHERE_VOLUME,
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
    data='{steam: 44630, freedom: null, lathe: "maiores metrics"}',
    name='bitterly North',
    pod_security_policies=[
        'bandwidth',
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
            'North',
        ],
        allowed_host_paths=[
            shared.AllowedHostPath(
                path_prefix='since DNS Central',
                read_only=False,
            ),
        ],
        allowed_proc_mount_types=[
            shared.AllowedProcMountType.DEFAULT,
        ],
        allowed_unsafe_sysctls=[
            'Mercedes',
        ],
        default_allow_privilege_escalation=False,
        description='Customer-focused eco-centric encryption',
        forbidden_sysctls=[
            'Checking',
        ],
        fs_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=885380,
                    min=870395,
                ),
            ],
            rule=shared.RunAsGroupStrategy.RUN_AS_ANY,
        ),
        host_ipc=False,
        host_network=False,
        host_pid=False,
        host_ports=[
            shared.HostPortRange(
                max=208639,
                min=494299,
            ),
        ],
        id='9d9afbb9-b687-4b2c-be0a-637e73494546',
        is_securecn_default_profile=False,
        name='Silicon sensor',
        privileged=False,
        read_only_root_file_system=False,
        required_drop_capabilities=[
            'ex',
        ],
        run_as_group=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=639188,
                    min=375698,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
        ),
        run_as_user=shared.RunAsUserStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=34862,
                    min=966964,
                ),
            ],
            rule=shared.RunAsUserStrategy.MUST_RUN_AS,
        ),
        seccomp_profile='114f1e40-0857-4100-95d7-43f0167fa418',
        supplemental_groups=shared.RunAsGroupStrategyOptions(
            ranges=[
                shared.IDRange(
                    max=807200,
                    min=91090,
                ),
            ],
            rule=shared.RunAsGroupStrategy.MUST_RUN_AS,
        ),
        volumes=[
            shared.PSPVolumeTypes.SCALE_IO,
        ],
    ),
    profile_id='30ce44b3-7a43-4d84-b255-0fa77d979933',
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
        data='{incandescence: 66214, hint: null, licorice: "Mobility lime"}',
        name='BMX Cambridgeshire wherever',
        pod_security_policies=[
            'plum',
        ],
    ),
    profile_id='36c76ef4-4408-4a69-9bd6-c47238638eac',
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

