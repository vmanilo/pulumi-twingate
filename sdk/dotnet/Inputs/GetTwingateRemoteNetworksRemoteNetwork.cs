// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Twingate.Inputs
{

    public sealed class GetTwingateRemoteNetworksRemoteNetworkArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Remote Network
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        /// <summary>
        /// The location of the Remote Network. Must be one of the following: AWS, AZURE, GOOGLE*CLOUD, ON*PREMISE, OTHER.
        /// </summary>
        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        /// <summary>
        /// The name of the Remote Network
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetTwingateRemoteNetworksRemoteNetworkArgs()
        {
        }
        public static new GetTwingateRemoteNetworksRemoteNetworkArgs Empty => new GetTwingateRemoteNetworksRemoteNetworkArgs();
    }
}
