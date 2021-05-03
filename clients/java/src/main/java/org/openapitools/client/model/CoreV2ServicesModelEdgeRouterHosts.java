/*
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


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.CoreV2ServicesModelServerEgress;

/**
 * CoreV2ServicesModelEdgeRouterHosts
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-05-03T11:59:07.273777-04:00[America/New_York]")
public class CoreV2ServicesModelEdgeRouterHosts {
  public static final String SERIALIZED_NAME_EDGE_ROUTER_ID = "edgeRouterId";
  @SerializedName(SERIALIZED_NAME_EDGE_ROUTER_ID)
  private String edgeRouterId;

  public static final String SERIALIZED_NAME_SERVER_EGRESS = "serverEgress";
  @SerializedName(SERIALIZED_NAME_SERVER_EGRESS)
  private CoreV2ServicesModelServerEgress serverEgress;


  public CoreV2ServicesModelEdgeRouterHosts edgeRouterId(String edgeRouterId) {
    
    this.edgeRouterId = edgeRouterId;
    return this;
  }

   /**
   * Get edgeRouterId
   * @return edgeRouterId
  **/
  @ApiModelProperty(required = true, value = "")

  public String getEdgeRouterId() {
    return edgeRouterId;
  }


  public void setEdgeRouterId(String edgeRouterId) {
    this.edgeRouterId = edgeRouterId;
  }


  public CoreV2ServicesModelEdgeRouterHosts serverEgress(CoreV2ServicesModelServerEgress serverEgress) {
    
    this.serverEgress = serverEgress;
    return this;
  }

   /**
   * Get serverEgress
   * @return serverEgress
  **/
  @ApiModelProperty(required = true, value = "")

  public CoreV2ServicesModelServerEgress getServerEgress() {
    return serverEgress;
  }


  public void setServerEgress(CoreV2ServicesModelServerEgress serverEgress) {
    this.serverEgress = serverEgress;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CoreV2ServicesModelEdgeRouterHosts coreV2ServicesModelEdgeRouterHosts = (CoreV2ServicesModelEdgeRouterHosts) o;
    return Objects.equals(this.edgeRouterId, coreV2ServicesModelEdgeRouterHosts.edgeRouterId) &&
        Objects.equals(this.serverEgress, coreV2ServicesModelEdgeRouterHosts.serverEgress);
  }

  @Override
  public int hashCode() {
    return Objects.hash(edgeRouterId, serverEgress);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CoreV2ServicesModelEdgeRouterHosts {\n");
    sb.append("    edgeRouterId: ").append(toIndentedString(edgeRouterId)).append("\n");
    sb.append("    serverEgress: ").append(toIndentedString(serverEgress)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

