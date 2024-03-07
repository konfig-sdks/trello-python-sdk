# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from trello_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from trello_python_sdk.api_response import AsyncGeneratorResponse
from trello_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from trello_python_sdk import schemas  # noqa: F401



from ...api_client import Dictionary

# Query params
ActionsSchema = schemas.StrSchema
ActionsEntitiesSchema = schemas.StrSchema
ActionsDisplaySchema = schemas.StrSchema
ActionsLimitSchema = schemas.StrSchema
ActionFieldsSchema = schemas.StrSchema
ActionSinceSchema = schemas.StrSchema
ActionBeforeSchema = schemas.StrSchema
CardsSchema = schemas.StrSchema
CardFieldsSchema = schemas.StrSchema
CardMembersSchema = schemas.StrSchema
CardMemberFieldsSchema = schemas.StrSchema
CardAttachmentsSchema = schemas.StrSchema
CardAttachmentFieldsSchema = schemas.StrSchema
CardStickersSchema = schemas.StrSchema
BoardsSchema = schemas.StrSchema
BoardFieldsSchema = schemas.StrSchema
BoardActionsSchema = schemas.StrSchema
BoardActionsEntitiesSchema = schemas.StrSchema
BoardActionsDisplaySchema = schemas.StrSchema
BoardActionsFormatSchema = schemas.StrSchema
BoardActionsSinceSchema = schemas.StrSchema
BoardActionsLimitSchema = schemas.StrSchema
BoardActionFieldsSchema = schemas.StrSchema
BoardListsSchema = schemas.StrSchema
BoardMembershipsSchema = schemas.StrSchema
BoardOrganizationSchema = schemas.StrSchema
BoardOrganizationFieldsSchema = schemas.StrSchema
BoardsInvitedSchema = schemas.StrSchema
BoardsInvitedFieldsSchema = schemas.StrSchema
BoardStarsSchema = schemas.StrSchema
SavedSearchesSchema = schemas.StrSchema
OrganizationsSchema = schemas.StrSchema
OrganizationFieldsSchema = schemas.StrSchema
OrganizationPaidAccountSchema = schemas.StrSchema
OrganizationsInvitedSchema = schemas.StrSchema
OrganizationsInvitedFieldsSchema = schemas.StrSchema
NotificationsSchema = schemas.StrSchema
NotificationsEntitiesSchema = schemas.StrSchema
NotificationsDisplaySchema = schemas.StrSchema
NotificationsLimitSchema = schemas.StrSchema
NotificationFieldsSchema = schemas.StrSchema
NotificationMemberCreatorSchema = schemas.StrSchema
NotificationMemberCreatorFieldsSchema = schemas.StrSchema
NotificationBeforeSchema = schemas.StrSchema
NotificationSinceSchema = schemas.StrSchema
TokensSchema = schemas.StrSchema
PaidAccountSchema = schemas.StrSchema
BoardBackgroundsSchema = schemas.StrSchema
CustomBoardBackgroundsSchema = schemas.StrSchema
CustomStickersSchema = schemas.StrSchema
CustomEmojiSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'actions': typing.Union[ActionsSchema, str, ],
        'actions_entities': typing.Union[ActionsEntitiesSchema, str, ],
        'actions_display': typing.Union[ActionsDisplaySchema, str, ],
        'actions_limit': typing.Union[ActionsLimitSchema, str, ],
        'action_fields': typing.Union[ActionFieldsSchema, str, ],
        'action_since': typing.Union[ActionSinceSchema, str, ],
        'action_before': typing.Union[ActionBeforeSchema, str, ],
        'cards': typing.Union[CardsSchema, str, ],
        'card_fields': typing.Union[CardFieldsSchema, str, ],
        'card_members': typing.Union[CardMembersSchema, str, ],
        'card_member_fields': typing.Union[CardMemberFieldsSchema, str, ],
        'card_attachments': typing.Union[CardAttachmentsSchema, str, ],
        'card_attachment_fields': typing.Union[CardAttachmentFieldsSchema, str, ],
        'card_stickers': typing.Union[CardStickersSchema, str, ],
        'boards': typing.Union[BoardsSchema, str, ],
        'board_fields': typing.Union[BoardFieldsSchema, str, ],
        'board_actions': typing.Union[BoardActionsSchema, str, ],
        'board_actions_entities': typing.Union[BoardActionsEntitiesSchema, str, ],
        'board_actions_display': typing.Union[BoardActionsDisplaySchema, str, ],
        'board_actions_format': typing.Union[BoardActionsFormatSchema, str, ],
        'board_actions_since': typing.Union[BoardActionsSinceSchema, str, ],
        'board_actions_limit': typing.Union[BoardActionsLimitSchema, str, ],
        'board_action_fields': typing.Union[BoardActionFieldsSchema, str, ],
        'board_lists': typing.Union[BoardListsSchema, str, ],
        'board_memberships': typing.Union[BoardMembershipsSchema, str, ],
        'board_organization': typing.Union[BoardOrganizationSchema, str, ],
        'board_organization_fields': typing.Union[BoardOrganizationFieldsSchema, str, ],
        'boardsInvited': typing.Union[BoardsInvitedSchema, str, ],
        'boardsInvited_fields': typing.Union[BoardsInvitedFieldsSchema, str, ],
        'boardStars': typing.Union[BoardStarsSchema, str, ],
        'savedSearches': typing.Union[SavedSearchesSchema, str, ],
        'organizations': typing.Union[OrganizationsSchema, str, ],
        'organization_fields': typing.Union[OrganizationFieldsSchema, str, ],
        'organization_paid_account': typing.Union[OrganizationPaidAccountSchema, str, ],
        'organizationsInvited': typing.Union[OrganizationsInvitedSchema, str, ],
        'organizationsInvited_fields': typing.Union[OrganizationsInvitedFieldsSchema, str, ],
        'notifications': typing.Union[NotificationsSchema, str, ],
        'notifications_entities': typing.Union[NotificationsEntitiesSchema, str, ],
        'notifications_display': typing.Union[NotificationsDisplaySchema, str, ],
        'notifications_limit': typing.Union[NotificationsLimitSchema, str, ],
        'notification_fields': typing.Union[NotificationFieldsSchema, str, ],
        'notification_memberCreator': typing.Union[NotificationMemberCreatorSchema, str, ],
        'notification_memberCreator_fields': typing.Union[NotificationMemberCreatorFieldsSchema, str, ],
        'notification_before': typing.Union[NotificationBeforeSchema, str, ],
        'notification_since': typing.Union[NotificationSinceSchema, str, ],
        'tokens': typing.Union[TokensSchema, str, ],
        'paid_account': typing.Union[PaidAccountSchema, str, ],
        'boardBackgrounds': typing.Union[BoardBackgroundsSchema, str, ],
        'customBoardBackgrounds': typing.Union[CustomBoardBackgroundsSchema, str, ],
        'customStickers': typing.Union[CustomStickersSchema, str, ],
        'customEmoji': typing.Union[CustomEmojiSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_actions = api_client.QueryParameter(
    name="actions",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsSchema,
    explode=True,
)
request_query_actions_entities = api_client.QueryParameter(
    name="actions_entities",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsEntitiesSchema,
    explode=True,
)
request_query_actions_display = api_client.QueryParameter(
    name="actions_display",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsDisplaySchema,
    explode=True,
)
request_query_actions_limit = api_client.QueryParameter(
    name="actions_limit",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsLimitSchema,
    explode=True,
)
request_query_action_fields = api_client.QueryParameter(
    name="action_fields",
    style=api_client.ParameterStyle.FORM,
    schema=ActionFieldsSchema,
    explode=True,
)
request_query_action_since = api_client.QueryParameter(
    name="action_since",
    style=api_client.ParameterStyle.FORM,
    schema=ActionSinceSchema,
    explode=True,
)
request_query_action_before = api_client.QueryParameter(
    name="action_before",
    style=api_client.ParameterStyle.FORM,
    schema=ActionBeforeSchema,
    explode=True,
)
request_query_cards = api_client.QueryParameter(
    name="cards",
    style=api_client.ParameterStyle.FORM,
    schema=CardsSchema,
    explode=True,
)
request_query_card_fields = api_client.QueryParameter(
    name="card_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CardFieldsSchema,
    explode=True,
)
request_query_card_members = api_client.QueryParameter(
    name="card_members",
    style=api_client.ParameterStyle.FORM,
    schema=CardMembersSchema,
    explode=True,
)
request_query_card_member_fields = api_client.QueryParameter(
    name="card_member_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CardMemberFieldsSchema,
    explode=True,
)
request_query_card_attachments = api_client.QueryParameter(
    name="card_attachments",
    style=api_client.ParameterStyle.FORM,
    schema=CardAttachmentsSchema,
    explode=True,
)
request_query_card_attachment_fields = api_client.QueryParameter(
    name="card_attachment_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CardAttachmentFieldsSchema,
    explode=True,
)
request_query_card_stickers = api_client.QueryParameter(
    name="card_stickers",
    style=api_client.ParameterStyle.FORM,
    schema=CardStickersSchema,
    explode=True,
)
request_query_boards = api_client.QueryParameter(
    name="boards",
    style=api_client.ParameterStyle.FORM,
    schema=BoardsSchema,
    explode=True,
)
request_query_board_fields = api_client.QueryParameter(
    name="board_fields",
    style=api_client.ParameterStyle.FORM,
    schema=BoardFieldsSchema,
    explode=True,
)
request_query_board_actions = api_client.QueryParameter(
    name="board_actions",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionsSchema,
    explode=True,
)
request_query_board_actions_entities = api_client.QueryParameter(
    name="board_actions_entities",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionsEntitiesSchema,
    explode=True,
)
request_query_board_actions_display = api_client.QueryParameter(
    name="board_actions_display",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionsDisplaySchema,
    explode=True,
)
request_query_board_actions_format = api_client.QueryParameter(
    name="board_actions_format",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionsFormatSchema,
    explode=True,
)
request_query_board_actions_since = api_client.QueryParameter(
    name="board_actions_since",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionsSinceSchema,
    explode=True,
)
request_query_board_actions_limit = api_client.QueryParameter(
    name="board_actions_limit",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionsLimitSchema,
    explode=True,
)
request_query_board_action_fields = api_client.QueryParameter(
    name="board_action_fields",
    style=api_client.ParameterStyle.FORM,
    schema=BoardActionFieldsSchema,
    explode=True,
)
request_query_board_lists = api_client.QueryParameter(
    name="board_lists",
    style=api_client.ParameterStyle.FORM,
    schema=BoardListsSchema,
    explode=True,
)
request_query_board_memberships = api_client.QueryParameter(
    name="board_memberships",
    style=api_client.ParameterStyle.FORM,
    schema=BoardMembershipsSchema,
    explode=True,
)
request_query_board_organization = api_client.QueryParameter(
    name="board_organization",
    style=api_client.ParameterStyle.FORM,
    schema=BoardOrganizationSchema,
    explode=True,
)
request_query_board_organization_fields = api_client.QueryParameter(
    name="board_organization_fields",
    style=api_client.ParameterStyle.FORM,
    schema=BoardOrganizationFieldsSchema,
    explode=True,
)
request_query_boards_invited = api_client.QueryParameter(
    name="boardsInvited",
    style=api_client.ParameterStyle.FORM,
    schema=BoardsInvitedSchema,
    explode=True,
)
request_query_boards_invited_fields = api_client.QueryParameter(
    name="boardsInvited_fields",
    style=api_client.ParameterStyle.FORM,
    schema=BoardsInvitedFieldsSchema,
    explode=True,
)
request_query_board_stars = api_client.QueryParameter(
    name="boardStars",
    style=api_client.ParameterStyle.FORM,
    schema=BoardStarsSchema,
    explode=True,
)
request_query_saved_searches = api_client.QueryParameter(
    name="savedSearches",
    style=api_client.ParameterStyle.FORM,
    schema=SavedSearchesSchema,
    explode=True,
)
request_query_organizations = api_client.QueryParameter(
    name="organizations",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationsSchema,
    explode=True,
)
request_query_organization_fields = api_client.QueryParameter(
    name="organization_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationFieldsSchema,
    explode=True,
)
request_query_organization_paid_account = api_client.QueryParameter(
    name="organization_paid_account",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationPaidAccountSchema,
    explode=True,
)
request_query_organizations_invited = api_client.QueryParameter(
    name="organizationsInvited",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationsInvitedSchema,
    explode=True,
)
request_query_organizations_invited_fields = api_client.QueryParameter(
    name="organizationsInvited_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationsInvitedFieldsSchema,
    explode=True,
)
request_query_notifications = api_client.QueryParameter(
    name="notifications",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationsSchema,
    explode=True,
)
request_query_notifications_entities = api_client.QueryParameter(
    name="notifications_entities",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationsEntitiesSchema,
    explode=True,
)
request_query_notifications_display = api_client.QueryParameter(
    name="notifications_display",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationsDisplaySchema,
    explode=True,
)
request_query_notifications_limit = api_client.QueryParameter(
    name="notifications_limit",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationsLimitSchema,
    explode=True,
)
request_query_notification_fields = api_client.QueryParameter(
    name="notification_fields",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationFieldsSchema,
    explode=True,
)
request_query_notification_member_creator = api_client.QueryParameter(
    name="notification_memberCreator",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationMemberCreatorSchema,
    explode=True,
)
request_query_notification_member_creator_fields = api_client.QueryParameter(
    name="notification_memberCreator_fields",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationMemberCreatorFieldsSchema,
    explode=True,
)
request_query_notification_before = api_client.QueryParameter(
    name="notification_before",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationBeforeSchema,
    explode=True,
)
request_query_notification_since = api_client.QueryParameter(
    name="notification_since",
    style=api_client.ParameterStyle.FORM,
    schema=NotificationSinceSchema,
    explode=True,
)
request_query_tokens = api_client.QueryParameter(
    name="tokens",
    style=api_client.ParameterStyle.FORM,
    schema=TokensSchema,
    explode=True,
)
request_query_paid_account = api_client.QueryParameter(
    name="paid_account",
    style=api_client.ParameterStyle.FORM,
    schema=PaidAccountSchema,
    explode=True,
)
request_query_board_backgrounds = api_client.QueryParameter(
    name="boardBackgrounds",
    style=api_client.ParameterStyle.FORM,
    schema=BoardBackgroundsSchema,
    explode=True,
)
request_query_custom_board_backgrounds = api_client.QueryParameter(
    name="customBoardBackgrounds",
    style=api_client.ParameterStyle.FORM,
    schema=CustomBoardBackgroundsSchema,
    explode=True,
)
request_query_custom_stickers = api_client.QueryParameter(
    name="customStickers",
    style=api_client.ParameterStyle.FORM,
    schema=CustomStickersSchema,
    explode=True,
)
request_query_custom_emoji = api_client.QueryParameter(
    name="customEmoji",
    style=api_client.ParameterStyle.FORM,
    schema=CustomEmojiSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
# Path params
IdMemberSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idMember': typing.Union[IdMemberSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id_member = api_client.PathParameter(
    name="idMember",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdMemberSchema,
    required=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


class BaseApi(api_client.Api):

    def _get_by_id_mapped_args(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if actions is not None:
            _query_params["actions"] = actions
        if actions_entities is not None:
            _query_params["actions_entities"] = actions_entities
        if actions_display is not None:
            _query_params["actions_display"] = actions_display
        if actions_limit is not None:
            _query_params["actions_limit"] = actions_limit
        if action_fields is not None:
            _query_params["action_fields"] = action_fields
        if action_since is not None:
            _query_params["action_since"] = action_since
        if action_before is not None:
            _query_params["action_before"] = action_before
        if cards is not None:
            _query_params["cards"] = cards
        if card_fields is not None:
            _query_params["card_fields"] = card_fields
        if card_members is not None:
            _query_params["card_members"] = card_members
        if card_member_fields is not None:
            _query_params["card_member_fields"] = card_member_fields
        if card_attachments is not None:
            _query_params["card_attachments"] = card_attachments
        if card_attachment_fields is not None:
            _query_params["card_attachment_fields"] = card_attachment_fields
        if card_stickers is not None:
            _query_params["card_stickers"] = card_stickers
        if boards is not None:
            _query_params["boards"] = boards
        if board_fields is not None:
            _query_params["board_fields"] = board_fields
        if board_actions is not None:
            _query_params["board_actions"] = board_actions
        if board_actions_entities is not None:
            _query_params["board_actions_entities"] = board_actions_entities
        if board_actions_display is not None:
            _query_params["board_actions_display"] = board_actions_display
        if board_actions_format is not None:
            _query_params["board_actions_format"] = board_actions_format
        if board_actions_since is not None:
            _query_params["board_actions_since"] = board_actions_since
        if board_actions_limit is not None:
            _query_params["board_actions_limit"] = board_actions_limit
        if board_action_fields is not None:
            _query_params["board_action_fields"] = board_action_fields
        if board_lists is not None:
            _query_params["board_lists"] = board_lists
        if board_memberships is not None:
            _query_params["board_memberships"] = board_memberships
        if board_organization is not None:
            _query_params["board_organization"] = board_organization
        if board_organization_fields is not None:
            _query_params["board_organization_fields"] = board_organization_fields
        if boards_invited is not None:
            _query_params["boardsInvited"] = boards_invited
        if boards_invited_fields is not None:
            _query_params["boardsInvited_fields"] = boards_invited_fields
        if board_stars is not None:
            _query_params["boardStars"] = board_stars
        if saved_searches is not None:
            _query_params["savedSearches"] = saved_searches
        if organizations is not None:
            _query_params["organizations"] = organizations
        if organization_fields is not None:
            _query_params["organization_fields"] = organization_fields
        if organization_paid_account is not None:
            _query_params["organization_paid_account"] = organization_paid_account
        if organizations_invited is not None:
            _query_params["organizationsInvited"] = organizations_invited
        if organizations_invited_fields is not None:
            _query_params["organizationsInvited_fields"] = organizations_invited_fields
        if notifications is not None:
            _query_params["notifications"] = notifications
        if notifications_entities is not None:
            _query_params["notifications_entities"] = notifications_entities
        if notifications_display is not None:
            _query_params["notifications_display"] = notifications_display
        if notifications_limit is not None:
            _query_params["notifications_limit"] = notifications_limit
        if notification_fields is not None:
            _query_params["notification_fields"] = notification_fields
        if notification_member_creator is not None:
            _query_params["notification_memberCreator"] = notification_member_creator
        if notification_member_creator_fields is not None:
            _query_params["notification_memberCreator_fields"] = notification_member_creator_fields
        if notification_before is not None:
            _query_params["notification_before"] = notification_before
        if notification_since is not None:
            _query_params["notification_since"] = notification_since
        if tokens is not None:
            _query_params["tokens"] = tokens
        if paid_account is not None:
            _query_params["paid_account"] = paid_account
        if board_backgrounds is not None:
            _query_params["boardBackgrounds"] = board_backgrounds
        if custom_board_backgrounds is not None:
            _query_params["customBoardBackgrounds"] = custom_board_backgrounds
        if custom_stickers is not None:
            _query_params["customStickers"] = custom_stickers
        if custom_emoji is not None:
            _query_params["customEmoji"] = custom_emoji
        if fields is not None:
            _query_params["fields"] = fields
        if id_member is not None:
            _path_params["idMember"] = id_member
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_by_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        getMembersByIdMember()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_member,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_actions,
            request_query_actions_entities,
            request_query_actions_display,
            request_query_actions_limit,
            request_query_action_fields,
            request_query_action_since,
            request_query_action_before,
            request_query_cards,
            request_query_card_fields,
            request_query_card_members,
            request_query_card_member_fields,
            request_query_card_attachments,
            request_query_card_attachment_fields,
            request_query_card_stickers,
            request_query_boards,
            request_query_board_fields,
            request_query_board_actions,
            request_query_board_actions_entities,
            request_query_board_actions_display,
            request_query_board_actions_format,
            request_query_board_actions_since,
            request_query_board_actions_limit,
            request_query_board_action_fields,
            request_query_board_lists,
            request_query_board_memberships,
            request_query_board_organization,
            request_query_board_organization_fields,
            request_query_boards_invited,
            request_query_boards_invited_fields,
            request_query_board_stars,
            request_query_saved_searches,
            request_query_organizations,
            request_query_organization_fields,
            request_query_organization_paid_account,
            request_query_organizations_invited,
            request_query_organizations_invited_fields,
            request_query_notifications,
            request_query_notifications_entities,
            request_query_notifications_display,
            request_query_notifications_limit,
            request_query_notification_fields,
            request_query_notification_member_creator,
            request_query_notification_member_creator_fields,
            request_query_notification_before,
            request_query_notification_since,
            request_query_tokens,
            request_query_paid_account,
            request_query_board_backgrounds,
            request_query_custom_board_backgrounds,
            request_query_custom_stickers,
            request_query_custom_emoji,
            request_query_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/members/{idMember}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_by_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        getMembersByIdMember()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_member,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_actions,
            request_query_actions_entities,
            request_query_actions_display,
            request_query_actions_limit,
            request_query_action_fields,
            request_query_action_since,
            request_query_action_before,
            request_query_cards,
            request_query_card_fields,
            request_query_card_members,
            request_query_card_member_fields,
            request_query_card_attachments,
            request_query_card_attachment_fields,
            request_query_card_stickers,
            request_query_boards,
            request_query_board_fields,
            request_query_board_actions,
            request_query_board_actions_entities,
            request_query_board_actions_display,
            request_query_board_actions_format,
            request_query_board_actions_since,
            request_query_board_actions_limit,
            request_query_board_action_fields,
            request_query_board_lists,
            request_query_board_memberships,
            request_query_board_organization,
            request_query_board_organization_fields,
            request_query_boards_invited,
            request_query_boards_invited_fields,
            request_query_board_stars,
            request_query_saved_searches,
            request_query_organizations,
            request_query_organization_fields,
            request_query_organization_paid_account,
            request_query_organizations_invited,
            request_query_organizations_invited_fields,
            request_query_notifications,
            request_query_notifications_entities,
            request_query_notifications_display,
            request_query_notifications_limit,
            request_query_notification_fields,
            request_query_notification_member_creator,
            request_query_notification_member_creator_fields,
            request_query_notification_before,
            request_query_notification_since,
            request_query_tokens,
            request_query_paid_account,
            request_query_board_backgrounds,
            request_query_custom_board_backgrounds,
            request_query_custom_stickers,
            request_query_custom_emoji,
            request_query_fields,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/members/{idMember}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_by_id(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_member=id_member,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_since=action_since,
            action_before=action_before,
            cards=cards,
            card_fields=card_fields,
            card_members=card_members,
            card_member_fields=card_member_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_stickers=card_stickers,
            boards=boards,
            board_fields=board_fields,
            board_actions=board_actions,
            board_actions_entities=board_actions_entities,
            board_actions_display=board_actions_display,
            board_actions_format=board_actions_format,
            board_actions_since=board_actions_since,
            board_actions_limit=board_actions_limit,
            board_action_fields=board_action_fields,
            board_lists=board_lists,
            board_memberships=board_memberships,
            board_organization=board_organization,
            board_organization_fields=board_organization_fields,
            boards_invited=boards_invited,
            boards_invited_fields=boards_invited_fields,
            board_stars=board_stars,
            saved_searches=saved_searches,
            organizations=organizations,
            organization_fields=organization_fields,
            organization_paid_account=organization_paid_account,
            organizations_invited=organizations_invited,
            organizations_invited_fields=organizations_invited_fields,
            notifications=notifications,
            notifications_entities=notifications_entities,
            notifications_display=notifications_display,
            notifications_limit=notifications_limit,
            notification_fields=notification_fields,
            notification_member_creator=notification_member_creator,
            notification_member_creator_fields=notification_member_creator_fields,
            notification_before=notification_before,
            notification_since=notification_since,
            tokens=tokens,
            paid_account=paid_account,
            board_backgrounds=board_backgrounds,
            custom_board_backgrounds=custom_board_backgrounds,
            custom_stickers=custom_stickers,
            custom_emoji=custom_emoji,
            fields=fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_id(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_member=id_member,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_since=action_since,
            action_before=action_before,
            cards=cards,
            card_fields=card_fields,
            card_members=card_members,
            card_member_fields=card_member_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_stickers=card_stickers,
            boards=boards,
            board_fields=board_fields,
            board_actions=board_actions,
            board_actions_entities=board_actions_entities,
            board_actions_display=board_actions_display,
            board_actions_format=board_actions_format,
            board_actions_since=board_actions_since,
            board_actions_limit=board_actions_limit,
            board_action_fields=board_action_fields,
            board_lists=board_lists,
            board_memberships=board_memberships,
            board_organization=board_organization,
            board_organization_fields=board_organization_fields,
            boards_invited=boards_invited,
            boards_invited_fields=boards_invited_fields,
            board_stars=board_stars,
            saved_searches=saved_searches,
            organizations=organizations,
            organization_fields=organization_fields,
            organization_paid_account=organization_paid_account,
            organizations_invited=organizations_invited,
            organizations_invited_fields=organizations_invited_fields,
            notifications=notifications,
            notifications_entities=notifications_entities,
            notifications_display=notifications_display,
            notifications_limit=notifications_limit,
            notification_fields=notification_fields,
            notification_member_creator=notification_member_creator,
            notification_member_creator_fields=notification_member_creator_fields,
            notification_before=notification_before,
            notification_since=notification_since,
            tokens=tokens,
            paid_account=paid_account,
            board_backgrounds=board_backgrounds,
            custom_board_backgrounds=custom_board_backgrounds,
            custom_stickers=custom_stickers,
            custom_emoji=custom_emoji,
            fields=fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetById(BaseApi):

    async def aget_by_id(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_by_id(
            id_member=id_member,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_since=action_since,
            action_before=action_before,
            cards=cards,
            card_fields=card_fields,
            card_members=card_members,
            card_member_fields=card_member_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_stickers=card_stickers,
            boards=boards,
            board_fields=board_fields,
            board_actions=board_actions,
            board_actions_entities=board_actions_entities,
            board_actions_display=board_actions_display,
            board_actions_format=board_actions_format,
            board_actions_since=board_actions_since,
            board_actions_limit=board_actions_limit,
            board_action_fields=board_action_fields,
            board_lists=board_lists,
            board_memberships=board_memberships,
            board_organization=board_organization,
            board_organization_fields=board_organization_fields,
            boards_invited=boards_invited,
            boards_invited_fields=boards_invited_fields,
            board_stars=board_stars,
            saved_searches=saved_searches,
            organizations=organizations,
            organization_fields=organization_fields,
            organization_paid_account=organization_paid_account,
            organizations_invited=organizations_invited,
            organizations_invited_fields=organizations_invited_fields,
            notifications=notifications,
            notifications_entities=notifications_entities,
            notifications_display=notifications_display,
            notifications_limit=notifications_limit,
            notification_fields=notification_fields,
            notification_member_creator=notification_member_creator,
            notification_member_creator_fields=notification_member_creator_fields,
            notification_before=notification_before,
            notification_since=notification_since,
            tokens=tokens,
            paid_account=paid_account,
            board_backgrounds=board_backgrounds,
            custom_board_backgrounds=custom_board_backgrounds,
            custom_stickers=custom_stickers,
            custom_emoji=custom_emoji,
            fields=fields,
            **kwargs,
        )
    
    
    def get_by_id(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_by_id(
            id_member=id_member,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_since=action_since,
            action_before=action_before,
            cards=cards,
            card_fields=card_fields,
            card_members=card_members,
            card_member_fields=card_member_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_stickers=card_stickers,
            boards=boards,
            board_fields=board_fields,
            board_actions=board_actions,
            board_actions_entities=board_actions_entities,
            board_actions_display=board_actions_display,
            board_actions_format=board_actions_format,
            board_actions_since=board_actions_since,
            board_actions_limit=board_actions_limit,
            board_action_fields=board_action_fields,
            board_lists=board_lists,
            board_memberships=board_memberships,
            board_organization=board_organization,
            board_organization_fields=board_organization_fields,
            boards_invited=boards_invited,
            boards_invited_fields=boards_invited_fields,
            board_stars=board_stars,
            saved_searches=saved_searches,
            organizations=organizations,
            organization_fields=organization_fields,
            organization_paid_account=organization_paid_account,
            organizations_invited=organizations_invited,
            organizations_invited_fields=organizations_invited_fields,
            notifications=notifications,
            notifications_entities=notifications_entities,
            notifications_display=notifications_display,
            notifications_limit=notifications_limit,
            notification_fields=notification_fields,
            notification_member_creator=notification_member_creator,
            notification_member_creator_fields=notification_member_creator_fields,
            notification_before=notification_before,
            notification_since=notification_since,
            tokens=tokens,
            paid_account=paid_account,
            board_backgrounds=board_backgrounds,
            custom_board_backgrounds=custom_board_backgrounds,
            custom_stickers=custom_stickers,
            custom_emoji=custom_emoji,
            fields=fields,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_member=id_member,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_since=action_since,
            action_before=action_before,
            cards=cards,
            card_fields=card_fields,
            card_members=card_members,
            card_member_fields=card_member_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_stickers=card_stickers,
            boards=boards,
            board_fields=board_fields,
            board_actions=board_actions,
            board_actions_entities=board_actions_entities,
            board_actions_display=board_actions_display,
            board_actions_format=board_actions_format,
            board_actions_since=board_actions_since,
            board_actions_limit=board_actions_limit,
            board_action_fields=board_action_fields,
            board_lists=board_lists,
            board_memberships=board_memberships,
            board_organization=board_organization,
            board_organization_fields=board_organization_fields,
            boards_invited=boards_invited,
            boards_invited_fields=boards_invited_fields,
            board_stars=board_stars,
            saved_searches=saved_searches,
            organizations=organizations,
            organization_fields=organization_fields,
            organization_paid_account=organization_paid_account,
            organizations_invited=organizations_invited,
            organizations_invited_fields=organizations_invited_fields,
            notifications=notifications,
            notifications_entities=notifications_entities,
            notifications_display=notifications_display,
            notifications_limit=notifications_limit,
            notification_fields=notification_fields,
            notification_member_creator=notification_member_creator,
            notification_member_creator_fields=notification_member_creator_fields,
            notification_before=notification_before,
            notification_since=notification_since,
            tokens=tokens,
            paid_account=paid_account,
            board_backgrounds=board_backgrounds,
            custom_board_backgrounds=custom_board_backgrounds,
            custom_stickers=custom_stickers,
            custom_emoji=custom_emoji,
            fields=fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_member: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_since: typing.Optional[str] = None,
        action_before: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_member_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        boards: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        board_actions: typing.Optional[str] = None,
        board_actions_entities: typing.Optional[str] = None,
        board_actions_display: typing.Optional[str] = None,
        board_actions_format: typing.Optional[str] = None,
        board_actions_since: typing.Optional[str] = None,
        board_actions_limit: typing.Optional[str] = None,
        board_action_fields: typing.Optional[str] = None,
        board_lists: typing.Optional[str] = None,
        board_memberships: typing.Optional[str] = None,
        board_organization: typing.Optional[str] = None,
        board_organization_fields: typing.Optional[str] = None,
        boards_invited: typing.Optional[str] = None,
        boards_invited_fields: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        saved_searches: typing.Optional[str] = None,
        organizations: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_paid_account: typing.Optional[str] = None,
        organizations_invited: typing.Optional[str] = None,
        organizations_invited_fields: typing.Optional[str] = None,
        notifications: typing.Optional[str] = None,
        notifications_entities: typing.Optional[str] = None,
        notifications_display: typing.Optional[str] = None,
        notifications_limit: typing.Optional[str] = None,
        notification_fields: typing.Optional[str] = None,
        notification_member_creator: typing.Optional[str] = None,
        notification_member_creator_fields: typing.Optional[str] = None,
        notification_before: typing.Optional[str] = None,
        notification_since: typing.Optional[str] = None,
        tokens: typing.Optional[str] = None,
        paid_account: typing.Optional[str] = None,
        board_backgrounds: typing.Optional[str] = None,
        custom_board_backgrounds: typing.Optional[str] = None,
        custom_stickers: typing.Optional[str] = None,
        custom_emoji: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_member=id_member,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_since=action_since,
            action_before=action_before,
            cards=cards,
            card_fields=card_fields,
            card_members=card_members,
            card_member_fields=card_member_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_stickers=card_stickers,
            boards=boards,
            board_fields=board_fields,
            board_actions=board_actions,
            board_actions_entities=board_actions_entities,
            board_actions_display=board_actions_display,
            board_actions_format=board_actions_format,
            board_actions_since=board_actions_since,
            board_actions_limit=board_actions_limit,
            board_action_fields=board_action_fields,
            board_lists=board_lists,
            board_memberships=board_memberships,
            board_organization=board_organization,
            board_organization_fields=board_organization_fields,
            boards_invited=boards_invited,
            boards_invited_fields=boards_invited_fields,
            board_stars=board_stars,
            saved_searches=saved_searches,
            organizations=organizations,
            organization_fields=organization_fields,
            organization_paid_account=organization_paid_account,
            organizations_invited=organizations_invited,
            organizations_invited_fields=organizations_invited_fields,
            notifications=notifications,
            notifications_entities=notifications_entities,
            notifications_display=notifications_display,
            notifications_limit=notifications_limit,
            notification_fields=notification_fields,
            notification_member_creator=notification_member_creator,
            notification_member_creator_fields=notification_member_creator_fields,
            notification_before=notification_before,
            notification_since=notification_since,
            tokens=tokens,
            paid_account=paid_account,
            board_backgrounds=board_backgrounds,
            custom_board_backgrounds=custom_board_backgrounds,
            custom_stickers=custom_stickers,
            custom_emoji=custom_emoji,
            fields=fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

