# coding: utf-8

"""
    Edge-API

    The Edge-API is built under the BIND5G project and its purpose is to act as an intermidiator between the NaaS API and the Kubernetes cluster. The NaaS API is a general API in respect of the project to remotely and automatically deploy, manage and control 5G and MEC infrastructures for a vast amount of experiments. On the other hand, the Edge-API is a specific backend API to manage Kubernetes resources and deploy application instances into the cluster.  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: mdalgitsis@vicomtech.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.scale_vertical import ScaleVertical  # noqa: E501
from swagger_client.rest import ApiException


class TestScaleVertical(unittest.TestCase):
    """ScaleVertical unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScaleVertical(self):
        """Test ScaleVertical"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.scale_vertical.ScaleVertical()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
