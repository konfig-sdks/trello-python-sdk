# coding: utf-8
"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

import typing
import inspect
from datetime import date, datetime
from trello_python_sdk.client_custom import ClientCustom
from trello_python_sdk.configuration import Configuration
from trello_python_sdk.api_client import ApiClient
from trello_python_sdk.type_util import copy_signature
from trello_python_sdk.apis.tags.action_api import ActionApi
from trello_python_sdk.apis.tags.batch_api import BatchApi
from trello_python_sdk.apis.tags.board_api import BoardApi
from trello_python_sdk.apis.tags.card_api import CardApi
from trello_python_sdk.apis.tags.checklist_api import ChecklistApi
from trello_python_sdk.apis.tags.label_api import LabelApi
from trello_python_sdk.apis.tags.model_list_api import ModelListApi
from trello_python_sdk.apis.tags.member_api import MemberApi
from trello_python_sdk.apis.tags.notification_api import NotificationApi
from trello_python_sdk.apis.tags.organization_api import OrganizationApi
from trello_python_sdk.apis.tags.search_api import SearchApi
from trello_python_sdk.apis.tags.session_api import SessionApi
from trello_python_sdk.apis.tags.token_api import TokenApi
from trello_python_sdk.apis.tags.type_api import TypeApi
from trello_python_sdk.apis.tags.webhook_api import WebhookApi



class Trello(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.action: ActionApi = ActionApi(api_client)
        self.batch: BatchApi = BatchApi(api_client)
        self.board: BoardApi = BoardApi(api_client)
        self.card: CardApi = CardApi(api_client)
        self.checklist: ChecklistApi = ChecklistApi(api_client)
        self.label: LabelApi = LabelApi(api_client)
        self.list: ModelListApi = ModelListApi(api_client)
        self.member: MemberApi = MemberApi(api_client)
        self.notification: NotificationApi = NotificationApi(api_client)
        self.organization: OrganizationApi = OrganizationApi(api_client)
        self.search: SearchApi = SearchApi(api_client)
        self.session: SessionApi = SessionApi(api_client)
        self.token: TokenApi = TokenApi(api_client)
        self.type: TypeApi = TypeApi(api_client)
        self.webhook: WebhookApi = WebhookApi(api_client)
