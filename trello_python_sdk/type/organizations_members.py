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


class RequiredOrganizationsMembers(TypedDict):
    pass

class OptionalOrganizationsMembers(TypedDict, total=False):
    # An email address
    email: str

    # A string with a length of at least 1.  Cannot begin or end with a space.
    fullName: str

    # One of: admin, normal or observer
    type: str

class OrganizationsMembers(RequiredOrganizationsMembers, OptionalOrganizationsMembers):
    pass
