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


class CardsAttachments(BaseModel):
    # A file
    file: typing.Optional[str] = Field(None, alias='file')

    # a string with a length from 0 to 256
    mime_type: typing.Optional[str] = Field(None, alias='mimeType')

    # a string with a length from 0 to 256
    name: typing.Optional[str] = Field(None, alias='name')

    # A URL starting with http:// or https:// or null
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
