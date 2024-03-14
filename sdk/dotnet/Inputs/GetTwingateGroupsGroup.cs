// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Twingate.Inputs
{

    public sealed class GetTwingateGroupsGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Group
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        /// <summary>
        /// Indicates if the Group is active
        /// </summary>
        [Input("isActive", required: true)]
        public bool IsActive { get; set; }

        /// <summary>
        /// The name of the Group
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The Security Policy assigned to the Group.
        /// </summary>
        [Input("securityPolicyId", required: true)]
        public string SecurityPolicyId { get; set; } = null!;

        /// <summary>
        /// The type of the Group
        /// </summary>
        [Input("type", required: true)]
        public string Type { get; set; } = null!;

        public GetTwingateGroupsGroupArgs()
        {
        }
        public static new GetTwingateGroupsGroupArgs Empty => new GetTwingateGroupsGroupArgs();
    }
}
