// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package twingate

import (
	"context"
	"reflect"

	"github.com/Twingate/pulumi-twingate/sdk/go/twingate/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A Remote Network represents a single private network in Twingate that can have one or more Connectors and Resources assigned to it. You must create a Remote Network before creating Resources and Connectors that belong to it. For more information, see Twingate's [documentation](https://docs.twingate.com/docs/remote-networks).
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
//			_, err := twingate.LookupTwingateRemoteNetwork(ctx, &twingate.LookupTwingateRemoteNetworkArgs{
//				Name: pulumi.StringRef("<your network's name>"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupTwingateRemoteNetwork(ctx *pulumi.Context, args *LookupTwingateRemoteNetworkArgs, opts ...pulumi.InvokeOption) (*LookupTwingateRemoteNetworkResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTwingateRemoteNetworkResult
	err := ctx.Invoke("twingate:index/getTwingateRemoteNetwork:getTwingateRemoteNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTwingateRemoteNetwork.
type LookupTwingateRemoteNetworkArgs struct {
	// The ID of the Remote Network
	Id *string `pulumi:"id"`
	// The name of the Remote Network
	Name *string `pulumi:"name"`
}

// A collection of values returned by getTwingateRemoteNetwork.
type LookupTwingateRemoteNetworkResult struct {
	// The ID of the Remote Network
	Id *string `pulumi:"id"`
	// The location of the Remote Network. Must be one of the following: AWS, AZURE, GOOGLE*CLOUD, ON*PREMISE, OTHER.
	Location string `pulumi:"location"`
	// The name of the Remote Network
	Name *string `pulumi:"name"`
}

func LookupTwingateRemoteNetworkOutput(ctx *pulumi.Context, args LookupTwingateRemoteNetworkOutputArgs, opts ...pulumi.InvokeOption) LookupTwingateRemoteNetworkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTwingateRemoteNetworkResult, error) {
			args := v.(LookupTwingateRemoteNetworkArgs)
			r, err := LookupTwingateRemoteNetwork(ctx, &args, opts...)
			var s LookupTwingateRemoteNetworkResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTwingateRemoteNetworkResultOutput)
}

// A collection of arguments for invoking getTwingateRemoteNetwork.
type LookupTwingateRemoteNetworkOutputArgs struct {
	// The ID of the Remote Network
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The name of the Remote Network
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupTwingateRemoteNetworkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTwingateRemoteNetworkArgs)(nil)).Elem()
}

// A collection of values returned by getTwingateRemoteNetwork.
type LookupTwingateRemoteNetworkResultOutput struct{ *pulumi.OutputState }

func (LookupTwingateRemoteNetworkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTwingateRemoteNetworkResult)(nil)).Elem()
}

func (o LookupTwingateRemoteNetworkResultOutput) ToLookupTwingateRemoteNetworkResultOutput() LookupTwingateRemoteNetworkResultOutput {
	return o
}

func (o LookupTwingateRemoteNetworkResultOutput) ToLookupTwingateRemoteNetworkResultOutputWithContext(ctx context.Context) LookupTwingateRemoteNetworkResultOutput {
	return o
}

// The ID of the Remote Network
func (o LookupTwingateRemoteNetworkResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTwingateRemoteNetworkResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The location of the Remote Network. Must be one of the following: AWS, AZURE, GOOGLE*CLOUD, ON*PREMISE, OTHER.
func (o LookupTwingateRemoteNetworkResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTwingateRemoteNetworkResult) string { return v.Location }).(pulumi.StringOutput)
}

// The name of the Remote Network
func (o LookupTwingateRemoteNetworkResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTwingateRemoteNetworkResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTwingateRemoteNetworkResultOutput{})
}