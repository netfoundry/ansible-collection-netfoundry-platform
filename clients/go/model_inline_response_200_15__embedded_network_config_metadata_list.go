/*
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 5229
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// InlineResponse20015EmbeddedNetworkConfigMetadataList struct for InlineResponse20015EmbeddedNetworkConfigMetadataList
type InlineResponse20015EmbeddedNetworkConfigMetadataList struct {
	NetworkControllerVolumeSize float32 `json:"networkControllerVolumeSize"`
	GatewayVolumeSize float32 `json:"gatewayVolumeSize"`
	Name string `json:"name"`
	GcpTransferNodeSize string `json:"gcpTransferNodeSize"`
	AwsNetworkControllerSize string `json:"awsNetworkControllerSize"`
	TransferNodeVolumeSize float32 `json:"transferNodeVolumeSize"`
	AwsGatewaySize string `json:"awsGatewaySize"`
	OcpTransferNodeSize string `json:"ocpTransferNodeSize"`
	AwsTransferNodeSize string `json:"awsTransferNodeSize"`
	Id string `json:"id"`
	AzureTransferNodeSize string `json:"azureTransferNodeSize"`
	AlicloudTransferNodeSize string `json:"alicloudTransferNodeSize"`
	Links InlineResponse2002EmbeddedLinks `json:"_links"`
}
