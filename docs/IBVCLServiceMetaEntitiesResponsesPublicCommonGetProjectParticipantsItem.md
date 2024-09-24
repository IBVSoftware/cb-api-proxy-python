# IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**IBVCLServiceMetaEntitiesAuthenticatedUser**](IBVCLServiceMetaEntitiesAuthenticatedUser.md) |  | [optional] 
**permission** | [**IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum**](IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum.md) |  | [optional] 
**participation_type** | [**IBVCLServiceMetaEntitiesProjectParticipationTypeEnum**](IBVCLServiceMetaEntitiesProjectParticipationTypeEnum.md) |  | [optional] 
**last_access_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_project_participants_item import IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_project_participants_item_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_project_participants_item_dict = ibvcl_service_meta_entities_responses_public_common_get_project_participants_item_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem from a dict
ibvcl_service_meta_entities_responses_public_common_get_project_participants_item_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem.from_dict(ibvcl_service_meta_entities_responses_public_common_get_project_participants_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


