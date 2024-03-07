# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

import unittest

import os
from pprint import pprint
from trello_python_sdk import Trello

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        trello = Trello(
        
                        api_key = 'YOUR_API_KEY',
        
                        api_token = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(trello)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
