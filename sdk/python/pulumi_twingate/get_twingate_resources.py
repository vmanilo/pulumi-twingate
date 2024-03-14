# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetTwingateResourcesResult',
    'AwaitableGetTwingateResourcesResult',
    'get_twingate_resources',
    'get_twingate_resources_output',
]

@pulumi.output_type
class GetTwingateResourcesResult:
    """
    A collection of values returned by getTwingateResources.
    """
    def __init__(__self__, id=None, name=None, resources=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resources and not isinstance(resources, list):
            raise TypeError("Expected argument 'resources' to be a list")
        pulumi.set(__self__, "resources", resources)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resources(self) -> Optional[Sequence['outputs.GetTwingateResourcesResourceResult']]:
        """
        List of Resources
        """
        return pulumi.get(self, "resources")


class AwaitableGetTwingateResourcesResult(GetTwingateResourcesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTwingateResourcesResult(
            id=self.id,
            name=self.name,
            resources=self.resources)


def get_twingate_resources(name: Optional[str] = None,
                           resources: Optional[Sequence[pulumi.InputType['GetTwingateResourcesResourceArgs']]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTwingateResourcesResult:
    """
    Resources in Twingate represent servers on the private network that clients can connect to. Resources can be defined by IP, CIDR range, FQDN, or DNS zone. For more information, see the Twingate [documentation](https://docs.twingate.com/docs/resources-and-access-nodes).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_twingate as twingate

    foo = twingate.get_twingate_resources(name="<your resource's name>")
    ```


    :param str name: The name of the Resource
    :param Sequence[pulumi.InputType['GetTwingateResourcesResourceArgs']] resources: List of Resources
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resources'] = resources
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('twingate:index/getTwingateResources:getTwingateResources', __args__, opts=opts, typ=GetTwingateResourcesResult).value

    return AwaitableGetTwingateResourcesResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        resources=pulumi.get(__ret__, 'resources'))


@_utilities.lift_output_func(get_twingate_resources)
def get_twingate_resources_output(name: Optional[pulumi.Input[str]] = None,
                                  resources: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetTwingateResourcesResourceArgs']]]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTwingateResourcesResult]:
    """
    Resources in Twingate represent servers on the private network that clients can connect to. Resources can be defined by IP, CIDR range, FQDN, or DNS zone. For more information, see the Twingate [documentation](https://docs.twingate.com/docs/resources-and-access-nodes).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_twingate as twingate

    foo = twingate.get_twingate_resources(name="<your resource's name>")
    ```


    :param str name: The name of the Resource
    :param Sequence[pulumi.InputType['GetTwingateResourcesResourceArgs']] resources: List of Resources
    """
    ...
