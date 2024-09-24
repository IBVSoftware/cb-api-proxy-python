# IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 
**results** | [**List[IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsItem]**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result_dict = ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult from a dict
ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult.from_dict(ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


