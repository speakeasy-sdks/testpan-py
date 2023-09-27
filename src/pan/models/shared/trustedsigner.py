"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import trustedsignercloudaccount as shared_trustedsignercloudaccount
from ..shared import trustedsignercluster as shared_trustedsignercluster
from ..shared import trustedsignerkey as shared_trustedsignerkey
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TrustedSignerInput:
    r"""Trusted signers profile"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    keys: Optional[list[shared_trustedsignerkey.TrustedSignerKey]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keys'), 'exclude': lambda f: f is None }})
    trusted_signer_cloud_accounts: Optional[list[shared_trustedsignercloudaccount.TrustedSignerCloudAccountInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trustedSignerCloudAccounts'), 'exclude': lambda f: f is None }})
    trusted_signer_clusters: Optional[list[shared_trustedsignercluster.TrustedSignerClusterInput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trustedSignerClusters'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TrustedSigner:
    r"""Trusted signers profile"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    keys: Optional[list[shared_trustedsignerkey.TrustedSignerKey]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keys'), 'exclude': lambda f: f is None }})
    trusted_signer_cloud_accounts: Optional[list[shared_trustedsignercloudaccount.TrustedSignerCloudAccount]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trustedSignerCloudAccounts'), 'exclude': lambda f: f is None }})
    trusted_signer_clusters: Optional[list[shared_trustedsignercluster.TrustedSignerCluster]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trustedSignerClusters'), 'exclude': lambda f: f is None }})
    

