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


class Lists(BaseModel):
    #  true or false
    closed: typing.Optional[str] = Field(None, alias='closed')

    # id of the board that the list should be added to
    id_board: typing.Optional[str] = Field(None, alias='idBoard')

    # The id of the list to copy into a new list.
    id_list_source: typing.Optional[str] = Field(None, alias='idListSource')

    # a string with a length from 1 to 16384
    name: typing.Optional[str] = Field(None, alias='name')

    # A position. top , bottom , or a positive number.
    pos: typing.Optional[str] = Field(None, alias='pos')

    #  true or false
    subscribed: typing.Optional[str] = Field(None, alias='subscribed')
    class Config:
        arbitrary_types_allowed = True
