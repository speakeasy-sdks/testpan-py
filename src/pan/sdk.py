"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .advisor import Advisor
from .agent_management import AgentManagement
from .api import API
from .api_security import APISecurity
from .api_security_policies import APISecurityPolicies
from .apps import Apps
from .audit_logs import AuditLogs
from .aws import Aws
from .bfla import Bfla
from .cd import Cd
from .ci_cd_policies import CICDPolicies
from .cli import Cli
from .cluster_events_policies import ClusterEventsPolicies
from .connection_policies import ConnectionPolicies
from .dashboard import Dashboard
from .deployers import Deployers
from .environment_policies import EnvironmentPolicies
from .envs import Envs
from .expansions import Expansions
from .gateways import Gateways
from .images_and_vulnerabilities import ImagesAndVulnerabilities
from .k8s_cis_benchmark import K8sCisBenchmark
from .kubernetes import Kubernetes
from .mitre import Mitre
from .performance import Performance
from .psp_profiles import PspProfiles
from .registries import Registries
from .risk_assessment import RiskAssessment
from .runtime_map import RuntimeMap
from .sdkconfiguration import SDKConfiguration
from .serverless import Serverless
from .serverless_policies import ServerlessPolicies
from .settings import Settings
from .telemetries import Telemetries
from .tokens import Tokens
from .truncation import Truncation
from .trusted_signers import TrustedSigners
from .users import Users
from .vulnerabilities import Vulnerabilities
from pan import utils
from pan._hooks import SDKHooks
from pan.models import shared
from typing import Callable, Dict, Optional, Union

class Pan:
    r"""https://panoptica.readme.io/reference - Product Documentation"""
    users: Users
    r"""APIs used for login and password management"""
    images_and_vulnerabilities: ImagesAndVulnerabilities
    r"""APIs used to define and manage  image hashes"""
    advisor: Advisor
    r"""APIs used to get policy recommendations"""
    agent_management: AgentManagement
    r"""APIs use to  interact with  agents"""
    api: API
    r"""APIs to get the Secure Application API specification file"""
    api_security: APISecurity
    r"""APIs used to manage Api Security"""
    performance: Performance
    bfla: Bfla
    api_security_policies: APISecurityPolicies
    r"""APIs used to  define and manage api security policies"""
    telemetries: Telemetries
    r"""APIs used to query for telemetries"""
    apps: Apps
    r"""APIs used to define apps"""
    environment_policies: EnvironmentPolicies
    r"""APIs used to  define and manage environment policies"""
    audit_logs: AuditLogs
    r"""APIs used to retrieve  audit logs"""
    aws: Aws
    r"""APIs used to change  credentials or return details about the  user's AWS environment"""
    cd: Cd
    r"""APIs used to query for CD pipelines results"""
    ci_cd_policies: CICDPolicies
    r"""APIs used to  define and manage CI/CD policies"""
    serverless: Serverless
    connection_policies: ConnectionPolicies
    r"""APIs used to  define and manage connection policies"""
    dashboard: Dashboard
    r"""APIs to get dashboard statistics"""
    deployers: Deployers
    r"""APIs used to manage deployers on Secure Application"""
    envs: Envs
    r"""APIs used to define environments"""
    expansions: Expansions
    r"""APIs used to manage expansions on Secure Application"""
    gateways: Gateways
    kubernetes: Kubernetes
    r"""APIs used to manage Kubernetes clusters on Secure Application"""
    k8s_cis_benchmark: K8sCisBenchmark
    r"""APIs to get the kubernetes cis benchmark data"""
    cluster_events_policies: ClusterEventsPolicies
    r"""APIs used to  define and manage cluster events policies"""
    mitre: Mitre
    runtime_map: RuntimeMap
    r"""APIs used to  query for network map"""
    psp_profiles: PspProfiles
    r"""APIs used to manage pod security standards profiles on Secure Application"""
    registries: Registries
    r"""APIs used to  define and manage registries"""
    risk_assessment: RiskAssessment
    r"""APIs used to manage risk assessment on Kubernetes clusters"""
    settings: Settings
    r"""APIs used  to configure system settings"""
    serverless_policies: ServerlessPolicies
    tokens: Tokens
    cli: Cli
    r"""APIs to get the Secure Application CLI"""
    truncation: Truncation
    r"""APIs to delete workloads"""
    trusted_signers: TrustedSigners
    r"""APIs used to  define and manage trusted signers"""
    vulnerabilities: Vulnerabilities

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[utils.RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration._hooks = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.users = Users(self.sdk_configuration)
        self.images_and_vulnerabilities = ImagesAndVulnerabilities(self.sdk_configuration)
        self.advisor = Advisor(self.sdk_configuration)
        self.agent_management = AgentManagement(self.sdk_configuration)
        self.api = API(self.sdk_configuration)
        self.api_security = APISecurity(self.sdk_configuration)
        self.performance = Performance(self.sdk_configuration)
        self.bfla = Bfla(self.sdk_configuration)
        self.api_security_policies = APISecurityPolicies(self.sdk_configuration)
        self.telemetries = Telemetries(self.sdk_configuration)
        self.apps = Apps(self.sdk_configuration)
        self.environment_policies = EnvironmentPolicies(self.sdk_configuration)
        self.audit_logs = AuditLogs(self.sdk_configuration)
        self.aws = Aws(self.sdk_configuration)
        self.cd = Cd(self.sdk_configuration)
        self.ci_cd_policies = CICDPolicies(self.sdk_configuration)
        self.serverless = Serverless(self.sdk_configuration)
        self.connection_policies = ConnectionPolicies(self.sdk_configuration)
        self.dashboard = Dashboard(self.sdk_configuration)
        self.deployers = Deployers(self.sdk_configuration)
        self.envs = Envs(self.sdk_configuration)
        self.expansions = Expansions(self.sdk_configuration)
        self.gateways = Gateways(self.sdk_configuration)
        self.kubernetes = Kubernetes(self.sdk_configuration)
        self.k8s_cis_benchmark = K8sCisBenchmark(self.sdk_configuration)
        self.cluster_events_policies = ClusterEventsPolicies(self.sdk_configuration)
        self.mitre = Mitre(self.sdk_configuration)
        self.runtime_map = RuntimeMap(self.sdk_configuration)
        self.psp_profiles = PspProfiles(self.sdk_configuration)
        self.registries = Registries(self.sdk_configuration)
        self.risk_assessment = RiskAssessment(self.sdk_configuration)
        self.settings = Settings(self.sdk_configuration)
        self.serverless_policies = ServerlessPolicies(self.sdk_configuration)
        self.tokens = Tokens(self.sdk_configuration)
        self.cli = Cli(self.sdk_configuration)
        self.truncation = Truncation(self.sdk_configuration)
        self.trusted_signers = TrustedSigners(self.sdk_configuration)
        self.vulnerabilities = Vulnerabilities(self.sdk_configuration)
