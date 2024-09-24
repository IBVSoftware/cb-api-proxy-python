# IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**authorization_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result_dict = ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult from a dict
ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult.from_dict(ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


