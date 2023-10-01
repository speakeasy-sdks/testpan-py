"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pan import utils
from pan.models import errors, operations, shared
from typing import Optional

class Performance:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_api_security_api_catalog_id_hit_count_graph(self, request: operations.GetAPISecurityAPICatalogIDHitCountGraphRequest) -> operations.GetAPISecurityAPICatalogIDHitCountGraphResponse:
        r"""Get hit count for specific spec path"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAPISecurityAPICatalogIDHitCountGraphRequest, base_url, '/apiSecurity/api/{catalogId}/hitCountGraph', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAPISecurityAPICatalogIDHitCountGraphRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAPISecurityAPICatalogIDHitCountGraphResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.APIServiceSpecPathHitCountGraphPoint]])
                res.api_service_spec_path_hit_count_graph = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_performance_metrics(self, request: operations.GetPerformanceMetricsRequest) -> operations.GetPerformanceMetricsResponse:
        r"""Get performance metrics for a connection between workloads"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/performanceMetrics'
        headers = {}
        query_params = utils.get_query_params(operations.GetPerformanceMetricsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPerformanceMetricsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PerformanceMetrics])
                res.performance_metrics = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    