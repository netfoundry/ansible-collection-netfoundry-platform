/*
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 5229
 * 
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct InlineResponse2003EmbeddedModel {
    #[serde(rename = "edgeRouterAttributes")]
    pub edge_router_attributes: Vec<String>,
    #[serde(rename = "serverEgress", skip_serializing_if = "Option::is_none")]
    pub server_egress: Option<crate::models::InlineResponse2003EmbeddedModelServerEgress>,
    #[serde(rename = "bindEndpointAttributes", skip_serializing_if = "Option::is_none")]
    pub bind_endpoint_attributes: Option<Vec<String>>,
    #[serde(rename = "clientIngress")]
    pub client_ingress: crate::models::InlineResponse2003EmbeddedModelClientIngress,
    #[serde(rename = "edgeRouterHosts", skip_serializing_if = "Option::is_none")]
    pub edge_router_hosts: Option<Vec<crate::models::InlineResponse2003EmbeddedModelEdgeRouterHosts>>,
}

impl InlineResponse2003EmbeddedModel {
    pub fn new(edge_router_attributes: Vec<String>, client_ingress: crate::models::InlineResponse2003EmbeddedModelClientIngress) -> InlineResponse2003EmbeddedModel {
        InlineResponse2003EmbeddedModel {
            edge_router_attributes,
            server_egress: None,
            bind_endpoint_attributes: None,
            client_ingress,
            edge_router_hosts: None,
        }
    }
}


