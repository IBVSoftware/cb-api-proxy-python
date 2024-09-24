# IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_device_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**background_color** | **str** |  | [optional] 
**is_activity_log_enabled** | **bool** |  | [optional] 
**is_versioning_enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest from a JSON string
ibvcl_service_meta_entities_requests_public_v20_create_project_request_instance = IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_requests_public_v20_create_project_request_dict = ibvcl_service_meta_entities_requests_public_v20_create_project_request_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest from a dict
ibvcl_service_meta_entities_requests_public_v20_create_project_request_from_dict = IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest.from_dict(ibvcl_service_meta_entities_requests_public_v20_create_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


