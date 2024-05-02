// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Twingate.Twingate
{
    /// <summary>
    /// Users provides different levels of write capabilities across the Twingate Admin Console. For more information, see Twingate's [documentation](https://www.twingate.com/docs/users).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Twingate = Twingate.Twingate;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var user = new Twingate.TwingateUser("user", new()
    ///     {
    ///         Email = "sample@company.com",
    ///         FirstName = "Twin",
    ///         LastName = "Gate",
    ///         Role = "DEVOPS",
    ///         SendInvite = true,
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [TwingateResourceType("twingate:index/twingateUser:TwingateUser")]
    public partial class TwingateUser : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The User's email address
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// The User's first name
        /// </summary>
        [Output("firstName")]
        public Output<string> FirstName { get; private set; } = null!;

        /// <summary>
        /// Determines whether the User is active or not. Inactive users will be not able to sign in.
        /// </summary>
        [Output("isActive")]
        public Output<bool> IsActive { get; private set; } = null!;

        /// <summary>
        /// The User's last name
        /// </summary>
        [Output("lastName")]
        public Output<string> LastName { get; private set; } = null!;

        /// <summary>
        /// Determines the User's role. Either ADMIN, DEVOPS, SUPPORT or MEMBER.
        /// </summary>
        [Output("role")]
        public Output<string> Role { get; private set; } = null!;

        /// <summary>
        /// Determines whether to send an email invitation to the User. True by default.
        /// </summary>
        [Output("sendInvite")]
        public Output<bool> SendInvite { get; private set; } = null!;

        /// <summary>
        /// Indicates the User's type. Either MANUAL or SYNCED.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a TwingateUser resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TwingateUser(string name, TwingateUserArgs args, CustomResourceOptions? options = null)
            : base("twingate:index/twingateUser:TwingateUser", name, args ?? new TwingateUserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TwingateUser(string name, Input<string> id, TwingateUserState? state = null, CustomResourceOptions? options = null)
            : base("twingate:index/twingateUser:TwingateUser", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/Twingate/pulumi-twingate",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TwingateUser resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TwingateUser Get(string name, Input<string> id, TwingateUserState? state = null, CustomResourceOptions? options = null)
        {
            return new TwingateUser(name, id, state, options);
        }
    }

    public sealed class TwingateUserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The User's email address
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// The User's first name
        /// </summary>
        [Input("firstName")]
        public Input<string>? FirstName { get; set; }

        /// <summary>
        /// Determines whether the User is active or not. Inactive users will be not able to sign in.
        /// </summary>
        [Input("isActive")]
        public Input<bool>? IsActive { get; set; }

        /// <summary>
        /// The User's last name
        /// </summary>
        [Input("lastName")]
        public Input<string>? LastName { get; set; }

        /// <summary>
        /// Determines the User's role. Either ADMIN, DEVOPS, SUPPORT or MEMBER.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        /// <summary>
        /// Determines whether to send an email invitation to the User. True by default.
        /// </summary>
        [Input("sendInvite")]
        public Input<bool>? SendInvite { get; set; }

        public TwingateUserArgs()
        {
        }
        public static new TwingateUserArgs Empty => new TwingateUserArgs();
    }

    public sealed class TwingateUserState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The User's email address
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// The User's first name
        /// </summary>
        [Input("firstName")]
        public Input<string>? FirstName { get; set; }

        /// <summary>
        /// Determines whether the User is active or not. Inactive users will be not able to sign in.
        /// </summary>
        [Input("isActive")]
        public Input<bool>? IsActive { get; set; }

        /// <summary>
        /// The User's last name
        /// </summary>
        [Input("lastName")]
        public Input<string>? LastName { get; set; }

        /// <summary>
        /// Determines the User's role. Either ADMIN, DEVOPS, SUPPORT or MEMBER.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        /// <summary>
        /// Determines whether to send an email invitation to the User. True by default.
        /// </summary>
        [Input("sendInvite")]
        public Input<bool>? SendInvite { get; set; }

        /// <summary>
        /// Indicates the User's type. Either MANUAL or SYNCED.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public TwingateUserState()
        {
        }
        public static new TwingateUserState Empty => new TwingateUserState();
    }
}
