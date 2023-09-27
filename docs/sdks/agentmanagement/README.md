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
    download_as_xlsx=False,
    environment_name=[
        'possimus',
    ],
    host_name=[
        'facilis',
    ],
    risk=[
        operations.GetAgentsRisk.LOW,
    ],
    sort_dir=operations.GetAgentsSortDir.ASC,
    sort_key=operations.GetAgentsSortKey.RISK,
    status=[
        operations.GetAgentsStatus.INACTIVE,
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
    agent_id='fd5e60b3-75ed-44f6-bbee-41f33317fe35',
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
    agent_status_update=shared.AgentStatusUpdate(
        active=False,
    ),
    agent_id='b60eb1ea-4265-455b-a3c2-8744ed53b88f',
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

