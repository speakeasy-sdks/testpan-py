<!-- Start SDK Example Usage -->


```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="",
        username="",
    ),
)

req = operations.DeleteAPISecurityPolicyPolicyIDRequest(
    policy_id='04ae1a0e-dcb7-4d2b-b7a6-f7ca105f8c92',
)

res = s.api_security_policies.delete_api_security_policy_policy_id_(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->