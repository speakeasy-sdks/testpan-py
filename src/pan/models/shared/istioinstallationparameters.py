"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class IstioInstallationParameters:
    r"""istio related information"""
    is_istio_already_installed: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isIstioAlreadyInstalled'), 'exclude': lambda f: f is None }})
    r"""indicates whether Istio is already installed on this cluster (which means Secure Application should not install it)"""
    istio_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('istioVersion'), 'exclude': lambda f: f is None }})
    r"""when istio already installed, choose the version from supported istio versions list: /istio/supportedVersions"""
    

