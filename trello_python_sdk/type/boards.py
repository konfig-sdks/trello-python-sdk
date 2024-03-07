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


RequiredBoards = TypedDict("RequiredBoards", {
    })

OptionalBoards = TypedDict("OptionalBoards", {
    #  true or false
    "closed": str,

    # a string with a length from 0 to 16384
    "desc": str,

    # The id of the board to copy into the new board
    "idBoardSource": str,

    # The id or name of the organization to add the board to.
    "idOrganization": str,

    # Components of the source board to copy.
    "keepFromSource": str,

    # a string with a length from 0 to 16384
    "labelNames/blue": str,

    # a string with a length from 0 to 16384
    "labelNames/green": str,

    # a string with a length from 0 to 16384
    "labelNames/orange": str,

    # a string with a length from 0 to 16384
    "labelNames/purple": str,

    # a string with a length from 0 to 16384
    "labelNames/red": str,

    # a string with a length from 0 to 16384
    "labelNames/yellow": str,

    # a string with a length from 1 to 16384
    "name": str,

    # all or a comma-separated list of: calendar, cardAging, recap or voting
    "powerUps": str,

    # A standard background name, or the id of a custom background
    "prefs/background": str,

    #  true or false
    "prefs/calendarFeedEnabled": str,

    # One of: pirate or regular
    "prefs/cardAging": str,

    #  true or false
    "prefs/cardCovers": str,

    # One of: disabled, members, observers, org or public
    "prefs/comments": str,

    # One of: admins or members
    "prefs/invitations": str,

    # One of: org, private or public
    "prefs/permissionLevel": str,

    #  true or false
    "prefs/selfJoin": str,

    # One of: disabled, members, observers, org or public
    "prefs/voting": str,

    # a string with a length from 0 to 16384
    "prefs_background": str,

    # One of: pirate or regular
    "prefs_cardAging": str,

    #  true or false
    "prefs_cardCovers": str,

    # One of: disabled, members, observers, org or public
    "prefs_comments": str,

    # One of: admins or members
    "prefs_invitations": str,

    # One of: org, private or public
    "prefs_permissionLevel": str,

    #  true or false
    "prefs_selfJoin": str,

    # One of: disabled, members, observers, org or public
    "prefs_voting": str,

    #  true or false
    "subscribed": str,
    }, total=False)

class Boards(RequiredBoards, OptionalBoards):
    pass
