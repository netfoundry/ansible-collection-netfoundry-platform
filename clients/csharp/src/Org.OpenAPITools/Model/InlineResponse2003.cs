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
    /// InlineResponse2003
    /// </summary>
    [DataContract]
    public partial class InlineResponse2003 :  IEquatable<InlineResponse2003>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse2003" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected InlineResponse2003() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineResponse2003" /> class.
        /// </summary>
        /// <param name="embedded">embedded.</param>
        /// <param name="links">links (required).</param>
        /// <param name="page">page (required).</param>
        public InlineResponse2003(InlineResponse2003Embedded embedded = default(InlineResponse2003Embedded), InlineResponse2002EmbeddedLinks links = default(InlineResponse2002EmbeddedLinks), InlineResponse2001Page page = default(InlineResponse2001Page))
        {
            // to ensure "links" is required (not null)
            if (links == null)
            {
                throw new InvalidDataException("links is a required property for InlineResponse2003 and cannot be null");
            }
            else
            {
                this.Links = links;
            }
            
            // to ensure "page" is required (not null)
            if (page == null)
            {
                throw new InvalidDataException("page is a required property for InlineResponse2003 and cannot be null");
            }
            else
            {
                this.Page = page;
            }
            
            this.Embedded = embedded;
        }
        
        /// <summary>
        /// Gets or Sets Embedded
        /// </summary>
        [DataMember(Name="_embedded", EmitDefaultValue=false)]
        public InlineResponse2003Embedded Embedded { get; set; }

        /// <summary>
        /// Gets or Sets Links
        /// </summary>
        [DataMember(Name="_links", EmitDefaultValue=true)]
        public InlineResponse2002EmbeddedLinks Links { get; set; }

        /// <summary>
        /// Gets or Sets Page
        /// </summary>
        [DataMember(Name="page", EmitDefaultValue=true)]
        public InlineResponse2001Page Page { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InlineResponse2003 {\n");
            sb.Append("  Embedded: ").Append(Embedded).Append("\n");
            sb.Append("  Links: ").Append(Links).Append("\n");
            sb.Append("  Page: ").Append(Page).Append("\n");
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
            return this.Equals(input as InlineResponse2003);
        }

        /// <summary>
        /// Returns true if InlineResponse2003 instances are equal
        /// </summary>
        /// <param name="input">Instance of InlineResponse2003 to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InlineResponse2003 input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Embedded == input.Embedded ||
                    (this.Embedded != null &&
                    this.Embedded.Equals(input.Embedded))
                ) && 
                (
                    this.Links == input.Links ||
                    (this.Links != null &&
                    this.Links.Equals(input.Links))
                ) && 
                (
                    this.Page == input.Page ||
                    (this.Page != null &&
                    this.Page.Equals(input.Page))
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
                if (this.Embedded != null)
                    hashCode = hashCode * 59 + this.Embedded.GetHashCode();
                if (this.Links != null)
                    hashCode = hashCode * 59 + this.Links.GetHashCode();
                if (this.Page != null)
                    hashCode = hashCode * 59 + this.Page.GetHashCode();
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
