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
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteSettingsIntegrationsCaIDRequest(
    id='2b23989d-8ad5-450f-8a76-f44a753018c5',
)

res = s.settings.delete_settings_integrations_ca_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.DeleteSettingsIntegrationsCaIDRequest](../../models/operations/deletesettingsintegrationscaidrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.DeleteSettingsIntegrationsCaIDResponse](../../models/operations/deletesettingsintegrationscaidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_settings_integrations_event_forwarding_event_forwarding_id_

Delete the event forwarding integration details with the given id

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteSettingsIntegrationsEventForwardingEventForwardingIDRequest(
    event_forwarding_id='a54e5100-941b-4501-ab74-aa7fd2e0ccc3',
)

res = s.settings.delete_settings_integrations_event_forwarding_event_forwarding_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                                    | [operations.DeleteSettingsIntegrationsEventForwardingEventForwardingIDRequest](../../models/operations/deletesettingsintegrationseventforwardingeventforwardingidrequest.md) | :heavy_check_mark:                                                                                                                                                           | The request object to use for the request.                                                                                                                                   |


### Response

**[operations.DeleteSettingsIntegrationsEventForwardingEventForwardingIDResponse](../../models/operations/deletesettingsintegrationseventforwardingeventforwardingidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_settings_agents_update

Get the agents update configurations

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.settings.get_settings_agents_update()

if res.agents_update_settings is not None:
    # handle response
    pass
```


### Response

**[operations.GetSettingsAgentsUpdateResponse](../../models/operations/getsettingsagentsupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_settings_integrations_ca

Get the CA integration details

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.settings.get_settings_integrations_ca()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetSettingsIntegrationsCaResponse](../../models/operations/getsettingsintegrationscaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_settings_integrations_event_forwarding

Get the event forwarding integration details

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.settings.get_settings_integrations_event_forwarding()

if res.events_forwarding_details_list is not None:
    # handle response
    pass
```


### Response

**[operations.GetSettingsIntegrationsEventForwardingResponse](../../models/operations/getsettingsintegrationseventforwardingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_seccomp_profiles_validate_data

Test the seccomp profile data

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.SeccompProfileData()

res = s.settings.post_seccomp_profiles_validate_data(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.SeccompProfileData](../../models/shared/seccompprofiledata.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.PostSeccompProfilesValidateDataResponse](../../models/operations/postseccompprofilesvalidatedataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_agents_update_update_now

Update the agents of the account now

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.settings.post_settings_agents_update_update_now()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.PostSettingsAgentsUpdateUpdateNowResponse](../../models/operations/postsettingsagentsupdateupdatenowresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_ca

Set the CA integration details

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.CaIntegrationRequest(
    certificate='string',
    issuer_name='string',
    name='string',
)

res = s.settings.post_settings_integrations_ca(req)

if res.ca_integration_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.CaIntegrationRequest](../../models/shared/caintegrationrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PostSettingsIntegrationsCaResponse](../../models/operations/postsettingsintegrationscaresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_event_forwarding

Set the event forwarding integration details

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.EventsForwardingDetailsInput(
    events_forwarding_details_type=shared.EventsForwardingDetailsTypeEnum.TEAMS_VULNERABILITY_EVENTS_FORWARDING_DETAILS,
    events_to_forward=[
        shared.EventsToForward.ATTACK_PATH,
    ],
    name='string',
)

res = s.settings.post_settings_integrations_event_forwarding(req)

if res.events_forwarding_details is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.EventsForwardingDetailsInput](../../models/shared/eventsforwardingdetailsinput.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PostSettingsIntegrationsEventForwardingResponse](../../models/operations/postsettingsintegrationseventforwardingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_opsgenie_test_integration

Test the connection to Opsgenie

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestOpsgenieConnectionRequest(
    token='string',
)

res = s.settings.post_settings_integrations_opsgenie_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.TestOpsgenieConnectionRequest](../../models/shared/testopsgenieconnectionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PostSettingsIntegrationsOpsgenieTestIntegrationResponse](../../models/operations/postsettingsintegrationsopsgenietestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_securex_test_integration

Test the SecureX integration by sending test message to the provided URL

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestSecureXIntegrationRequest(
    url='https://angelic-mortgage.name',
)

res = s.settings.post_settings_integrations_securex_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.TestSecureXIntegrationRequest](../../models/shared/testsecurexintegrationrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PostSettingsIntegrationsSecurexTestIntegrationResponse](../../models/operations/postsettingsintegrationssecurextestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_slack_test_integration

Test the Slack integration by sending test message to the provided URL

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestSlackIntegrationRequest(
    url='https://every-vibration.name',
)

res = s.settings.post_settings_integrations_slack_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestSlackIntegrationRequest](../../models/shared/testslackintegrationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsSlackTestIntegrationResponse](../../models/operations/postsettingsintegrationsslacktestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_splunk_test_integration

Test the connection to Splunk

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestSplunkConnectionRequest(
    token='string',
    url='http://same-shopper.biz',
)

res = s.settings.post_settings_integrations_splunk_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestSplunkConnectionRequest](../../models/shared/testsplunkconnectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsSplunkTestIntegrationResponse](../../models/operations/postsettingsintegrationssplunktestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_sumo_logic_test_integration

Test the Sumo Logic integration by sending test message to the provided URL

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestSumoLogicIntegrationRequest(
    url='http://sudden-concern.name',
)

res = s.settings.post_settings_integrations_sumo_logic_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.TestSumoLogicIntegrationRequest](../../models/shared/testsumologicintegrationrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PostSettingsIntegrationsSumoLogicTestIntegrationResponse](../../models/operations/postsettingsintegrationssumologictestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_teams_test_integration

Test the connection to Teams

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestTeamsIntegrationRequest(
    url='http://faraway-rayon.info',
)

res = s.settings.post_settings_integrations_teams_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestTeamsIntegrationRequest](../../models/shared/testteamsintegrationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsTeamsTestIntegrationResponse](../../models/operations/postsettingsintegrationsteamstestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## post_settings_integrations_webex_test_integration

Test the Webex integration by sending test message to the provided URL

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.TestWebexIntegrationRequest(
    url='http://charming-gadget.info',
)

res = s.settings.post_settings_integrations_webex_test_integration(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.TestWebexIntegrationRequest](../../models/shared/testwebexintegrationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PostSettingsIntegrationsWebexTestIntegrationResponse](../../models/operations/postsettingsintegrationswebextestintegrationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_settings_agents_update

get the agents update configurations.

### Example Usage

```python
import pan
from pan.models import shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = shared.AgentsUpdateSettingsInput()

res = s.settings.put_settings_agents_update(req)

if res.agents_update_settings is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.AgentsUpdateSettingsInput](../../models/shared/agentsupdatesettingsinput.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutSettingsAgentsUpdateResponse](../../models/operations/putsettingsagentsupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_settings_integrations_ca_id_

Edit the CA integration details

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutSettingsIntegrationsCaIDRequest(
    ca_integration_request=shared.CaIntegrationRequest(
        certificate='string',
        issuer_name='string',
        name='string',
    ),
    id='3150c8bd-a77d-45f8-8b65-8d2fdcaeae55',
)

res = s.settings.put_settings_integrations_ca_id_(req)

if res.ca_integration_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.PutSettingsIntegrationsCaIDRequest](../../models/operations/putsettingsintegrationscaidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PutSettingsIntegrationsCaIDResponse](../../models/operations/putsettingsintegrationscaidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_settings_integrations_event_forwarding_event_forwarding_id_

Edit the event forwarding integration details

### Example Usage

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PutSettingsIntegrationsEventForwardingEventForwardingIDRequest(
    splunk_events_forwarding_details=shared.SplunkEventsForwardingDetails(
        events_forwarding_details_type=shared.EventsForwardingDetailsTypeEnum.WEBEX_EVENTS_FORWARDING_DETAILS,
        events_to_forward=[
            shared.EventsToForward.NOTIFICATION,
        ],
        name='string',
        token='string',
    ),
    event_forwarding_id='a96473ef-b0fd-4047-9c2d-c1b408bce49d',
)

res = s.settings.put_settings_integrations_event_forwarding_event_forwarding_id_(req)

if res.events_forwarding_details is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                                              | Type                                                                                                                                                                   | Required                                                                                                                                                               | Description                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                                              | [operations.PutSettingsIntegrationsEventForwardingEventForwardingIDRequest](../../models/operations/putsettingsintegrationseventforwardingeventforwardingidrequest.md) | :heavy_check_mark:                                                                                                                                                     | The request object to use for the request.                                                                                                                             |


### Response

**[operations.PutSettingsIntegrationsEventForwardingEventForwardingIDResponse](../../models/operations/putsettingsintegrationseventforwardingeventforwardingidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
