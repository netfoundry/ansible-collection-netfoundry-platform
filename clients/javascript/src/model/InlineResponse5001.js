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
import InlineResponse5001Status from './InlineResponse5001Status';

/**
 * The InlineResponse5001 model module.
 * @module model/InlineResponse5001
 * @version 5229
 */
class InlineResponse5001 {
    /**
     * Constructs a new <code>InlineResponse5001</code>.
     * @alias module:model/InlineResponse5001
     * @param errors {Array.<String>} 
     * @param status {module:model/InlineResponse5001Status} 
     * @param traceId {String} 
     */
    constructor(errors, status, traceId) { 
        
        InlineResponse5001.initialize(this, errors, status, traceId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, errors, status, traceId) { 
        obj['errors'] = errors;
        obj['status'] = status;
        obj['traceId'] = traceId;
    }

    /**
     * Constructs a <code>InlineResponse5001</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InlineResponse5001} obj Optional instance to populate.
     * @return {module:model/InlineResponse5001} The populated <code>InlineResponse5001</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InlineResponse5001();

            if (data.hasOwnProperty('errors')) {
                obj['errors'] = ApiClient.convertToType(data['errors'], ['String']);
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = InlineResponse5001Status.constructFromObject(data['status']);
            }
            if (data.hasOwnProperty('traceId')) {
                obj['traceId'] = ApiClient.convertToType(data['traceId'], 'String');
            }
        }
        return obj;
    }


}

/**
 * @member {Array.<String>} errors
 */
InlineResponse5001.prototype['errors'] = undefined;

/**
 * @member {module:model/InlineResponse5001Status} status
 */
InlineResponse5001.prototype['status'] = undefined;

/**
 * @member {String} traceId
 */
InlineResponse5001.prototype['traceId'] = undefined;






export default InlineResponse5001;

