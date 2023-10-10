# AgentManagement
(*agent_management*)

## Overview

APIs use to  interact with  agents

### Available Operations

* [get_agents](#get_agents) - List all installed agents
* [post_agents_agent_id_update](#post_agents_agent_id_update) - Update the agent with the given id to the latest agent version
* [post_agents_agent_id_update_state](#post_agents_agent_id_update_state) - Update the status of an agent with the given id

## get_agents

List all installed agents

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

req = operations.GetAgentsRequest(
    environment_name=[
        'Account',
    ],
    host_name=[
        'Shoes',
    ],
    risk=[
        operations.GetAgentsRisk.UNDEFINED,
    ],
    status=[
        operations.GetAgentsStatus.ACTIVE,
    ],
)

res = s.agent_management.get_agents(req)

if res.agents is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetAgentsRequest](../../models/operations/getagentsrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetAgentsResponse](../../models/operations/getagentsresponse.md)**


## post_agents_agent_id_update

Update the agent with the given id to the latest agent version

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

req = operations.PostAgentsAgentIDUpdateRequest(
    agent_id='0a0835d7-8d36-4444-8529-411e73a9b7a8',
)

res = s.agent_management.post_agents_agent_id_update(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostAgentsAgentIDUpdateRequest](../../models/operations/postagentsagentidupdaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostAgentsAgentIDUpdateResponse](../../models/operations/postagentsagentidupdateresponse.md)**


## post_agents_agent_id_update_state

Update the status of an agent with the given id

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

req = operations.PostAgentsAgentIDUpdateStateRequest(
    agent_status_update=shared.AgentStatusUpdate(),
    agent_id='34a187e9-3552-49e2-8694-f733a8b3f850',
)

res = s.agent_management.post_agents_agent_id_update_state(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostAgentsAgentIDUpdateStateRequest](../../models/operations/postagentsagentidupdatestaterequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostAgentsAgentIDUpdateStateResponse](../../models/operations/postagentsagentidupdatestateresponse.md)**

