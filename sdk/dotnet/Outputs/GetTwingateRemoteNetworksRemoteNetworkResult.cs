// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Twingate.Outputs
{

    [OutputType]
    public sealed class GetTwingateRemoteNetworksRemoteNetworkResult
    {
        /// <summary>
        /// The ID of the Remote Network
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The location of the Remote Network. Must be one of the following: AWS, AZURE, GOOGLE*CLOUD, ON*PREMISE, OTHER.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// The name of the Remote Network
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetTwingateRemoteNetworksRemoteNetworkResult(
            string id,

            string location,

            string name)
        {
            Id = id;
            Location = location;
            Name = name;
        }
    }
}
