/**
* untitled API
* No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
*
* The version of the OpenAPI document: 5229
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package org.openapitools.client.models

import org.openapitools.client.models.InlineResponse200LinksNetwork
import org.openapitools.client.models.InlineResponse200LinksSelf

import com.squareup.moshi.Json
/**
 * 
 * @param network 
 * @param self 
 */

data class InlineResponse200Links (
    @Json(name = "network")
    val network: InlineResponse200LinksNetwork,
    @Json(name = "self")
    val self: InlineResponse200LinksSelf
)
