<!-- Start SDK Example Usage [usage] -->
```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteUsersUserIDRequest(
    user_id='2d4aef6d-76db-4c57-a2a3-fe8efd3db6e2',
)

res = s.users.delete_users_user_id_(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->