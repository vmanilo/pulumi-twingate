// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package twingate

import (
	"context"
	"reflect"

	"github.com/Twingate/pulumi-twingate/sdk/go/twingate/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Service Accounts offer a way to provide programmatic, centrally-controlled, and consistent access controls.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/Twingate/pulumi-twingate/sdk/go/twingate"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := twingate.GetTwingateServiceAccounts(ctx, &twingate.GetTwingateServiceAccountsArgs{
//				Name: pulumi.StringRef("<your service account's name>"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetTwingateServiceAccounts(ctx *pulumi.Context, args *GetTwingateServiceAccountsArgs, opts ...pulumi.InvokeOption) (*GetTwingateServiceAccountsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetTwingateServiceAccountsResult
	err := ctx.Invoke("twingate:index/getTwingateServiceAccounts:getTwingateServiceAccounts", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTwingateServiceAccounts.
type GetTwingateServiceAccountsArgs struct {
	// Name of the Service Account
	Name *string `pulumi:"name"`
	// List of Service Accounts
	ServiceAccounts []GetTwingateServiceAccountsServiceAccount `pulumi:"serviceAccounts"`
}

// A collection of values returned by getTwingateServiceAccounts.
type GetTwingateServiceAccountsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Filter results by the name of the Service Account.
	Name *string `pulumi:"name"`
	// List of Service Accounts
	ServiceAccounts []GetTwingateServiceAccountsServiceAccount `pulumi:"serviceAccounts"`
}

func GetTwingateServiceAccountsOutput(ctx *pulumi.Context, args GetTwingateServiceAccountsOutputArgs, opts ...pulumi.InvokeOption) GetTwingateServiceAccountsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetTwingateServiceAccountsResult, error) {
			args := v.(GetTwingateServiceAccountsArgs)
			r, err := GetTwingateServiceAccounts(ctx, &args, opts...)
			var s GetTwingateServiceAccountsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetTwingateServiceAccountsResultOutput)
}

// A collection of arguments for invoking getTwingateServiceAccounts.
type GetTwingateServiceAccountsOutputArgs struct {
	// Name of the Service Account
	Name pulumi.StringPtrInput `pulumi:"name"`
	// List of Service Accounts
	ServiceAccounts GetTwingateServiceAccountsServiceAccountArrayInput `pulumi:"serviceAccounts"`
}

func (GetTwingateServiceAccountsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTwingateServiceAccountsArgs)(nil)).Elem()
}

// A collection of values returned by getTwingateServiceAccounts.
type GetTwingateServiceAccountsResultOutput struct{ *pulumi.OutputState }

func (GetTwingateServiceAccountsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetTwingateServiceAccountsResult)(nil)).Elem()
}

func (o GetTwingateServiceAccountsResultOutput) ToGetTwingateServiceAccountsResultOutput() GetTwingateServiceAccountsResultOutput {
	return o
}

func (o GetTwingateServiceAccountsResultOutput) ToGetTwingateServiceAccountsResultOutputWithContext(ctx context.Context) GetTwingateServiceAccountsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetTwingateServiceAccountsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetTwingateServiceAccountsResult) string { return v.Id }).(pulumi.StringOutput)
}

// Filter results by the name of the Service Account.
func (o GetTwingateServiceAccountsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetTwingateServiceAccountsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// List of Service Accounts
func (o GetTwingateServiceAccountsResultOutput) ServiceAccounts() GetTwingateServiceAccountsServiceAccountArrayOutput {
	return o.ApplyT(func(v GetTwingateServiceAccountsResult) []GetTwingateServiceAccountsServiceAccount {
		return v.ServiceAccounts
	}).(GetTwingateServiceAccountsServiceAccountArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetTwingateServiceAccountsResultOutput{})
}