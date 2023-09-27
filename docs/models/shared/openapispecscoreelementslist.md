# OpenAPISpecScoreElementsList


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `elements`                                                                          | list[[OpenAPISpecScoreElement](../../models/shared/openapispecscoreelement.md)]     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `severity`                                                                          | [Optional[APISecurityRiskSeverity]](../../models/shared/apisecurityriskseverity.md) | :heavy_minus_sign:                                                                  | An `enum`eration.                                                                   |
| `vulnerabilities_summary`                                                           | [Optional[VulnerabilitiesSummary]](../../models/shared/vulnerabilitiessummary.md)   | :heavy_minus_sign:                                                                  | Vulnerabilities summary by severity                                                 |