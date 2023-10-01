# Settings
(*settings*)

## Overview

APIs used  to configure system settings

### Available Operations

* [delete_settings_integrations_ca_id_](#delete_settings_integrations_ca_id_) - Delete the CA integration details
* [delete_settings_integrations_event_forwarding_event_forwarding_id_](#delete_settings_integrations_event_forwarding_event_forwarding_id_) - Delete the event forwarding integration details with the given id
* [get_settings_agents_update](#get_settings_agents_update) - Get the agents update configurations
* [get_settings_integrations_ca](#get_settings_integrations_ca) - Get the CA integration details
* [get_settings_integrations_event_forwarding](#get_settings_integrations_event_forwarding) - Get the event forwarding integration details
* [post_seccomp_profiles_validate_data](#post_seccomp_profiles_validate_data) - Test the seccomp profile data
* [post_settings_agents_update_update_now](#post_settings_agents_update_update_now) - Update the agents of the account now
* [post_settings_integrations_ca](#post_settings_integrations_ca) - Set the CA integration details
* [post_settings_integrations_event_forwarding](#post_settings_integrations_event_forwarding) - Set the event forwarding integration details
* [post_settings_integrations_opsgenie_test_integration](#post_settings_integrations_opsgenie_test_integration) - Test the connection to Opsgenie
* [post_settings_integrations_securex_test_integration](#post_settings_integrations_securex_test_integration) - Test the SecureX integration by sending test message to the provided URL
* [post_settings_integrations_slack_test_integration](#post_settings_integrations_slack_test_integration) - Test the Slack integration by sending test message to the provided URL
* [post_settings_integrations_splunk_test_integration](#post_settings_integrations_splunk_test_integration) - Test the connection to Splunk
* [post_settings_integrations_sumo_logic_test_integration](#post_settings_integrations_sumo_logic_test_integration) - Test the Sumo Logic integration by sending test message to the provided URL
* [post_settings_integrations_teams_test_integration](#post_settings_integrations_teams_test_integration) - Test the connection to Teams
* [post_settings_integrations_webex_test_integration](#post_settings_integrations_webex_test_integration) - Test the Webex integration by sending test message to the provided URL
* [put_settings_agents_update](#put_settings_agents_update) - get the agents update configurations.
* [put_settings_integrations_ca_id_](#put_settings_integrations_ca_id_) - Edit the CA integration details
* [put_settings_integrations_event_forwarding_event_forwarding_id_](#put_settings_integrations_event_forwarding_event_forwarding_id_) - Edit the event forwarding integration details

## delete_settings_integrations_ca_id_

Delete the CA integration details

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

req = operations.DeleteSettingsIntegrationsCaIDRequest(
    id='2b23989d-8ad5-450f-8a76-f44a753018c5',
)

res = s.settings.delete_settings_integrations_ca_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteSettingsIntegrationsCaIDRequest](../../models/operations/deletesettingsintegrationscaidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteSettingsIntegrationsCaIDResponse](../../models/operations/deletesettingsintegrationscaidresponse.md)**


## delete_settings_integrations_event_forwarding_event_forwarding_id_

Delete the event forwarding integration details with the given id

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

req = operations.DeleteSettingsIntegrationsEventForwardingEventForwardingIDRequest(
    event_forwarding_id='a54e5100-941b-4501-ab74-aa7fd2e0ccc3',
)

res = s.settings.delete_settings_integrations_event_forwarding_event_forwarding_id_(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.DeleteSettingsIntegrationsEventForwardingEventForwardingIDRequest](../../models/operations/deletesettingsintegrationseventforwardingeventforwardingidrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.DeleteSettingsIntegrationsEventForwardingEventForwardingIDResponse](../../models/operations/deletesettingsintegrationseventforwardingeventforwardingidresponse.md)**


## get_settings_agents_update

Get the agents update configurations

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


res = s.settings.get_settings_agents_update()

if res.agents_update_settings is not None:
    # handle response
```


### Response

**[operations.GetSettingsAgentsUpdateResponse](../../models/operations/getsettingsagentsupdateresponse.md)**


## get_settings_integrations_ca

Get the CA integration details

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


res = s.settings.get_settings_integrations_ca()

if res.ca_integration_response_with_clusters is not None:
    # handle response
```


### Response

**[operations.GetSettingsIntegrationsCaResponse](../../models/operations/getsettingsintegrationscaresponse.md)**


## get_settings_integrations_event_forwarding

Get the event forwarding integration details

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


res = s.settings.get_settings_integrations_event_forwarding()

if res.events_forwarding_details_list is not None:
    # handle response
```


### Response

**[operations.GetSettingsIntegrationsEventForwardingResponse](../../models/operations/getsettingsintegrationseventforwardingresponse.md)**


## post_seccomp_profiles_validate_data

Test the seccomp profile data

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

req = shared.SeccompProfileData(
    data='{cycle: 29272, settlement: null, collaboration: "grey yearly"}',
)

res = s.settings.post_seccomp_profiles_validate_data(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.SeccompProfileData](../../models/shared/seccompprofiledata.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostSeccompProfilesValidateDataResponse](../../models/operations/postseccompprofilesvalidatedataresponse.md)**


## post_settings_agents_update_update_now

Update the agents of the account now

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


res = s.settings.post_settings_agents_update_update_now()

if res.status_code == 200:
    # handle response
```


### Response

**[operations.PostSettingsAgentsUpdateUpdateNowResponse](../../models/operations/postsettingsagentsupdateupdatenowresponse.md)**


## post_settings_integrations_ca

Set the CA integration details

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

req = shared.CaIntegrationRequestInput(
    certificate='prickly',
    issuer_name='Loan whereas green',
    issuer_namespace='Loan wield cyan',
    name='Northwest Wagon Soft',
)

res = s.settings.post_settings_integrations_ca(req)

if res.ca_integration_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.CaIntegrationRequestInput](../../models/shared/caintegrationrequestinput.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PostSettingsIntegrationsCaResponse](../../models/operations/postsettingsintegrationscaresponse.md)**


## post_settings_integrations_event_forwarding

Set the event forwarding integration details

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

req = shared.EventsForwardingDetailsInput(
    events_forwarding_details_type=shared.EventsForwardingDetailsTypeEnum.TEAMS_VULNERABILITY_EVENTS_FORWARDING_DETAILS,
    events_to_forward=[
        shared.EventsToForward.ATTACK_PATH,
    ],
    name='Soft dull alliance',
    url='https://truthful-campaigning.name',
)

res = s.settings.post_settings_integrations_event_forwarding(req)

if res.events_forwarding_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.EventsForwardingDetailsInput](../../models/shared/eventsforwardingdetailsinput.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PostSettingsIntegrationsEventForwardingResponse](../../models/operations/postsettingsintegrationseventforwardingresponse.md)**


## post_settings_integrations_opsgenie_test_integration

Test the connection to Opsgenie

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

req = shared.TestOpsgenieConnectionRequest(
    token='pish invoice',
)

res = s.settings.post_settings_integrations_opsgenie_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.TestOpsgenieConnectionRequest](../../models/shared/testopsgenieconnectionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PostSettingsIntegrationsOpsgenieTestIntegrationResponse](../../models/operations/postsettingsintegrationsopsgenietestintegrationresponse.md)**


## post_settings_integrations_securex_test_integration

Test the SecureX integration by sending test message to the provided URL

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

req = shared.TestSecureXIntegrationRequest(
    url='https://angelic-mortgage.name',
)

res = s.settings.post_settings_integrations_securex_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.TestSecureXIntegrationRequest](../../models/shared/testsecurexintegrationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PostSettingsIntegrationsSecurexTestIntegrationResponse](../../models/operations/postsettingsintegrationssecurextestintegrationresponse.md)**


## post_settings_integrations_slack_test_integration

Test the Slack integration by sending test message to the provided URL

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

req = shared.TestSlackIntegrationRequest(
    url='https://every-vibration.name',
)

res = s.settings.post_settings_integrations_slack_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestSlackIntegrationRequest](../../models/shared/testslackintegrationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsSlackTestIntegrationResponse](../../models/operations/postsettingsintegrationsslacktestintegrationresponse.md)**


## post_settings_integrations_splunk_test_integration

Test the connection to Splunk

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

req = shared.TestSplunkConnectionRequest(
    is_cloud=False,
    port=353653,
    token='orange XSS meter',
    url='http://legal-pea.com',
)

res = s.settings.post_settings_integrations_splunk_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestSplunkConnectionRequest](../../models/shared/testsplunkconnectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsSplunkTestIntegrationResponse](../../models/operations/postsettingsintegrationssplunktestintegrationresponse.md)**


## post_settings_integrations_sumo_logic_test_integration

Test the Sumo Logic integration by sending test message to the provided URL

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

req = shared.TestSumoLogicIntegrationRequest(
    url='http://sudden-concern.name',
)

res = s.settings.post_settings_integrations_sumo_logic_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.TestSumoLogicIntegrationRequest](../../models/shared/testsumologicintegrationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PostSettingsIntegrationsSumoLogicTestIntegrationResponse](../../models/operations/postsettingsintegrationssumologictestintegrationresponse.md)**


## post_settings_integrations_teams_test_integration

Test the connection to Teams

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

req = shared.TestTeamsIntegrationRequest(
    url='http://faraway-rayon.info',
)

res = s.settings.post_settings_integrations_teams_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestTeamsIntegrationRequest](../../models/shared/testteamsintegrationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsTeamsTestIntegrationResponse](../../models/operations/postsettingsintegrationsteamstestintegrationresponse.md)**


## post_settings_integrations_webex_test_integration

Test the Webex integration by sending test message to the provided URL

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

req = shared.TestWebexIntegrationRequest(
    url='http://charming-gadget.info',
)

res = s.settings.post_settings_integrations_webex_test_integration(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestWebexIntegrationRequest](../../models/shared/testwebexintegrationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsWebexTestIntegrationResponse](../../models/operations/postsettingsintegrationswebextestintegrationresponse.md)**


## put_settings_agents_update

get the agents update configurations.

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

req = shared.AgentsUpdateSettingsInput(
    is_manual_update=False,
    is_update_now_enabled=False,
)

res = s.settings.put_settings_agents_update(req)

if res.agents_update_settings is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.AgentsUpdateSettingsInput](../../models/shared/agentsupdatesettingsinput.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutSettingsAgentsUpdateResponse](../../models/operations/putsettingsagentsupdateresponse.md)**


## put_settings_integrations_ca_id_

Edit the CA integration details

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

req = operations.PutSettingsIntegrationsCaIDRequest(
    ca_integration_request_input=shared.CaIntegrationRequestInput(
        certificate='Berkshire',
        issuer_name='Bicycle',
        issuer_namespace='Central UDP recontextualize',
        name='Peru Market',
    ),
    id='d2fdcaea-e550-46a1-9b8c-391af00a780a',
)

res = s.settings.put_settings_integrations_ca_id_(req)

if res.ca_integration_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutSettingsIntegrationsCaIDRequest](../../models/operations/putsettingsintegrationscaidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutSettingsIntegrationsCaIDResponse](../../models/operations/putsettingsintegrationscaidresponse.md)**


## put_settings_integrations_event_forwarding_event_forwarding_id_

Edit the event forwarding integration details

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

req = operations.PutSettingsIntegrationsEventForwardingEventForwardingIDRequest(
    splunk_events_forwarding_details_input=shared.SplunkEventsForwardingDetailsInput(
        events_forwarding_details_type=shared.EventsForwardingDetailsTypeEnum.WEBEX_EVENTS_FORWARDING_DETAILS,
        events_to_forward=[
            shared.EventsToForward.NOTIFICATION,
        ],
        is_cloud=False,
        name='Genderqueer deploy',
        port=212010,
        source_name='proposal Yemen Audi',
        token='RSS',
        url='https://crafty-spec.net',
    ),
    event_forwarding_id='1b408bce-49d2-438c-ae86-ac5f2202c79c',
)

res = s.settings.put_settings_integrations_event_forwarding_event_forwarding_id_(req)

if res.events_forwarding_details is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.PutSettingsIntegrationsEventForwardingEventForwardingIDRequest](../../models/operations/putsettingsintegrationseventforwardingeventforwardingidrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.PutSettingsIntegrationsEventForwardingEventForwardingIDResponse](../../models/operations/putsettingsintegrationseventforwardingeventforwardingidresponse.md)**
