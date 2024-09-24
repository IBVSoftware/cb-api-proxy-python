# IBVCLServiceMetaEntitiesTileStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**tile_id** | **str** |  | [optional] 
**old_tile_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**type_tile** | [**IBVCLServiceMetaEntitiesTileType**](IBVCLServiceMetaEntitiesTileType.md) |  | [optional] 
**tile_content** | [**IBVCLServiceMetaEntitiesITileContent**](IBVCLServiceMetaEntitiesITileContent.md) |  | [optional] 
**position_x** | **float** |  | [optional] 
**position_y** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**z_index** | **int** |  | [optional] 
**scale_x** | **float** |  | [optional] 
**scale_y** | **float** |  | [optional] 
**rotation** | **float** |  | [optional] 
**locked_user** | **str** |  | [optional] 
**pinned_state** | [**IBVCLServiceMetaEntitiesTilePinnedStateEnum**](IBVCLServiceMetaEntitiesTilePinnedStateEnum.md) |  | [optional] 
**background_color** | **str** |  | [optional] 
**total_thumb_up** | **int** |  | [optional] 
**total_thumb_down** | **int** |  | [optional] 
**overall_rating** | **float** |  | [optional] 
**total_rates** | **int** |  | [optional] 
**azure_blob_status** | [**IBVCLServiceMetaEntitiesTileBlobStatus**](IBVCLServiceMetaEntitiesTileBlobStatus.md) |  | [optional] 
**original_file_name** | **str** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**booked_by** | **str** |  | [optional] 
**booking_date** | **datetime** |  | [optional] 
**retry** | **int** |  | [optional] 
**state_m_status** | [**IBVCLServiceMetaEntitiesStateMachineStatus**](IBVCLServiceMetaEntitiesStateMachineStatus.md) |  | [optional] 
**locked_by** | **str** |  | [optional] 
**locked_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.ibvcl_service_meta_entities_tile_status import IBVCLServiceMetaEntitiesTileStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IBVCLServiceMetaEntitiesTileStatus from a JSON string
ibvcl_service_meta_entities_tile_status_instance = IBVCLServiceMetaEntitiesTileStatus.from_json(json)
# print the JSON string representation of the object
print(IBVCLServiceMetaEntitiesTileStatus.to_json())

# convert the object into a dict
ibvcl_service_meta_entities_tile_status_dict = ibvcl_service_meta_entities_tile_status_instance.to_dict()
# create an instance of IBVCLServiceMetaEntitiesTileStatus from a dict
ibvcl_service_meta_entities_tile_status_from_dict = IBVCLServiceMetaEntitiesTileStatus.from_dict(ibvcl_service_meta_entities_tile_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


