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


RequiredOrganizations = TypedDict("RequiredOrganizations", {
    })

OptionalOrganizations = TypedDict("OptionalOrganizations", {
    # a string with a length from 0 to 16384
    "desc": str,

    # A string with a length of at least 1.  Cannot begin or end with a space.
    "displayName": str,

    # a string with a length from 0 to 16384
    "name": str,

    # The google apps domain to link this org to.
    "prefs/associatedDomain": str,

    # One of: admin, none or org
    "prefs/boardVisibilityRestrict/org": str,

    # One of: admin, none or org
    "prefs/boardVisibilityRestrict/private": str,

    # One of: admin, none or org
    "prefs/boardVisibilityRestrict/public": str,

    #  true or false
    "prefs/externalMembersDisabled": str,

    # a number from 1 to 2
    "prefs/googleAppsVersion": str,

    # An email address with optional expansion tokens
    "prefs/orgInviteRestrict": str,

    # One of: private or public
    "prefs/permissionLevel": str,

    # A URL starting with http:// or https:// or null
    "website": str,
    }, total=False)

class Organizations(RequiredOrganizations, OptionalOrganizations):
    pass
