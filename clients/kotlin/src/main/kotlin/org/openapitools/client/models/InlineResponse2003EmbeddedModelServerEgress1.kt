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


import com.squareup.moshi.Json
/**
 * 
 * @param host 
 * @param port 
 * @param protocol 
 */

data class InlineResponse2003EmbeddedModelServerEgress1 (
    @Json(name = "host")
    val host: kotlin.String,
    @Json(name = "port")
    val port: java.math.BigDecimal,
    @Json(name = "protocol")
    val protocol: kotlin.String
)

