# coding: utf-8

"""
    Mock Server API

    MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS with clients written in Java, JavaScript and Ruby and a simple REST API (as shown below).  MockServer Proxy is a proxy that introspects all proxied traffic including encrypted SSL traffic and supports Port Forwarding, Web Proxying (i.e. HTTP proxy), HTTPS Tunneling Proxying (using HTTP CONNECT) and SOCKS Proxying (i.e. dynamic port forwarding).  Both MockServer and the MockServer Proxy record all received requests so that it is possible to verify exactly what requests have been sent by the system under test.  # noqa: E501

    OpenAPI spec version: 5.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class VerificationSequence(object):
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
        'http_requests': 'list[HttpRequest]'
    }

    attribute_map = {
        'http_requests': 'httpRequests'
    }

    def __init__(self, http_requests=None):  # noqa: E501
        """VerificationSequence - a model defined in OpenAPI"""  # noqa: E501

        self._http_requests = None
        self.discriminator = None

        if http_requests is not None:
            self.http_requests = http_requests

    @property
    def http_requests(self):
        """Gets the http_requests of this VerificationSequence.  # noqa: E501


        :return: The http_requests of this VerificationSequence.  # noqa: E501
        :rtype: list[HttpRequest]
        """
        return self._http_requests

    @http_requests.setter
    def http_requests(self, http_requests):
        """Sets the http_requests of this VerificationSequence.


        :param http_requests: The http_requests of this VerificationSequence.  # noqa: E501
        :type: list[HttpRequest]
        """

        self._http_requests = http_requests

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
        if not isinstance(other, VerificationSequence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
