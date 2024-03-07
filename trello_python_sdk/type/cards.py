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


class RequiredCards(TypedDict):
    pass

class OptionalCards(TypedDict, total=False):
    #  true or false
    closed: str

    # a string with a length from 0 to 16384
    desc: str

    # A date, or null
    due: str

    # A file
    fileSource: str

    # Id of the image attachment of this card to use as its cover, or null for no cover
    idAttachmentCover: str

    # id of the board the card should be moved to
    idBoard: str

    # The id of the card to copy into a new card.
    idCardSource: str

    # A comma-separated list of objectIds, 24-character hex strings
    idLabels: str

    # id of the list that the card should be added to
    idList: str

    # A comma-separated list of objectIds, 24-character hex strings
    idMembers: str

    # Properties of the card to copy over from the source.
    keepFromSource: str

    # all or a comma-separated list of: blue, green, orange, purple, red or yellow
    labels: str

    # The name of the new card.  It isn&#39;t required if the name is being copied from provided by a URL, file or card that is being copied.
    name: str

    # A position. top , bottom , or a positive number.
    pos: str

    #  true or false
    subscribed: str

    # A URL starting with http:// or https:// or null
    urlSource: str

class Cards(RequiredCards, OptionalCards):
    pass
