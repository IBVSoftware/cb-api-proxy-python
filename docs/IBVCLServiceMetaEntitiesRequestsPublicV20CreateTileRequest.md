# IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_device_id** | **str** |  | [optional] 
**tile** | [**IBVCLServiceMetaEntitiesTileStatus**](IBVCLServiceMetaEntitiesTileStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_tile_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest from a JSON string
ibvcl_service_meta_entities_requests_public_v20_create_tile_request_instance = IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_requests_public_v20_create_tile_request_dict = ibvcl_service_meta_entities_requests_public_v20_create_tile_request_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest from a dict
ibvcl_service_meta_entities_requests_public_v20_create_tile_request_from_dict = IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest.from_dict(ibvcl_service_meta_entities_requests_public_v20_create_tile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


