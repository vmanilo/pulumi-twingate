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
    public sealed class TwingateResourceProtocols
    {
        /// <summary>
        /// Whether to allow ICMP (ping) traffic
        /// </summary>
        public readonly bool? AllowIcmp;
        public readonly Outputs.TwingateResourceProtocolsTcp Tcp;
        public readonly Outputs.TwingateResourceProtocolsUdp Udp;

        [OutputConstructor]
        private TwingateResourceProtocols(
            bool? allowIcmp,

            Outputs.TwingateResourceProtocolsTcp tcp,

            Outputs.TwingateResourceProtocolsUdp udp)
        {
            AllowIcmp = allowIcmp;
            Tcp = tcp;
            Udp = udp;
        }
    }
}
