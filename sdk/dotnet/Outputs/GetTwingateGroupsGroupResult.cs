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
    public sealed class GetTwingateGroupsGroupResult
    {
        /// <summary>
        /// The ID of the Group
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Indicates if the Group is active
        /// </summary>
        public readonly bool IsActive;
        /// <summary>
        /// The name of the Group
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The Security Policy assigned to the Group.
        /// </summary>
        public readonly string SecurityPolicyId;
        /// <summary>
        /// The type of the Group
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetTwingateGroupsGroupResult(
            string id,

            bool isActive,

            string name,

            string securityPolicyId,

            string type)
        {
            Id = id;
            IsActive = isActive;
            Name = name;
            SecurityPolicyId = securityPolicyId;
            Type = type;
        }
    }
}
