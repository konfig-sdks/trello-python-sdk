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
from trello_python_sdk.paths.webhooks_id_webhook_id_model import put
from trello_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWebhooksIdWebhookIdModel(ApiTestMixin, unittest.TestCase):
    """
    WebhooksIdWebhookIdModel unit test stubs
        updateWebhooksIdModelByIdWebhook()
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''




if __name__ == '__main__':
    unittest.main()
