# IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**IBVCLServiceMetaEntitiesResponsesPublicCommonProject**](IBVCLServiceMetaEntitiesResponsesPublicCommonProject.md) |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**permission** | [**IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum**](IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum.md) |  | [optional] 
**is_licensed** | **bool** |  | [optional] 
**last_access_date** | **datetime** |  | [optional] 
**number_of_participants** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_participating_projects_item import IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_participating_projects_item_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_participating_projects_item_dict = ibvcl_service_meta_entities_responses_public_common_get_participating_projects_item_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem from a dict
ibvcl_service_meta_entities_responses_public_common_get_participating_projects_item_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem.from_dict(ibvcl_service_meta_entities_responses_public_common_get_participating_projects_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


