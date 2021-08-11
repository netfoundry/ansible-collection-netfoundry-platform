# coding: utf-8

"""
    untitled API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5170
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.inline_response2023 import InlineResponse2023  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse2023(unittest.TestCase):
    """InlineResponse2023 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2023
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response2023.InlineResponse2023()  # noqa: E501
        if include_optional :
            return InlineResponse2023(
                deleted_at = null, 
                network_id = '0', 
                name = '0', 
                updated_at = '0', 
                model = openapi_client.models.inline_response_202_3_model.inline_response_202_3_model(
                    bind_endpoint_attributes = [
                        '0'
                        ], 
                    client_ingress = openapi_client.models.inline_response_202_3_model_client_ingress.inline_response_202_3_model_clientIngress(
                        addresses = [
                            '0'
                            ], 
                        ports = [
                            openapi_client.models.inline_response_200_3__embedded_model_client_ingress_ports.inline_response_200_3__embedded_model_clientIngress_ports(
                                high = 1.337, 
                                low = 1.337, )
                            ], 
                        protocols = [
                            '0'
                            ], ), 
                    edge_router_attributes = [
                        '0'
                        ], 
                    server_egress = openapi_client.models._core_v2_services__service_id__model_server_egress._core_v2_services__serviceId__model_serverEgress(
                        dial_intercept_address = null, 
                        dial_intercept_port = null, 
                        port = 1.337, 
                        dial_intercept_protocol = True, 
                        address = '0', 
                        protocol = null, ), ), 
                ziti_id = '0', 
                owner_identity_id = '0', 
                attributes = [
                    '0'
                    ], 
                model_type = '0', 
                id = '0', 
                config_id_by_config_type_id = openapi_client.models.inline_response_202_3_config_id_by_config_type_id.inline_response_202_3_configIdByConfigTypeId(
                    714a918a_7935_4b4f_82c3_afbadcd9e59b = '0', 
                    7cafedc5_17b8_4c1e_8b6f_0d9bc1b4b7bc = '0', 
                    d75e27f0_ebab_4567_8440_c24f02f2eca5 = '0', 
                    ea6e632b_d8e1_420f_bd8f_ad50b067bad6 = '0', ), 
                created_at = '0', 
                created_by = '0', 
                deleted_by = null, 
                encryption_required = True, 
                authority = null, 
                links = openapi_client.models.inline_response_202_1__links.inline_response_202_1__links(
                    network = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                        href = '0', 
                        profile = '0', ), 
                    process = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                        href = '0', 
                        profile = '0', ), 
                    self = openapi_client.models.inline_response_200__links_self.inline_response_200__links_self(
                        href = '0', ), )
            )
        else :
            return InlineResponse2023(
                deleted_at = null,
                network_id = '0',
                name = '0',
                updated_at = '0',
                model = openapi_client.models.inline_response_202_3_model.inline_response_202_3_model(
                    bind_endpoint_attributes = [
                        '0'
                        ], 
                    client_ingress = openapi_client.models.inline_response_202_3_model_client_ingress.inline_response_202_3_model_clientIngress(
                        addresses = [
                            '0'
                            ], 
                        ports = [
                            openapi_client.models.inline_response_200_3__embedded_model_client_ingress_ports.inline_response_200_3__embedded_model_clientIngress_ports(
                                high = 1.337, 
                                low = 1.337, )
                            ], 
                        protocols = [
                            '0'
                            ], ), 
                    edge_router_attributes = [
                        '0'
                        ], 
                    server_egress = openapi_client.models._core_v2_services__service_id__model_server_egress._core_v2_services__serviceId__model_serverEgress(
                        dial_intercept_address = null, 
                        dial_intercept_port = null, 
                        port = 1.337, 
                        dial_intercept_protocol = True, 
                        address = '0', 
                        protocol = null, ), ),
                ziti_id = '0',
                owner_identity_id = '0',
                attributes = [
                    '0'
                    ],
                model_type = '0',
                id = '0',
                config_id_by_config_type_id = openapi_client.models.inline_response_202_3_config_id_by_config_type_id.inline_response_202_3_configIdByConfigTypeId(
                    714a918a_7935_4b4f_82c3_afbadcd9e59b = '0', 
                    7cafedc5_17b8_4c1e_8b6f_0d9bc1b4b7bc = '0', 
                    d75e27f0_ebab_4567_8440_c24f02f2eca5 = '0', 
                    ea6e632b_d8e1_420f_bd8f_ad50b067bad6 = '0', ),
                created_at = '0',
                created_by = '0',
                deleted_by = null,
                encryption_required = True,
                authority = null,
                links = openapi_client.models.inline_response_202_1__links.inline_response_202_1__links(
                    network = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                        href = '0', 
                        profile = '0', ), 
                    process = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                        href = '0', 
                        profile = '0', ), 
                    self = openapi_client.models.inline_response_200__links_self.inline_response_200__links_self(
                        href = '0', ), ),
        )

    def testInlineResponse2023(self):
        """Test InlineResponse2023"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()