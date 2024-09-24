# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request import IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest

class TestIBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest(unittest.TestCase):
    """IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest:
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest`
        """
        model = IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest()
        if include_optional:
            return IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest(
                unique_device_id = '',
                username = '',
                status = 56,
                permission = 56
            )
        else:
            return IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest(
        )
        """

    def testIBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest(self):
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
