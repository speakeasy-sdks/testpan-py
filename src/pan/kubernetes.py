"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from pan import utils
from pan.models import errors, operations, shared
from typing import Optional

class Kubernetes:
    r"""APIs used to manage Kubernetes clusters on Secure Application"""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def delete_kubernetes_clusters_kubernetes_cluster_id_(self, request: operations.DeleteKubernetesClustersKubernetesClusterIDRequest) -> operations.DeleteKubernetesClustersKubernetesClusterIDResponse:
        r"""Delete a Kubernetes cluster"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteKubernetesClustersKubernetesClusterIDRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteKubernetesClustersKubernetesClusterIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def delete_pod_definitions_pod_id_(self, request: operations.DeletePodDefinitionsPodIDRequest) -> operations.DeletePodDefinitionsPodIDResponse:
        r"""Delete a pod definition"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeletePodDefinitionsPodIDRequest, base_url, '/podDefinitions/{podId}', request)
        headers = {}
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeletePodDefinitionsPodIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 204:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_get_controller_data_cluster_id_(self, request: operations.GetGetControllerDataClusterIDRequest) -> operations.GetGetControllerDataClusterIDResponse:
        r"""get controller data using clusterId"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetGetControllerDataClusterIDRequest, base_url, '/getControllerData/{clusterId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetGetControllerDataClusterIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ControllerDataResponse])
                res.controller_data_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_istio_supported_versions(self) -> operations.GetIstioSupportedVersionsResponse:
        r"""Get a list of istio releases that are supported by Secure Application agent. sorted from latest to oldest"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/istio/supportedVersions'
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetIstioSupportedVersionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[str]])
                res.get_istio_supported_versions_200_application_json_strings = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 401 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters(self, request: operations.GetKubernetesClustersRequest) -> operations.GetKubernetesClustersResponse:
        r"""get a list of current Kubernetes clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/kubernetesClusters'
        headers = {}
        query_params = utils.get_query_params(operations.GetKubernetesClustersRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.KubernetesClusterController]])
                res.kubernetes_cluster_controllers = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters_kubernetes_cluster_id_(self, request: operations.GetKubernetesClustersKubernetesClusterIDRequest) -> operations.GetKubernetesClustersKubernetesClusterIDResponse:
        r"""get the Kubernetes cluster with the given id"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetKubernetesClustersKubernetesClusterIDRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersKubernetesClusterIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.KubernetesCluster])
                res.kubernetes_cluster = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters_kubernetes_cluster_id_delete_dependencies(self, request: operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesRequest) -> operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesResponse:
        r"""get dependencies which need to be handled in order to delete specified Kubernetes cluster"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}/deleteDependencies', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersKubernetesClusterIDDeleteDependenciesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.KubernetesClusterDeleteDependencies])
                res.kubernetes_cluster_delete_dependencies = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters_kubernetes_cluster_id_download_bundle(self, request: operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest) -> operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleResponse:
        r"""Get Secure Application installation script
        In order to install,  extract and run \"./install_bundle.sh\" 
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}/download_bundle', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersKubernetesClusterIDDownloadBundleResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                res.get_kubernetes_clusters_kubernetes_cluster_id_download_bundle_200_application_json_binary_string = http_res
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters_kubernetes_cluster_id_get_helm_commands(self, request: operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsRequest) -> operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsResponse:
        r"""Get Panoptica Aug release Helm command"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}/getHelmCommands', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersKubernetesClusterIDGetHelmCommandsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.HelmCommandsInstallation])
                res.helm_commands_installation = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters_kubernetes_cluster_id_namespaces(self, request: operations.GetKubernetesClustersKubernetesClusterIDNamespacesRequest) -> operations.GetKubernetesClustersKubernetesClusterIDNamespacesResponse:
        r"""List namespaces on a specific Kubernetes cluster"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetKubernetesClustersKubernetesClusterIDNamespacesRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}/namespaces', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetKubernetesClustersKubernetesClusterIDNamespacesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersKubernetesClusterIDNamespacesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.KubernetesNamespace]])
                res.kubernetes_namespace_responses = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_kubernetes_clusters_kubernetes_cluster_id_services(self, request: operations.GetKubernetesClustersKubernetesClusterIDServicesRequest) -> operations.GetKubernetesClustersKubernetesClusterIDServicesResponse:
        r"""List services on a specific Kubernetes cluster"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetKubernetesClustersKubernetesClusterIDServicesRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}/services', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetKubernetesClustersKubernetesClusterIDServicesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetKubernetesClustersKubernetesClusterIDServicesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.KubernetesService]])
                res.kubernetes_services = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_lean_kubernetes_clusters(self, request: operations.GetLeanKubernetesClustersRequest) -> operations.GetLeanKubernetesClustersResponse:
        r"""get a list of current Kubernetes clusters"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/leanKubernetesClusters'
        headers = {}
        query_params = utils.get_query_params(operations.GetLeanKubernetesClustersRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetLeanKubernetesClustersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.LeanKubernetesCluster]])
                res.lean_kubernetes_clusters = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_namespaces(self, request: operations.GetNamespacesRequest) -> operations.GetNamespacesResponse:
        r"""Get a list of current Kubernetes namespaces"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/namespaces'
        headers = {}
        query_params = utils.get_query_params(operations.GetNamespacesRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetNamespacesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.Namespace]])
                res.namespaces = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_pod_definitions(self, request: operations.GetPodDefinitionsRequest) -> operations.GetPodDefinitionsResponse:
        r"""Get all pod definitions on the system"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/podDefinitions'
        headers = {}
        query_params = utils.get_query_params(operations.GetPodDefinitionsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetPodDefinitionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.PodDefinition]])
                res.pod_definitions = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def post_kubernetes_clusters(self, request: shared.KubernetesCluster) -> operations.PostKubernetesClustersResponse:
        r"""Add a new Kubernetes cluster to Secure Application"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/kubernetesClusters'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostKubernetesClustersResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.KubernetesCluster])
                res.kubernetes_cluster = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def post_pod_definitions(self, request: shared.PodDefinitionInput) -> operations.PostPodDefinitionsResponse:
        r"""Create a new pod definition"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/podDefinitions'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostPodDefinitionsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PodDefinition])
                res.pod_definition = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 409 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    def put_kubernetes_clusters_kubernetes_cluster_id_(self, request: operations.PutKubernetesClustersKubernetesClusterIDRequest) -> operations.PutKubernetesClustersKubernetesClusterIDResponse:
        r"""Update the Kubernetes cluster"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutKubernetesClustersKubernetesClusterIDRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "kubernetes_cluster", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutKubernetesClustersKubernetesClusterIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.KubernetesCluster])
                res.kubernetes_cluster = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def put_kubernetes_clusters_kubernetes_cluster_id_managed_by_helm(self, request: operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmRequest) -> operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmResponse:
        r"""Update the Kubernetes cluster which managed by HELM"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmRequest, base_url, '/kubernetesClusters/{kubernetesClusterId}/managedByHelm', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "edit_kubernetes_cluster_managed_by_helm", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutKubernetesClustersKubernetesClusterIDManagedByHelmResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.KubernetesCluster])
                res.kubernetes_cluster = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIResponse])
                res.api_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def put_pod_definitions_pod_id_(self, request: operations.PutPodDefinitionsPodIDRequest) -> operations.PutPodDefinitionsPodIDResponse:
        r"""Change pod definition"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.PutPodDefinitionsPodIDRequest, base_url, '/podDefinitions/{podId}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "pod_definition_input", False, False, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutPodDefinitionsPodIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.PodDefinition])
                res.pod_definition = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    