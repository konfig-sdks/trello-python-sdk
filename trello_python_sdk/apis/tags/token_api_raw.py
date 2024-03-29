# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.tokens_token.delete import DeleteByTokenRaw
from trello_python_sdk.paths.tokens_token.get import GetByTokenRaw
from trello_python_sdk.paths.tokens_token_field.get import GetByTokenByFieldRaw
from trello_python_sdk.paths.tokens_token_member_field.get import GetMemberByFieldRaw
from trello_python_sdk.paths.tokens_token_member.get import GetMemberByTokenRaw
from trello_python_sdk.paths.tokens_token_webhooks_id_webhook.get import GetWebhookByIdRaw
from trello_python_sdk.paths.tokens_token_webhooks.get import GetWebhooksRaw
from trello_python_sdk.paths.tokens_token_webhooks.post import RegisterWebhookRaw
from trello_python_sdk.paths.tokens_token_webhooks_id_webhook.delete import RemoveByTokenByIdWebhookRaw
from trello_python_sdk.paths.tokens_token_webhooks.put import UpdateWebhooksByTokenRaw


class TokenApiRaw(
    DeleteByTokenRaw,
    GetByTokenRaw,
    GetByTokenByFieldRaw,
    GetMemberByFieldRaw,
    GetMemberByTokenRaw,
    GetWebhookByIdRaw,
    GetWebhooksRaw,
    RegisterWebhookRaw,
    RemoveByTokenByIdWebhookRaw,
    UpdateWebhooksByTokenRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
