# IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**result** | [**IBVCLServiceMetaEntitiesAuthenticatedUserExt**](IBVCLServiceMetaEntitiesAuthenticatedUserExt.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result_dict = ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult from a dict
ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult.from_dict(ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


