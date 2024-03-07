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


class Cards(BaseModel):
    #  true or false
    closed: typing.Optional[str] = Field(None, alias='closed')

    # a string with a length from 0 to 16384
    desc: typing.Optional[str] = Field(None, alias='desc')

    # A date, or null
    due: typing.Optional[str] = Field(None, alias='due')

    # A file
    file_source: typing.Optional[str] = Field(None, alias='fileSource')

    # Id of the image attachment of this card to use as its cover, or null for no cover
    id_attachment_cover: typing.Optional[str] = Field(None, alias='idAttachmentCover')

    # id of the board the card should be moved to
    id_board: typing.Optional[str] = Field(None, alias='idBoard')

    # The id of the card to copy into a new card.
    id_card_source: typing.Optional[str] = Field(None, alias='idCardSource')

    # A comma-separated list of objectIds, 24-character hex strings
    id_labels: typing.Optional[str] = Field(None, alias='idLabels')

    # id of the list that the card should be added to
    id_list: typing.Optional[str] = Field(None, alias='idList')

    # A comma-separated list of objectIds, 24-character hex strings
    id_members: typing.Optional[str] = Field(None, alias='idMembers')

    # Properties of the card to copy over from the source.
    keep_from_source: typing.Optional[str] = Field(None, alias='keepFromSource')

    # all or a comma-separated list of: blue, green, orange, purple, red or yellow
    labels: typing.Optional[str] = Field(None, alias='labels')

    # The name of the new card.  It isn&#39;t required if the name is being copied from provided by a URL, file or card that is being copied.
    name: typing.Optional[str] = Field(None, alias='name')

    # A position. top , bottom , or a positive number.
    pos: typing.Optional[str] = Field(None, alias='pos')

    #  true or false
    subscribed: typing.Optional[str] = Field(None, alias='subscribed')

    # A URL starting with http:// or https:// or null
    url_source: typing.Optional[str] = Field(None, alias='urlSource')
    class Config:
        arbitrary_types_allowed = True
