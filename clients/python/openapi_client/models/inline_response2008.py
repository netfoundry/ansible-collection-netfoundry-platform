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


class InlineResponse2008(object):
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
        'mfa_enabled': 'bool',
        'deleted_at': 'object',
        'network_id': 'str',
        'name': 'str',
        'updated_at': 'str',
        'sync_id': 'object',
        'session_identity_id': 'object',
        'os_release': 'object',
        'sync_resource_id': 'object',
        'ziti_id': 'str',
        'app_version': 'object',
        'branch': 'object',
        'os': 'object',
        'owner_identity_id': 'str',
        'has_edge_router_connection': 'bool',
        'attributes': 'list[str]',
        'has_api_session': 'bool',
        'revision': 'object',
        'version': 'object',
        'jwt': 'str',
        'id': 'str',
        'session_active': 'bool',
        'jwt_expires_at': 'str',
        'created_at': 'str',
        'arch': 'object',
        'created_by': 'str',
        'deleted_by': 'object',
        'type': 'object',
        'os_version': 'object',
        'app_id': 'object',
        'links': 'InlineResponse200Links'
    }

    attribute_map = {
        'mfa_enabled': 'mfaEnabled',
        'deleted_at': 'deletedAt',
        'network_id': 'networkId',
        'name': 'name',
        'updated_at': 'updatedAt',
        'sync_id': 'syncId',
        'session_identity_id': 'sessionIdentityId',
        'os_release': 'osRelease',
        'sync_resource_id': 'syncResourceId',
        'ziti_id': 'zitiId',
        'app_version': 'appVersion',
        'branch': 'branch',
        'os': 'os',
        'owner_identity_id': 'ownerIdentityId',
        'has_edge_router_connection': 'hasEdgeRouterConnection',
        'attributes': 'attributes',
        'has_api_session': 'hasApiSession',
        'revision': 'revision',
        'version': 'version',
        'jwt': 'jwt',
        'id': 'id',
        'session_active': 'sessionActive',
        'jwt_expires_at': 'jwtExpiresAt',
        'created_at': 'createdAt',
        'arch': 'arch',
        'created_by': 'createdBy',
        'deleted_by': 'deletedBy',
        'type': 'type',
        'os_version': 'osVersion',
        'app_id': 'appId',
        'links': '_links'
    }

    def __init__(self, mfa_enabled=None, deleted_at=None, network_id=None, name=None, updated_at=None, sync_id=None, session_identity_id=None, os_release=None, sync_resource_id=None, ziti_id=None, app_version=None, branch=None, os=None, owner_identity_id=None, has_edge_router_connection=None, attributes=None, has_api_session=None, revision=None, version=None, jwt=None, id=None, session_active=None, jwt_expires_at=None, created_at=None, arch=None, created_by=None, deleted_by=None, type=None, os_version=None, app_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2008 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mfa_enabled = None
        self._deleted_at = None
        self._network_id = None
        self._name = None
        self._updated_at = None
        self._sync_id = None
        self._session_identity_id = None
        self._os_release = None
        self._sync_resource_id = None
        self._ziti_id = None
        self._app_version = None
        self._branch = None
        self._os = None
        self._owner_identity_id = None
        self._has_edge_router_connection = None
        self._attributes = None
        self._has_api_session = None
        self._revision = None
        self._version = None
        self._jwt = None
        self._id = None
        self._session_active = None
        self._jwt_expires_at = None
        self._created_at = None
        self._arch = None
        self._created_by = None
        self._deleted_by = None
        self._type = None
        self._os_version = None
        self._app_id = None
        self._links = None
        self.discriminator = None

        self.mfa_enabled = mfa_enabled
        self.deleted_at = deleted_at
        self.network_id = network_id
        self.name = name
        self.updated_at = updated_at
        self.sync_id = sync_id
        self.session_identity_id = session_identity_id
        self.os_release = os_release
        self.sync_resource_id = sync_resource_id
        self.ziti_id = ziti_id
        self.app_version = app_version
        self.branch = branch
        self.os = os
        self.owner_identity_id = owner_identity_id
        self.has_edge_router_connection = has_edge_router_connection
        self.attributes = attributes
        self.has_api_session = has_api_session
        self.revision = revision
        self.version = version
        self.jwt = jwt
        self.id = id
        self.session_active = session_active
        self.jwt_expires_at = jwt_expires_at
        self.created_at = created_at
        self.arch = arch
        self.created_by = created_by
        self.deleted_by = deleted_by
        self.type = type
        self.os_version = os_version
        self.app_id = app_id
        self.links = links

    @property
    def mfa_enabled(self):
        """Gets the mfa_enabled of this InlineResponse2008.  # noqa: E501


        :return: The mfa_enabled of this InlineResponse2008.  # noqa: E501
        :rtype: bool
        """
        return self._mfa_enabled

    @mfa_enabled.setter
    def mfa_enabled(self, mfa_enabled):
        """Sets the mfa_enabled of this InlineResponse2008.


        :param mfa_enabled: The mfa_enabled of this InlineResponse2008.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and mfa_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `mfa_enabled`, must not be `None`")  # noqa: E501

        self._mfa_enabled = mfa_enabled

    @property
    def deleted_at(self):
        """Gets the deleted_at of this InlineResponse2008.  # noqa: E501


        :return: The deleted_at of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this InlineResponse2008.


        :param deleted_at: The deleted_at of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and deleted_at is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def network_id(self):
        """Gets the network_id of this InlineResponse2008.  # noqa: E501


        :return: The network_id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this InlineResponse2008.


        :param network_id: The network_id of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and network_id is None:  # noqa: E501
            raise ValueError("Invalid value for `network_id`, must not be `None`")  # noqa: E501

        self._network_id = network_id

    @property
    def name(self):
        """Gets the name of this InlineResponse2008.  # noqa: E501


        :return: The name of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2008.


        :param name: The name of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineResponse2008.  # noqa: E501


        :return: The updated_at of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineResponse2008.


        :param updated_at: The updated_at of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def sync_id(self):
        """Gets the sync_id of this InlineResponse2008.  # noqa: E501


        :return: The sync_id of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._sync_id

    @sync_id.setter
    def sync_id(self, sync_id):
        """Sets the sync_id of this InlineResponse2008.


        :param sync_id: The sync_id of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and sync_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sync_id`, must not be `None`")  # noqa: E501

        self._sync_id = sync_id

    @property
    def session_identity_id(self):
        """Gets the session_identity_id of this InlineResponse2008.  # noqa: E501


        :return: The session_identity_id of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._session_identity_id

    @session_identity_id.setter
    def session_identity_id(self, session_identity_id):
        """Sets the session_identity_id of this InlineResponse2008.


        :param session_identity_id: The session_identity_id of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and session_identity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_identity_id`, must not be `None`")  # noqa: E501

        self._session_identity_id = session_identity_id

    @property
    def os_release(self):
        """Gets the os_release of this InlineResponse2008.  # noqa: E501


        :return: The os_release of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._os_release

    @os_release.setter
    def os_release(self, os_release):
        """Sets the os_release of this InlineResponse2008.


        :param os_release: The os_release of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and os_release is None:  # noqa: E501
            raise ValueError("Invalid value for `os_release`, must not be `None`")  # noqa: E501

        self._os_release = os_release

    @property
    def sync_resource_id(self):
        """Gets the sync_resource_id of this InlineResponse2008.  # noqa: E501


        :return: The sync_resource_id of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._sync_resource_id

    @sync_resource_id.setter
    def sync_resource_id(self, sync_resource_id):
        """Sets the sync_resource_id of this InlineResponse2008.


        :param sync_resource_id: The sync_resource_id of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and sync_resource_id is None:  # noqa: E501
            raise ValueError("Invalid value for `sync_resource_id`, must not be `None`")  # noqa: E501

        self._sync_resource_id = sync_resource_id

    @property
    def ziti_id(self):
        """Gets the ziti_id of this InlineResponse2008.  # noqa: E501


        :return: The ziti_id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._ziti_id

    @ziti_id.setter
    def ziti_id(self, ziti_id):
        """Sets the ziti_id of this InlineResponse2008.


        :param ziti_id: The ziti_id of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ziti_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ziti_id`, must not be `None`")  # noqa: E501

        self._ziti_id = ziti_id

    @property
    def app_version(self):
        """Gets the app_version of this InlineResponse2008.  # noqa: E501


        :return: The app_version of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this InlineResponse2008.


        :param app_version: The app_version of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and app_version is None:  # noqa: E501
            raise ValueError("Invalid value for `app_version`, must not be `None`")  # noqa: E501

        self._app_version = app_version

    @property
    def branch(self):
        """Gets the branch of this InlineResponse2008.  # noqa: E501


        :return: The branch of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this InlineResponse2008.


        :param branch: The branch of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and branch is None:  # noqa: E501
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501

        self._branch = branch

    @property
    def os(self):
        """Gets the os of this InlineResponse2008.  # noqa: E501


        :return: The os of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this InlineResponse2008.


        :param os: The os of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def owner_identity_id(self):
        """Gets the owner_identity_id of this InlineResponse2008.  # noqa: E501


        :return: The owner_identity_id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._owner_identity_id

    @owner_identity_id.setter
    def owner_identity_id(self, owner_identity_id):
        """Sets the owner_identity_id of this InlineResponse2008.


        :param owner_identity_id: The owner_identity_id of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and owner_identity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_identity_id`, must not be `None`")  # noqa: E501

        self._owner_identity_id = owner_identity_id

    @property
    def has_edge_router_connection(self):
        """Gets the has_edge_router_connection of this InlineResponse2008.  # noqa: E501


        :return: The has_edge_router_connection of this InlineResponse2008.  # noqa: E501
        :rtype: bool
        """
        return self._has_edge_router_connection

    @has_edge_router_connection.setter
    def has_edge_router_connection(self, has_edge_router_connection):
        """Sets the has_edge_router_connection of this InlineResponse2008.


        :param has_edge_router_connection: The has_edge_router_connection of this InlineResponse2008.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and has_edge_router_connection is None:  # noqa: E501
            raise ValueError("Invalid value for `has_edge_router_connection`, must not be `None`")  # noqa: E501

        self._has_edge_router_connection = has_edge_router_connection

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse2008.  # noqa: E501


        :return: The attributes of this InlineResponse2008.  # noqa: E501
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse2008.


        :param attributes: The attributes of this InlineResponse2008.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def has_api_session(self):
        """Gets the has_api_session of this InlineResponse2008.  # noqa: E501


        :return: The has_api_session of this InlineResponse2008.  # noqa: E501
        :rtype: bool
        """
        return self._has_api_session

    @has_api_session.setter
    def has_api_session(self, has_api_session):
        """Sets the has_api_session of this InlineResponse2008.


        :param has_api_session: The has_api_session of this InlineResponse2008.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and has_api_session is None:  # noqa: E501
            raise ValueError("Invalid value for `has_api_session`, must not be `None`")  # noqa: E501

        self._has_api_session = has_api_session

    @property
    def revision(self):
        """Gets the revision of this InlineResponse2008.  # noqa: E501


        :return: The revision of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this InlineResponse2008.


        :param revision: The revision of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def version(self):
        """Gets the version of this InlineResponse2008.  # noqa: E501


        :return: The version of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineResponse2008.


        :param version: The version of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def jwt(self):
        """Gets the jwt of this InlineResponse2008.  # noqa: E501


        :return: The jwt of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this InlineResponse2008.


        :param jwt: The jwt of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and jwt is None:  # noqa: E501
            raise ValueError("Invalid value for `jwt`, must not be `None`")  # noqa: E501

        self._jwt = jwt

    @property
    def id(self):
        """Gets the id of this InlineResponse2008.  # noqa: E501


        :return: The id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2008.


        :param id: The id of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def session_active(self):
        """Gets the session_active of this InlineResponse2008.  # noqa: E501


        :return: The session_active of this InlineResponse2008.  # noqa: E501
        :rtype: bool
        """
        return self._session_active

    @session_active.setter
    def session_active(self, session_active):
        """Sets the session_active of this InlineResponse2008.


        :param session_active: The session_active of this InlineResponse2008.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and session_active is None:  # noqa: E501
            raise ValueError("Invalid value for `session_active`, must not be `None`")  # noqa: E501

        self._session_active = session_active

    @property
    def jwt_expires_at(self):
        """Gets the jwt_expires_at of this InlineResponse2008.  # noqa: E501


        :return: The jwt_expires_at of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._jwt_expires_at

    @jwt_expires_at.setter
    def jwt_expires_at(self, jwt_expires_at):
        """Sets the jwt_expires_at of this InlineResponse2008.


        :param jwt_expires_at: The jwt_expires_at of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and jwt_expires_at is None:  # noqa: E501
            raise ValueError("Invalid value for `jwt_expires_at`, must not be `None`")  # noqa: E501

        self._jwt_expires_at = jwt_expires_at

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse2008.  # noqa: E501


        :return: The created_at of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse2008.


        :param created_at: The created_at of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def arch(self):
        """Gets the arch of this InlineResponse2008.  # noqa: E501


        :return: The arch of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this InlineResponse2008.


        :param arch: The arch of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and arch is None:  # noqa: E501
            raise ValueError("Invalid value for `arch`, must not be `None`")  # noqa: E501

        self._arch = arch

    @property
    def created_by(self):
        """Gets the created_by of this InlineResponse2008.  # noqa: E501


        :return: The created_by of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InlineResponse2008.


        :param created_by: The created_by of this InlineResponse2008.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def deleted_by(self):
        """Gets the deleted_by of this InlineResponse2008.  # noqa: E501


        :return: The deleted_by of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._deleted_by

    @deleted_by.setter
    def deleted_by(self, deleted_by):
        """Sets the deleted_by of this InlineResponse2008.


        :param deleted_by: The deleted_by of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and deleted_by is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_by`, must not be `None`")  # noqa: E501

        self._deleted_by = deleted_by

    @property
    def type(self):
        """Gets the type of this InlineResponse2008.  # noqa: E501


        :return: The type of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2008.


        :param type: The type of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def os_version(self):
        """Gets the os_version of this InlineResponse2008.  # noqa: E501


        :return: The os_version of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this InlineResponse2008.


        :param os_version: The os_version of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and os_version is None:  # noqa: E501
            raise ValueError("Invalid value for `os_version`, must not be `None`")  # noqa: E501

        self._os_version = os_version

    @property
    def app_id(self):
        """Gets the app_id of this InlineResponse2008.  # noqa: E501


        :return: The app_id of this InlineResponse2008.  # noqa: E501
        :rtype: object
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this InlineResponse2008.


        :param app_id: The app_id of this InlineResponse2008.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def links(self):
        """Gets the links of this InlineResponse2008.  # noqa: E501


        :return: The links of this InlineResponse2008.  # noqa: E501
        :rtype: InlineResponse200Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this InlineResponse2008.


        :param links: The links of this InlineResponse2008.  # noqa: E501
        :type: InlineResponse200Links
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
        if not isinstance(other, InlineResponse2008):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2008):
            return True

        return self.to_dict() != other.to_dict()
