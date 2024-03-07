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


class Cards(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            closed = schemas.StrSchema
            desc = schemas.StrSchema
            due = schemas.StrSchema
            fileSource = schemas.StrSchema
            idAttachmentCover = schemas.StrSchema
            idBoard = schemas.StrSchema
            idCardSource = schemas.StrSchema
            idLabels = schemas.StrSchema
            idList = schemas.StrSchema
            idMembers = schemas.StrSchema
            keepFromSource = schemas.StrSchema
            labels = schemas.StrSchema
            name = schemas.StrSchema
            pos = schemas.StrSchema
            subscribed = schemas.StrSchema
            urlSource = schemas.StrSchema
            __annotations__ = {
                "closed": closed,
                "desc": desc,
                "due": due,
                "fileSource": fileSource,
                "idAttachmentCover": idAttachmentCover,
                "idBoard": idBoard,
                "idCardSource": idCardSource,
                "idLabels": idLabels,
                "idList": idList,
                "idMembers": idMembers,
                "keepFromSource": keepFromSource,
                "labels": labels,
                "name": name,
                "pos": pos,
                "subscribed": subscribed,
                "urlSource": urlSource,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed"]) -> MetaOapg.properties.closed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desc"]) -> MetaOapg.properties.desc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due"]) -> MetaOapg.properties.due: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileSource"]) -> MetaOapg.properties.fileSource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idAttachmentCover"]) -> MetaOapg.properties.idAttachmentCover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idBoard"]) -> MetaOapg.properties.idBoard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idCardSource"]) -> MetaOapg.properties.idCardSource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idLabels"]) -> MetaOapg.properties.idLabels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idList"]) -> MetaOapg.properties.idList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idMembers"]) -> MetaOapg.properties.idMembers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keepFromSource"]) -> MetaOapg.properties.keepFromSource: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pos"]) -> MetaOapg.properties.pos: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscribed"]) -> MetaOapg.properties.subscribed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["urlSource"]) -> MetaOapg.properties.urlSource: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["closed", "desc", "due", "fileSource", "idAttachmentCover", "idBoard", "idCardSource", "idLabels", "idList", "idMembers", "keepFromSource", "labels", "name", "pos", "subscribed", "urlSource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed"]) -> typing.Union[MetaOapg.properties.closed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desc"]) -> typing.Union[MetaOapg.properties.desc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due"]) -> typing.Union[MetaOapg.properties.due, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileSource"]) -> typing.Union[MetaOapg.properties.fileSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idAttachmentCover"]) -> typing.Union[MetaOapg.properties.idAttachmentCover, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idBoard"]) -> typing.Union[MetaOapg.properties.idBoard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idCardSource"]) -> typing.Union[MetaOapg.properties.idCardSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idLabels"]) -> typing.Union[MetaOapg.properties.idLabels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idList"]) -> typing.Union[MetaOapg.properties.idList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idMembers"]) -> typing.Union[MetaOapg.properties.idMembers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keepFromSource"]) -> typing.Union[MetaOapg.properties.keepFromSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pos"]) -> typing.Union[MetaOapg.properties.pos, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscribed"]) -> typing.Union[MetaOapg.properties.subscribed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["urlSource"]) -> typing.Union[MetaOapg.properties.urlSource, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["closed", "desc", "due", "fileSource", "idAttachmentCover", "idBoard", "idCardSource", "idLabels", "idList", "idMembers", "keepFromSource", "labels", "name", "pos", "subscribed", "urlSource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        closed: typing.Union[MetaOapg.properties.closed, str, schemas.Unset] = schemas.unset,
        desc: typing.Union[MetaOapg.properties.desc, str, schemas.Unset] = schemas.unset,
        due: typing.Union[MetaOapg.properties.due, str, schemas.Unset] = schemas.unset,
        fileSource: typing.Union[MetaOapg.properties.fileSource, str, schemas.Unset] = schemas.unset,
        idAttachmentCover: typing.Union[MetaOapg.properties.idAttachmentCover, str, schemas.Unset] = schemas.unset,
        idBoard: typing.Union[MetaOapg.properties.idBoard, str, schemas.Unset] = schemas.unset,
        idCardSource: typing.Union[MetaOapg.properties.idCardSource, str, schemas.Unset] = schemas.unset,
        idLabels: typing.Union[MetaOapg.properties.idLabels, str, schemas.Unset] = schemas.unset,
        idList: typing.Union[MetaOapg.properties.idList, str, schemas.Unset] = schemas.unset,
        idMembers: typing.Union[MetaOapg.properties.idMembers, str, schemas.Unset] = schemas.unset,
        keepFromSource: typing.Union[MetaOapg.properties.keepFromSource, str, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        pos: typing.Union[MetaOapg.properties.pos, str, schemas.Unset] = schemas.unset,
        subscribed: typing.Union[MetaOapg.properties.subscribed, str, schemas.Unset] = schemas.unset,
        urlSource: typing.Union[MetaOapg.properties.urlSource, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Cards':
        return super().__new__(
            cls,
            *args,
            closed=closed,
            desc=desc,
            due=due,
            fileSource=fileSource,
            idAttachmentCover=idAttachmentCover,
            idBoard=idBoard,
            idCardSource=idCardSource,
            idLabels=idLabels,
            idList=idList,
            idMembers=idMembers,
            keepFromSource=keepFromSource,
            labels=labels,
            name=name,
            pos=pos,
            subscribed=subscribed,
            urlSource=urlSource,
            _configuration=_configuration,
            **kwargs,
        )
