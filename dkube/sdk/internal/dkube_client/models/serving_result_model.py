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


class ServingResultModel(object):
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
        'modeldir': 'str',
        'servingurl': 'str'
    }

    attribute_map = {
        'modeldir': 'modeldir',
        'servingurl': 'servingurl'
    }

    def __init__(self, modeldir=None, servingurl=None):  # noqa: E501
        """ServingResultModel - a model defined in Swagger"""  # noqa: E501

        self._modeldir = None
        self._servingurl = None
        self.discriminator = None

        if modeldir is not None:
            self.modeldir = modeldir
        if servingurl is not None:
            self.servingurl = servingurl

    @property
    def modeldir(self):
        """Gets the modeldir of this ServingResultModel.  # noqa: E501

        Name of dir where the artificats of this model are stored  # noqa: E501

        :return: The modeldir of this ServingResultModel.  # noqa: E501
        :rtype: str
        """
        return self._modeldir

    @modeldir.setter
    def modeldir(self, modeldir):
        """Sets the modeldir of this ServingResultModel.

        Name of dir where the artificats of this model are stored  # noqa: E501

        :param modeldir: The modeldir of this ServingResultModel.  # noqa: E501
        :type: str
        """

        self._modeldir = modeldir

    @property
    def servingurl(self):
        """Gets the servingurl of this ServingResultModel.  # noqa: E501


        :return: The servingurl of this ServingResultModel.  # noqa: E501
        :rtype: str
        """
        return self._servingurl

    @servingurl.setter
    def servingurl(self, servingurl):
        """Sets the servingurl of this ServingResultModel.


        :param servingurl: The servingurl of this ServingResultModel.  # noqa: E501
        :type: str
        """

        self._servingurl = servingurl

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
        if issubclass(ServingResultModel, dict):
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
        if not isinstance(other, ServingResultModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
