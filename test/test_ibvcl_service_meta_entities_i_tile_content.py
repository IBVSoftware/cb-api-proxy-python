# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ibvcl_service_meta_entities_i_tile_content import IBVCLServiceMetaEntitiesITileContent

class TestIBVCLServiceMetaEntitiesITileContent(unittest.TestCase):
    """IBVCLServiceMetaEntitiesITileContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IBVCLServiceMetaEntitiesITileContent:
        """Test IBVCLServiceMetaEntitiesITileContent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IBVCLServiceMetaEntitiesITileContent`
        """
        model = IBVCLServiceMetaEntitiesITileContent()
        if include_optional:
            return IBVCLServiceMetaEntitiesITileContent(
                j_son_type = ''
            )
        else:
            return IBVCLServiceMetaEntitiesITileContent(
        )
        """

    def testIBVCLServiceMetaEntitiesITileContent(self):
        """Test IBVCLServiceMetaEntitiesITileContent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
