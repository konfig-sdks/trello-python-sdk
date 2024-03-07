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


class Checklists(BaseModel):
    # id of the board that the checklist should be added to
    id_board: typing.Optional[str] = Field(None, alias='idBoard')

    # id of the card that the checklist should be added to
    id_card: typing.Optional[str] = Field(None, alias='idCard')

    # The id of the source checklist to copy into a new checklist.
    id_checklist_source: typing.Optional[str] = Field(None, alias='idChecklistSource')

    # a string with a length from 0 to 16384
    name: typing.Optional[str] = Field(None, alias='name')

    # A position. top , bottom , or a positive number.
    pos: typing.Optional[str] = Field(None, alias='pos')
    class Config:
        arbitrary_types_allowed = True
