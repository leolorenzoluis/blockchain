# coding: utf-8

"""
    Azure Blockchain Workbench REST API

    The Azure Blockchain Workbench REST API is a Workbench extensibility point, which allows developers to create and manage blockchain applications, manage users and organizations within a consortium, integrate blockchain applications into services and platforms, perform transactions on a blockchain, and retrieve transactional and contract data from a blockchain.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.checkers_api import CheckersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCheckersApi(unittest.TestCase):
    """CheckersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.checkers_api.CheckersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_application_post(self):
        """Test case for check_application_post

        Check validity of application configuration for Workbench  # noqa: E501
        """
        pass

    def test_check_contract_code_post(self):
        """Test case for check_contract_code_post

        Check validity of application ledger implementation for Workbench  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()