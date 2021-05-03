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
import { InlineResponse20018Embedded } from './inlineResponse20018Embedded';
import { InlineResponse2001Page } from './inlineResponse2001Page';
import { InlineResponse2002EmbeddedLinks } from './inlineResponse2002EmbeddedLinks';

export class InlineResponse20018 {
    'embedded'?: InlineResponse20018Embedded;
    'links': InlineResponse2002EmbeddedLinks;
    'page': InlineResponse2001Page;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "embedded",
            "baseName": "_embedded",
            "type": "InlineResponse20018Embedded"
        },
        {
            "name": "links",
            "baseName": "_links",
            "type": "InlineResponse2002EmbeddedLinks"
        },
        {
            "name": "page",
            "baseName": "page",
            "type": "InlineResponse2001Page"
        }    ];

    static getAttributeTypeMap() {
        return InlineResponse20018.attributeTypeMap;
    }
}

