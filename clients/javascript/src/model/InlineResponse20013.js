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
 *
 */

import ApiClient from '../ApiClient';
import AnyType from './AnyType';
import InlineResponse2001EmbeddedLinks from './InlineResponse2001EmbeddedLinks';

/**
 * The InlineResponse20013 model module.
 * @module model/InlineResponse20013
 * @version 5229
 */
class InlineResponse20013 {
    /**
     * Constructs a new <code>InlineResponse20013</code>.
     * @alias module:model/InlineResponse20013
     * @param deletedAt {module:model/AnyType} 
     * @param name {String} 
     * @param updatedAt {String} 
     * @param size {String} 
     * @param ownerIdentityId {String} 
     * @param productVersion {String} 
     * @param networkGroupId {String} 
     * @param id {String} 
     * @param status {String} 
     * @param createdAt {String} 
     * @param createdBy {String} 
     * @param deletedBy {module:model/AnyType} 
     * @param o365BreakoutCategory {String} 
     * @param links {module:model/InlineResponse2001EmbeddedLinks} 
     */
    constructor(deletedAt, name, updatedAt, size, ownerIdentityId, productVersion, networkGroupId, id, status, createdAt, createdBy, deletedBy, o365BreakoutCategory, links) { 
        
        InlineResponse20013.initialize(this, deletedAt, name, updatedAt, size, ownerIdentityId, productVersion, networkGroupId, id, status, createdAt, createdBy, deletedBy, o365BreakoutCategory, links);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, deletedAt, name, updatedAt, size, ownerIdentityId, productVersion, networkGroupId, id, status, createdAt, createdBy, deletedBy, o365BreakoutCategory, links) { 
        obj['deletedAt'] = deletedAt;
        obj['name'] = name;
        obj['updatedAt'] = updatedAt;
        obj['size'] = size;
        obj['ownerIdentityId'] = ownerIdentityId;
        obj['productVersion'] = productVersion;
        obj['networkGroupId'] = networkGroupId;
        obj['id'] = id;
        obj['status'] = status;
        obj['createdAt'] = createdAt;
        obj['createdBy'] = createdBy;
        obj['deletedBy'] = deletedBy;
        obj['o365BreakoutCategory'] = o365BreakoutCategory;
        obj['_links'] = links;
    }

    /**
     * Constructs a <code>InlineResponse20013</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InlineResponse20013} obj Optional instance to populate.
     * @return {module:model/InlineResponse20013} The populated <code>InlineResponse20013</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InlineResponse20013();

            if (data.hasOwnProperty('deletedAt')) {
                obj['deletedAt'] = ApiClient.convertToType(data['deletedAt'], AnyType);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'String');
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], 'String');
            }
            if (data.hasOwnProperty('locationCode')) {
                obj['locationCode'] = ApiClient.convertToType(data['locationCode'], 'String');
            }
            if (data.hasOwnProperty('ownerIdentityId')) {
                obj['ownerIdentityId'] = ApiClient.convertToType(data['ownerIdentityId'], 'String');
            }
            if (data.hasOwnProperty('productVersion')) {
                obj['productVersion'] = ApiClient.convertToType(data['productVersion'], 'String');
            }
            if (data.hasOwnProperty('networkGroupId')) {
                obj['networkGroupId'] = ApiClient.convertToType(data['networkGroupId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('sdsPassword')) {
                obj['sdsPassword'] = ApiClient.convertToType(data['sdsPassword'], 'String');
            }
            if (data.hasOwnProperty('createdAt')) {
                obj['createdAt'] = ApiClient.convertToType(data['createdAt'], 'String');
            }
            if (data.hasOwnProperty('createdBy')) {
                obj['createdBy'] = ApiClient.convertToType(data['createdBy'], 'String');
            }
            if (data.hasOwnProperty('deletedBy')) {
                obj['deletedBy'] = ApiClient.convertToType(data['deletedBy'], AnyType);
            }
            if (data.hasOwnProperty('networkController')) {
                obj['networkController'] = ApiClient.convertToType(data['networkController'], AnyType);
            }
            if (data.hasOwnProperty('o365BreakoutCategory')) {
                obj['o365BreakoutCategory'] = ApiClient.convertToType(data['o365BreakoutCategory'], 'String');
            }
            if (data.hasOwnProperty('_links')) {
                obj['_links'] = InlineResponse2001EmbeddedLinks.constructFromObject(data['_links']);
            }
        }
        return obj;
    }


}

/**
 * @member {module:model/AnyType} deletedAt
 */
InlineResponse20013.prototype['deletedAt'] = undefined;

/**
 * @member {String} name
 */
InlineResponse20013.prototype['name'] = undefined;

/**
 * @member {String} updatedAt
 */
InlineResponse20013.prototype['updatedAt'] = undefined;

/**
 * @member {String} size
 */
InlineResponse20013.prototype['size'] = undefined;

/**
 * @member {String} locationCode
 */
InlineResponse20013.prototype['locationCode'] = undefined;

/**
 * @member {String} ownerIdentityId
 */
InlineResponse20013.prototype['ownerIdentityId'] = undefined;

/**
 * @member {String} productVersion
 */
InlineResponse20013.prototype['productVersion'] = undefined;

/**
 * @member {String} networkGroupId
 */
InlineResponse20013.prototype['networkGroupId'] = undefined;

/**
 * @member {String} id
 */
InlineResponse20013.prototype['id'] = undefined;

/**
 * @member {String} status
 */
InlineResponse20013.prototype['status'] = undefined;

/**
 * @member {String} sdsPassword
 */
InlineResponse20013.prototype['sdsPassword'] = undefined;

/**
 * @member {String} createdAt
 */
InlineResponse20013.prototype['createdAt'] = undefined;

/**
 * @member {String} createdBy
 */
InlineResponse20013.prototype['createdBy'] = undefined;

/**
 * @member {module:model/AnyType} deletedBy
 */
InlineResponse20013.prototype['deletedBy'] = undefined;

/**
 * @member {module:model/AnyType} networkController
 */
InlineResponse20013.prototype['networkController'] = undefined;

/**
 * @member {String} o365BreakoutCategory
 */
InlineResponse20013.prototype['o365BreakoutCategory'] = undefined;

/**
 * @member {module:model/InlineResponse2001EmbeddedLinks} _links
 */
InlineResponse20013.prototype['_links'] = undefined;






export default InlineResponse20013;

