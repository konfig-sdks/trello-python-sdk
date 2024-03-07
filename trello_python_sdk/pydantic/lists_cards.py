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


class ListsCards(BaseModel):
    # a string with a length from 0 to 16384
    desc: typing.Optional[str] = Field(None, alias='desc')

    # A date, or null
    due: typing.Optional[str] = Field(None, alias='due')

    # A comma-separated list of objectIds, 24-character hex strings
    id_members: typing.Optional[str] = Field(None, alias='idMembers')

    # all or a comma-separated list of: blue, green, orange, purple, red or yellow
    labels: typing.Optional[str] = Field(None, alias='labels')

    # a string with a length from 1 to 16384
    name: typing.Optional[str] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
