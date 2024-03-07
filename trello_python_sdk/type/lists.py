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


class RequiredLists(TypedDict):
    pass

class OptionalLists(TypedDict, total=False):
    #  true or false
    closed: str

    # id of the board that the list should be added to
    idBoard: str

    # The id of the list to copy into a new list.
    idListSource: str

    # a string with a length from 1 to 16384
    name: str

    # A position. top , bottom , or a positive number.
    pos: str

    #  true or false
    subscribed: str

class Lists(RequiredLists, OptionalLists):
    pass
