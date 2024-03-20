// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Users provides different levels of write capabilities across the Twingate Admin Console. For more information, see Twingate's [documentation](https://www.twingate.com/docs/users).
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as twingate from "@twingate/pulumi-twingate";
 *
 * const user = new twingate.TwingateUser("user", {
 *     email: "sample@company.com",
 *     firstName: "Twin",
 *     lastName: "Gate",
 *     role: "DEVOPS",
 *     sendInvite: true,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export class TwingateUser extends pulumi.CustomResource {
    /**
     * Get an existing TwingateUser resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TwingateUserState, opts?: pulumi.CustomResourceOptions): TwingateUser {
        return new TwingateUser(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'twingate:index/twingateUser:TwingateUser';

    /**
     * Returns true if the given object is an instance of TwingateUser.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TwingateUser {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TwingateUser.__pulumiType;
    }

    /**
     * The User's email address
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * The User's first name
     */
    public readonly firstName!: pulumi.Output<string>;
    /**
     * Determines whether the User is active or not. Inactive users will be not able to sign in.
     */
    public readonly isActive!: pulumi.Output<boolean>;
    /**
     * The User's last name
     */
    public readonly lastName!: pulumi.Output<string>;
    /**
     * Determines the User's role. Either ADMIN, DEVOPS, SUPPORT or MEMBER.
     */
    public readonly role!: pulumi.Output<string>;
    /**
     * Determines whether to send an email invitation to the User. True by default.
     */
    public readonly sendInvite!: pulumi.Output<boolean>;
    /**
     * Indicates the User's type. Either MANUAL or SYNCED.
     */
    public /*out*/ readonly type!: pulumi.Output<string>;

    /**
     * Create a TwingateUser resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TwingateUserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TwingateUserArgs | TwingateUserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TwingateUserState | undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["firstName"] = state ? state.firstName : undefined;
            resourceInputs["isActive"] = state ? state.isActive : undefined;
            resourceInputs["lastName"] = state ? state.lastName : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
            resourceInputs["sendInvite"] = state ? state.sendInvite : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as TwingateUserArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["firstName"] = args ? args.firstName : undefined;
            resourceInputs["isActive"] = args ? args.isActive : undefined;
            resourceInputs["lastName"] = args ? args.lastName : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["sendInvite"] = args ? args.sendInvite : undefined;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TwingateUser.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TwingateUser resources.
 */
export interface TwingateUserState {
    /**
     * The User's email address
     */
    email?: pulumi.Input<string>;
    /**
     * The User's first name
     */
    firstName?: pulumi.Input<string>;
    /**
     * Determines whether the User is active or not. Inactive users will be not able to sign in.
     */
    isActive?: pulumi.Input<boolean>;
    /**
     * The User's last name
     */
    lastName?: pulumi.Input<string>;
    /**
     * Determines the User's role. Either ADMIN, DEVOPS, SUPPORT or MEMBER.
     */
    role?: pulumi.Input<string>;
    /**
     * Determines whether to send an email invitation to the User. True by default.
     */
    sendInvite?: pulumi.Input<boolean>;
    /**
     * Indicates the User's type. Either MANUAL or SYNCED.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TwingateUser resource.
 */
export interface TwingateUserArgs {
    /**
     * The User's email address
     */
    email: pulumi.Input<string>;
    /**
     * The User's first name
     */
    firstName?: pulumi.Input<string>;
    /**
     * Determines whether the User is active or not. Inactive users will be not able to sign in.
     */
    isActive?: pulumi.Input<boolean>;
    /**
     * The User's last name
     */
    lastName?: pulumi.Input<string>;
    /**
     * Determines the User's role. Either ADMIN, DEVOPS, SUPPORT or MEMBER.
     */
    role?: pulumi.Input<string>;
    /**
     * Determines whether to send an email invitation to the User. True by default.
     */
    sendInvite?: pulumi.Input<boolean>;
}
