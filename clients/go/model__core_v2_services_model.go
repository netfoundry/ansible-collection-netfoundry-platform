/*
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 5229
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// CoreV2ServicesModel struct for CoreV2ServicesModel
type CoreV2ServicesModel struct {
	EdgeRouterAttributes []string `json:"edgeRouterAttributes"`
	ServerEgress InlineResponse2003EmbeddedModelServerEgress `json:"serverEgress,omitempty"`
	BindEndpointAttributes []string `json:"bindEndpointAttributes,omitempty"`
	ClientIngress CoreV2ServicesModelClientIngress `json:"clientIngress"`
	EdgeRouterHosts []CoreV2ServicesModelEdgeRouterHosts `json:"edgeRouterHosts,omitempty"`
}