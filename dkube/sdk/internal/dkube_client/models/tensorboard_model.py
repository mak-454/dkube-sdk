# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TensorboardModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version': 'str',
        'uuid': 'str',
        'url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'version': 'version',
        'uuid': 'uuid',
        'url': 'url',
        'status': 'status'
    }

    def __init__(self, version=None, uuid=None, url=None, status=None):  # noqa: E501
        """TensorboardModel - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._uuid = None
        self._url = None
        self._status = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if uuid is not None:
            self.uuid = uuid
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status

    @property
    def version(self):
        """Gets the version of this TensorboardModel.  # noqa: E501


        :return: The version of this TensorboardModel.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TensorboardModel.


        :param version: The version of this TensorboardModel.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def uuid(self):
        """Gets the uuid of this TensorboardModel.  # noqa: E501


        :return: The uuid of this TensorboardModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this TensorboardModel.


        :param uuid: The uuid of this TensorboardModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def url(self):
        """Gets the url of this TensorboardModel.  # noqa: E501


        :return: The url of this TensorboardModel.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TensorboardModel.


        :param url: The url of this TensorboardModel.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this TensorboardModel.  # noqa: E501


        :return: The status of this TensorboardModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TensorboardModel.


        :param status: The status of this TensorboardModel.  # noqa: E501
        :type: str
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TensorboardModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TensorboardModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other