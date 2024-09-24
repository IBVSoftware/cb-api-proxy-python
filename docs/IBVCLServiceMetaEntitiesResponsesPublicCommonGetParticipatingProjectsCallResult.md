# IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 
**results** | [**List[IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem]**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result_dict = ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult from a dict
ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult.from_dict(ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


