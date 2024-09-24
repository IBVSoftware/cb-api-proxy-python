# IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**product_id** | **int** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**number_of_owned_projects** | **int** |  | [optional] 
**has_pending_subscription_invitation** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result_dict = ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult from a dict
ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult.from_dict(ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


