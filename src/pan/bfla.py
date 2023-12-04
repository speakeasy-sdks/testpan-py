"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pan import utils
from pan.models import errors, operations, shared
from typing import Optional

class Bfla:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def delete_api_security_internal_catalog_catalog_id_bfla_detection(self, request: operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest) -> operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionResponse:
        r"""stop bfla detection phase"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla/detection', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.DeleteAPISecurityInternalCatalogCatalogIDBflaDetectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def delete_api_security_internal_catalog_catalog_id_bfla_learning(self, request: operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest) -> operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningResponse:
        r"""stop bfla learning phase"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla/learning', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.DeleteAPISecurityInternalCatalogCatalogIDBflaLearningResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_api_security_internal_catalog_catalog_id_bfla(self, request: operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest) -> operations.GetAPISecurityInternalCatalogCatalogIDBflaResponse:
        r"""Get bfla info for given catalogId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAPISecurityInternalCatalogCatalogIDBflaRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetAPISecurityInternalCatalogCatalogIDBflaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIServiceBflaInfo])
                res.api_service_bfla_info = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_api_security_internal_catalog_catalog_id_bfla_detection(self, request: operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionRequest) -> operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionResponse:
        r"""Start new bfla detection phase"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla/detection', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bfla_duration_configuration", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostAPISecurityInternalCatalogCatalogIDBflaDetectionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_api_security_internal_catalog_catalog_id_bfla_learning(self, request: operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningRequest) -> operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningResponse:
        r"""Start new bfla learning phase"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla/learning', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "bfla_duration_configuration", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostAPISecurityInternalCatalogCatalogIDBflaLearningResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def post_api_security_internal_catalog_catalog_id_bfla_reset(self, request: operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest) -> operations.PostAPISecurityInternalCatalogCatalogIDBflaResetResponse:
        r"""Reset bfla model"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PostAPISecurityInternalCatalogCatalogIDBflaResetRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla/reset', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PostAPISecurityInternalCatalogCatalogIDBflaResetResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def put_api_security_internal_catalog_catalog_id_bfla(self, request: operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest) -> operations.PutAPISecurityInternalCatalogCatalogIDBflaResponse:
        r"""update BFLA info for this catalogId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutAPISecurityInternalCatalogCatalogIDBflaRequest, base_url, '/apiSecurity/internalCatalog/{catalogId}/bfla', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "api_service_bfla_info", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PutAPISecurityInternalCatalogCatalogIDBflaResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.res = http_res.content
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    