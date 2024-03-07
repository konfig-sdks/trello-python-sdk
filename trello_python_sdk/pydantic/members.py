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


class Members(BaseModel):
    # One of: gravatar, none or upload
    avatar_source: typing.Optional[str] = Field(None, alias='avatarSource')

    # a string with a length from 0 to 16384
    bio: typing.Optional[str] = Field(None, alias='bio')

    # A string with a length of at least 1.  Cannot begin or end with a space.
    full_name: typing.Optional[str] = Field(None, alias='fullName')

    # A string with a length from 1 to 4.  Cannot begin or end with a space
    initials: typing.Optional[str] = Field(None, alias='initials')

    #  true or false
    prefs/color_blind_: typing.Optional[str] = Field(None, alias='prefs/colorBlind')

    # a string with a length from 0 to 255
    prefs/locale_: typing.Optional[str] = Field(None, alias='prefs/locale')

    # -1 (disabled), 1 or 60
    prefs/minutes_between_summaries_: typing.Optional[str] = Field(None, alias='prefs/minutesBetweenSummaries')

    # A string with a length of at least 3.  Only lowercase letters, underscores, and numbers are allowed.  Must be unique.
    username: typing.Optional[str] = Field(None, alias='username')
    class Config:
        arbitrary_types_allowed = True
