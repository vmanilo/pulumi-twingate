// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Twingate.Inputs
{

    public sealed class GetTwingateSecurityPoliciesSecurityPolicyArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Return a matching Security Policy by its ID. The ID for the Security Policy can be obtained from the Admin API or the URL string in the Admin Console.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        /// <summary>
        /// Return a Security Policy that exactly matches this name.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetTwingateSecurityPoliciesSecurityPolicyArgs()
        {
        }
        public static new GetTwingateSecurityPoliciesSecurityPolicyArgs Empty => new GetTwingateSecurityPoliciesSecurityPolicyArgs();
    }
}
