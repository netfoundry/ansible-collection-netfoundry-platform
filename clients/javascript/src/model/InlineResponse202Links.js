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
import InlineResponse200LinksNetwork from './InlineResponse200LinksNetwork';
import InlineResponse200LinksSelf from './InlineResponse200LinksSelf';

/**
 * The InlineResponse202Links model module.
 * @module model/InlineResponse202Links
 * @version 5229
 */
class InlineResponse202Links {
    /**
     * Constructs a new <code>InlineResponse202Links</code>.
     * @alias module:model/InlineResponse202Links
     * @param services {module:model/InlineResponse200LinksSelf} 
     * @param networks {module:model/InlineResponse200LinksNetwork} 
     * @param appWans {module:model/InlineResponse200LinksSelf} 
     * @param process {module:model/InlineResponse200LinksNetwork} 
     * @param endpoints {module:model/InlineResponse200LinksSelf} 
     * @param certificateAuthorities {module:model/InlineResponse200LinksSelf} 
     * @param self {module:model/InlineResponse200LinksSelf} 
     * @param processExecutions {module:model/InlineResponse200LinksNetwork} 
     * @param networkControllers {module:model/InlineResponse200LinksSelf} 
     * @param postureChecks {module:model/InlineResponse200LinksSelf} 
     * @param edgeRouters {module:model/InlineResponse200LinksSelf} 
     * @param edgeRouterPolicies {module:model/InlineResponse200LinksSelf} 
     */
    constructor(services, networks, appWans, process, endpoints, certificateAuthorities, self, processExecutions, networkControllers, postureChecks, edgeRouters, edgeRouterPolicies) { 
        
        InlineResponse202Links.initialize(this, services, networks, appWans, process, endpoints, certificateAuthorities, self, processExecutions, networkControllers, postureChecks, edgeRouters, edgeRouterPolicies);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, services, networks, appWans, process, endpoints, certificateAuthorities, self, processExecutions, networkControllers, postureChecks, edgeRouters, edgeRouterPolicies) { 
        obj['services'] = services;
        obj['networks'] = networks;
        obj['app-wans'] = appWans;
        obj['process'] = process;
        obj['endpoints'] = endpoints;
        obj['certificate-authorities'] = certificateAuthorities;
        obj['self'] = self;
        obj['process-executions'] = processExecutions;
        obj['network-controllers'] = networkControllers;
        obj['posture-checks'] = postureChecks;
        obj['edge-routers'] = edgeRouters;
        obj['edge-router-policies'] = edgeRouterPolicies;
    }

    /**
     * Constructs a <code>InlineResponse202Links</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/InlineResponse202Links} obj Optional instance to populate.
     * @return {module:model/InlineResponse202Links} The populated <code>InlineResponse202Links</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new InlineResponse202Links();

            if (data.hasOwnProperty('services')) {
                obj['services'] = InlineResponse200LinksSelf.constructFromObject(data['services']);
            }
            if (data.hasOwnProperty('networks')) {
                obj['networks'] = InlineResponse200LinksNetwork.constructFromObject(data['networks']);
            }
            if (data.hasOwnProperty('app-wans')) {
                obj['app-wans'] = InlineResponse200LinksSelf.constructFromObject(data['app-wans']);
            }
            if (data.hasOwnProperty('process')) {
                obj['process'] = InlineResponse200LinksNetwork.constructFromObject(data['process']);
            }
            if (data.hasOwnProperty('endpoints')) {
                obj['endpoints'] = InlineResponse200LinksSelf.constructFromObject(data['endpoints']);
            }
            if (data.hasOwnProperty('certificate-authorities')) {
                obj['certificate-authorities'] = InlineResponse200LinksSelf.constructFromObject(data['certificate-authorities']);
            }
            if (data.hasOwnProperty('self')) {
                obj['self'] = InlineResponse200LinksSelf.constructFromObject(data['self']);
            }
            if (data.hasOwnProperty('process-executions')) {
                obj['process-executions'] = InlineResponse200LinksNetwork.constructFromObject(data['process-executions']);
            }
            if (data.hasOwnProperty('network-controllers')) {
                obj['network-controllers'] = InlineResponse200LinksSelf.constructFromObject(data['network-controllers']);
            }
            if (data.hasOwnProperty('posture-checks')) {
                obj['posture-checks'] = InlineResponse200LinksSelf.constructFromObject(data['posture-checks']);
            }
            if (data.hasOwnProperty('edge-routers')) {
                obj['edge-routers'] = InlineResponse200LinksSelf.constructFromObject(data['edge-routers']);
            }
            if (data.hasOwnProperty('edge-router-policies')) {
                obj['edge-router-policies'] = InlineResponse200LinksSelf.constructFromObject(data['edge-router-policies']);
            }
        }
        return obj;
    }


}

/**
 * @member {module:model/InlineResponse200LinksSelf} services
 */
InlineResponse202Links.prototype['services'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksNetwork} networks
 */
InlineResponse202Links.prototype['networks'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} app-wans
 */
InlineResponse202Links.prototype['app-wans'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksNetwork} process
 */
InlineResponse202Links.prototype['process'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} endpoints
 */
InlineResponse202Links.prototype['endpoints'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} certificate-authorities
 */
InlineResponse202Links.prototype['certificate-authorities'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} self
 */
InlineResponse202Links.prototype['self'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksNetwork} process-executions
 */
InlineResponse202Links.prototype['process-executions'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} network-controllers
 */
InlineResponse202Links.prototype['network-controllers'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} posture-checks
 */
InlineResponse202Links.prototype['posture-checks'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} edge-routers
 */
InlineResponse202Links.prototype['edge-routers'] = undefined;

/**
 * @member {module:model/InlineResponse200LinksSelf} edge-router-policies
 */
InlineResponse202Links.prototype['edge-router-policies'] = undefined;






export default InlineResponse202Links;
