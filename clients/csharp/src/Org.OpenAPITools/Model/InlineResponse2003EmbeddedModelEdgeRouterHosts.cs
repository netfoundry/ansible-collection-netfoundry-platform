/* 
 * untitled API
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 5229
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// InlineResponse2003EmbeddedModelEdgeRouterHosts
    /// </summary>
    [DataContract]
    public partial class InlineResponse2003EmbeddedModelEdgeRouterHosts :  IEquatable<InlineResponse2003EmbeddedModelEdgeRouterHosts>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse2003EmbeddedModelEdgeRouterHosts" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected InlineResponse2003EmbeddedModelEdgeRouterHosts() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse2003EmbeddedModelEdgeRouterHosts" /> class.
        /// </summary>
        /// <param name="edgeRouterId">edgeRouterId (required).</param>
        /// <param name="serverEgress">serverEgress (required).</param>
        public InlineResponse2003EmbeddedModelEdgeRouterHosts(string edgeRouterId = default(string), InlineResponse2003EmbeddedModelServerEgress1 serverEgress = default(InlineResponse2003EmbeddedModelServerEgress1))
        {
            // to ensure "edgeRouterId" is required (not null)
            if (edgeRouterId == null)
            {
                throw new InvalidDataException("edgeRouterId is a required property for InlineResponse2003EmbeddedModelEdgeRouterHosts and cannot be null");
            }
            else
            {
                this.EdgeRouterId = edgeRouterId;
            }
            
            // to ensure "serverEgress" is required (not null)
            if (serverEgress == null)
            {
                throw new InvalidDataException("serverEgress is a required property for InlineResponse2003EmbeddedModelEdgeRouterHosts and cannot be null");
            }
            else
            {
                this.ServerEgress = serverEgress;
            }
            
        }
        
        /// <summary>
        /// Gets or Sets EdgeRouterId
        /// </summary>
        [DataMember(Name="edgeRouterId", EmitDefaultValue=true)]
        public string EdgeRouterId { get; set; }

        /// <summary>
        /// Gets or Sets ServerEgress
        /// </summary>
        [DataMember(Name="serverEgress", EmitDefaultValue=true)]
        public InlineResponse2003EmbeddedModelServerEgress1 ServerEgress { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InlineResponse2003EmbeddedModelEdgeRouterHosts {\n");
            sb.Append("  EdgeRouterId: ").Append(EdgeRouterId).Append("\n");
            sb.Append("  ServerEgress: ").Append(ServerEgress).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as InlineResponse2003EmbeddedModelEdgeRouterHosts);
        }

        /// <summary>
        /// Returns true if InlineResponse2003EmbeddedModelEdgeRouterHosts instances are equal
        /// </summary>
        /// <param name="input">Instance of InlineResponse2003EmbeddedModelEdgeRouterHosts to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InlineResponse2003EmbeddedModelEdgeRouterHosts input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.EdgeRouterId == input.EdgeRouterId ||
                    (this.EdgeRouterId != null &&
                    this.EdgeRouterId.Equals(input.EdgeRouterId))
                ) && 
                (
                    this.ServerEgress == input.ServerEgress ||
                    (this.ServerEgress != null &&
                    this.ServerEgress.Equals(input.ServerEgress))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.EdgeRouterId != null)
                    hashCode = hashCode * 59 + this.EdgeRouterId.GetHashCode();
                if (this.ServerEgress != null)
                    hashCode = hashCode * 59 + this.ServerEgress.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
