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


class HttpForward(object):
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
        'host': 'str',
        'port': 'int',
        'scheme': 'str',
        'delay': 'Delay'
    }

    attribute_map = {
        'host': 'host',
        'port': 'port',
        'scheme': 'scheme',
        'delay': 'delay'
    }

    def __init__(self, host=None, port=None, scheme=None, delay=None):  # noqa: E501
        """HttpForward - a model defined in OpenAPI"""  # noqa: E501

        self._host = None
        self._port = None
        self._scheme = None
        self._delay = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if scheme is not None:
            self.scheme = scheme
        if delay is not None:
            self.delay = delay

    @property
    def host(self):
        """Gets the host of this HttpForward.  # noqa: E501


        :return: The host of this HttpForward.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HttpForward.


        :param host: The host of this HttpForward.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this HttpForward.  # noqa: E501


        :return: The port of this HttpForward.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HttpForward.


        :param port: The port of this HttpForward.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def scheme(self):
        """Gets the scheme of this HttpForward.  # noqa: E501


        :return: The scheme of this HttpForward.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this HttpForward.


        :param scheme: The scheme of this HttpForward.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS"]  # noqa: E501
        if scheme not in allowed_values:
            raise ValueError(
                "Invalid value for `scheme` ({0}), must be one of {1}"  # noqa: E501
                .format(scheme, allowed_values)
            )

        self._scheme = scheme

    @property
    def delay(self):
        """Gets the delay of this HttpForward.  # noqa: E501


        :return: The delay of this HttpForward.  # noqa: E501
        :rtype: Delay
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this HttpForward.


        :param delay: The delay of this HttpForward.  # noqa: E501
        :type: Delay
        """

        self._delay = delay

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
        if not isinstance(other, HttpForward):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other