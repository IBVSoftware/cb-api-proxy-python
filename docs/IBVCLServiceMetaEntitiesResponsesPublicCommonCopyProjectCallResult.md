# IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**operation_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**status** | [**IBVCLServiceMetaEntitiesStateMachineStatus**](IBVCLServiceMetaEntitiesStateMachineStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_copy_project_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult from a JSON string
ibvcl_service_meta_entities_responses_public_common_copy_project_call_result_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_copy_project_call_result_dict = ibvcl_service_meta_entities_responses_public_common_copy_project_call_result_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult from a dict
ibvcl_service_meta_entities_responses_public_common_copy_project_call_result_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult.from_dict(ibvcl_service_meta_entities_responses_public_common_copy_project_call_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


