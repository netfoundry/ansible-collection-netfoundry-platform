/*
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 5229
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// InlineResponse2003EmbeddedModelClientIngress struct for InlineResponse2003EmbeddedModelClientIngress
type InlineResponse2003EmbeddedModelClientIngress struct {
	Protocols []string `json:"protocols,omitempty"`
	Host string `json:"host,omitempty"`
	Ports []InlineResponse2003EmbeddedModelClientIngressPorts `json:"ports,omitempty"`
	Port float32 `json:"port,omitempty"`
	Addresses []string `json:"addresses,omitempty"`
}
