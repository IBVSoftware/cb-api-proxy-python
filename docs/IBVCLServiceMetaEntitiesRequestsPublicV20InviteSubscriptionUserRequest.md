# IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_device_id** | **str** |  | [optional] 
**invitation_accept_url** | **str** |  | [optional] 
**invitation_reject_url** | **str** |  | [optional] 
**message_theme** | **str** |  | [optional] 
**user** | [**IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserItem**](IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request import IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest from a JSON string
ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request_instance = IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request_dict = ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest from a dict
ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request_from_dict = IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest.from_dict(ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


