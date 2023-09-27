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
    policy_id='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
)

res = s.api_security_policies.delete_api_security_policy_policy_id_(req)

if res.status_code == 200:
    # handle response
```
<!-- End SDK Example Usage -->