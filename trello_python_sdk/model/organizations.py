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


class Organizations(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            desc = schemas.StrSchema
            displayName = schemas.StrSchema
            name = schemas.StrSchema
            prefs_associated_domain = schemas.StrSchema
            prefs_board_visibility_restrict_org = schemas.StrSchema
            prefs_board_visibility_restrict_private = schemas.StrSchema
            prefs_board_visibility_restrict_public = schemas.StrSchema
            prefs_external_members_disabled = schemas.StrSchema
            prefs_google_apps_version = schemas.StrSchema
            prefs_org_invite_restrict = schemas.StrSchema
            prefs_permission_level = schemas.StrSchema
            website = schemas.StrSchema
            __annotations__ = {
                "desc": desc,
                "displayName": displayName,
                "name": name,
                "prefs/associatedDomain": prefs_associated_domain,
                "prefs/boardVisibilityRestrict/org": prefs_board_visibility_restrict_org,
                "prefs/boardVisibilityRestrict/private": prefs_board_visibility_restrict_private,
                "prefs/boardVisibilityRestrict/public": prefs_board_visibility_restrict_public,
                "prefs/externalMembersDisabled": prefs_external_members_disabled,
                "prefs/googleAppsVersion": prefs_google_apps_version,
                "prefs/orgInviteRestrict": prefs_org_invite_restrict,
                "prefs/permissionLevel": prefs_permission_level,
                "website": website,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["desc"]) -> MetaOapg.properties.desc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/associatedDomain"]) -> MetaOapg.properties.prefs_associated_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/boardVisibilityRestrict/org"]) -> MetaOapg.properties.prefs_board_visibility_restrict_org: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/boardVisibilityRestrict/private"]) -> MetaOapg.properties.prefs_board_visibility_restrict_private: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/boardVisibilityRestrict/public"]) -> MetaOapg.properties.prefs_board_visibility_restrict_public: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/externalMembersDisabled"]) -> MetaOapg.properties.prefs_external_members_disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/googleAppsVersion"]) -> MetaOapg.properties.prefs_google_apps_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/orgInviteRestrict"]) -> MetaOapg.properties.prefs_org_invite_restrict: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prefs/permissionLevel"]) -> MetaOapg.properties.prefs_permission_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["desc", "displayName", "name", "prefs/associatedDomain", "prefs/boardVisibilityRestrict/org", "prefs/boardVisibilityRestrict/private", "prefs/boardVisibilityRestrict/public", "prefs/externalMembersDisabled", "prefs/googleAppsVersion", "prefs/orgInviteRestrict", "prefs/permissionLevel", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["desc"]) -> typing.Union[MetaOapg.properties.desc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/associatedDomain"]) -> typing.Union[MetaOapg.properties.prefs_associated_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/boardVisibilityRestrict/org"]) -> typing.Union[MetaOapg.properties.prefs_board_visibility_restrict_org, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/boardVisibilityRestrict/private"]) -> typing.Union[MetaOapg.properties.prefs_board_visibility_restrict_private, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/boardVisibilityRestrict/public"]) -> typing.Union[MetaOapg.properties.prefs_board_visibility_restrict_public, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/externalMembersDisabled"]) -> typing.Union[MetaOapg.properties.prefs_external_members_disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/googleAppsVersion"]) -> typing.Union[MetaOapg.properties.prefs_google_apps_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/orgInviteRestrict"]) -> typing.Union[MetaOapg.properties.prefs_org_invite_restrict, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prefs/permissionLevel"]) -> typing.Union[MetaOapg.properties.prefs_permission_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["desc", "displayName", "name", "prefs/associatedDomain", "prefs/boardVisibilityRestrict/org", "prefs/boardVisibilityRestrict/private", "prefs/boardVisibilityRestrict/public", "prefs/externalMembersDisabled", "prefs/googleAppsVersion", "prefs/orgInviteRestrict", "prefs/permissionLevel", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        desc: typing.Union[MetaOapg.properties.desc, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Organizations':
        return super().__new__(
            cls,
            *args,
            desc=desc,
            displayName=displayName,
            name=name,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )
