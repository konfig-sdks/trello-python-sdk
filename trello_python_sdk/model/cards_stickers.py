# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from trello_python_sdk import schemas  # noqa: F401


class CardsStickers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            image = schemas.StrSchema
            left = schemas.StrSchema
            rotate = schemas.StrSchema
            top = schemas.StrSchema
            zIndex = schemas.StrSchema
            __annotations__ = {
                "image": image,
                "left": left,
                "rotate": rotate,
                "top": top,
                "zIndex": zIndex,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["left"]) -> MetaOapg.properties.left: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rotate"]) -> MetaOapg.properties.rotate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["top"]) -> MetaOapg.properties.top: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zIndex"]) -> MetaOapg.properties.zIndex: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["image", "left", "rotate", "top", "zIndex", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["left"]) -> typing.Union[MetaOapg.properties.left, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rotate"]) -> typing.Union[MetaOapg.properties.rotate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["top"]) -> typing.Union[MetaOapg.properties.top, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zIndex"]) -> typing.Union[MetaOapg.properties.zIndex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["image", "left", "rotate", "top", "zIndex", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        left: typing.Union[MetaOapg.properties.left, str, schemas.Unset] = schemas.unset,
        rotate: typing.Union[MetaOapg.properties.rotate, str, schemas.Unset] = schemas.unset,
        top: typing.Union[MetaOapg.properties.top, str, schemas.Unset] = schemas.unset,
        zIndex: typing.Union[MetaOapg.properties.zIndex, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardsStickers':
        return super().__new__(
            cls,
            *args,
            image=image,
            left=left,
            rotate=rotate,
            top=top,
            zIndex=zIndex,
            _configuration=_configuration,
            **kwargs,
        )