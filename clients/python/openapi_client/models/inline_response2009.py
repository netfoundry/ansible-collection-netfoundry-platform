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


class InlineResponse2009(object):
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
        'expires_at': 'str',
        'registration_key': 'str'
    }

    attribute_map = {
        'expires_at': 'expiresAt',
        'registration_key': 'registrationKey'
    }

    def __init__(self, expires_at=None, registration_key=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2009 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expires_at = None
        self._registration_key = None
        self.discriminator = None

        self.expires_at = expires_at
        self.registration_key = registration_key

    @property
    def expires_at(self):
        """Gets the expires_at of this InlineResponse2009.  # noqa: E501


        :return: The expires_at of this InlineResponse2009.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this InlineResponse2009.


        :param expires_at: The expires_at of this InlineResponse2009.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and expires_at is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_at`, must not be `None`")  # noqa: E501

        self._expires_at = expires_at

    @property
    def registration_key(self):
        """Gets the registration_key of this InlineResponse2009.  # noqa: E501


        :return: The registration_key of this InlineResponse2009.  # noqa: E501
        :rtype: str
        """
        return self._registration_key

    @registration_key.setter
    def registration_key(self, registration_key):
        """Sets the registration_key of this InlineResponse2009.


        :param registration_key: The registration_key of this InlineResponse2009.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and registration_key is None:  # noqa: E501
            raise ValueError("Invalid value for `registration_key`, must not be `None`")  # noqa: E501

        self._registration_key = registration_key

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
        if not isinstance(other, InlineResponse2009):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2009):
            return True

        return self.to_dict() != other.to_dict()