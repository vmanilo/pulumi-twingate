// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Twingate.Twingate.Outputs
{

    [OutputType]
    public sealed class TwingateResourceProtocolsTcp
    {
        /// <summary>
        /// Whether to allow or deny all ports, or restrict protocol access within certain port ranges: Can be `RESTRICTED` (only listed ports are allowed), `ALLOW_ALL`, or `DENY_ALL`
        /// </summary>
        public readonly string? Policy;
        /// <summary>
        /// List of port ranges between 1 and 65535 inclusive, in the format `100-200` for a range, or `8080` for a single port
        /// </summary>
        public readonly ImmutableArray<string> Ports;

        [OutputConstructor]
        private TwingateResourceProtocolsTcp(
            string? policy,

            ImmutableArray<string> ports)
        {
            Policy = policy;
            Ports = ports;
        }
    }
}
