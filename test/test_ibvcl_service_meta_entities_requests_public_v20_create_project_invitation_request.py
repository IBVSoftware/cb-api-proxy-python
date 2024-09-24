# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest

class TestIBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest(unittest.TestCase):
    """IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest:
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest`
        """
        model = IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest()
        if include_optional:
            return IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest(
                unique_device_id = '',
                email = '',
                notes = '',
                member_permission = 0,
                guest_permission = 0,
                invitation_url = '',
                valid_for_minutes = 56,
                password = '',
                guest_identification_required = True,
                message_theme = ''
            )
        else:
            return IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest(
        )
        """

    def testIBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest(self):
        """Test IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
