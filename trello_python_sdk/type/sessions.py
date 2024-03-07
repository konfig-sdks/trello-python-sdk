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


class RequiredSessions(TypedDict):
    pass

class OptionalSessions(TypedDict, total=False):
    # The id of the board you&#39;re viewing.  Boards with no viewers will not get updates about members&#39; statuses.
    idBoard: str

    # One of: active, disconnected or idle
    status: str

class Sessions(RequiredSessions, OptionalSessions):
    pass
