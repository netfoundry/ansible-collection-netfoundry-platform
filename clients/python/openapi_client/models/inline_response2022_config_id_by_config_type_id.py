# coding: utf-8

"""
    untitled API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5229
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class InlineResponse2022ConfigIdByConfigTypeId(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'aca7f705_9f00_4ff6_8b86_63a4d44bde8a': 'str',
        '_6cd51ae0_cfe4_499d_88d8_d02a9e18b25f': 'str',
        'd28725c0_9771_47d7_a9da_e408bd0adf4e': 'str',
        '_888d6565_4359_4d91_b38d_0a24124e4456': 'str',
        'feb075cd_dd2b_47c5_922c_86ef3b06fb16': 'str'
    }

    attribute_map = {
        'aca7f705_9f00_4ff6_8b86_63a4d44bde8a': 'aca7f705-9f00-4ff6-8b86-63a4d44bde8a',
        '_6cd51ae0_cfe4_499d_88d8_d02a9e18b25f': '6cd51ae0-cfe4-499d-88d8-d02a9e18b25f',
        'd28725c0_9771_47d7_a9da_e408bd0adf4e': 'd28725c0-9771-47d7-a9da-e408bd0adf4e',
        '_888d6565_4359_4d91_b38d_0a24124e4456': '888d6565-4359-4d91-b38d-0a24124e4456',
        'feb075cd_dd2b_47c5_922c_86ef3b06fb16': 'feb075cd-dd2b-47c5-922c-86ef3b06fb16'
    }

    def __init__(self, aca7f705_9f00_4ff6_8b86_63a4d44bde8a=None, _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f=None, d28725c0_9771_47d7_a9da_e408bd0adf4e=None, _888d6565_4359_4d91_b38d_0a24124e4456=None, feb075cd_dd2b_47c5_922c_86ef3b06fb16=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2022ConfigIdByConfigTypeId - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._aca7f705_9f00_4ff6_8b86_63a4d44bde8a = None
        self.__6cd51ae0_cfe4_499d_88d8_d02a9e18b25f = None
        self._d28725c0_9771_47d7_a9da_e408bd0adf4e = None
        self.__888d6565_4359_4d91_b38d_0a24124e4456 = None
        self._feb075cd_dd2b_47c5_922c_86ef3b06fb16 = None
        self.discriminator = None

        if aca7f705_9f00_4ff6_8b86_63a4d44bde8a is not None:
            self.aca7f705_9f00_4ff6_8b86_63a4d44bde8a = aca7f705_9f00_4ff6_8b86_63a4d44bde8a
        if _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f is not None:
            self._6cd51ae0_cfe4_499d_88d8_d02a9e18b25f = _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f
        if d28725c0_9771_47d7_a9da_e408bd0adf4e is not None:
            self.d28725c0_9771_47d7_a9da_e408bd0adf4e = d28725c0_9771_47d7_a9da_e408bd0adf4e
        if _888d6565_4359_4d91_b38d_0a24124e4456 is not None:
            self._888d6565_4359_4d91_b38d_0a24124e4456 = _888d6565_4359_4d91_b38d_0a24124e4456
        if feb075cd_dd2b_47c5_922c_86ef3b06fb16 is not None:
            self.feb075cd_dd2b_47c5_922c_86ef3b06fb16 = feb075cd_dd2b_47c5_922c_86ef3b06fb16

    @property
    def aca7f705_9f00_4ff6_8b86_63a4d44bde8a(self):
        """Gets the aca7f705_9f00_4ff6_8b86_63a4d44bde8a of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501


        :return: The aca7f705_9f00_4ff6_8b86_63a4d44bde8a of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :rtype: str
        """
        return self._aca7f705_9f00_4ff6_8b86_63a4d44bde8a

    @aca7f705_9f00_4ff6_8b86_63a4d44bde8a.setter
    def aca7f705_9f00_4ff6_8b86_63a4d44bde8a(self, aca7f705_9f00_4ff6_8b86_63a4d44bde8a):
        """Sets the aca7f705_9f00_4ff6_8b86_63a4d44bde8a of this InlineResponse2022ConfigIdByConfigTypeId.


        :param aca7f705_9f00_4ff6_8b86_63a4d44bde8a: The aca7f705_9f00_4ff6_8b86_63a4d44bde8a of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :type: str
        """

        self._aca7f705_9f00_4ff6_8b86_63a4d44bde8a = aca7f705_9f00_4ff6_8b86_63a4d44bde8a

    @property
    def _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f(self):
        """Gets the _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501


        :return: The _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :rtype: str
        """
        return self.__6cd51ae0_cfe4_499d_88d8_d02a9e18b25f

    @_6cd51ae0_cfe4_499d_88d8_d02a9e18b25f.setter
    def _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f(self, _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f):
        """Sets the _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f of this InlineResponse2022ConfigIdByConfigTypeId.


        :param _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f: The _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :type: str
        """

        self.__6cd51ae0_cfe4_499d_88d8_d02a9e18b25f = _6cd51ae0_cfe4_499d_88d8_d02a9e18b25f

    @property
    def d28725c0_9771_47d7_a9da_e408bd0adf4e(self):
        """Gets the d28725c0_9771_47d7_a9da_e408bd0adf4e of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501


        :return: The d28725c0_9771_47d7_a9da_e408bd0adf4e of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :rtype: str
        """
        return self._d28725c0_9771_47d7_a9da_e408bd0adf4e

    @d28725c0_9771_47d7_a9da_e408bd0adf4e.setter
    def d28725c0_9771_47d7_a9da_e408bd0adf4e(self, d28725c0_9771_47d7_a9da_e408bd0adf4e):
        """Sets the d28725c0_9771_47d7_a9da_e408bd0adf4e of this InlineResponse2022ConfigIdByConfigTypeId.


        :param d28725c0_9771_47d7_a9da_e408bd0adf4e: The d28725c0_9771_47d7_a9da_e408bd0adf4e of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :type: str
        """

        self._d28725c0_9771_47d7_a9da_e408bd0adf4e = d28725c0_9771_47d7_a9da_e408bd0adf4e

    @property
    def _888d6565_4359_4d91_b38d_0a24124e4456(self):
        """Gets the _888d6565_4359_4d91_b38d_0a24124e4456 of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501


        :return: The _888d6565_4359_4d91_b38d_0a24124e4456 of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :rtype: str
        """
        return self.__888d6565_4359_4d91_b38d_0a24124e4456

    @_888d6565_4359_4d91_b38d_0a24124e4456.setter
    def _888d6565_4359_4d91_b38d_0a24124e4456(self, _888d6565_4359_4d91_b38d_0a24124e4456):
        """Sets the _888d6565_4359_4d91_b38d_0a24124e4456 of this InlineResponse2022ConfigIdByConfigTypeId.


        :param _888d6565_4359_4d91_b38d_0a24124e4456: The _888d6565_4359_4d91_b38d_0a24124e4456 of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :type: str
        """

        self.__888d6565_4359_4d91_b38d_0a24124e4456 = _888d6565_4359_4d91_b38d_0a24124e4456

    @property
    def feb075cd_dd2b_47c5_922c_86ef3b06fb16(self):
        """Gets the feb075cd_dd2b_47c5_922c_86ef3b06fb16 of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501


        :return: The feb075cd_dd2b_47c5_922c_86ef3b06fb16 of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :rtype: str
        """
        return self._feb075cd_dd2b_47c5_922c_86ef3b06fb16

    @feb075cd_dd2b_47c5_922c_86ef3b06fb16.setter
    def feb075cd_dd2b_47c5_922c_86ef3b06fb16(self, feb075cd_dd2b_47c5_922c_86ef3b06fb16):
        """Sets the feb075cd_dd2b_47c5_922c_86ef3b06fb16 of this InlineResponse2022ConfigIdByConfigTypeId.


        :param feb075cd_dd2b_47c5_922c_86ef3b06fb16: The feb075cd_dd2b_47c5_922c_86ef3b06fb16 of this InlineResponse2022ConfigIdByConfigTypeId.  # noqa: E501
        :type: str
        """

        self._feb075cd_dd2b_47c5_922c_86ef3b06fb16 = feb075cd_dd2b_47c5_922c_86ef3b06fb16

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2022ConfigIdByConfigTypeId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2022ConfigIdByConfigTypeId):
            return True

        return self.to_dict() != other.to_dict()
