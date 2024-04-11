# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'TwingateResourceAccessGroupArgs',
    'TwingateResourceAccessServiceArgs',
    'TwingateResourceProtocolsArgs',
    'TwingateResourceProtocolsTcpArgs',
    'TwingateResourceProtocolsUdpArgs',
    'GetTwingateResourceProtocolsArgs',
    'GetTwingateResourceProtocolsTcpArgs',
    'GetTwingateResourceProtocolsUdpArgs',
]

@pulumi.input_type
class TwingateResourceAccessGroupArgs:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 security_policy_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] group_id: Group ID that will have permission to access the Resource.
        :param pulumi.Input[str] security_policy_id: The ID of a `get_twingate_security_policy` to use as the access policy for the group IDs in the access block.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if security_policy_id is not None:
            pulumi.set(__self__, "security_policy_id", security_policy_id)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Group ID that will have permission to access the Resource.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="securityPolicyId")
    def security_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a `get_twingate_security_policy` to use as the access policy for the group IDs in the access block.
        """
        return pulumi.get(self, "security_policy_id")

    @security_policy_id.setter
    def security_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_policy_id", value)


@pulumi.input_type
class TwingateResourceAccessServiceArgs:
    def __init__(__self__, *,
                 service_account_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] service_account_id: The ID of the service account that should have access to this Resource.
        """
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the service account that should have access to this Resource.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)


@pulumi.input_type
class TwingateResourceProtocolsArgs:
    def __init__(__self__, *,
                 allow_icmp: Optional[pulumi.Input[bool]] = None,
                 tcp: Optional[pulumi.Input['TwingateResourceProtocolsTcpArgs']] = None,
                 udp: Optional[pulumi.Input['TwingateResourceProtocolsUdpArgs']] = None):
        """
        :param pulumi.Input[bool] allow_icmp: Whether to allow ICMP (ping) traffic
        """
        if allow_icmp is not None:
            pulumi.set(__self__, "allow_icmp", allow_icmp)
        if tcp is not None:
            pulumi.set(__self__, "tcp", tcp)
        if udp is not None:
            pulumi.set(__self__, "udp", udp)

    @property
    @pulumi.getter(name="allowIcmp")
    def allow_icmp(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to allow ICMP (ping) traffic
        """
        return pulumi.get(self, "allow_icmp")

    @allow_icmp.setter
    def allow_icmp(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_icmp", value)

    @property
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input['TwingateResourceProtocolsTcpArgs']]:
        return pulumi.get(self, "tcp")

    @tcp.setter
    def tcp(self, value: Optional[pulumi.Input['TwingateResourceProtocolsTcpArgs']]):
        pulumi.set(self, "tcp", value)

    @property
    @pulumi.getter
    def udp(self) -> Optional[pulumi.Input['TwingateResourceProtocolsUdpArgs']]:
        return pulumi.get(self, "udp")

    @udp.setter
    def udp(self, value: Optional[pulumi.Input['TwingateResourceProtocolsUdpArgs']]):
        pulumi.set(self, "udp", value)


@pulumi.input_type
class TwingateResourceProtocolsTcpArgs:
    def __init__(__self__, *,
                 policy: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ports", value)


@pulumi.input_type
class TwingateResourceProtocolsUdpArgs:
    def __init__(__self__, *,
                 policy: Optional[pulumi.Input[str]] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ports", value)


@pulumi.input_type
class GetTwingateResourceProtocolsArgs:
    def __init__(__self__, *,
                 allow_icmp: bool,
                 tcp: Optional['GetTwingateResourceProtocolsTcpArgs'] = None,
                 udp: Optional['GetTwingateResourceProtocolsUdpArgs'] = None):
        """
        :param bool allow_icmp: Whether to allow ICMP (ping) traffic
        """
        pulumi.set(__self__, "allow_icmp", allow_icmp)
        if tcp is not None:
            pulumi.set(__self__, "tcp", tcp)
        if udp is not None:
            pulumi.set(__self__, "udp", udp)

    @property
    @pulumi.getter(name="allowIcmp")
    def allow_icmp(self) -> bool:
        """
        Whether to allow ICMP (ping) traffic
        """
        return pulumi.get(self, "allow_icmp")

    @allow_icmp.setter
    def allow_icmp(self, value: bool):
        pulumi.set(self, "allow_icmp", value)

    @property
    @pulumi.getter
    def tcp(self) -> Optional['GetTwingateResourceProtocolsTcpArgs']:
        return pulumi.get(self, "tcp")

    @tcp.setter
    def tcp(self, value: Optional['GetTwingateResourceProtocolsTcpArgs']):
        pulumi.set(self, "tcp", value)

    @property
    @pulumi.getter
    def udp(self) -> Optional['GetTwingateResourceProtocolsUdpArgs']:
        return pulumi.get(self, "udp")

    @udp.setter
    def udp(self, value: Optional['GetTwingateResourceProtocolsUdpArgs']):
        pulumi.set(self, "udp", value)


@pulumi.input_type
class GetTwingateResourceProtocolsTcpArgs:
    def __init__(__self__, *,
                 policy: str,
                 ports: Sequence[str]):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: str):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Sequence[str]):
        pulumi.set(self, "ports", value)


@pulumi.input_type
class GetTwingateResourceProtocolsUdpArgs:
    def __init__(__self__, *,
                 policy: str,
                 ports: Sequence[str]):
        """
        :param str policy: Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        :param Sequence[str] ports: List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        pulumi.set(__self__, "policy", policy)
        pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter
    def policy(self) -> str:
        """
        Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: str):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter
    def ports(self) -> Sequence[str]:
        """
        List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Sequence[str]):
        pulumi.set(self, "ports", value)


