# APIProviderScoreGrade


## Fields

| Field                                                                                                     | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `additional_info`                                                                                         | list[[shared.AdditionalInfo](undefined/models/shared/additionalinfo.md)]                                  | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `avg_vulnerability_duration`                                                                              | *Optional[int]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `categories`                                                                                              | dict[str, [shared.CategoryScoreGradeNoFindings](undefined/models/shared/categoryscoregradenofindings.md)] | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `confidence`                                                                                              | [Optional[shared.RiskConfidenceEnum]](undefined/models/shared/riskconfidenceenum.md)                      | :heavy_minus_sign:                                                                                        | An enumeration.                                                                                           |
| `curated`                                                                                                 | *Optional[bool]*                                                                                          | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `last_finding_date`                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                      | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `last_vulnerability_date`                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                      | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `provider`                                                                                                | [Optional[shared.APIProviderBase]](undefined/models/shared/apiproviderbase.md)                            | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `provider_id`                                                                                             | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `risk`                                                                                                    | [Optional[shared.APISecurityRiskSeverity]](undefined/models/shared/apisecurityriskseverity.md)            | :heavy_check_mark:                                                                                        | An `enum`eration.                                                                                         |
| `scorer_version`                                                                                          | *Optional[int]*                                                                                           | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `trend`                                                                                                   | [Optional[shared.RiskTrendEnum]](undefined/models/shared/risktrendenum.md)                                | :heavy_minus_sign:                                                                                        | An enumeration.                                                                                           |