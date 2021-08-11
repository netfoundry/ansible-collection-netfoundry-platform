/*
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 5229
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi
// InlineResponse20013 struct for InlineResponse20013
type InlineResponse20013 struct {
	DeletedAt interface{} `json:"deletedAt"`
	Name string `json:"name"`
	UpdatedAt string `json:"updatedAt"`
	Size string `json:"size"`
	LocationCode string `json:"locationCode,omitempty"`
	OwnerIdentityId string `json:"ownerIdentityId"`
	ProductVersion string `json:"productVersion"`
	NetworkGroupId string `json:"networkGroupId"`
	Id string `json:"id"`
	Status string `json:"status"`
	SdsPassword string `json:"sdsPassword,omitempty"`
	CreatedAt string `json:"createdAt"`
	CreatedBy string `json:"createdBy"`
	DeletedBy interface{} `json:"deletedBy"`
	NetworkController interface{} `json:"networkController,omitempty"`
	O365BreakoutCategory string `json:"o365BreakoutCategory"`
	Links InlineResponse2001EmbeddedLinks `json:"_links"`
}