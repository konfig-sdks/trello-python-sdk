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


class Boards(BaseModel):
    #  true or false
    closed: typing.Optional[str] = Field(None, alias='closed')

    # a string with a length from 0 to 16384
    desc: typing.Optional[str] = Field(None, alias='desc')

    # The id of the board to copy into the new board
    id_board_source: typing.Optional[str] = Field(None, alias='idBoardSource')

    # The id or name of the organization to add the board to.
    id_organization: typing.Optional[str] = Field(None, alias='idOrganization')

    # Components of the source board to copy.
    keep_from_source: typing.Optional[str] = Field(None, alias='keepFromSource')

    # a string with a length from 0 to 16384
    label_names/blue_: typing.Optional[str] = Field(None, alias='labelNames/blue')

    # a string with a length from 0 to 16384
    label_names/green_: typing.Optional[str] = Field(None, alias='labelNames/green')

    # a string with a length from 0 to 16384
    label_names/orange_: typing.Optional[str] = Field(None, alias='labelNames/orange')

    # a string with a length from 0 to 16384
    label_names/purple_: typing.Optional[str] = Field(None, alias='labelNames/purple')

    # a string with a length from 0 to 16384
    label_names/red_: typing.Optional[str] = Field(None, alias='labelNames/red')

    # a string with a length from 0 to 16384
    label_names/yellow_: typing.Optional[str] = Field(None, alias='labelNames/yellow')

    # a string with a length from 1 to 16384
    name: typing.Optional[str] = Field(None, alias='name')

    # all or a comma-separated list of: calendar, cardAging, recap or voting
    power_ups: typing.Optional[str] = Field(None, alias='powerUps')

    # A standard background name, or the id of a custom background
    prefs/background_: typing.Optional[str] = Field(None, alias='prefs/background')

    #  true or false
    prefs/calendar_feed_enabled_: typing.Optional[str] = Field(None, alias='prefs/calendarFeedEnabled')

    # One of: pirate or regular
    prefs/card_aging_: typing.Optional[str] = Field(None, alias='prefs/cardAging')

    #  true or false
    prefs/card_covers_: typing.Optional[str] = Field(None, alias='prefs/cardCovers')

    # One of: disabled, members, observers, org or public
    prefs/comments_: typing.Optional[str] = Field(None, alias='prefs/comments')

    # One of: admins or members
    prefs/invitations_: typing.Optional[str] = Field(None, alias='prefs/invitations')

    # One of: org, private or public
    prefs/permission_level_: typing.Optional[str] = Field(None, alias='prefs/permissionLevel')

    #  true or false
    prefs/self_join_: typing.Optional[str] = Field(None, alias='prefs/selfJoin')

    # One of: disabled, members, observers, org or public
    prefs/voting_: typing.Optional[str] = Field(None, alias='prefs/voting')

    # a string with a length from 0 to 16384
    prefs_background: typing.Optional[str] = Field(None, alias='prefs_background')

    # One of: pirate or regular
    prefs_card_aging: typing.Optional[str] = Field(None, alias='prefs_cardAging')

    #  true or false
    prefs_card_covers: typing.Optional[str] = Field(None, alias='prefs_cardCovers')

    # One of: disabled, members, observers, org or public
    prefs_comments: typing.Optional[str] = Field(None, alias='prefs_comments')

    # One of: admins or members
    prefs_invitations: typing.Optional[str] = Field(None, alias='prefs_invitations')

    # One of: org, private or public
    prefs_permission_level: typing.Optional[str] = Field(None, alias='prefs_permissionLevel')

    #  true or false
    prefs_self_join: typing.Optional[str] = Field(None, alias='prefs_selfJoin')

    # One of: disabled, members, observers, org or public
    prefs_voting: typing.Optional[str] = Field(None, alias='prefs_voting')

    #  true or false
    subscribed: typing.Optional[str] = Field(None, alias='subscribed')
    class Config:
        arbitrary_types_allowed = True
