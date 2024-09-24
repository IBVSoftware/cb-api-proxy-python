# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request import IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest

class TestIBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest(unittest.TestCase):
    """IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest:
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest`
        """
        model = IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest()
        if include_optional:
            return IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest(
                unique_device_id = '',
                username = '',
                permission = 0
            )
        else:
            return IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest(
        )
        """

    def testIBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest(self):
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
