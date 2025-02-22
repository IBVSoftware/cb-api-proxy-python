# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_copy_project_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult

class TestIBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult(unittest.TestCase):
    """IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult:
        """Test IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult`
        """
        model = IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult()
        if include_optional:
            return IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult(
                error_code = 56,
                operation_id = 56,
                project_id = 56,
                status = 0
            )
        else:
            return IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult(
        )
        """

    def testIBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult(self):
        """Test IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
