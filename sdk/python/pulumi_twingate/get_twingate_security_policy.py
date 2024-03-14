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
    'GetTwingateSecurityPolicyResult',
    'AwaitableGetTwingateSecurityPolicyResult',
    'get_twingate_security_policy',
    'get_twingate_security_policy_output',
]

@pulumi.output_type
class GetTwingateSecurityPolicyResult:
    """
    A collection of values returned by getTwingateSecurityPolicy.
    """
    def __init__(__self__, id=None, name=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Return a Security Policy by its ID. The ID for the Security Policy can be obtained from the Admin API or the URL string in the Admin Console.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Return a Security Policy that exactly matches this name.
        """
        return pulumi.get(self, "name")


class AwaitableGetTwingateSecurityPolicyResult(GetTwingateSecurityPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTwingateSecurityPolicyResult(
            id=self.id,
            name=self.name)


def get_twingate_security_policy(id: Optional[str] = None,
                                 name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTwingateSecurityPolicyResult:
    """
    Security Policies are defined in the Twingate Admin Console and determine user and device authentication requirements for Resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_twingate as twingate

    foo = twingate.get_twingate_security_policy(name="<your security policy name>")
    ```


    :param str id: Return a Security Policy by its ID. The ID for the Security Policy can be obtained from the Admin API or the URL string in the Admin Console.
    :param str name: Return a Security Policy that exactly matches this name.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('twingate:index/getTwingateSecurityPolicy:getTwingateSecurityPolicy', __args__, opts=opts, typ=GetTwingateSecurityPolicyResult).value

    return AwaitableGetTwingateSecurityPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'))


@_utilities.lift_output_func(get_twingate_security_policy)
def get_twingate_security_policy_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                                        name: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTwingateSecurityPolicyResult]:
    """
    Security Policies are defined in the Twingate Admin Console and determine user and device authentication requirements for Resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_twingate as twingate

    foo = twingate.get_twingate_security_policy(name="<your security policy name>")
    ```


    :param str id: Return a Security Policy by its ID. The ID for the Security Policy can be obtained from the Admin API or the URL string in the Admin Console.
    :param str name: Return a Security Policy that exactly matches this name.
    """
    ...