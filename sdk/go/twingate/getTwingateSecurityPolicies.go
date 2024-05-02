// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package twingate

import (
	"context"
	"reflect"

	"github.com/Twingate/pulumi-twingate/sdk/v3/go/twingate/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Security Policies are defined in the Twingate Admin Console and determine user and device authentication requirements for Resources.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/Twingate/pulumi-twingate/sdk/v3/go/twingate"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := twingate.GetTwingateSecurityPolicies(ctx, &twingate.GetTwingateSecurityPoliciesArgs{
//				Name: pulumi.StringRef("<your security policy's name>"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetTwingateSecurityPolicies(ctx *pulumi.Context, args *GetTwingateSecurityPoliciesArgs, opts ...pulumi.InvokeOption) (*GetTwingateSecurityPoliciesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetTwingateSecurityPoliciesResult
	err := ctx.Invoke("twingate:index/getTwingateSecurityPolicies:getTwingateSecurityPolicies", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTwingateSecurityPolicies.
type GetTwingateSecurityPoliciesArgs struct {
	// Returns only security policies that exactly match this name. If no options are passed it will return all security policies. Only one option can be used at a time.
	Name *string `pulumi:"name"`
	// Match when the value exist in the name of the security policy.
	NameContains *string `pulumi:"nameContains"`
	// Match when the exact value does not exist in the name of the security policy.
	NameExclude *string `pulumi:"nameExclude"`
	// The name of the security policy must start with the value.
	NamePrefix *string `pulumi:"namePrefix"`
	// The regular expression match of the name of the security policy.
	NameRegexp *string `pulumi:"nameRegexp"`
	// The name of the security policy must end with the value.
	NameSuffix *string `pulumi:"nameSuffix"`
}

// A collection of values returned by getTwingateSecurityPolicies.
type GetTwingateSecurityPoliciesResult struct {
	// The ID of this resource.
	Id string `pulumi:"id"`
	// Returns only security policies that exactly match this name. If no options are passed it will return all security policies. Only one option can be used at a time.
	Name *string `pulumi:"name"`
	// Match when the value exist in the name of the security policy.
	NameContains *string `pulumi:"nameContains"`
	// Match when the exact value does not exist in the name of the security policy.
	NameExclude *string `pulumi:"nameExclude"`
	// The name of the security policy must start with the value.
	NamePrefix *string `pulumi:"namePrefix"`
	// The regular expression match of the name of the security policy.
	NameRegexp *string `pulumi:"nameRegexp"`
	// The name of the security policy must end with the value.
	NameSuffix       *string                                     `pulumi:"nameSuffix"`
	SecurityPolicies []GetTwingateSecurityPoliciesSecurityPolicy `pulumi:"securityPolicies"`
}

func GetTwingateSecurityPoliciesOutput(ctx *pulumi.Context, args GetTwingateSecurityPoliciesOutputArgs, opts ...pulumi.InvokeOption) GetTwingateSecurityPoliciesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetTwingateSecurityPoliciesResult, error) {
			args := v.(GetTwingateSecurityPoliciesArgs)
			r, err := GetTwingateSecurityPolicies(ctx, &args, opts...)
			var s GetTwingateSecurityPoliciesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetTwingateSecurityPoliciesResultOutput)
}

// A collection of arguments for invoking getTwingateSecurityPolicies.
type GetTwingateSecurityPoliciesOutputArgs struct {
	// Returns only security policies that exactly match this name. If no options are passed it will return all security policies. Only one option can be used at a time.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Match when the value exist in the name of the security policy.
	NameContains pulumi.StringPtrInput `pulumi:"nameContains"`
	// Match when the exact value does not exist in the name of the security policy.
	NameExclude pulumi.StringPtrInput `pulumi:"nameExclude"`
	// The name of the security policy must start with the value.
	NamePrefix pulumi.StringPtrInput `pulumi:"namePrefix"`
	// The regular expression match of the name of the security policy.
	NameRegexp pulumi.StringPtrInput `pulumi:"nameRegexp"`
	// The name of the security policy must end with the value.
	NameSuffix pulumi.StringPtrInput `pulumi:"nameSuffix"`
}

func (GetTwingateSecurityPoliciesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTwingateSecurityPoliciesArgs)(nil)).Elem()
}

// A collection of values returned by getTwingateSecurityPolicies.
type GetTwingateSecurityPoliciesResultOutput struct{ *pulumi.OutputState }

func (GetTwingateSecurityPoliciesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTwingateSecurityPoliciesResult)(nil)).Elem()
}

func (o GetTwingateSecurityPoliciesResultOutput) ToGetTwingateSecurityPoliciesResultOutput() GetTwingateSecurityPoliciesResultOutput {
	return o
}

func (o GetTwingateSecurityPoliciesResultOutput) ToGetTwingateSecurityPoliciesResultOutputWithContext(ctx context.Context) GetTwingateSecurityPoliciesResultOutput {
	return o
}

// The ID of this resource.
func (o GetTwingateSecurityPoliciesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) string { return v.Id }).(pulumi.StringOutput)
}

// Returns only security policies that exactly match this name. If no options are passed it will return all security policies. Only one option can be used at a time.
func (o GetTwingateSecurityPoliciesResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// Match when the value exist in the name of the security policy.
func (o GetTwingateSecurityPoliciesResultOutput) NameContains() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) *string { return v.NameContains }).(pulumi.StringPtrOutput)
}

// Match when the exact value does not exist in the name of the security policy.
func (o GetTwingateSecurityPoliciesResultOutput) NameExclude() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) *string { return v.NameExclude }).(pulumi.StringPtrOutput)
}

// The name of the security policy must start with the value.
func (o GetTwingateSecurityPoliciesResultOutput) NamePrefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) *string { return v.NamePrefix }).(pulumi.StringPtrOutput)
}

// The regular expression match of the name of the security policy.
func (o GetTwingateSecurityPoliciesResultOutput) NameRegexp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) *string { return v.NameRegexp }).(pulumi.StringPtrOutput)
}

// The name of the security policy must end with the value.
func (o GetTwingateSecurityPoliciesResultOutput) NameSuffix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) *string { return v.NameSuffix }).(pulumi.StringPtrOutput)
}

func (o GetTwingateSecurityPoliciesResultOutput) SecurityPolicies() GetTwingateSecurityPoliciesSecurityPolicyArrayOutput {
	return o.ApplyT(func(v GetTwingateSecurityPoliciesResult) []GetTwingateSecurityPoliciesSecurityPolicy {
		return v.SecurityPolicies
	}).(GetTwingateSecurityPoliciesSecurityPolicyArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetTwingateSecurityPoliciesResultOutput{})
}
