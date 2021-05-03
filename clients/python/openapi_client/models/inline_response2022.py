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


class InlineResponse2022(object):
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
        'deleted_at': 'str',
        'network_id': 'str',
        'name': 'str',
        'updated_at': 'str',
        'model': 'object',
        'ziti_id': 'object',
        'owner_identity_id': 'str',
        'attributes': 'object',
        'model_type': 'str',
        'id': 'str',
        'config_id_by_config_type_id': 'InlineResponse2022ConfigIdByConfigTypeId',
        'created_at': 'str',
        'created_by': 'str',
        'deleted_by': 'str',
        'encryption_required': 'bool',
        'authority': 'object',
        'links': 'InlineResponse2021Links'
    }

    attribute_map = {
        'deleted_at': 'deletedAt',
        'network_id': 'networkId',
        'name': 'name',
        'updated_at': 'updatedAt',
        'model': 'model',
        'ziti_id': 'zitiId',
        'owner_identity_id': 'ownerIdentityId',
        'attributes': 'attributes',
        'model_type': 'modelType',
        'id': 'id',
        'config_id_by_config_type_id': 'configIdByConfigTypeId',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'deleted_by': 'deletedBy',
        'encryption_required': 'encryptionRequired',
        'authority': 'authority',
        'links': '_links'
    }

    def __init__(self, deleted_at=None, network_id=None, name=None, updated_at=None, model=None, ziti_id=None, owner_identity_id=None, attributes=None, model_type=None, id=None, config_id_by_config_type_id=None, created_at=None, created_by=None, deleted_by=None, encryption_required=None, authority=None, links=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2022 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deleted_at = None
        self._network_id = None
        self._name = None
        self._updated_at = None
        self._model = None
        self._ziti_id = None
        self._owner_identity_id = None
        self._attributes = None
        self._model_type = None
        self._id = None
        self._config_id_by_config_type_id = None
        self._created_at = None
        self._created_by = None
        self._deleted_by = None
        self._encryption_required = None
        self._authority = None
        self._links = None
        self.discriminator = None

        self.deleted_at = deleted_at
        self.network_id = network_id
        self.name = name
        self.updated_at = updated_at
        self.model = model
        self.ziti_id = ziti_id
        self.owner_identity_id = owner_identity_id
        self.attributes = attributes
        self.model_type = model_type
        self.id = id
        self.config_id_by_config_type_id = config_id_by_config_type_id
        self.created_at = created_at
        self.created_by = created_by
        self.deleted_by = deleted_by
        self.encryption_required = encryption_required
        self.authority = authority
        self.links = links

    @property
    def deleted_at(self):
        """Gets the deleted_at of this InlineResponse2022.  # noqa: E501


        :return: The deleted_at of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this InlineResponse2022.


        :param deleted_at: The deleted_at of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and deleted_at is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def network_id(self):
        """Gets the network_id of this InlineResponse2022.  # noqa: E501


        :return: The network_id of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this InlineResponse2022.


        :param network_id: The network_id of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and network_id is None:  # noqa: E501
            raise ValueError("Invalid value for `network_id`, must not be `None`")  # noqa: E501

        self._network_id = network_id

    @property
    def name(self):
        """Gets the name of this InlineResponse2022.  # noqa: E501


        :return: The name of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2022.


        :param name: The name of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse2022.  # noqa: E501


        :return: The updated_at of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse2022.


        :param updated_at: The updated_at of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def model(self):
        """Gets the model of this InlineResponse2022.  # noqa: E501


        :return: The model of this InlineResponse2022.  # noqa: E501
        :rtype: object
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InlineResponse2022.


        :param model: The model of this InlineResponse2022.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def ziti_id(self):
        """Gets the ziti_id of this InlineResponse2022.  # noqa: E501


        :return: The ziti_id of this InlineResponse2022.  # noqa: E501
        :rtype: object
        """
        return self._ziti_id

    @ziti_id.setter
    def ziti_id(self, ziti_id):
        """Sets the ziti_id of this InlineResponse2022.


        :param ziti_id: The ziti_id of this InlineResponse2022.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and ziti_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ziti_id`, must not be `None`")  # noqa: E501

        self._ziti_id = ziti_id

    @property
    def owner_identity_id(self):
        """Gets the owner_identity_id of this InlineResponse2022.  # noqa: E501


        :return: The owner_identity_id of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._owner_identity_id

    @owner_identity_id.setter
    def owner_identity_id(self, owner_identity_id):
        """Sets the owner_identity_id of this InlineResponse2022.


        :param owner_identity_id: The owner_identity_id of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_identity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_identity_id`, must not be `None`")  # noqa: E501

        self._owner_identity_id = owner_identity_id

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse2022.  # noqa: E501


        :return: The attributes of this InlineResponse2022.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse2022.


        :param attributes: The attributes of this InlineResponse2022.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def model_type(self):
        """Gets the model_type of this InlineResponse2022.  # noqa: E501


        :return: The model_type of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this InlineResponse2022.


        :param model_type: The model_type of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and model_type is None:  # noqa: E501
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def id(self):
        """Gets the id of this InlineResponse2022.  # noqa: E501


        :return: The id of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2022.


        :param id: The id of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def config_id_by_config_type_id(self):
        """Gets the config_id_by_config_type_id of this InlineResponse2022.  # noqa: E501


        :return: The config_id_by_config_type_id of this InlineResponse2022.  # noqa: E501
        :rtype: InlineResponse2022ConfigIdByConfigTypeId
        """
        return self._config_id_by_config_type_id

    @config_id_by_config_type_id.setter
    def config_id_by_config_type_id(self, config_id_by_config_type_id):
        """Sets the config_id_by_config_type_id of this InlineResponse2022.


        :param config_id_by_config_type_id: The config_id_by_config_type_id of this InlineResponse2022.  # noqa: E501
        :type: InlineResponse2022ConfigIdByConfigTypeId
        """
        if self.local_vars_configuration.client_side_validation and config_id_by_config_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `config_id_by_config_type_id`, must not be `None`")  # noqa: E501

        self._config_id_by_config_type_id = config_id_by_config_type_id

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2022.  # noqa: E501


        :return: The created_at of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2022.


        :param created_at: The created_at of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this InlineResponse2022.  # noqa: E501


        :return: The created_by of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineResponse2022.


        :param created_by: The created_by of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def deleted_by(self):
        """Gets the deleted_by of this InlineResponse2022.  # noqa: E501


        :return: The deleted_by of this InlineResponse2022.  # noqa: E501
        :rtype: str
        """
        return self._deleted_by

    @deleted_by.setter
    def deleted_by(self, deleted_by):
        """Sets the deleted_by of this InlineResponse2022.


        :param deleted_by: The deleted_by of this InlineResponse2022.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and deleted_by is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_by`, must not be `None`")  # noqa: E501

        self._deleted_by = deleted_by

    @property
    def encryption_required(self):
        """Gets the encryption_required of this InlineResponse2022.  # noqa: E501


        :return: The encryption_required of this InlineResponse2022.  # noqa: E501
        :rtype: bool
        """
        return self._encryption_required

    @encryption_required.setter
    def encryption_required(self, encryption_required):
        """Sets the encryption_required of this InlineResponse2022.


        :param encryption_required: The encryption_required of this InlineResponse2022.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and encryption_required is None:  # noqa: E501
            raise ValueError("Invalid value for `encryption_required`, must not be `None`")  # noqa: E501

        self._encryption_required = encryption_required

    @property
    def authority(self):
        """Gets the authority of this InlineResponse2022.  # noqa: E501


        :return: The authority of this InlineResponse2022.  # noqa: E501
        :rtype: object
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this InlineResponse2022.


        :param authority: The authority of this InlineResponse2022.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and authority is None:  # noqa: E501
            raise ValueError("Invalid value for `authority`, must not be `None`")  # noqa: E501

        self._authority = authority

    @property
    def links(self):
        """Gets the links of this InlineResponse2022.  # noqa: E501


        :return: The links of this InlineResponse2022.  # noqa: E501
        :rtype: InlineResponse2021Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InlineResponse2022.


        :param links: The links of this InlineResponse2022.  # noqa: E501
        :type: InlineResponse2021Links
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

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
        if not isinstance(other, InlineResponse2022):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2022):
            return True

        return self.to_dict() != other.to_dict()
