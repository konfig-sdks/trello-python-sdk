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


class RequiredCardsIdAttachmentCover(TypedDict):
    pass

class OptionalCardsIdAttachmentCover(TypedDict, total=False):
    # Id of the image attachment of this card to use as its cover, or null for no cover
    value: str

class CardsIdAttachmentCover(RequiredCardsIdAttachmentCover, OptionalCardsIdAttachmentCover):
    pass
