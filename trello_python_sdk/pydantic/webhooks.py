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


class Webhooks(BaseModel):
    # a string with a length from 0 to 16384
    description: typing.Optional[str] = Field(None, alias='description')

    #  true or false
    active: typing.Optional[str] = Field(None, alias='active')

    # A valid URL that is reachable with a HEAD request
    callback_u_r_l: typing.Optional[str] = Field(None, alias='callbackURL')

    # id of the model that should be hooked
    id_model: typing.Optional[str] = Field(None, alias='idModel')
    class Config:
        arbitrary_types_allowed = True
