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
import { AnyType } from './anyType';
import { InlineResponse20014UpdatedAt } from './inlineResponse20014UpdatedAt';

export class InlineResponse20014IdentityProviders {
    'deletedAt': AnyType;
    'name': string;
    'updatedAt': AnyType;
    'auth0ConnectionType': string;
    'auth0ConnectionId': string;
    'id': string;
    'createdAt': InlineResponse20014UpdatedAt;
    'organizationId': string;
    'active': boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "deletedAt",
            "baseName": "deletedAt",
            "type": "AnyType"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "updatedAt",
            "baseName": "updatedAt",
            "type": "AnyType"
        },
        {
            "name": "auth0ConnectionType",
            "baseName": "auth0ConnectionType",
            "type": "string"
        },
        {
            "name": "auth0ConnectionId",
            "baseName": "auth0ConnectionId",
            "type": "string"
        },
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "createdAt",
            "baseName": "createdAt",
            "type": "InlineResponse20014UpdatedAt"
        },
        {
            "name": "organizationId",
            "baseName": "organizationId",
            "type": "string"
        },
        {
            "name": "active",
            "baseName": "active",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return InlineResponse20014IdentityProviders.attributeTypeMap;
    }
}

