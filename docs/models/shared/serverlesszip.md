# ServerlessZip


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `id`                                                                                         | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `is_identified`                                                                              | *Optional[bool]*                                                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `name`                                                                                       | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | zip name that was given by the user to the cli                                               |
| `sha256`                                                                                     | *Optional[str]*                                                                              | :heavy_minus_sign:                                                                           | the zip file's sha256 identifier                                                             |
| `source_type`                                                                                | [Optional[shared.ZipSourceType]](undefined/models/shared/zipsourcetype.md)                   | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `time_updated`                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                         | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `vulnerabilities_summary`                                                                    | [Optional[shared.VulnerabilitiesSummary]](undefined/models/shared/vulnerabilitiessummary.md) | :heavy_minus_sign:                                                                           | Vulnerabilities summary by severity                                                          |