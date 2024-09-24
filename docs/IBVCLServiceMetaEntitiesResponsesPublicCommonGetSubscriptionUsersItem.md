# IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**status** | [**IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserStatusEnum**](IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserStatusEnum.md) |  | [optional] 
**permission** | [**IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserPermissionEnum**](IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserPermissionEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_subscription_users_item import IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem from a JSON string
ibvcl_service_meta_entities_responses_public_common_get_subscription_users_item_instance = IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_responses_public_common_get_subscription_users_item_dict = ibvcl_service_meta_entities_responses_public_common_get_subscription_users_item_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem from a dict
ibvcl_service_meta_entities_responses_public_common_get_subscription_users_item_from_dict = IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem.from_dict(ibvcl_service_meta_entities_responses_public_common_get_subscription_users_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


