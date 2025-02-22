# coding: utf-8

"""
    Collaboard Public Web API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.ibvcl_service_meta_entities_i_tile_content import IBVCLServiceMetaEntitiesITileContent
from openapi_client.models.ibvcl_service_meta_entities_state_machine_status import IBVCLServiceMetaEntitiesStateMachineStatus
from openapi_client.models.ibvcl_service_meta_entities_tile_blob_status import IBVCLServiceMetaEntitiesTileBlobStatus
from openapi_client.models.ibvcl_service_meta_entities_tile_pinned_state_enum import IBVCLServiceMetaEntitiesTilePinnedStateEnum
from openapi_client.models.ibvcl_service_meta_entities_tile_type import IBVCLServiceMetaEntitiesTileType
from typing import Optional, Set
from typing_extensions import Self

class IBVCLServiceMetaEntitiesTileStatus(BaseModel):
    """
    IBVCLServiceMetaEntitiesTileStatus
    """ # noqa: E501
    project_id: Optional[StrictInt] = Field(default=None, alias="projectId")
    tile_id: Optional[StrictStr] = Field(default=None, alias="tileId")
    old_tile_id: Optional[StrictStr] = Field(default=None, alias="oldTileId")
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    type_tile: Optional[IBVCLServiceMetaEntitiesTileType] = Field(default=None, alias="typeTile")
    tile_content: Optional[IBVCLServiceMetaEntitiesITileContent] = Field(default=None, alias="tileContent")
    position_x: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="positionX")
    position_y: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="positionY")
    height: Optional[Union[StrictFloat, StrictInt]] = None
    width: Optional[Union[StrictFloat, StrictInt]] = None
    z_index: Optional[StrictInt] = Field(default=None, alias="zIndex")
    scale_x: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="scaleX")
    scale_y: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="scaleY")
    rotation: Optional[Union[StrictFloat, StrictInt]] = None
    locked_user: Optional[StrictStr] = Field(default=None, alias="lockedUser")
    pinned_state: Optional[IBVCLServiceMetaEntitiesTilePinnedStateEnum] = Field(default=None, alias="pinnedState")
    background_color: Optional[StrictStr] = Field(default=None, alias="backgroundColor")
    total_thumb_up: Optional[StrictInt] = Field(default=None, alias="totalThumbUp")
    total_thumb_down: Optional[StrictInt] = Field(default=None, alias="totalThumbDown")
    overall_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="overallRating")
    total_rates: Optional[StrictInt] = Field(default=None, alias="totalRates")
    azure_blob_status: Optional[IBVCLServiceMetaEntitiesTileBlobStatus] = Field(default=None, alias="azureBlobStatus")
    original_file_name: Optional[StrictStr] = Field(default=None, alias="originalFileName")
    is_hidden: Optional[StrictBool] = Field(default=None, alias="isHidden")
    is_deleted: Optional[StrictBool] = Field(default=None, alias="isDeleted")
    booked_by: Optional[StrictStr] = Field(default=None, alias="bookedBy")
    booking_date: Optional[datetime] = Field(default=None, alias="bookingDate")
    retry: Optional[StrictInt] = None
    state_m_status: Optional[IBVCLServiceMetaEntitiesStateMachineStatus] = Field(default=None, alias="stateMStatus")
    locked_by: Optional[StrictStr] = Field(default=None, alias="lockedBy")
    locked_date: Optional[datetime] = Field(default=None, alias="lockedDate")
    __properties: ClassVar[List[str]] = ["projectId", "tileId", "oldTileId", "parentId", "typeTile", "tileContent", "positionX", "positionY", "height", "width", "zIndex", "scaleX", "scaleY", "rotation", "lockedUser", "pinnedState", "backgroundColor", "totalThumbUp", "totalThumbDown", "overallRating", "totalRates", "azureBlobStatus", "originalFileName", "isHidden", "isDeleted", "bookedBy", "bookingDate", "retry", "stateMStatus", "lockedBy", "lockedDate"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IBVCLServiceMetaEntitiesTileStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tile_content
        if self.tile_content:
            _dict['tileContent'] = self.tile_content.to_dict()
        # set to None if locked_user (nullable) is None
        # and model_fields_set contains the field
        if self.locked_user is None and "locked_user" in self.model_fields_set:
            _dict['lockedUser'] = None

        # set to None if background_color (nullable) is None
        # and model_fields_set contains the field
        if self.background_color is None and "background_color" in self.model_fields_set:
            _dict['backgroundColor'] = None

        # set to None if original_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.original_file_name is None and "original_file_name" in self.model_fields_set:
            _dict['originalFileName'] = None

        # set to None if locked_by (nullable) is None
        # and model_fields_set contains the field
        if self.locked_by is None and "locked_by" in self.model_fields_set:
            _dict['lockedBy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IBVCLServiceMetaEntitiesTileStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projectId": obj.get("projectId"),
            "tileId": obj.get("tileId"),
            "oldTileId": obj.get("oldTileId"),
            "parentId": obj.get("parentId"),
            "typeTile": obj.get("typeTile"),
            "tileContent": IBVCLServiceMetaEntitiesITileContent.from_dict(obj["tileContent"]) if obj.get("tileContent") is not None else None,
            "positionX": obj.get("positionX"),
            "positionY": obj.get("positionY"),
            "height": obj.get("height"),
            "width": obj.get("width"),
            "zIndex": obj.get("zIndex"),
            "scaleX": obj.get("scaleX"),
            "scaleY": obj.get("scaleY"),
            "rotation": obj.get("rotation"),
            "lockedUser": obj.get("lockedUser"),
            "pinnedState": obj.get("pinnedState"),
            "backgroundColor": obj.get("backgroundColor"),
            "totalThumbUp": obj.get("totalThumbUp"),
            "totalThumbDown": obj.get("totalThumbDown"),
            "overallRating": obj.get("overallRating"),
            "totalRates": obj.get("totalRates"),
            "azureBlobStatus": obj.get("azureBlobStatus"),
            "originalFileName": obj.get("originalFileName"),
            "isHidden": obj.get("isHidden"),
            "isDeleted": obj.get("isDeleted"),
            "bookedBy": obj.get("bookedBy"),
            "bookingDate": obj.get("bookingDate"),
            "retry": obj.get("retry"),
            "stateMStatus": obj.get("stateMStatus"),
            "lockedBy": obj.get("lockedBy"),
            "lockedDate": obj.get("lockedDate")
        })
        return _obj


