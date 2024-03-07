# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.types_id.get import GetById
from trello_python_sdk.apis.tags.type_api_raw import TypeApiRaw


class TypeApi(
    GetById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TypeApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TypeApiRaw(api_client)
