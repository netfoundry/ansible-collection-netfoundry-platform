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
pub struct InlineResponse2006Embedded {
    #[serde(rename = "appWanList")]
    pub app_wan_list: Vec<crate::models::InlineResponse200>,
}

impl InlineResponse2006Embedded {
    pub fn new(app_wan_list: Vec<crate::models::InlineResponse200>) -> InlineResponse2006Embedded {
        InlineResponse2006Embedded {
            app_wan_list,
        }
    }
}


