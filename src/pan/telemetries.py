"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pan import utils
from pan.models import errors, operations, shared
from typing import List, Optional

class Telemetries:
    r"""APIs used to query for telemetries"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_app_telemetries(self, request: operations.GetAppTelemetriesRequest) -> operations.GetAppTelemetriesResponse:
        r"""Get App telemetries"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/appTelemetries'
        headers = {}
        query_params = utils.get_query_params(operations.GetAppTelemetriesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAppTelemetriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.AppTelemetry]])
                res.app_telemetries = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_app_telemetries_app_telemetry_id_(self, request: operations.GetAppTelemetriesAppTelemetryIDRequest) -> operations.GetAppTelemetriesAppTelemetryIDResponse:
        r"""Get App telemetry by ID"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAppTelemetriesAppTelemetryIDRequest, base_url, '/appTelemetries/{appTelemetryId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAppTelemetriesAppTelemetryIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AppTelemetry])
                res.app_telemetry = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 404 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_app_telemetries_app_telemetry_id_api_risk_info(self, request: operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest) -> operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoResponse:
        r"""Get API risks info of given app telemetry"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoRequest, base_url, '/appTelemetries/{appTelemetryId}/apiRiskInfo', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAppTelemetriesAppTelemetryIDAPIRiskInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.APIRiskInfo]])
                res.api_risk_infos = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_app_telemetries_app_telemetry_id_image_packages(self, request: operations.GetAppTelemetriesAppTelemetryIDImagePackagesRequest) -> operations.GetAppTelemetriesAppTelemetryIDImagePackagesResponse:
        r"""list packages with licenses runnin on a pod"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAppTelemetriesAppTelemetryIDImagePackagesRequest, base_url, '/appTelemetries/{appTelemetryId}/imagePackages', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAppTelemetriesAppTelemetryIDImagePackagesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.ImagesWithLicenses]])
                res.images_with_licenses = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 404 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_app_telemetries_app_telemetry_id_injection_info(self, request: operations.GetAppTelemetriesAppTelemetryIDInjectionInfoRequest) -> operations.GetAppTelemetriesAppTelemetryIDInjectionInfoResponse:
        r"""Get token injection info of given app telemetry"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAppTelemetriesAppTelemetryIDInjectionInfoRequest, base_url, '/appTelemetries/{appTelemetryId}/injectionInfo', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAppTelemetriesAppTelemetryIDInjectionInfoResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.TokenInjectionInfo]])
                res.token_injection_infos = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_connection_telemetries(self, request: operations.GetConnectionTelemetriesRequest) -> operations.GetConnectionTelemetriesResponse:
        r"""Get connection telemetries"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/connectionTelemetries'
        headers = {}
        query_params = utils.get_query_params(operations.GetConnectionTelemetriesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetConnectionTelemetriesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.ConnectionTelemetry]])
                res.connection_telemetries = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_connection_telemetries_connection_telemetry_id_(self, request: operations.GetConnectionTelemetriesConnectionTelemetryIDRequest) -> operations.GetConnectionTelemetriesConnectionTelemetryIDResponse:
        r"""get details for a single connection telemetry"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetConnectionTelemetriesConnectionTelemetryIDRequest, base_url, '/connectionTelemetries/{connectionTelemetryId}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetConnectionTelemetriesConnectionTelemetryIDRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetConnectionTelemetriesConnectionTelemetryIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectionTelemetry])
                res.connection_telemetry = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    