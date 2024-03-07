# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

import unittest
from unittest.mock import patch

import urllib3

import trello_python_sdk
from trello_python_sdk.paths.members_id_member_board_stars import get
from trello_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMembersIdMemberBoardStars(ApiTestMixin, unittest.TestCase):
    """
    MembersIdMemberBoardStars unit test stubs
        getMembersBoardStarsByIdMember()
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
