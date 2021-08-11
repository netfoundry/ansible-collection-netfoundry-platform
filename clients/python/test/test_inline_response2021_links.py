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
from openapi_client.models.inline_response2021_links import InlineResponse2021Links  # noqa: E501
from openapi_client.rest import ApiException

class TestInlineResponse2021Links(unittest.TestCase):
    """InlineResponse2021Links unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2021Links
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.inline_response2021_links.InlineResponse2021Links()  # noqa: E501
        if include_optional :
            return InlineResponse2021Links(
                network = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                    href = '0', 
                    profile = '0', ), 
                process = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                    href = '0', 
                    profile = '0', ), 
                _self = openapi_client.models.inline_response_200__links_self.inline_response_200__links_self(
                    href = '0', )
            )
        else :
            return InlineResponse2021Links(
                network = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                    href = '0', 
                    profile = '0', ),
                process = openapi_client.models.inline_response_200__links_network.inline_response_200__links_network(
                    href = '0', 
                    profile = '0', ),
                _self = openapi_client.models.inline_response_200__links_self.inline_response_200__links_self(
                    href = '0', ),
        )

    def testInlineResponse2021Links(self):
        """Test InlineResponse2021Links"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()