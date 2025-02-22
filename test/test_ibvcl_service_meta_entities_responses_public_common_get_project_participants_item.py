# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_project_participants_item import IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem

class TestIBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem(unittest.TestCase):
    """IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem:
        """Test IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem`
        """
        model = IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem()
        if include_optional:
            return IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem(
                user = openapi_client.models.ibv/cl_service/meta_entities/authenticated_user.IBV.CLService.MetaEntities.AuthenticatedUser(
                    date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    date_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    date_last_activity = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                permission = 0,
                participation_type = 0,
                last_access_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem(
        )
        """

    def testIBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem(self):
        """Test IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
