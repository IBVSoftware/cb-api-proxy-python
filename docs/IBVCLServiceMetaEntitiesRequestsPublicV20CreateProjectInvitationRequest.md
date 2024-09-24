# IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_device_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**member_permission** | [**IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum**](IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum.md) |  | [optional] 
**guest_permission** | [**IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum**](IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum.md) |  | [optional] 
**invitation_url** | **str** |  | [optional] 
**valid_for_minutes** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**guest_identification_required** | **bool** |  | [optional] 
**message_theme** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest from a JSON string
ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request_instance = IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request_dict = ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest from a dict
ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request_from_dict = IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest.from_dict(ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


