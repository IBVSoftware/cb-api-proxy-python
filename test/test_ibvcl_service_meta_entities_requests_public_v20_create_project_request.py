# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest

class TestIBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest(unittest.TestCase):
    """IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest:
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest`
        """
        model = IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest()
        if include_optional:
            return IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest(
                unique_device_id = '',
                description = '',
                background_color = '',
                is_activity_log_enabled = True,
                is_versioning_enabled = True
            )
        else:
            return IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest(
        )
        """

    def testIBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest(self):
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
