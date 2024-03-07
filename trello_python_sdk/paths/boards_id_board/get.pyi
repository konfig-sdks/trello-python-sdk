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
ActionsFormatSchema = schemas.StrSchema
ActionsSinceSchema = schemas.StrSchema
ActionsLimitSchema = schemas.StrSchema
ActionFieldsSchema = schemas.StrSchema
ActionMemberSchema = schemas.StrSchema
ActionMemberFieldsSchema = schemas.StrSchema
ActionMemberCreatorSchema = schemas.StrSchema
ActionMemberCreatorFieldsSchema = schemas.StrSchema
CardsSchema = schemas.StrSchema
CardFieldsSchema = schemas.StrSchema
CardAttachmentsSchema = schemas.StrSchema
CardAttachmentFieldsSchema = schemas.StrSchema
CardChecklistsSchema = schemas.StrSchema
CardStickersSchema = schemas.StrSchema
BoardStarsSchema = schemas.StrSchema
LabelsSchema = schemas.StrSchema
LabelFieldsSchema = schemas.StrSchema
LabelsLimitSchema = schemas.StrSchema
ListsSchema = schemas.StrSchema
ListFieldsSchema = schemas.StrSchema
MembershipsSchema = schemas.StrSchema
MembershipsMemberSchema = schemas.StrSchema
MembershipsMemberFieldsSchema = schemas.StrSchema
MembersSchema = schemas.StrSchema
MemberFieldsSchema = schemas.StrSchema
MembersInvitedSchema = schemas.StrSchema
MembersInvitedFieldsSchema = schemas.StrSchema
ChecklistsSchema = schemas.StrSchema
ChecklistFieldsSchema = schemas.StrSchema
OrganizationSchema = schemas.StrSchema
OrganizationFieldsSchema = schemas.StrSchema
OrganizationMembershipsSchema = schemas.StrSchema
MyPrefsSchema = schemas.StrSchema
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
        'actions_format': typing.Union[ActionsFormatSchema, str, ],
        'actions_since': typing.Union[ActionsSinceSchema, str, ],
        'actions_limit': typing.Union[ActionsLimitSchema, str, ],
        'action_fields': typing.Union[ActionFieldsSchema, str, ],
        'action_member': typing.Union[ActionMemberSchema, str, ],
        'action_member_fields': typing.Union[ActionMemberFieldsSchema, str, ],
        'action_memberCreator': typing.Union[ActionMemberCreatorSchema, str, ],
        'action_memberCreator_fields': typing.Union[ActionMemberCreatorFieldsSchema, str, ],
        'cards': typing.Union[CardsSchema, str, ],
        'card_fields': typing.Union[CardFieldsSchema, str, ],
        'card_attachments': typing.Union[CardAttachmentsSchema, str, ],
        'card_attachment_fields': typing.Union[CardAttachmentFieldsSchema, str, ],
        'card_checklists': typing.Union[CardChecklistsSchema, str, ],
        'card_stickers': typing.Union[CardStickersSchema, str, ],
        'boardStars': typing.Union[BoardStarsSchema, str, ],
        'labels': typing.Union[LabelsSchema, str, ],
        'label_fields': typing.Union[LabelFieldsSchema, str, ],
        'labels_limit': typing.Union[LabelsLimitSchema, str, ],
        'lists': typing.Union[ListsSchema, str, ],
        'list_fields': typing.Union[ListFieldsSchema, str, ],
        'memberships': typing.Union[MembershipsSchema, str, ],
        'memberships_member': typing.Union[MembershipsMemberSchema, str, ],
        'memberships_member_fields': typing.Union[MembershipsMemberFieldsSchema, str, ],
        'members': typing.Union[MembersSchema, str, ],
        'member_fields': typing.Union[MemberFieldsSchema, str, ],
        'membersInvited': typing.Union[MembersInvitedSchema, str, ],
        'membersInvited_fields': typing.Union[MembersInvitedFieldsSchema, str, ],
        'checklists': typing.Union[ChecklistsSchema, str, ],
        'checklist_fields': typing.Union[ChecklistFieldsSchema, str, ],
        'organization': typing.Union[OrganizationSchema, str, ],
        'organization_fields': typing.Union[OrganizationFieldsSchema, str, ],
        'organization_memberships': typing.Union[OrganizationMembershipsSchema, str, ],
        'myPrefs': typing.Union[MyPrefsSchema, str, ],
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
request_query_actions_format = api_client.QueryParameter(
    name="actions_format",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsFormatSchema,
    explode=True,
)
request_query_actions_since = api_client.QueryParameter(
    name="actions_since",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsSinceSchema,
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
request_query_action_member = api_client.QueryParameter(
    name="action_member",
    style=api_client.ParameterStyle.FORM,
    schema=ActionMemberSchema,
    explode=True,
)
request_query_action_member_fields = api_client.QueryParameter(
    name="action_member_fields",
    style=api_client.ParameterStyle.FORM,
    schema=ActionMemberFieldsSchema,
    explode=True,
)
request_query_action_member_creator = api_client.QueryParameter(
    name="action_memberCreator",
    style=api_client.ParameterStyle.FORM,
    schema=ActionMemberCreatorSchema,
    explode=True,
)
request_query_action_member_creator_fields = api_client.QueryParameter(
    name="action_memberCreator_fields",
    style=api_client.ParameterStyle.FORM,
    schema=ActionMemberCreatorFieldsSchema,
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
request_query_card_checklists = api_client.QueryParameter(
    name="card_checklists",
    style=api_client.ParameterStyle.FORM,
    schema=CardChecklistsSchema,
    explode=True,
)
request_query_card_stickers = api_client.QueryParameter(
    name="card_stickers",
    style=api_client.ParameterStyle.FORM,
    schema=CardStickersSchema,
    explode=True,
)
request_query_board_stars = api_client.QueryParameter(
    name="boardStars",
    style=api_client.ParameterStyle.FORM,
    schema=BoardStarsSchema,
    explode=True,
)
request_query_labels = api_client.QueryParameter(
    name="labels",
    style=api_client.ParameterStyle.FORM,
    schema=LabelsSchema,
    explode=True,
)
request_query_label_fields = api_client.QueryParameter(
    name="label_fields",
    style=api_client.ParameterStyle.FORM,
    schema=LabelFieldsSchema,
    explode=True,
)
request_query_labels_limit = api_client.QueryParameter(
    name="labels_limit",
    style=api_client.ParameterStyle.FORM,
    schema=LabelsLimitSchema,
    explode=True,
)
request_query_lists = api_client.QueryParameter(
    name="lists",
    style=api_client.ParameterStyle.FORM,
    schema=ListsSchema,
    explode=True,
)
request_query_list_fields = api_client.QueryParameter(
    name="list_fields",
    style=api_client.ParameterStyle.FORM,
    schema=ListFieldsSchema,
    explode=True,
)
request_query_memberships = api_client.QueryParameter(
    name="memberships",
    style=api_client.ParameterStyle.FORM,
    schema=MembershipsSchema,
    explode=True,
)
request_query_memberships_member = api_client.QueryParameter(
    name="memberships_member",
    style=api_client.ParameterStyle.FORM,
    schema=MembershipsMemberSchema,
    explode=True,
)
request_query_memberships_member_fields = api_client.QueryParameter(
    name="memberships_member_fields",
    style=api_client.ParameterStyle.FORM,
    schema=MembershipsMemberFieldsSchema,
    explode=True,
)
request_query_members = api_client.QueryParameter(
    name="members",
    style=api_client.ParameterStyle.FORM,
    schema=MembersSchema,
    explode=True,
)
request_query_member_fields = api_client.QueryParameter(
    name="member_fields",
    style=api_client.ParameterStyle.FORM,
    schema=MemberFieldsSchema,
    explode=True,
)
request_query_members_invited = api_client.QueryParameter(
    name="membersInvited",
    style=api_client.ParameterStyle.FORM,
    schema=MembersInvitedSchema,
    explode=True,
)
request_query_members_invited_fields = api_client.QueryParameter(
    name="membersInvited_fields",
    style=api_client.ParameterStyle.FORM,
    schema=MembersInvitedFieldsSchema,
    explode=True,
)
request_query_checklists = api_client.QueryParameter(
    name="checklists",
    style=api_client.ParameterStyle.FORM,
    schema=ChecklistsSchema,
    explode=True,
)
request_query_checklist_fields = api_client.QueryParameter(
    name="checklist_fields",
    style=api_client.ParameterStyle.FORM,
    schema=ChecklistFieldsSchema,
    explode=True,
)
request_query_organization = api_client.QueryParameter(
    name="organization",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationSchema,
    explode=True,
)
request_query_organization_fields = api_client.QueryParameter(
    name="organization_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationFieldsSchema,
    explode=True,
)
request_query_organization_memberships = api_client.QueryParameter(
    name="organization_memberships",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationMembershipsSchema,
    explode=True,
)
request_query_my_prefs = api_client.QueryParameter(
    name="myPrefs",
    style=api_client.ParameterStyle.FORM,
    schema=MyPrefsSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
# Path params
IdBoardSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idBoard': typing.Union[IdBoardSchema, str, ],
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


request_path_id_board = api_client.PathParameter(
    name="idBoard",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdBoardSchema,
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
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
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
        if actions_format is not None:
            _query_params["actions_format"] = actions_format
        if actions_since is not None:
            _query_params["actions_since"] = actions_since
        if actions_limit is not None:
            _query_params["actions_limit"] = actions_limit
        if action_fields is not None:
            _query_params["action_fields"] = action_fields
        if action_member is not None:
            _query_params["action_member"] = action_member
        if action_member_fields is not None:
            _query_params["action_member_fields"] = action_member_fields
        if action_member_creator is not None:
            _query_params["action_memberCreator"] = action_member_creator
        if action_member_creator_fields is not None:
            _query_params["action_memberCreator_fields"] = action_member_creator_fields
        if cards is not None:
            _query_params["cards"] = cards
        if card_fields is not None:
            _query_params["card_fields"] = card_fields
        if card_attachments is not None:
            _query_params["card_attachments"] = card_attachments
        if card_attachment_fields is not None:
            _query_params["card_attachment_fields"] = card_attachment_fields
        if card_checklists is not None:
            _query_params["card_checklists"] = card_checklists
        if card_stickers is not None:
            _query_params["card_stickers"] = card_stickers
        if board_stars is not None:
            _query_params["boardStars"] = board_stars
        if labels is not None:
            _query_params["labels"] = labels
        if label_fields is not None:
            _query_params["label_fields"] = label_fields
        if labels_limit is not None:
            _query_params["labels_limit"] = labels_limit
        if lists is not None:
            _query_params["lists"] = lists
        if list_fields is not None:
            _query_params["list_fields"] = list_fields
        if memberships is not None:
            _query_params["memberships"] = memberships
        if memberships_member is not None:
            _query_params["memberships_member"] = memberships_member
        if memberships_member_fields is not None:
            _query_params["memberships_member_fields"] = memberships_member_fields
        if members is not None:
            _query_params["members"] = members
        if member_fields is not None:
            _query_params["member_fields"] = member_fields
        if members_invited is not None:
            _query_params["membersInvited"] = members_invited
        if members_invited_fields is not None:
            _query_params["membersInvited_fields"] = members_invited_fields
        if checklists is not None:
            _query_params["checklists"] = checklists
        if checklist_fields is not None:
            _query_params["checklist_fields"] = checklist_fields
        if organization is not None:
            _query_params["organization"] = organization
        if organization_fields is not None:
            _query_params["organization_fields"] = organization_fields
        if organization_memberships is not None:
            _query_params["organization_memberships"] = organization_memberships
        if my_prefs is not None:
            _query_params["myPrefs"] = my_prefs
        if fields is not None:
            _query_params["fields"] = fields
        if id_board is not None:
            _path_params["idBoard"] = id_board
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
        getBoardsByIdBoard()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_board,
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
            request_query_actions_format,
            request_query_actions_since,
            request_query_actions_limit,
            request_query_action_fields,
            request_query_action_member,
            request_query_action_member_fields,
            request_query_action_member_creator,
            request_query_action_member_creator_fields,
            request_query_cards,
            request_query_card_fields,
            request_query_card_attachments,
            request_query_card_attachment_fields,
            request_query_card_checklists,
            request_query_card_stickers,
            request_query_board_stars,
            request_query_labels,
            request_query_label_fields,
            request_query_labels_limit,
            request_query_lists,
            request_query_list_fields,
            request_query_memberships,
            request_query_memberships_member,
            request_query_memberships_member_fields,
            request_query_members,
            request_query_member_fields,
            request_query_members_invited,
            request_query_members_invited_fields,
            request_query_checklists,
            request_query_checklist_fields,
            request_query_organization,
            request_query_organization_fields,
            request_query_organization_memberships,
            request_query_my_prefs,
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
            path_template='/boards/{idBoard}',
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
        getBoardsByIdBoard()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_board,
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
            request_query_actions_format,
            request_query_actions_since,
            request_query_actions_limit,
            request_query_action_fields,
            request_query_action_member,
            request_query_action_member_fields,
            request_query_action_member_creator,
            request_query_action_member_creator_fields,
            request_query_cards,
            request_query_card_fields,
            request_query_card_attachments,
            request_query_card_attachment_fields,
            request_query_card_checklists,
            request_query_card_stickers,
            request_query_board_stars,
            request_query_labels,
            request_query_label_fields,
            request_query_labels_limit,
            request_query_lists,
            request_query_list_fields,
            request_query_memberships,
            request_query_memberships_member,
            request_query_memberships_member_fields,
            request_query_members,
            request_query_member_fields,
            request_query_members_invited,
            request_query_members_invited_fields,
            request_query_checklists,
            request_query_checklist_fields,
            request_query_organization,
            request_query_organization_fields,
            request_query_organization_memberships,
            request_query_my_prefs,
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
            path_template='/boards/{idBoard}',
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
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_board=id_board,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_format=actions_format,
            actions_since=actions_since,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_member=action_member,
            action_member_fields=action_member_fields,
            action_member_creator=action_member_creator,
            action_member_creator_fields=action_member_creator_fields,
            cards=cards,
            card_fields=card_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_checklists=card_checklists,
            card_stickers=card_stickers,
            board_stars=board_stars,
            labels=labels,
            label_fields=label_fields,
            labels_limit=labels_limit,
            lists=lists,
            list_fields=list_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
            checklists=checklists,
            checklist_fields=checklist_fields,
            organization=organization,
            organization_fields=organization_fields,
            organization_memberships=organization_memberships,
            my_prefs=my_prefs,
            fields=fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_id(
        self,
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_board=id_board,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_format=actions_format,
            actions_since=actions_since,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_member=action_member,
            action_member_fields=action_member_fields,
            action_member_creator=action_member_creator,
            action_member_creator_fields=action_member_creator_fields,
            cards=cards,
            card_fields=card_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_checklists=card_checklists,
            card_stickers=card_stickers,
            board_stars=board_stars,
            labels=labels,
            label_fields=label_fields,
            labels_limit=labels_limit,
            lists=lists,
            list_fields=list_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
            checklists=checklists,
            checklist_fields=checklist_fields,
            organization=organization,
            organization_fields=organization_fields,
            organization_memberships=organization_memberships,
            my_prefs=my_prefs,
            fields=fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetById(BaseApi):

    async def aget_by_id(
        self,
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_by_id(
            id_board=id_board,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_format=actions_format,
            actions_since=actions_since,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_member=action_member,
            action_member_fields=action_member_fields,
            action_member_creator=action_member_creator,
            action_member_creator_fields=action_member_creator_fields,
            cards=cards,
            card_fields=card_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_checklists=card_checklists,
            card_stickers=card_stickers,
            board_stars=board_stars,
            labels=labels,
            label_fields=label_fields,
            labels_limit=labels_limit,
            lists=lists,
            list_fields=list_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
            checklists=checklists,
            checklist_fields=checklist_fields,
            organization=organization,
            organization_fields=organization_fields,
            organization_memberships=organization_memberships,
            my_prefs=my_prefs,
            fields=fields,
            **kwargs,
        )
    
    
    def get_by_id(
        self,
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_by_id(
            id_board=id_board,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_format=actions_format,
            actions_since=actions_since,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_member=action_member,
            action_member_fields=action_member_fields,
            action_member_creator=action_member_creator,
            action_member_creator_fields=action_member_creator_fields,
            cards=cards,
            card_fields=card_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_checklists=card_checklists,
            card_stickers=card_stickers,
            board_stars=board_stars,
            labels=labels,
            label_fields=label_fields,
            labels_limit=labels_limit,
            lists=lists,
            list_fields=list_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
            checklists=checklists,
            checklist_fields=checklist_fields,
            organization=organization,
            organization_fields=organization_fields,
            organization_memberships=organization_memberships,
            my_prefs=my_prefs,
            fields=fields,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_board=id_board,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_format=actions_format,
            actions_since=actions_since,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_member=action_member,
            action_member_fields=action_member_fields,
            action_member_creator=action_member_creator,
            action_member_creator_fields=action_member_creator_fields,
            cards=cards,
            card_fields=card_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_checklists=card_checklists,
            card_stickers=card_stickers,
            board_stars=board_stars,
            labels=labels,
            label_fields=label_fields,
            labels_limit=labels_limit,
            lists=lists,
            list_fields=list_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
            checklists=checklists,
            checklist_fields=checklist_fields,
            organization=organization,
            organization_fields=organization_fields,
            organization_memberships=organization_memberships,
            my_prefs=my_prefs,
            fields=fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_board: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        action_member: typing.Optional[str] = None,
        action_member_fields: typing.Optional[str] = None,
        action_member_creator: typing.Optional[str] = None,
        action_member_creator_fields: typing.Optional[str] = None,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        card_attachment_fields: typing.Optional[str] = None,
        card_checklists: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        board_stars: typing.Optional[str] = None,
        labels: typing.Optional[str] = None,
        label_fields: typing.Optional[str] = None,
        labels_limit: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        checklist_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organization_memberships: typing.Optional[str] = None,
        my_prefs: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_board=id_board,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_format=actions_format,
            actions_since=actions_since,
            actions_limit=actions_limit,
            action_fields=action_fields,
            action_member=action_member,
            action_member_fields=action_member_fields,
            action_member_creator=action_member_creator,
            action_member_creator_fields=action_member_creator_fields,
            cards=cards,
            card_fields=card_fields,
            card_attachments=card_attachments,
            card_attachment_fields=card_attachment_fields,
            card_checklists=card_checklists,
            card_stickers=card_stickers,
            board_stars=board_stars,
            labels=labels,
            label_fields=label_fields,
            labels_limit=labels_limit,
            lists=lists,
            list_fields=list_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
            checklists=checklists,
            checklist_fields=checklist_fields,
            organization=organization,
            organization_fields=organization_fields,
            organization_memberships=organization_memberships,
            my_prefs=my_prefs,
            fields=fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

