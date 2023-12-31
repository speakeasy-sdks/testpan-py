"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pan import utils
from pan.models import errors, operations, shared
from typing import List, Optional

class Dashboard:
    r"""APIs to get dashboard statistics"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_dashboard_apisec_risk_findings(self, request: operations.GetDashboardApisecRiskFindingsRequest) -> operations.GetDashboardApisecRiskFindingsResponse:
        r"""Get API sec risk findings widget"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/apisec/riskFindings'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardApisecRiskFindingsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardApisecRiskFindingsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APISecRiskFindingsWidget])
                res.api_sec_risk_findings_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_apisec_risk_findings_trend(self, request: operations.GetDashboardApisecRiskFindingsTrendRequest) -> operations.GetDashboardApisecRiskFindingsTrendResponse:
        r"""Get API sec risk findings trend graph widget for the last 30 days"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/apisec/riskFindingsTrend'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardApisecRiskFindingsTrendRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardApisecRiskFindingsTrendResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APISecRiskFindingsTrendWidget])
                res.api_sec_risk_findings_trend_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_apisec_specs_and_operations_diffs(self, request: operations.GetDashboardApisecSpecsAndOperationsDiffsRequest) -> operations.GetDashboardApisecSpecsAndOperationsDiffsResponse:
        r"""Get API sec specs and operations diffs widget"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/apisec/specsAndOperationsDiffs'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardApisecSpecsAndOperationsDiffsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardApisecSpecsAndOperationsDiffsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SpecsAndOperationsDiffsWidget])
                res.specs_and_operations_diffs_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_apisec_top_risky_apis(self, request: operations.GetDashboardApisecTopRiskyApisRequest) -> operations.GetDashboardApisecTopRiskyApisResponse:
        r"""Get API sec top risky APIs widget"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/apisec/topRiskyApis'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardApisecTopRiskyApisRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardApisecTopRiskyApisResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APISecTopRiskyApisWidget])
                res.api_sec_top_risky_apis_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_apisec_top_risky_findings(self, request: operations.GetDashboardApisecTopRiskyFindingsRequest) -> operations.GetDashboardApisecTopRiskyFindingsResponse:
        r"""Get API sec top risky findings widget"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/apisec/topRiskyFindings'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardApisecTopRiskyFindingsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardApisecTopRiskyFindingsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APISecTopRiskyFindingsWidget])
                res.api_sec_top_risky_findings_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_clusters(self) -> operations.GetDashboardClustersResponse:
        r"""Get the active clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/clusters'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardClustersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.ClusterDetails]])
                res.clusters_details = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_connection_telemetries(self) -> operations.GetDashboardConnectionTelemetriesResponse:
        r"""Get pod connection dashboard data for all clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/connectionTelemetries'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardConnectionTelemetriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TimeBasedWidget])
                res.time_based_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_kubernetes_audit_logs(self) -> operations.GetDashboardKubernetesAuditLogsResponse:
        r"""Get kubernetes audit logs dashboard data for all clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/kubernetesAuditLogs'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardKubernetesAuditLogsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TimeBasedWidget])
                res.time_based_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_operational_bar(self, request: operations.GetDashboardOperationalBarRequest) -> operations.GetDashboardOperationalBarResponse:
        r"""Get the operation data dashboard for the given kubernetesClusterId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/operationalBar'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardOperationalBarRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardOperationalBarResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OperationalBar])
                res.operational_bar = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_permissions(self, request: operations.GetDashboardPermissionsRequest) -> operations.GetDashboardPermissionsResponse:
        r"""Get permissions dashboard data for the given kubernetesClusterIds"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/permissions'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardPermissionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardPermissionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PermissionsWidget])
                res.permissions_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_pod_telemetries(self) -> operations.GetDashboardPodTelemetriesResponse:
        r"""Get pod telemetries dashboard data for all clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/podTelemetries'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardPodTelemetriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TimeBasedWidget])
                res.time_based_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_report_download(self) -> operations.GetDashboardReportDownloadResponse:
        r"""Download Secure Application security report"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/report/download'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardReportDownloadResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.stream = http_res
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_report_status(self) -> operations.GetDashboardReportStatusResponse:
        r"""Get Secure Application report security status"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/report/status'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardReportStatusResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ReportStatus])
                res.report_status = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_security_context(self, request: operations.GetDashboardSecurityContextRequest) -> operations.GetDashboardSecurityContextResponse:
        r"""Get security context dashboard data for all clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/securityContext'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardSecurityContextRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardSecurityContextResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.SecurityContextWidget])
                res.security_context_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_top_security_risks(self, request: operations.GetDashboardTopSecurityRisksRequest) -> operations.GetDashboardTopSecurityRisksResponse:
        r"""Get the top risky deployments dashboard data for the given kubernetesClusterIds"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/topSecurityRisks'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardTopSecurityRisksRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardTopSecurityRisksResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TopSecurityRisksWidget])
                res.top_security_risks_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_vulnerabilities(self, request: operations.GetDashboardVulnerabilitiesRequest) -> operations.GetDashboardVulnerabilitiesResponse:
        r"""Get vulnerabilities dashboard data for the given kubernetesClusterId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/vulnerabilities'
        headers = {}
        query_params = utils.get_query_params(operations.GetDashboardVulnerabilitiesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardVulnerabilitiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.VulnerabilitiesWidget])
                res.vulnerabilities_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_kubernetes_cluster_id_connection_telemetries(self, request: operations.GetDashboardKubernetesClusterIDConnectionTelemetriesRequest) -> operations.GetDashboardKubernetesClusterIDConnectionTelemetriesResponse:
        r"""Get connection telemetries dashboard data for the given kubernetesClusterId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetDashboardKubernetesClusterIDConnectionTelemetriesRequest, base_url, '/dashboard/{kubernetesClusterId}/connectionTelemetries', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardKubernetesClusterIDConnectionTelemetriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TimeBasedWidget])
                res.time_based_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_kubernetes_cluster_id_kubernetes_audit_logs(self, request: operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsRequest) -> operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsResponse:
        r"""Get kubernetes audit logs dashboard data for the given kubernetesClusterId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsRequest, base_url, '/dashboard/{kubernetesClusterId}/kubernetesAuditLogs', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardKubernetesClusterIDKubernetesAuditLogsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TimeBasedWidget])
                res.time_based_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_dashboard_kubernetes_cluster_id_pod_telemetries(self, request: operations.GetDashboardKubernetesClusterIDPodTelemetriesRequest) -> operations.GetDashboardKubernetesClusterIDPodTelemetriesResponse:
        r"""Get pod telemetries dashboard data for the given kubernetesClusterId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetDashboardKubernetesClusterIDPodTelemetriesRequest, base_url, '/dashboard/{kubernetesClusterId}/podTelemetries', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetDashboardKubernetesClusterIDPodTelemetriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TimeBasedWidget])
                res.time_based_widget = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_licensing_dashboard(self) -> operations.GetLicensingDashboardResponse:
        r"""Get licensing dashboard data"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/licensingDashboard'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetLicensingDashboardResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.LicensingDashboard])
                res.licensing_dashboard = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def post_dashboard_report_generate(self) -> operations.PostDashboardReportGenerateResponse:
        r"""Generate Secure Application security report"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/dashboard/report/generate'
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostDashboardReportGenerateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    