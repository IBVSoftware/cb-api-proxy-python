# IBVCLServiceMetaEntitiesResponsesPublicCommonProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **int** |  | [optional] 
**container_uri** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**created_by_user** | **str** |  | [optional] 
**created_by_unique_machine_id** | **str** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**updated_by_user** | **str** |  | [optional] 
**last_update** | **datetime** |  | [optional] 
**zoom_factor** | **float** |  | [optional] 
**offset_x** | **float** |  | [optional] 
**offset_y** | **float** |  | [optional] 
**presenter** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_project import IBVCLServiceMetaEntitiesResponsesPublicCommonProject

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonProject from a JSON string
ibvcl_service_meta_entities_responses_public_common_project_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonProject.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonProject.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_project_dict = ibvcl_service_meta_entities_responses_public_common_project_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonProject from a dict
ibvcl_service_meta_entities_responses_public_common_project_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonProject.from_dict(ibvcl_service_meta_entities_responses_public_common_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


