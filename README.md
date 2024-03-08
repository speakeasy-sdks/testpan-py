# pan

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/testpan-py.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/bolt-php/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/testpan-py.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteUsersUserIDRequest(
    user_id='2d4aef6d-76db-4c57-a2a3-fe8efd3db6e2',
)

res = s.users.delete_users_user_id_(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [users](docs/sdks/users/README.md)

* [delete_users_user_id_](docs/sdks/users/README.md#delete_users_user_id_) - Delete a user
* [get_operator_credentials](docs/sdks/users/README.md#get_operator_credentials) - get the credentials of the Secure Application Operator service user
* [get_users](docs/sdks/users/README.md#get_users) - List current users
* [get_users_user_id_access_tokens](docs/sdks/users/README.md#get_users_user_id_access_tokens) - Get the  access tokens for the user
* [get_users_user_id_delete_dependencies](docs/sdks/users/README.md#get_users_user_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified user
* [post_account_usage_status](docs/sdks/users/README.md#post_account_usage_status) - an api to get the account usage status
* [post_change_password](docs/sdks/users/README.md#post_change_password) - Change the password for the current user
* [post_login](docs/sdks/users/README.md#post_login) - Login
* [post_logout](docs/sdks/users/README.md#post_logout) - Log out
* [post_me](docs/sdks/users/README.md#post_me) - an api to get current logged in user info
* [post_users](docs/sdks/users/README.md#post_users) - Create a user
* [post_users_accept_eula](docs/sdks/users/README.md#post_users_accept_eula) - Accept the EULA
* [post_users_trial](docs/sdks/users/README.md#post_users_trial) - Create a trail user
* [put_users_user_id_](docs/sdks/users/README.md#put_users_user_id_) - Change user details

### [images_and_vulnerabilities](docs/sdks/imagesandvulnerabilities/README.md)

* [delete_images_id_](docs/sdks/imagesandvulnerabilities/README.md#delete_images_id_) - Delete an image hash
* [get_account_vulnerabilities_xlsx](docs/sdks/imagesandvulnerabilities/README.md#get_account_vulnerabilities_xlsx) - Returns a xlsx file of images alongside to their vulnerabilities.
* [get_images](docs/sdks/imagesandvulnerabilities/README.md#get_images) - Returns a list of images
* [get_images_images_hash](docs/sdks/imagesandvulnerabilities/README.md#get_images_images_hash) - search for image hash in the account
* [get_images_vulnerabilities_by_image_name_and_hash](docs/sdks/imagesandvulnerabilities/README.md#get_images_vulnerabilities_by_image_name_and_hash) - Returns a list of vulnerabilities detected in the image
* [get_images_id_](docs/sdks/imagesandvulnerabilities/README.md#get_images_id_) - get an image
* [get_images_image_id_dockerfile_scan_results](docs/sdks/imagesandvulnerabilities/README.md#get_images_image_id_dockerfile_scan_results) - Returns a list of vulnerabilities detected in the  image
* [get_images_image_id_image_layers](docs/sdks/imagesandvulnerabilities/README.md#get_images_image_id_image_layers) - Returns a list of image layers
* [get_images_image_id_packages](docs/sdks/imagesandvulnerabilities/README.md#get_images_image_id_packages) - Returns a list of packages for a specific image
* [get_images_image_id_sbom_path](docs/sdks/imagesandvulnerabilities/README.md#get_images_image_id_sbom_path) - Returns the path to the SBOM in cloud storage
* [get_images_image_id_vulnerabilities](docs/sdks/imagesandvulnerabilities/README.md#get_images_image_id_vulnerabilities) - Returns a list of vulnerabilities detected in the image
* [post_images](docs/sdks/imagesandvulnerabilities/README.md#post_images) - Define a New image hash
* [post_images_approve](docs/sdks/imagesandvulnerabilities/README.md#post_images_approve) - Approve an image hash
* [post_images_image_id_dockerfile_scan_results_ignore](docs/sdks/imagesandvulnerabilities/README.md#post_images_image_id_dockerfile_scan_results_ignore) - Add / remove a list of  UUIDs of dockerfileScanResults from ignored list
* [post_images_image_id_vulnerabilities_ignore](docs/sdks/imagesandvulnerabilities/README.md#post_images_image_id_vulnerabilities_ignore) - Add / remove a list of  UUIDs of vulnerabilities from ignored list

### [advisor](docs/sdks/advisor/README.md)

* [get_advisor_cluster_event_rules](docs/sdks/advisor/README.md#get_advisor_cluster_event_rules) - Returns a list of suggested cluster event rules
* [get_advisor_connection_rules](docs/sdks/advisor/README.md#get_advisor_connection_rules) - Returns a list of suggested connection rules
* [get_advisor_environment](docs/sdks/advisor/README.md#get_advisor_environment) - Returns a list of suggested kubernetes environments
* [get_advisor_environment_rules](docs/sdks/advisor/README.md#get_advisor_environment_rules) - Returns a list of suggested environment rules
* [get_advisor_pod_security_policy](docs/sdks/advisor/README.md#get_advisor_pod_security_policy) - Returns a list of suggested kubernetes Pod Security Standards
* [get_advisor_queue_advisor_type_](docs/sdks/advisor/README.md#get_advisor_queue_advisor_type_) - Get status for policy advisor background job
* [post_advisor_run](docs/sdks/advisor/README.md#post_advisor_run) - Runs the policy advisor

### [agent_management](docs/sdks/agentmanagement/README.md)

* [get_agents](docs/sdks/agentmanagement/README.md#get_agents) - List all installed agents
* [post_agents_agent_id_update](docs/sdks/agentmanagement/README.md#post_agents_agent_id_update) - Update the agent with the given id to the latest agent version
* [post_agents_agent_id_update_state](docs/sdks/agentmanagement/README.md#post_agents_agent_id_update_state) - Update the status of an agent with the given id

### [api](docs/sdks/api/README.md)

* [get_api](docs/sdks/api/README.md#get_api) - Get Secure Application API as a Swagger file

### [api_security](docs/sdks/apisecurity/README.md)

* [delete_api_security_api_catalog_id_](docs/sdks/apisecurity/README.md#delete_api_security_api_catalog_id_) - Delete an API
* [delete_api_security_internal_catalog_catalog_id_bfla_detection](docs/sdks/apisecurity/README.md#delete_api_security_internal_catalog_catalog_id_bfla_detection) - stop bfla detection phase
* [delete_api_security_internal_catalog_catalog_id_bfla_learning](docs/sdks/apisecurity/README.md#delete_api_security_internal_catalog_catalog_id_bfla_learning) - stop bfla learning phase
* [delete_api_security_open_api_specs_catalog_id_](docs/sdks/apisecurity/README.md#delete_api_security_open_api_specs_catalog_id_) - delete open api spec include all of it findings and scores
* [delete_gateways_gateway_id_](docs/sdks/apisecurity/README.md#delete_gateways_gateway_id_) - Delete gateway
* [get_api_security_external_catalog](docs/sdks/apisecurity/README.md#get_api_security_external_catalog) - Get a list of APIs and their compliance
* [get_api_security_external_catalog_count](docs/sdks/apisecurity/README.md#get_api_security_external_catalog_count) - Get the number of existing 3rd party APIs in the inventory
* [get_api_security_external_catalog_catalog_id_](docs/sdks/apisecurity/README.md#get_api_security_external_catalog_catalog_id_) - Get information about a specific API
* [get_api_security_internal_catalog](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog) - Get a list of APIs and their compliance
* [get_api_security_internal_catalog_count](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog_count) - Get the number of existing 3rd party APIs in the inventory
* [get_api_security_internal_catalog_catalog_id_](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog_catalog_id_) - Get information about a specific API
* [get_api_security_internal_catalog_catalog_id_bfla](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog_catalog_id_bfla) - Get bfla info for given catalogId
* [get_api_security_internal_catalog_catalog_id_fuzzing_status](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog_catalog_id_fuzzing_status) - Get status of the last/running fuzzing test
* [get_api_security_internal_catalog_catalog_id_fuzzing_tests](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog_catalog_id_fuzzing_tests) - Get list of fuzzing tests
* [get_api_security_internal_catalog_catalog_id_trace_analysis](docs/sdks/apisecurity/README.md#get_api_security_internal_catalog_catalog_id_trace_analysis) - Get trace analysis details
* [get_api_security_open_api_specs_catalog_id_](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_) - Get provided and reconstructed open api specs for specific API
* [get_api_security_open_api_specs_catalog_id_diff_detection_status](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_diff_detection_status) - Get provided and reconstructed open api specs for specific API
* [get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_get_open_api_spec_score_status) - Get open api spec score status
* [get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_open_api_spec_swagger_json) - Get provided spec content as json
* [get_api_security_open_api_specs_catalog_id_reconstructed_spec_review](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_reconstructed_spec_review) - Get the suggestions of a spec reconstruction (or previously cached info)
* [get_api_security_open_api_specs_catalog_id_reconstructed_spec_status](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_reconstructed_spec_status) - Get the status of a spec reconstruction
* [get_api_security_open_api_specs_catalog_id_reconstructed_spec_json](docs/sdks/apisecurity/README.md#get_api_security_open_api_specs_catalog_id_reconstructed_spec_json) - Get reconstructed open api spec as json for specific API
* [get_api_security_risk_findings](docs/sdks/apisecurity/README.md#get_api_security_risk_findings) - Get a list of risk findings
* [get_api_security_risk_findings_categories](docs/sdks/apisecurity/README.md#get_api_security_risk_findings_categories) - Get a list of risk findings categories
* [get_api_security_risk_findings_sources](docs/sdks/apisecurity/README.md#get_api_security_risk_findings_sources) - Get a list of risk findings sources
* [get_api_security_risk_findings_risk_finding_id_](docs/sdks/apisecurity/README.md#get_api_security_risk_findings_risk_finding_id_) - Get a specific risk findings
* [get_api_security_catalog_id_delete_dependencies](docs/sdks/apisecurity/README.md#get_api_security_catalog_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified api security service
* [get_api_security_catalog_id_methods](docs/sdks/apisecurity/README.md#get_api_security_catalog_id_methods) - Get a list of an API spec methods for a specific API and its spec's tags
* [get_api_security_catalog_id_tags](docs/sdks/apisecurity/README.md#get_api_security_catalog_id_tags) - Get a list of an API spec tags or a specific API
* [get_dashboard_apisec_risk_findings](docs/sdks/apisecurity/README.md#get_dashboard_apisec_risk_findings) - Get API sec risk findings widget
* [get_dashboard_apisec_risk_findings_trend](docs/sdks/apisecurity/README.md#get_dashboard_apisec_risk_findings_trend) - Get API sec risk findings trend graph widget for the last 30 days
* [get_dashboard_apisec_specs_and_operations_diffs](docs/sdks/apisecurity/README.md#get_dashboard_apisec_specs_and_operations_diffs) - Get API sec specs and operations diffs widget
* [get_dashboard_apisec_top_risky_apis](docs/sdks/apisecurity/README.md#get_dashboard_apisec_top_risky_apis) - Get API sec top risky APIs widget
* [get_dashboard_apisec_top_risky_findings](docs/sdks/apisecurity/README.md#get_dashboard_apisec_top_risky_findings) - Get API sec top risky findings widget
* [get_gateways](docs/sdks/apisecurity/README.md#get_gateways) - Get gateways
* [get_gateways_clusters](docs/sdks/apisecurity/README.md#get_gateways_clusters) - Get clusters info
* [get_gateways_gateway_id_download_bundle](docs/sdks/apisecurity/README.md#get_gateways_gateway_id_download_bundle) - Get a GW installation script
* [post_api_security_api](docs/sdks/apisecurity/README.md#post_api_security_api) - Register an API for scoring
* [post_api_security_internal_catalog_catalog_id_bfla_detection](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_bfla_detection) - Start new bfla detection phase
* [post_api_security_internal_catalog_catalog_id_bfla_learning](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_bfla_learning) - Start new bfla learning phase
* [post_api_security_internal_catalog_catalog_id_bfla_reset](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_bfla_reset) - Reset bfla model
* [post_api_security_internal_catalog_catalog_id_reset_trace_analysis](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_reset_trace_analysis) - Reset trace analysis
* [post_api_security_internal_catalog_catalog_id_start_fuzzing](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_start_fuzzing) - Start new fuzzing test
* [post_api_security_internal_catalog_catalog_id_start_trace_analysis](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_start_trace_analysis) - Start trace analysis
* [post_api_security_internal_catalog_catalog_id_stop_fuzzing](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_stop_fuzzing) - Stop fuzzing test
* [post_api_security_internal_catalog_catalog_id_stop_trace_analysis](docs/sdks/apisecurity/README.md#post_api_security_internal_catalog_catalog_id_stop_trace_analysis) - Stop trace analysis
* [post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort](docs/sdks/apisecurity/README.md#post_api_security_open_api_specs_catalog_id_reconstructed_spec_abort) - abort learning and reconstructing an API via API Clarity
* [post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn](docs/sdks/apisecurity/README.md#post_api_security_open_api_specs_catalog_id_reconstructed_spec_learn) - Start learning and reconstructing an API via API Clarity
* [post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve](docs/sdks/apisecurity/README.md#post_api_security_open_api_specs_catalog_id_reconstructed_spec_review_approve) - Approve reconstructed spec suggestions (only 1 approval per catalogId)
* [post_api_security_open_api_specs_catalog_id_start_diffs_detection](docs/sdks/apisecurity/README.md#post_api_security_open_api_specs_catalog_id_start_diffs_detection) - Start spec diffs detection
* [post_api_security_open_api_specs_catalog_id_stop_diffs_detection](docs/sdks/apisecurity/README.md#post_api_security_open_api_specs_catalog_id_stop_diffs_detection) - stop spec diffs detection
* [post_gateways](docs/sdks/apisecurity/README.md#post_gateways) - Add new gateway
* [put_api_security_internal_catalog_catalog_id_bfla](docs/sdks/apisecurity/README.md#put_api_security_internal_catalog_catalog_id_bfla) - update BFLA info for this catalogId
* [put_api_security_open_api_specs_catalog_id_](docs/sdks/apisecurity/README.md#put_api_security_open_api_specs_catalog_id_) - Add or edit a spec about a specific API for the account
* [put_gateways_gateway_id_](docs/sdks/apisecurity/README.md#put_gateways_gateway_id_) - Edit gateway

### [performance](docs/sdks/performance/README.md)

* [get_api_security_api_catalog_id_hit_count_graph](docs/sdks/performance/README.md#get_api_security_api_catalog_id_hit_count_graph) - Get hit count for specific spec path
* [get_performance_metrics](docs/sdks/performance/README.md#get_performance_metrics) - Get performance metrics for a connection between workloads

### [bfla](docs/sdks/bfla/README.md)

* [delete_api_security_internal_catalog_catalog_id_bfla_detection](docs/sdks/bfla/README.md#delete_api_security_internal_catalog_catalog_id_bfla_detection) - stop bfla detection phase
* [delete_api_security_internal_catalog_catalog_id_bfla_learning](docs/sdks/bfla/README.md#delete_api_security_internal_catalog_catalog_id_bfla_learning) - stop bfla learning phase
* [get_api_security_internal_catalog_catalog_id_bfla](docs/sdks/bfla/README.md#get_api_security_internal_catalog_catalog_id_bfla) - Get bfla info for given catalogId
* [post_api_security_internal_catalog_catalog_id_bfla_detection](docs/sdks/bfla/README.md#post_api_security_internal_catalog_catalog_id_bfla_detection) - Start new bfla detection phase
* [post_api_security_internal_catalog_catalog_id_bfla_learning](docs/sdks/bfla/README.md#post_api_security_internal_catalog_catalog_id_bfla_learning) - Start new bfla learning phase
* [post_api_security_internal_catalog_catalog_id_bfla_reset](docs/sdks/bfla/README.md#post_api_security_internal_catalog_catalog_id_bfla_reset) - Reset bfla model
* [put_api_security_internal_catalog_catalog_id_bfla](docs/sdks/bfla/README.md#put_api_security_internal_catalog_catalog_id_bfla) - update BFLA info for this catalogId

### [api_security_policies](docs/sdks/apisecuritypolicies/README.md)

* [delete_api_security_policy_policy_id_](docs/sdks/apisecuritypolicies/README.md#delete_api_security_policy_policy_id_) - Delete api security policy
* [get_api_security_policy](docs/sdks/apisecuritypolicies/README.md#get_api_security_policy) - Get a list of API security policies
* [get_api_security_policy_policy_id_delete_dependencies](docs/sdks/apisecuritypolicies/README.md#get_api_security_policy_policy_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified api security service
* [post_api_security_policy](docs/sdks/apisecuritypolicies/README.md#post_api_security_policy) - Add new API security policy
* [put_api_security_policy_policy_id_](docs/sdks/apisecuritypolicies/README.md#put_api_security_policy_policy_id_) - Edit Api security policy.

### [telemetries](docs/sdks/telemetries/README.md)

* [get_app_telemetries](docs/sdks/telemetries/README.md#get_app_telemetries) - Get App telemetries
* [get_app_telemetries_app_telemetry_id_](docs/sdks/telemetries/README.md#get_app_telemetries_app_telemetry_id_) - Get App telemetry by ID
* [get_app_telemetries_app_telemetry_id_api_risk_info](docs/sdks/telemetries/README.md#get_app_telemetries_app_telemetry_id_api_risk_info) - Get API risks info of given app telemetry
* [get_app_telemetries_app_telemetry_id_image_packages](docs/sdks/telemetries/README.md#get_app_telemetries_app_telemetry_id_image_packages) - list packages with licenses runnin on a pod
* [get_app_telemetries_app_telemetry_id_injection_info](docs/sdks/telemetries/README.md#get_app_telemetries_app_telemetry_id_injection_info) - Get token injection info of given app telemetry
* [get_connection_telemetries](docs/sdks/telemetries/README.md#get_connection_telemetries) - Get connection telemetries
* [get_connection_telemetries_connection_telemetry_id_](docs/sdks/telemetries/README.md#get_connection_telemetries_connection_telemetry_id_) - get details for a single connection telemetry

### [apps](docs/sdks/apps/README.md)

* [get_apps](docs/sdks/apps/README.md#get_apps) - Returns a list of defined Apps
* [get_apps_app_id_](docs/sdks/apps/README.md#get_apps_app_id_) - Returns an App by its ID
* [post_apps](docs/sdks/apps/README.md#post_apps) - Define a New App
* [post_apps_delete](docs/sdks/apps/README.md#post_apps_delete) - Delete several Apps
* [put_apps_app_id_](docs/sdks/apps/README.md#put_apps_app_id_) - Edit the existing App

### [environment_policies](docs/sdks/environmentpolicies/README.md)

* [get_apps_policy](docs/sdks/environmentpolicies/README.md#get_apps_policy) - Get the current Apps policy
* [get_apps_policy_history](docs/sdks/environmentpolicies/README.md#get_apps_policy_history) - Get the history of Apps policies
* [get_apps_policy_search_options](docs/sdks/environmentpolicies/README.md#get_apps_policy_search_options) - Get the current Apps policy filter option
* [put_apps_policy](docs/sdks/environmentpolicies/README.md#put_apps_policy) - Set the current Apps policy

### [audit_logs](docs/sdks/auditlogs/README.md)

* [get_audit_logs](docs/sdks/auditlogs/README.md#get_audit_logs) - Get audit logs
* [get_audit_logs_actions](docs/sdks/auditlogs/README.md#get_audit_logs_actions) - Get all the audit logs actions
* [get_audit_logs_kubernetes](docs/sdks/auditlogs/README.md#get_audit_logs_kubernetes) - Get audit logs
* [get_audit_logs_kubernetes_actions](docs/sdks/auditlogs/README.md#get_audit_logs_kubernetes_actions) - Get all the kubernetes audit logs actions

### [aws](docs/sdks/aws/README.md)

* [get_aws_accounts](docs/sdks/aws/README.md#get_aws_accounts) - Get a list of AWS accounts
* [get_aws_roles](docs/sdks/aws/README.md#get_aws_roles) - Lists AWS role ARNs for the account
* [get_aws_tags](docs/sdks/aws/README.md#get_aws_tags) - Get a list of AWS tag keys
* [get_aws_aws_account_id_regions](docs/sdks/aws/README.md#get_aws_aws_account_id_regions) - Get a list of regions for the  AWS account
* [get_aws_aws_account_id_region_id_subnets](docs/sdks/aws/README.md#get_aws_aws_account_id_region_id_subnets) - Get a list of AWS subnets for an AWS account and region
* [get_aws_aws_account_id_region_id_vpcs](docs/sdks/aws/README.md#get_aws_aws_account_id_region_id_vpcs) - Get a list of VPCs for AWS accounts.
* [post_aws_roles](docs/sdks/aws/README.md#post_aws_roles) - Add AWS role to the account
* [put_aws_roles_role_id_](docs/sdks/aws/README.md#put_aws_roles_role_id_) - Change AWS role name

### [cd](docs/sdks/cd/README.md)

* [delete_cd_rule_id_connections_rule](docs/sdks/cd/README.md#delete_cd_rule_id_connections_rule) - delete a cd connection rule.
* [delete_cd_rule_id_serverless_rule](docs/sdks/cd/README.md#delete_cd_rule_id_serverless_rule) - delete a cd serverless rule.
* [get_cd](docs/sdks/cd/README.md#get_cd) - Get all the CD pipelines results
* [get_cd_resource_id_](docs/sdks/cd/README.md#get_cd_resource_id_) - Get A single CD pipeline results
* [get_cd_rule_id_connections_rule](docs/sdks/cd/README.md#get_cd_rule_id_connections_rule) - get a cd connection rule.
* [get_cd_rule_id_serverless_rule](docs/sdks/cd/README.md#get_cd_rule_id_serverless_rule) - get a cd serverless rule.
* [post_cd_connections_rule](docs/sdks/cd/README.md#post_cd_connections_rule) - Adds cd connection rule.
* [post_cd_serverless_rule](docs/sdks/cd/README.md#post_cd_serverless_rule) - Adds cd serverless rule.
* [put_cd_rule_id_connections_rule](docs/sdks/cd/README.md#put_cd_rule_id_connections_rule) - update a cd connection rule.
* [put_cd_rule_id_serverless_rule](docs/sdks/cd/README.md#put_cd_rule_id_serverless_rule) - update a cd serverless rule.

### [ci_cd_policies](docs/sdks/cicdpolicies/README.md)

* [delete_cd_policy_policy_id_](docs/sdks/cicdpolicies/README.md#delete_cd_policy_policy_id_) - Delete CD policy
* [delete_ci_policy_policy_id_](docs/sdks/cicdpolicies/README.md#delete_ci_policy_policy_id_) - Delete CI policy
* [get_cd_policy](docs/sdks/cicdpolicies/README.md#get_cd_policy) - Get the current CD policy
* [get_ci_policy](docs/sdks/cicdpolicies/README.md#get_ci_policy) - Get the current CI policy
* [post_cd_policy](docs/sdks/cicdpolicies/README.md#post_cd_policy) - Set the current CD policy. At least one CdPolicyElement should be present
* [post_ci_policy](docs/sdks/cicdpolicies/README.md#post_ci_policy) - Set the current CI policy
* [put_cd_policy_policy_id_](docs/sdks/cicdpolicies/README.md#put_cd_policy_policy_id_) - Edit CD policy. At least one CdPolicyElement should be present
* [put_ci_policy_policy_id_](docs/sdks/cicdpolicies/README.md#put_ci_policy_policy_id_) - Edit CI policy

### [serverless](docs/sdks/serverless/README.md)

* [delete_cloud_accounts_cloud_account_id_](docs/sdks/serverless/README.md#delete_cloud_accounts_cloud_account_id_) - Delete a cloud account
* [get_cloud_accounts](docs/sdks/serverless/README.md#get_cloud_accounts) - List all the cloud accounts on the system
* [get_cloud_accounts_azure_installation_details](docs/sdks/serverless/README.md#get_cloud_accounts_azure_installation_details) - Get the Azure installation details
* [get_cloud_accounts_installation_details](docs/sdks/serverless/README.md#get_cloud_accounts_installation_details) - Get the installation details
* [get_cloud_accounts_regions_aws](docs/sdks/serverless/README.md#get_cloud_accounts_regions_aws) - List all the possible regions of AWS
* [get_cloud_accounts_regions_azure](docs/sdks/serverless/README.md#get_cloud_accounts_regions_azure) - List all the possible regions of Azure
* [get_cloud_accounts_cloud_account_id_delete_dependencies](docs/sdks/serverless/README.md#get_cloud_accounts_cloud_account_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified cloud account
* [get_cloud_accounts_cloud_account_id_download_bundle](docs/sdks/serverless/README.md#get_cloud_accounts_cloud_account_id_download_bundle) - Get Secure Application installation script
* [get_serverless_functions](docs/sdks/serverless/README.md#get_serverless_functions) - Get serverless functions
* [get_serverless_functions_arns](docs/sdks/serverless/README.md#get_serverless_functions_arns) - Get serverless functions names
* [get_serverless_functions_names](docs/sdks/serverless/README.md#get_serverless_functions_names) - Get serverless functions names
* [get_serverless_functions_function_id_](docs/sdks/serverless/README.md#get_serverless_functions_function_id_) - Get Serverless Function by ID
* [get_serverless_functions_function_id_secrets](docs/sdks/serverless/README.md#get_serverless_functions_function_id_secrets) - Get Serverless Function secrets issues
* [get_serverless_functions_function_id_vulnerabilities](docs/sdks/serverless/README.md#get_serverless_functions_function_id_vulnerabilities) - Get Serverless Function Vulnerabilities by ID
* [get_serverless_zip_files](docs/sdks/serverless/README.md#get_serverless_zip_files) - Get serverless zip files that was scanned by cli
* [get_serverless_zip_files_zip_id_](docs/sdks/serverless/README.md#get_serverless_zip_files_zip_id_) - Get specific zip file record
* [get_serverless_zip_files_zip_id_packages](docs/sdks/serverless/README.md#get_serverless_zip_files_zip_id_packages) - Returns a list of packages for a specific serverless zip
* [get_serverless_zip_files_zip_id_vulnerabilities](docs/sdks/serverless/README.md#get_serverless_zip_files_zip_id_vulnerabilities) - Returns a list of vulnerabilities detected in the serverless zip
* [post_cloud_accounts_scan](docs/sdks/serverless/README.md#post_cloud_accounts_scan) - invoke cloud account scan
* [put_cloud_accounts_cloud_account_id_](docs/sdks/serverless/README.md#put_cloud_accounts_cloud_account_id_) - Edit cloud account definition

### [connection_policies](docs/sdks/connectionpolicies/README.md)

* [get_connections_policy](docs/sdks/connectionpolicies/README.md#get_connections_policy) - Get current connection policy
* [get_connections_policy_history](docs/sdks/connectionpolicies/README.md#get_connections_policy_history) - Get the history of the connection policies
* [get_connections_policy_kafka_actions](docs/sdks/connectionpolicies/README.md#get_connections_policy_kafka_actions) - Get the a list of kafka actions
* [get_connections_policy_kafka_kubernetes_cluster_id_brokers](docs/sdks/connectionpolicies/README.md#get_connections_policy_kafka_kubernetes_cluster_id_brokers) - Get the a list of kafka brokers
* [get_connections_policy_kafka_kubernetes_cluster_id_topics](docs/sdks/connectionpolicies/README.md#get_connections_policy_kafka_kubernetes_cluster_id_topics) - Get the a list of kafka topics
* [get_connections_policy_search_options](docs/sdks/connectionpolicies/README.md#get_connections_policy_search_options) - Get the current connection policy filter option
* [get_serverless_policy_history](docs/sdks/connectionpolicies/README.md#get_serverless_policy_history) - Get the history of the serverless policies
* [put_connections_policy](docs/sdks/connectionpolicies/README.md#put_connections_policy) - Set the current connection policy

### [dashboard](docs/sdks/dashboard/README.md)

* [get_dashboard_apisec_risk_findings](docs/sdks/dashboard/README.md#get_dashboard_apisec_risk_findings) - Get API sec risk findings widget
* [get_dashboard_apisec_risk_findings_trend](docs/sdks/dashboard/README.md#get_dashboard_apisec_risk_findings_trend) - Get API sec risk findings trend graph widget for the last 30 days
* [get_dashboard_apisec_specs_and_operations_diffs](docs/sdks/dashboard/README.md#get_dashboard_apisec_specs_and_operations_diffs) - Get API sec specs and operations diffs widget
* [get_dashboard_apisec_top_risky_apis](docs/sdks/dashboard/README.md#get_dashboard_apisec_top_risky_apis) - Get API sec top risky APIs widget
* [get_dashboard_apisec_top_risky_findings](docs/sdks/dashboard/README.md#get_dashboard_apisec_top_risky_findings) - Get API sec top risky findings widget
* [get_dashboard_clusters](docs/sdks/dashboard/README.md#get_dashboard_clusters) - Get the active clusters
* [get_dashboard_connection_telemetries](docs/sdks/dashboard/README.md#get_dashboard_connection_telemetries) - Get pod connection dashboard data for all clusters
* [get_dashboard_kubernetes_audit_logs](docs/sdks/dashboard/README.md#get_dashboard_kubernetes_audit_logs) - Get kubernetes audit logs dashboard data for all clusters
* [get_dashboard_operational_bar](docs/sdks/dashboard/README.md#get_dashboard_operational_bar) - Get the operation data dashboard for the given kubernetesClusterId
* [get_dashboard_permissions](docs/sdks/dashboard/README.md#get_dashboard_permissions) - Get permissions dashboard data for the given kubernetesClusterIds
* [get_dashboard_pod_telemetries](docs/sdks/dashboard/README.md#get_dashboard_pod_telemetries) - Get pod telemetries dashboard data for all clusters
* [get_dashboard_report_download](docs/sdks/dashboard/README.md#get_dashboard_report_download) - Download Secure Application security report
* [get_dashboard_report_status](docs/sdks/dashboard/README.md#get_dashboard_report_status) - Get Secure Application report security status
* [get_dashboard_security_context](docs/sdks/dashboard/README.md#get_dashboard_security_context) - Get security context dashboard data for all clusters
* [get_dashboard_top_security_risks](docs/sdks/dashboard/README.md#get_dashboard_top_security_risks) - Get the top risky deployments dashboard data for the given kubernetesClusterIds
* [get_dashboard_vulnerabilities](docs/sdks/dashboard/README.md#get_dashboard_vulnerabilities) - Get vulnerabilities dashboard data for the given kubernetesClusterId
* [get_dashboard_kubernetes_cluster_id_connection_telemetries](docs/sdks/dashboard/README.md#get_dashboard_kubernetes_cluster_id_connection_telemetries) - Get connection telemetries dashboard data for the given kubernetesClusterId
* [get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs](docs/sdks/dashboard/README.md#get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs) - Get kubernetes audit logs dashboard data for the given kubernetesClusterId
* [get_dashboard_kubernetes_cluster_id_pod_telemetries](docs/sdks/dashboard/README.md#get_dashboard_kubernetes_cluster_id_pod_telemetries) - Get pod telemetries dashboard data for the given kubernetesClusterId
* [get_licensing_dashboard](docs/sdks/dashboard/README.md#get_licensing_dashboard) - Get licensing dashboard data
* [post_dashboard_report_generate](docs/sdks/dashboard/README.md#post_dashboard_report_generate) - Generate Secure Application security report

### [deployers](docs/sdks/deployers/README.md)

* [delete_deployers_deployer_id_](docs/sdks/deployers/README.md#delete_deployers_deployer_id_) - Delete an deployer
* [get_deployers](docs/sdks/deployers/README.md#get_deployers) - List all the deployers on the system
* [get_deployers_service_accounts](docs/sdks/deployers/README.md#get_deployers_service_accounts) - List all the service account on the system
* [get_deployers_deployer_id_delete_dependencies](docs/sdks/deployers/README.md#get_deployers_deployer_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified deployer
* [post_deployers](docs/sdks/deployers/README.md#post_deployers) - Create a new deployer
* [put_deployers_deployer_id_](docs/sdks/deployers/README.md#put_deployers_deployer_id_) - Edit deployer definition

### [envs](docs/sdks/envs/README.md)

* [delete_environments_env_id_](docs/sdks/envs/README.md#delete_environments_env_id_)
* [get_environments](docs/sdks/envs/README.md#get_environments) - List all defined Secure Application environments
* [get_environments_env_id_](docs/sdks/envs/README.md#get_environments_env_id_) - get a Secure Application environment
* [get_environments_env_id_delete_dependencies](docs/sdks/envs/README.md#get_environments_env_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified environment
* [post_environments](docs/sdks/envs/README.md#post_environments) - Add a new environment
* [post_environments_batch](docs/sdks/envs/README.md#post_environments_batch) - Add a number of  Secure Application environments
* [post_environments_delete](docs/sdks/envs/README.md#post_environments_delete) - Delete multiple Secure Application environments
* [put_environments_env_id_](docs/sdks/envs/README.md#put_environments_env_id_) - Edit an existing Secure Application environment

### [expansions](docs/sdks/expansions/README.md)

* [delete_expansions_expansion_id_](docs/sdks/expansions/README.md#delete_expansions_expansion_id_) - Delete an expansion
* [get_expansions](docs/sdks/expansions/README.md#get_expansions) - List all the expansions on the system
* [get_expansions_expansion_id_install_expansion_tar_gz](docs/sdks/expansions/README.md#get_expansions_expansion_id_install_expansion_tar_gz) - Get the expansion installation
* [post_expansions](docs/sdks/expansions/README.md#post_expansions) - Create a new expansion
* [put_expansions_expansion_id_](docs/sdks/expansions/README.md#put_expansions_expansion_id_) - Edit expansion definition

### [gateways](docs/sdks/gateways/README.md)

* [delete_gateways_gateway_id_](docs/sdks/gateways/README.md#delete_gateways_gateway_id_) - Delete gateway
* [get_gateways](docs/sdks/gateways/README.md#get_gateways) - Get gateways
* [get_gateways_clusters](docs/sdks/gateways/README.md#get_gateways_clusters) - Get clusters info
* [get_gateways_gateway_id_download_bundle](docs/sdks/gateways/README.md#get_gateways_gateway_id_download_bundle) - Get a GW installation script
* [post_gateways](docs/sdks/gateways/README.md#post_gateways) - Add new gateway
* [put_gateways_gateway_id_](docs/sdks/gateways/README.md#put_gateways_gateway_id_) - Edit gateway

### [kubernetes](docs/sdks/kubernetes/README.md)

* [delete_kubernetes_clusters_kubernetes_cluster_id_](docs/sdks/kubernetes/README.md#delete_kubernetes_clusters_kubernetes_cluster_id_) - Delete a Kubernetes cluster
* [delete_pod_definitions_pod_id_](docs/sdks/kubernetes/README.md#delete_pod_definitions_pod_id_) - Delete a pod definition
* [get_get_controller_data_cluster_id_](docs/sdks/kubernetes/README.md#get_get_controller_data_cluster_id_) - get controller data using clusterId
* [get_istio_supported_versions](docs/sdks/kubernetes/README.md#get_istio_supported_versions) - Get a list of istio releases that are supported by Secure Application agent. sorted from latest to oldest
* [get_kubernetes_clusters](docs/sdks/kubernetes/README.md#get_kubernetes_clusters) - get a list of current Kubernetes clusters
* [get_kubernetes_clusters_kubernetes_cluster_id_](docs/sdks/kubernetes/README.md#get_kubernetes_clusters_kubernetes_cluster_id_) - get the Kubernetes cluster with the given id
* [get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies](docs/sdks/kubernetes/README.md#get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies) - get dependencies which need to be handled in order to delete specified Kubernetes cluster
* [get_kubernetes_clusters_kubernetes_cluster_id_download_bundle](docs/sdks/kubernetes/README.md#get_kubernetes_clusters_kubernetes_cluster_id_download_bundle) - Get Secure Application installation script
* [get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands](docs/sdks/kubernetes/README.md#get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands) - Get Panoptica Aug release Helm command
* [get_kubernetes_clusters_kubernetes_cluster_id_namespaces](docs/sdks/kubernetes/README.md#get_kubernetes_clusters_kubernetes_cluster_id_namespaces) - List namespaces on a specific Kubernetes cluster
* [get_kubernetes_clusters_kubernetes_cluster_id_services](docs/sdks/kubernetes/README.md#get_kubernetes_clusters_kubernetes_cluster_id_services) - List services on a specific Kubernetes cluster
* [get_lean_kubernetes_clusters](docs/sdks/kubernetes/README.md#get_lean_kubernetes_clusters) - get a list of current Kubernetes clusters
* [get_namespaces](docs/sdks/kubernetes/README.md#get_namespaces) - Get a list of current Kubernetes namespaces
* [get_pod_definitions](docs/sdks/kubernetes/README.md#get_pod_definitions) - Get all pod definitions on the system
* [post_kubernetes_clusters](docs/sdks/kubernetes/README.md#post_kubernetes_clusters) - Add a new Kubernetes cluster to Secure Application
* [post_pod_definitions](docs/sdks/kubernetes/README.md#post_pod_definitions) - Create a new pod definition
* [put_kubernetes_clusters_kubernetes_cluster_id_](docs/sdks/kubernetes/README.md#put_kubernetes_clusters_kubernetes_cluster_id_) - Update the Kubernetes cluster
* [put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm](docs/sdks/kubernetes/README.md#put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm) - Update the Kubernetes cluster which managed by HELM
* [put_pod_definitions_pod_id_](docs/sdks/kubernetes/README.md#put_pod_definitions_pod_id_) - Change pod definition

### [k8s_cis_benchmark](docs/sdks/k8scisbenchmark/README.md)

* [get_k8s_cis_benchmark](docs/sdks/k8scisbenchmark/README.md#get_k8s_cis_benchmark) - Get k8s cis benchmark for clusters
* [get_k8s_cis_benchmark_summary](docs/sdks/k8scisbenchmark/README.md#get_k8s_cis_benchmark_summary) - Get k8s cis benchmark summary of account
* [get_k8s_cis_benchmark_cluster_id_](docs/sdks/k8scisbenchmark/README.md#get_k8s_cis_benchmark_cluster_id_) - Get k8s cis benchmark for a specific cluster
* [post_k8s_cis_benchmark_cluster_id_](docs/sdks/k8scisbenchmark/README.md#post_k8s_cis_benchmark_cluster_id_) - initiate k8s cis benchmark scan for a specific cluster
* [put_k8s_cis_benchmark_cluster_id_](docs/sdks/k8scisbenchmark/README.md#put_k8s_cis_benchmark_cluster_id_) - edit k8s cis benchmark for a specific cluster with test statuses

### [cluster_events_policies](docs/sdks/clustereventspolicies/README.md)

* [get_kubernetes_api_policy](docs/sdks/clustereventspolicies/README.md#get_kubernetes_api_policy) - Get current Kubernetes API policy
* [get_kubernetes_api_policy_history](docs/sdks/clustereventspolicies/README.md#get_kubernetes_api_policy_history) - Get the history of the Kubernetes API policies
* [get_kubernetes_api_policy_kubernetes_resources](docs/sdks/clustereventspolicies/README.md#get_kubernetes_api_policy_kubernetes_resources) - Get the Kubernetes resource list
* [get_kubernetes_api_policy_kubernetes_users](docs/sdks/clustereventspolicies/README.md#get_kubernetes_api_policy_kubernetes_users) - Get the Kubernetes user list
* [get_kubernetes_api_policy_recommended_rules](docs/sdks/clustereventspolicies/README.md#get_kubernetes_api_policy_recommended_rules) - Get the recommended Kubernetes API rules
* [put_kubernetes_api_policy](docs/sdks/clustereventspolicies/README.md#put_kubernetes_api_policy) - set the current Kubernetes API policy

### [mitre](docs/sdks/mitre/README.md)

* [get_mitre_dashboard](docs/sdks/mitre/README.md#get_mitre_dashboard) - Get data for MITRE dashboard for all clusters
* [get_mitre_report_download](docs/sdks/mitre/README.md#get_mitre_report_download) - Download Mitre security report
* [get_mitre_report_status](docs/sdks/mitre/README.md#get_mitre_report_status) - Get Mitre report status
* [get_mitre_technique](docs/sdks/mitre/README.md#get_mitre_technique) - Get data for MITRE technique of the given mitreTechniqueType
* [post_mitre_report_generate](docs/sdks/mitre/README.md#post_mitre_report_generate) - Generate Mitre report
* [post_mitre_technique_fix](docs/sdks/mitre/README.md#post_mitre_technique_fix) - Post fix for MITRE technique of the given mitreTechniqueType

### [runtime_map](docs/sdks/runtimemap/README.md)

* [delete_network_map_queue_request_id_](docs/sdks/runtimemap/README.md#delete_network_map_queue_request_id_) - Cancel the network map background job
* [get_network_map](docs/sdks/runtimemap/README.md#get_network_map) - Get data for network map
* [get_network_map_queue_request_id_](docs/sdks/runtimemap/README.md#get_network_map_queue_request_id_) - Get status for network map background job
* [get_network_map_results_request_id_](docs/sdks/runtimemap/README.md#get_network_map_results_request_id_) - Get result for network map background job

### [psp_profiles](docs/sdks/pspprofiles/README.md)

* [delete_pod_security_policy_profiles_profile_id_](docs/sdks/pspprofiles/README.md#delete_pod_security_policy_profiles_profile_id_) - Delete a pod security policy standards
* [delete_seccomp_profiles_profile_id_](docs/sdks/pspprofiles/README.md#delete_seccomp_profiles_profile_id_) - Delete a seccomp profile
* [get_pod_security_policy_profiles](docs/sdks/pspprofiles/README.md#get_pod_security_policy_profiles) - Get all the pod security standards profiles on the system
* [get_seccomp_profiles](docs/sdks/pspprofiles/README.md#get_seccomp_profiles) - Get all the seccomp profiles on the system
* [post_pod_security_policy_profiles](docs/sdks/pspprofiles/README.md#post_pod_security_policy_profiles) - Create a new pod security standards
* [post_pod_security_policy_profiles_batch](docs/sdks/pspprofiles/README.md#post_pod_security_policy_profiles_batch) - Add a number of Pod Security Standards
* [post_seccomp_profiles](docs/sdks/pspprofiles/README.md#post_seccomp_profiles) - Add seccomp profile
* [put_pod_security_policy_profiles_profile_id_](docs/sdks/pspprofiles/README.md#put_pod_security_policy_profiles_profile_id_) - Change pod security standards profile
* [put_seccomp_profiles_profile_id_](docs/sdks/pspprofiles/README.md#put_seccomp_profiles_profile_id_) - Change seccomp profile

### [registries](docs/sdks/registries/README.md)

* [delete_registries_registry_id_](docs/sdks/registries/README.md#delete_registries_registry_id_) - Delete a registry
* [get_registries](docs/sdks/registries/README.md#get_registries) - Get a list of defined registries
* [post_registries](docs/sdks/registries/README.md#post_registries) - Add new registry
* [post_registries_test_connection](docs/sdks/registries/README.md#post_registries_test_connection) - test registry connection
* [post_registries_test_connection_registry_id_](docs/sdks/registries/README.md#post_registries_test_connection_registry_id_) - test registry connection
* [put_registries_registry_id_](docs/sdks/registries/README.md#put_registries_registry_id_) - edit existing registry

### [risk_assessment](docs/sdks/riskassessment/README.md)

* [delete_risk_assessment_ignored_risks_ignored_risk_id_](docs/sdks/riskassessment/README.md#delete_risk_assessment_ignored_risks_ignored_risk_id_) - Delete ignored risk
* [delete_risk_assessment_kubernetes_cluster_id_cancel](docs/sdks/riskassessment/README.md#delete_risk_assessment_kubernetes_cluster_id_cancel) - Cancel the runtime scan on the given cluster with the given id
* [get_risk_assessment](docs/sdks/riskassessment/README.md#get_risk_assessment) - Get risk assessment data for all clusters
* [get_risk_assessment_ignored_risks](docs/sdks/riskassessment/README.md#get_risk_assessment_ignored_risks) - Get all the ignored risks
* [get_risk_assessment_permissions](docs/sdks/riskassessment/README.md#get_risk_assessment_permissions) - Get list of clusters and their permissions
* [get_risk_assessment_permissions_cluster_id_](docs/sdks/riskassessment/README.md#get_risk_assessment_permissions_cluster_id_) - Get all of the users permissions
* [get_risk_assessment_permissions_cluster_id_owner_id_](docs/sdks/riskassessment/README.md#get_risk_assessment_permissions_cluster_id_owner_id_) - Get the owner permissions
* [get_risk_assessment_permissions_cluster_id_owner_id_role_id_](docs/sdks/riskassessment/README.md#get_risk_assessment_permissions_cluster_id_owner_id_role_id_) - Get the owner permissions
* [get_risk_assessment_poll](docs/sdks/riskassessment/README.md#get_risk_assessment_poll) - Poll running scans
* [get_risk_assessment_image_id_vulnerabilities](docs/sdks/riskassessment/README.md#get_risk_assessment_image_id_vulnerabilities) - Get all images of given risk assessment pod
* [get_risk_assessment_kubernetes_cluster_id_pods](docs/sdks/riskassessment/README.md#get_risk_assessment_kubernetes_cluster_id_pods) - Get all risk assessments of all pods of given cluster
* [post_risk_assessment_ignored_risks](docs/sdks/riskassessment/README.md#post_risk_assessment_ignored_risks) - Add ignore risk
* [post_risk_assessment_permissions_owner_id_approve](docs/sdks/riskassessment/README.md#post_risk_assessment_permissions_owner_id_approve) - add / remove permissions to /from the approved permissions list
* [post_risk_assessment_kubernetes_cluster_id_scan](docs/sdks/riskassessment/README.md#post_risk_assessment_kubernetes_cluster_id_scan) - Execute a new runtime scan on the given cluster with the given configuration
* [post_risk_assessment_kubernetes_cluster_id_settings](docs/sdks/riskassessment/README.md#post_risk_assessment_kubernetes_cluster_id_settings) - Save the runtime scan configuration on the given cluster
* [put_risk_assessment_ignored_risks_ignored_risk_id_](docs/sdks/riskassessment/README.md#put_risk_assessment_ignored_risks_ignored_risk_id_) - Edit ignore risk

### [settings](docs/sdks/settings/README.md)

* [delete_settings_integrations_ca_id_](docs/sdks/settings/README.md#delete_settings_integrations_ca_id_) - Delete the CA integration details
* [delete_settings_integrations_event_forwarding_event_forwarding_id_](docs/sdks/settings/README.md#delete_settings_integrations_event_forwarding_event_forwarding_id_) - Delete the event forwarding integration details with the given id
* [get_settings_agents_update](docs/sdks/settings/README.md#get_settings_agents_update) - Get the agents update configurations
* [get_settings_integrations_ca](docs/sdks/settings/README.md#get_settings_integrations_ca) - Get the CA integration details
* [get_settings_integrations_event_forwarding](docs/sdks/settings/README.md#get_settings_integrations_event_forwarding) - Get the event forwarding integration details
* [post_seccomp_profiles_validate_data](docs/sdks/settings/README.md#post_seccomp_profiles_validate_data) - Test the seccomp profile data
* [post_settings_agents_update_update_now](docs/sdks/settings/README.md#post_settings_agents_update_update_now) - Update the agents of the account now
* [post_settings_integrations_ca](docs/sdks/settings/README.md#post_settings_integrations_ca) - Set the CA integration details
* [post_settings_integrations_event_forwarding](docs/sdks/settings/README.md#post_settings_integrations_event_forwarding) - Set the event forwarding integration details
* [post_settings_integrations_opsgenie_test_integration](docs/sdks/settings/README.md#post_settings_integrations_opsgenie_test_integration) - Test the connection to Opsgenie
* [post_settings_integrations_securex_test_integration](docs/sdks/settings/README.md#post_settings_integrations_securex_test_integration) - Test the SecureX integration by sending test message to the provided URL
* [post_settings_integrations_slack_test_integration](docs/sdks/settings/README.md#post_settings_integrations_slack_test_integration) - Test the Slack integration by sending test message to the provided URL
* [post_settings_integrations_splunk_test_integration](docs/sdks/settings/README.md#post_settings_integrations_splunk_test_integration) - Test the connection to Splunk
* [post_settings_integrations_sumo_logic_test_integration](docs/sdks/settings/README.md#post_settings_integrations_sumo_logic_test_integration) - Test the Sumo Logic integration by sending test message to the provided URL
* [post_settings_integrations_teams_test_integration](docs/sdks/settings/README.md#post_settings_integrations_teams_test_integration) - Test the connection to Teams
* [post_settings_integrations_webex_test_integration](docs/sdks/settings/README.md#post_settings_integrations_webex_test_integration) - Test the Webex integration by sending test message to the provided URL
* [put_settings_agents_update](docs/sdks/settings/README.md#put_settings_agents_update) - get the agents update configurations.
* [put_settings_integrations_ca_id_](docs/sdks/settings/README.md#put_settings_integrations_ca_id_) - Edit the CA integration details
* [put_settings_integrations_event_forwarding_event_forwarding_id_](docs/sdks/settings/README.md#put_settings_integrations_event_forwarding_event_forwarding_id_) - Edit the event forwarding integration details

### [serverless_policies](docs/sdks/serverlesspolicies/README.md)

* [get_serverless_policy](docs/sdks/serverlesspolicies/README.md#get_serverless_policy) - Get current serverless policy
* [put_serverless_policy](docs/sdks/serverlesspolicies/README.md#put_serverless_policy) - Set the current serverless policy

### [tokens](docs/sdks/tokens/README.md)

* [delete_tokens_token_id_](docs/sdks/tokens/README.md#delete_tokens_token_id_) - Delete token
* [get_tokens](docs/sdks/tokens/README.md#get_tokens) - Get tokens
* [get_tokens_info](docs/sdks/tokens/README.md#get_tokens_info) - Get tokens by Ids
* [get_tokens_token_id_delete_dependencies](docs/sdks/tokens/README.md#get_tokens_token_id_delete_dependencies) - get dependancies which need to be handled in order to delete specified token
* [post_tokens](docs/sdks/tokens/README.md#post_tokens) - Add new token
* [put_tokens_token_id_](docs/sdks/tokens/README.md#put_tokens_token_id_) - Edit token

### [cli](docs/sdks/cli/README.md)

* [get_tools_cli_securecn_deployment_cli](docs/sdks/cli/README.md#get_tools_cli_securecn_deployment_cli) - Get the Secure Application deployment cli

### [truncation](docs/sdks/truncation/README.md)

* [get_truncation_images](docs/sdks/truncation/README.md#get_truncation_images) - Get workloads truncation time for account
* [get_truncation_workloads](docs/sdks/truncation/README.md#get_truncation_workloads) - Get workloads truncation time for account
* [post_truncation_images](docs/sdks/truncation/README.md#post_truncation_images) - Update workloads truncation status for account
* [post_truncation_workloads](docs/sdks/truncation/README.md#post_truncation_workloads) - Update workloads truncation status for account

### [trusted_signers](docs/sdks/trustedsigners/README.md)

* [delete_trusted_signers_trusted_signer_id_](docs/sdks/trustedsigners/README.md#delete_trusted_signers_trusted_signer_id_) - Delete a trusted signer
* [get_trusted_signers](docs/sdks/trustedsigners/README.md#get_trusted_signers) - Get a list of defined trusted signers
* [get_trusted_signers_trusted_signer_id_](docs/sdks/trustedsigners/README.md#get_trusted_signers_trusted_signer_id_) - get existing trusted signer
* [post_trusted_signers](docs/sdks/trustedsigners/README.md#post_trusted_signers) - Add new trusted signer
* [put_trusted_signers_trusted_signer_id_](docs/sdks/trustedsigners/README.md#put_trusted_signers_trusted_signer_id_) - edit existing trusted signer

### [vulnerabilities](docs/sdks/vulnerabilities/README.md)

* [get_vulnerabilities](docs/sdks/vulnerabilities/README.md#get_vulnerabilities) - search for vulnerability names in the account
<!-- End Available Resources and Operations [operations] -->



<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| errors.APIResponse | 402                | application/json   |
| errors.SDKError    | 4x-5xx             | */*                |

### Example

```python
import pan
from pan.models import errors, operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.PostLoginRequest()

res = None
try:
    res = s.users.post_login(req)
except errors.APIResponse as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.user_login_info is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https:///api` | None |

#### Example

```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    server_idx=0,
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteUsersUserIDRequest(
    user_id='2d4aef6d-76db-4c57-a2a3-fe8efd3db6e2',
)

res = s.users.delete_users_user_id_(req)

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    server_url="https:///api",
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteUsersUserIDRequest(
    user_id='2d4aef6d-76db-4c57-a2a3-fe8efd3db6e2',
)

res = s.users.delete_users_user_id_(req)

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import pan
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = pan.Pan(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name       | Type       | Scheme     |
| ---------- | ---------- | ---------- |
| `password` | http       | HTTP Basic |
| `username` | http       | HTTP Basic |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import pan
from pan.models import operations, shared

s = pan.Pan(
    security=shared.Security(
        password="<YOUR_PASSWORD_HERE>",
    ),
)

req = operations.DeleteUsersUserIDRequest(
    user_id='2d4aef6d-76db-4c57-a2a3-fe8efd3db6e2',
)

res = s.users.delete_users_user_id_(req)

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
