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
 * @param high 
 * @param low 
 */

data class InlineResponse2003EmbeddedModelClientIngressPorts (
    @Json(name = "high")
    val high: java.math.BigDecimal,
    @Json(name = "low")
    val low: java.math.BigDecimal
)

