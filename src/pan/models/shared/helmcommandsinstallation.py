"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from pan import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HelmCommandsInstallation:
    istio_helm_command: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('istioHelmCommand'), 'exclude': lambda f: f is None }})
    r"""Cmd of istio values"""
    panoptica_helm_command: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('panopticaHelmCommand'), 'exclude': lambda f: f is None }})
    r"""Cmd of panoptica values"""
    vault_helm_command: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vaultHelmCommand'), 'exclude': lambda f: f is None }})
    r"""Cmd of vault values"""
    

