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


class CardsStickers(BaseModel):
    # a string with a length from 0 to 16384
    image: typing.Optional[str] = Field(None, alias='image')

    # undefined
    left: typing.Optional[str] = Field(None, alias='left')

    # undefined
    rotate: typing.Optional[str] = Field(None, alias='rotate')

    # undefined
    top: typing.Optional[str] = Field(None, alias='top')

    # Valid Z values for stickers, must be an integer
    z_index: typing.Optional[str] = Field(None, alias='zIndex')
    class Config:
        arbitrary_types_allowed = True
