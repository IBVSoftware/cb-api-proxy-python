# IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_device_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**permission** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request import IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest from a JSON string
ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request_instance = IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request_dict = ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest from a dict
ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request_from_dict = IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest.from_dict(ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


