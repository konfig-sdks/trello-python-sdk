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


RequiredMembers = TypedDict("RequiredMembers", {
    })

OptionalMembers = TypedDict("OptionalMembers", {
    # One of: gravatar, none or upload
    "avatarSource": str,

    # a string with a length from 0 to 16384
    "bio": str,

    # A string with a length of at least 1.  Cannot begin or end with a space.
    "fullName": str,

    # A string with a length from 1 to 4.  Cannot begin or end with a space
    "initials": str,

    #  true or false
    "prefs/colorBlind": str,

    # a string with a length from 0 to 255
    "prefs/locale": str,

    # -1 (disabled), 1 or 60
    "prefs/minutesBetweenSummaries": str,

    # A string with a length of at least 3.  Only lowercase letters, underscores, and numbers are allowed.  Must be unique.
    "username": str,
    }, total=False)

class Members(RequiredMembers, OptionalMembers):
    pass
