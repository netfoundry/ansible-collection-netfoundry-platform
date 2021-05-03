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

/**
 * The InlineResponse2001LinksSelf model module.
 * @module model/InlineResponse2001LinksSelf
 * @version 5229
 */
class InlineResponse2001LinksSelf {
    /**
     * Constructs a new <code>InlineResponse2001LinksSelf</code>.
     * @alias module:model/InlineResponse2001LinksSelf
     * @param href {String} 
     * @param templated {Boolean} 
     */
    constructor(href, templated) { 
        
        InlineResponse2001LinksSelf.initialize(this, href, templated);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, href, templated) { 
        obj['href'] = href;
        obj['templated'] = templated;
    }

    /**
     * Constructs a <code>InlineResponse2001LinksSelf</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InlineResponse2001LinksSelf} obj Optional instance to populate.
     * @return {module:model/InlineResponse2001LinksSelf} The populated <code>InlineResponse2001LinksSelf</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InlineResponse2001LinksSelf();

            if (data.hasOwnProperty('href')) {
                obj['href'] = ApiClient.convertToType(data['href'], 'String');
            }
            if (data.hasOwnProperty('templated')) {
                obj['templated'] = ApiClient.convertToType(data['templated'], 'Boolean');
            }
        }
        return obj;
    }


}

/**
 * @member {String} href
 */
InlineResponse2001LinksSelf.prototype['href'] = undefined;

/**
 * @member {Boolean} templated
 */
InlineResponse2001LinksSelf.prototype['templated'] = undefined;






export default InlineResponse2001LinksSelf;

