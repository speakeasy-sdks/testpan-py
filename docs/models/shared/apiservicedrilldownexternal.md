# APIServiceDrillDownExternal


## Fields

| Field                                                                                                                                                             | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `classification`                                                                                                                                                  | list[*str*]                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                | API classification label as determined by Crankshaft, e.g. ['meetings', 'messaging']                                                                              |
| `client_workloads`                                                                                                                                                | list[[shared.APIServiceClientWorkload](undefined/models/shared/apiserviceclientworkload.md)]                                                                      | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `compliance`                                                                                                                                                      | [Optional[shared.APIServiceCompliance]](undefined/models/shared/apiservicecompliance.md)                                                                          | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `creation_timestamp`                                                                                                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `description`                                                                                                                                                     | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Textual description of the Service                                                                                                                                |
| `identifier`                                                                                                                                                      | *Optional[str]*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                | Unique identifier of the subject API as assigned by Crankshaft                                                                                                    |
| `is_api_tracing_enabled`                                                                                                                                          | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `link_doc`                                                                                                                                                        | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Location of the documentation. This can be an URL for example                                                                                                     |
| `name`                                                                                                                                                            | *Optional[str]*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                | API name, usually an FQDN as determined by crankshaft, it can be logical or can correspond to one of the endpoints where the API is reachable, i.e. api.webex.com |
| `openapi_spec_availablity`                                                                                                                                        | [Optional[shared.OpenAPISpecAvailability]](undefined/models/shared/openapispecavailability.md)                                                                    | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `provider`                                                                                                                                                        | [Optional[shared.APIProviderBase]](undefined/models/shared/apiproviderbase.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `risk`                                                                                                                                                            | [Optional[shared.APISecurityRiskSeverity]](undefined/models/shared/apisecurityriskseverity.md)                                                                    | :heavy_minus_sign:                                                                                                                                                | An `enum`eration.                                                                                                                                                 |
| `score`                                                                                                                                                           | [Optional[shared.APIServiceScore]](undefined/models/shared/apiservicescore.md)                                                                                    | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |
| `status`                                                                                                                                                          | [Optional[shared.APISecurityAPIStatus]](undefined/models/shared/apisecurityapistatus.md)                                                                          | :heavy_minus_sign:                                                                                                                                                | Api status enumeration.                                                                                                                                           |
| `status_description`                                                                                                                                              | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | N/A                                                                                                                                                               |