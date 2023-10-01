# CategoryScoreGradeNoFindings


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `additional_info`                                                                              | list[[shared.AdditionalInfo](undefined/models/shared/additionalinfo.md)]                       | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `confidence`                                                                                   | [Optional[shared.RiskConfidenceEnum]](undefined/models/shared/riskconfidenceenum.md)           | :heavy_minus_sign:                                                                             | An enumeration.                                                                                |
| `critical`                                                                                     | *Optional[int]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `high`                                                                                         | *Optional[int]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `low`                                                                                          | *Optional[int]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `medium`                                                                                       | *Optional[int]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `name`                                                                                         | *Optional[str]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `risk`                                                                                         | [Optional[shared.APISecurityRiskSeverity]](undefined/models/shared/apisecurityriskseverity.md) | :heavy_check_mark:                                                                             | An `enum`eration.                                                                              |
| `scorer_version`                                                                               | *Optional[int]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `trend`                                                                                        | [Optional[shared.RiskTrendEnum]](undefined/models/shared/risktrendenum.md)                     | :heavy_minus_sign:                                                                             | An enumeration.                                                                                |
| `unclassified`                                                                                 | *Optional[int]*                                                                                | :heavy_check_mark:                                                                             | N/A                                                                                            |