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
    /// InlineObject1
    /// </summary>
    [DataContract]
    public partial class InlineObject1 :  IEquatable<InlineObject1>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineObject1" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected InlineObject1() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="InlineObject1" /> class.
        /// </summary>
        /// <param name="networkId">networkId (required).</param>
        /// <param name="name">name (required).</param>
        /// <param name="model">model (required).</param>
        /// <param name="attributes">attributes (required).</param>
        /// <param name="modelType">modelType (required).</param>
        /// <param name="encryptionRequired">encryptionRequired (required).</param>
        public InlineObject1(string networkId = default(string), string name = default(string), CoreV2ServicesModel model = default(CoreV2ServicesModel), List<string> attributes = default(List<string>), string modelType = default(string), bool encryptionRequired = default(bool))
        {
            // to ensure "networkId" is required (not null)
            if (networkId == null)
            {
                throw new InvalidDataException("networkId is a required property for InlineObject1 and cannot be null");
            }
            else
            {
                this.NetworkId = networkId;
            }
            
            // to ensure "name" is required (not null)
            if (name == null)
            {
                throw new InvalidDataException("name is a required property for InlineObject1 and cannot be null");
            }
            else
            {
                this.Name = name;
            }
            
            // to ensure "model" is required (not null)
            if (model == null)
            {
                throw new InvalidDataException("model is a required property for InlineObject1 and cannot be null");
            }
            else
            {
                this.Model = model;
            }
            
            // to ensure "attributes" is required (not null)
            if (attributes == null)
            {
                throw new InvalidDataException("attributes is a required property for InlineObject1 and cannot be null");
            }
            else
            {
                this.Attributes = attributes;
            }
            
            // to ensure "modelType" is required (not null)
            if (modelType == null)
            {
                throw new InvalidDataException("modelType is a required property for InlineObject1 and cannot be null");
            }
            else
            {
                this.ModelType = modelType;
            }
            
            // to ensure "encryptionRequired" is required (not null)
            if (encryptionRequired == null)
            {
                throw new InvalidDataException("encryptionRequired is a required property for InlineObject1 and cannot be null");
            }
            else
            {
                this.EncryptionRequired = encryptionRequired;
            }
            
        }
        
        /// <summary>
        /// Gets or Sets NetworkId
        /// </summary>
        [DataMember(Name="networkId", EmitDefaultValue=true)]
        public string NetworkId { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name="name", EmitDefaultValue=true)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Model
        /// </summary>
        [DataMember(Name="model", EmitDefaultValue=true)]
        public CoreV2ServicesModel Model { get; set; }

        /// <summary>
        /// Gets or Sets Attributes
        /// </summary>
        [DataMember(Name="attributes", EmitDefaultValue=true)]
        public List<string> Attributes { get; set; }

        /// <summary>
        /// Gets or Sets ModelType
        /// </summary>
        [DataMember(Name="modelType", EmitDefaultValue=true)]
        public string ModelType { get; set; }

        /// <summary>
        /// Gets or Sets EncryptionRequired
        /// </summary>
        [DataMember(Name="encryptionRequired", EmitDefaultValue=true)]
        public bool EncryptionRequired { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class InlineObject1 {\n");
            sb.Append("  NetworkId: ").Append(NetworkId).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Model: ").Append(Model).Append("\n");
            sb.Append("  Attributes: ").Append(Attributes).Append("\n");
            sb.Append("  ModelType: ").Append(ModelType).Append("\n");
            sb.Append("  EncryptionRequired: ").Append(EncryptionRequired).Append("\n");
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
            return this.Equals(input as InlineObject1);
        }

        /// <summary>
        /// Returns true if InlineObject1 instances are equal
        /// </summary>
        /// <param name="input">Instance of InlineObject1 to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(InlineObject1 input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.NetworkId == input.NetworkId ||
                    (this.NetworkId != null &&
                    this.NetworkId.Equals(input.NetworkId))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Model == input.Model ||
                    (this.Model != null &&
                    this.Model.Equals(input.Model))
                ) && 
                (
                    this.Attributes == input.Attributes ||
                    this.Attributes != null &&
                    input.Attributes != null &&
                    this.Attributes.SequenceEqual(input.Attributes)
                ) && 
                (
                    this.ModelType == input.ModelType ||
                    (this.ModelType != null &&
                    this.ModelType.Equals(input.ModelType))
                ) && 
                (
                    this.EncryptionRequired == input.EncryptionRequired ||
                    (this.EncryptionRequired != null &&
                    this.EncryptionRequired.Equals(input.EncryptionRequired))
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
                if (this.NetworkId != null)
                    hashCode = hashCode * 59 + this.NetworkId.GetHashCode();
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Model != null)
                    hashCode = hashCode * 59 + this.Model.GetHashCode();
                if (this.Attributes != null)
                    hashCode = hashCode * 59 + this.Attributes.GetHashCode();
                if (this.ModelType != null)
                    hashCode = hashCode * 59 + this.ModelType.GetHashCode();
                if (this.EncryptionRequired != null)
                    hashCode = hashCode * 59 + this.EncryptionRequired.GetHashCode();
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
