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


class CardsAttachments(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            file = schemas.StrSchema
            mimeType = schemas.StrSchema
            name = schemas.StrSchema
            url = schemas.StrSchema
            __annotations__ = {
                "file": file,
                "mimeType": mimeType,
                "name": name,
                "url": url,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mimeType"]) -> MetaOapg.properties.mimeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file", "mimeType", "name", "url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> typing.Union[MetaOapg.properties.file, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mimeType"]) -> typing.Union[MetaOapg.properties.mimeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file", "mimeType", "name", "url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file: typing.Union[MetaOapg.properties.file, str, schemas.Unset] = schemas.unset,
        mimeType: typing.Union[MetaOapg.properties.mimeType, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardsAttachments':
        return super().__new__(
            cls,
            *args,
            file=file,
            mimeType=mimeType,
            name=name,
            url=url,
            _configuration=_configuration,
            **kwargs,
        )
