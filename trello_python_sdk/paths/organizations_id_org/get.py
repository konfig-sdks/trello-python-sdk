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

from . import path

# Query params
ActionsSchema = schemas.StrSchema
ActionsEntitiesSchema = schemas.StrSchema
ActionsDisplaySchema = schemas.StrSchema
ActionsLimitSchema = schemas.StrSchema
ActionFieldsSchema = schemas.StrSchema
MembershipsSchema = schemas.StrSchema
MembershipsMemberSchema = schemas.StrSchema
MembershipsMemberFieldsSchema = schemas.StrSchema
MembersSchema = schemas.StrSchema
MemberFieldsSchema = schemas.StrSchema
MemberActivitySchema = schemas.StrSchema
MembersInvitedSchema = schemas.StrSchema
MembersInvitedFieldsSchema = schemas.StrSchema
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
PaidAccountSchema = schemas.StrSchema
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
        'memberships': typing.Union[MembershipsSchema, str, ],
        'memberships_member': typing.Union[MembershipsMemberSchema, str, ],
        'memberships_member_fields': typing.Union[MembershipsMemberFieldsSchema, str, ],
        'members': typing.Union[MembersSchema, str, ],
        'member_fields': typing.Union[MemberFieldsSchema, str, ],
        'member_activity': typing.Union[MemberActivitySchema, str, ],
        'membersInvited': typing.Union[MembersInvitedSchema, str, ],
        'membersInvited_fields': typing.Union[MembersInvitedFieldsSchema, str, ],
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
        'paid_account': typing.Union[PaidAccountSchema, str, ],
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
request_query_member_activity = api_client.QueryParameter(
    name="member_activity",
    style=api_client.ParameterStyle.FORM,
    schema=MemberActivitySchema,
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
request_query_paid_account = api_client.QueryParameter(
    name="paid_account",
    style=api_client.ParameterStyle.FORM,
    schema=PaidAccountSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
# Path params
IdOrgSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idOrg': typing.Union[IdOrgSchema, str, ],
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


request_path_id_org = api_client.PathParameter(
    name="idOrg",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdOrgSchema,
    required=True,
)
_auth = [
    'api_key',
    'api_token',
]


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}


class BaseApi(api_client.Api):

    def _get_by_id_org_mapped_args(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
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
        if member_activity is not None:
            _query_params["member_activity"] = member_activity
        if members_invited is not None:
            _query_params["membersInvited"] = members_invited
        if members_invited_fields is not None:
            _query_params["membersInvited_fields"] = members_invited_fields
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
        if paid_account is not None:
            _query_params["paid_account"] = paid_account
        if fields is not None:
            _query_params["fields"] = fields
        if id_org is not None:
            _path_params["idOrg"] = id_org
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_by_id_org_oapg(
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
        getOrganizationsByIdOrg()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_org,
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
            request_query_memberships,
            request_query_memberships_member,
            request_query_memberships_member_fields,
            request_query_members,
            request_query_member_fields,
            request_query_member_activity,
            request_query_members_invited,
            request_query_members_invited_fields,
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
            request_query_paid_account,
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
            path_template='/organizations/{idOrg}',
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


    def _get_by_id_org_oapg(
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
        getOrganizationsByIdOrg()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_org,
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
            request_query_memberships,
            request_query_memberships_member,
            request_query_memberships_member_fields,
            request_query_members,
            request_query_member_fields,
            request_query_member_activity,
            request_query_members_invited,
            request_query_members_invited_fields,
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
            request_query_paid_account,
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
            path_template='/organizations/{idOrg}',
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


class GetByIdOrgRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_by_id_org(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_org_mapped_args(
            id_org=id_org,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            member_activity=member_activity,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
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
            paid_account=paid_account,
            fields=fields,
        )
        return await self._aget_by_id_org_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_id_org(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_org_mapped_args(
            id_org=id_org,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            member_activity=member_activity,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
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
            paid_account=paid_account,
            fields=fields,
        )
        return self._get_by_id_org_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetByIdOrg(BaseApi):

    async def aget_by_id_org(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_by_id_org(
            id_org=id_org,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            member_activity=member_activity,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
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
            paid_account=paid_account,
            fields=fields,
            **kwargs,
        )
    
    
    def get_by_id_org(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_by_id_org(
            id_org=id_org,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            member_activity=member_activity,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
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
            paid_account=paid_account,
            fields=fields,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_org_mapped_args(
            id_org=id_org,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            member_activity=member_activity,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
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
            paid_account=paid_account,
            fields=fields,
        )
        return await self._aget_by_id_org_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_org: str,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_display: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        memberships_member: typing.Optional[str] = None,
        memberships_member_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        member_activity: typing.Optional[str] = None,
        members_invited: typing.Optional[str] = None,
        members_invited_fields: typing.Optional[str] = None,
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
        paid_account: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_org_mapped_args(
            id_org=id_org,
            actions=actions,
            actions_entities=actions_entities,
            actions_display=actions_display,
            actions_limit=actions_limit,
            action_fields=action_fields,
            memberships=memberships,
            memberships_member=memberships_member,
            memberships_member_fields=memberships_member_fields,
            members=members,
            member_fields=member_fields,
            member_activity=member_activity,
            members_invited=members_invited,
            members_invited_fields=members_invited_fields,
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
            paid_account=paid_account,
            fields=fields,
        )
        return self._get_by_id_org_oapg(
            query_params=args.query,
            path_params=args.path,
        )

