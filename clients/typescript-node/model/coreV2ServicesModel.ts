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

import { RequestFile } from '../api';
import { CoreV2ServicesModelClientIngress } from './coreV2ServicesModelClientIngress';
import { CoreV2ServicesModelEdgeRouterHosts } from './coreV2ServicesModelEdgeRouterHosts';
import { InlineResponse2003EmbeddedModelServerEgress } from './inlineResponse2003EmbeddedModelServerEgress';

export class CoreV2ServicesModel {
    'edgeRouterAttributes': Array<string>;
    'serverEgress'?: InlineResponse2003EmbeddedModelServerEgress;
    'bindEndpointAttributes'?: Array<string>;
    'clientIngress': CoreV2ServicesModelClientIngress;
    'edgeRouterHosts'?: Array<CoreV2ServicesModelEdgeRouterHosts>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "edgeRouterAttributes",
            "baseName": "edgeRouterAttributes",
            "type": "Array<string>"
        },
        {
            "name": "serverEgress",
            "baseName": "serverEgress",
            "type": "InlineResponse2003EmbeddedModelServerEgress"
        },
        {
            "name": "bindEndpointAttributes",
            "baseName": "bindEndpointAttributes",
            "type": "Array<string>"
        },
        {
            "name": "clientIngress",
            "baseName": "clientIngress",
            "type": "CoreV2ServicesModelClientIngress"
        },
        {
            "name": "edgeRouterHosts",
            "baseName": "edgeRouterHosts",
            "type": "Array<CoreV2ServicesModelEdgeRouterHosts>"
        }    ];

    static getAttributeTypeMap() {
        return CoreV2ServicesModel.attributeTypeMap;
    }
}
