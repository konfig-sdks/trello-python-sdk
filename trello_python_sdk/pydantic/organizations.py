# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class Organizations(BaseModel):
    # a string with a length from 0 to 16384
    desc: typing.Optional[str] = Field(None, alias='desc')

    # A string with a length of at least 1.  Cannot begin or end with a space.
    display_name: typing.Optional[str] = Field(None, alias='displayName')

    # a string with a length from 0 to 16384
    name: typing.Optional[str] = Field(None, alias='name')

    # The google apps domain to link this org to.
    prefs/associated_domain_: typing.Optional[str] = Field(None, alias='prefs/associatedDomain')

    # One of: admin, none or org
    prefs/board_visibility_restrict/org_: typing.Optional[str] = Field(None, alias='prefs/boardVisibilityRestrict/org')

    # One of: admin, none or org
    prefs/board_visibility_restrict/private_: typing.Optional[str] = Field(None, alias='prefs/boardVisibilityRestrict/private')

    # One of: admin, none or org
    prefs/board_visibility_restrict/public_: typing.Optional[str] = Field(None, alias='prefs/boardVisibilityRestrict/public')

    #  true or false
    prefs/external_members_disabled_: typing.Optional[str] = Field(None, alias='prefs/externalMembersDisabled')

    # a number from 1 to 2
    prefs/google_apps_version_: typing.Optional[str] = Field(None, alias='prefs/googleAppsVersion')

    # An email address with optional expansion tokens
    prefs/org_invite_restrict_: typing.Optional[str] = Field(None, alias='prefs/orgInviteRestrict')

    # One of: private or public
    prefs/permission_level_: typing.Optional[str] = Field(None, alias='prefs/permissionLevel')

    # A URL starting with http:// or https:// or null
    website: typing.Optional[str] = Field(None, alias='website')
    class Config:
        arbitrary_types_allowed = True
