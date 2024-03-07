# coding: utf-8

# flake8: noqa

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

__version__ = "1.0"

# import ApiClient
from trello_python_sdk.api_client import ApiClient

# import Configuration
from trello_python_sdk.configuration import Configuration

# import exceptions
from trello_python_sdk.exceptions import OpenApiException
from trello_python_sdk.exceptions import ApiAttributeError
from trello_python_sdk.exceptions import ApiTypeError
from trello_python_sdk.exceptions import ApiValueError
from trello_python_sdk.exceptions import ApiKeyError
from trello_python_sdk.exceptions import ApiException

from trello_python_sdk.client import Trello
