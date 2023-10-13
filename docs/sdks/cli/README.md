# Cli
(*cli*)

## Overview

APIs to get the Secure Application CLI

### Available Operations

* [get_tools_cli_securecn_deployment_cli](#get_tools_cli_securecn_deployment_cli) - Get the Secure Application deployment cli

## get_tools_cli_securecn_deployment_cli

Get the Secure Application deployment cli

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


res = s.cli.get_tools_cli_securecn_deployment_cli()

if res.get_tools_cli_securecn_deployment_cli_200_application_json_binary_string is not None:
    # handle response
    pass
```


### Response

**[operations.GetToolsCliSecurecnDeploymentCliResponse](../../models/operations/gettoolsclisecurecndeploymentcliresponse.md)**

