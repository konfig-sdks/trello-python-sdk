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
AttachmentsSchema = schemas.StrSchema
AttachmentFieldsSchema = schemas.StrSchema
MembersSchema = schemas.StrSchema
MemberFieldsSchema = schemas.StrSchema
CheckItemStatesSchema = schemas.StrSchema
ChecklistsSchema = schemas.StrSchema
BoardSchema = schemas.StrSchema
BoardFieldsSchema = schemas.StrSchema
ModelListSchema = schemas.StrSchema
ListFieldsSchema = schemas.StrSchema
FilterSchema = schemas.StrSchema
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
        'attachments': typing.Union[AttachmentsSchema, str, ],
        'attachment_fields': typing.Union[AttachmentFieldsSchema, str, ],
        'members': typing.Union[MembersSchema, str, ],
        'member_fields': typing.Union[MemberFieldsSchema, str, ],
        'checkItemStates': typing.Union[CheckItemStatesSchema, str, ],
        'checklists': typing.Union[ChecklistsSchema, str, ],
        'board': typing.Union[BoardSchema, str, ],
        'board_fields': typing.Union[BoardFieldsSchema, str, ],
        'list': typing.Union[ModelListSchema, str, ],
        'list_fields': typing.Union[ListFieldsSchema, str, ],
        'filter': typing.Union[FilterSchema, str, ],
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
request_query_attachments = api_client.QueryParameter(
    name="attachments",
    style=api_client.ParameterStyle.FORM,
    schema=AttachmentsSchema,
    explode=True,
)
request_query_attachment_fields = api_client.QueryParameter(
    name="attachment_fields",
    style=api_client.ParameterStyle.FORM,
    schema=AttachmentFieldsSchema,
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
request_query_check_item_states = api_client.QueryParameter(
    name="checkItemStates",
    style=api_client.ParameterStyle.FORM,
    schema=CheckItemStatesSchema,
    explode=True,
)
request_query_checklists = api_client.QueryParameter(
    name="checklists",
    style=api_client.ParameterStyle.FORM,
    schema=ChecklistsSchema,
    explode=True,
)
request_query_board = api_client.QueryParameter(
    name="board",
    style=api_client.ParameterStyle.FORM,
    schema=BoardSchema,
    explode=True,
)
request_query_board_fields = api_client.QueryParameter(
    name="board_fields",
    style=api_client.ParameterStyle.FORM,
    schema=BoardFieldsSchema,
    explode=True,
)
request_query__list = api_client.QueryParameter(
    name="list",
    style=api_client.ParameterStyle.FORM,
    schema=ModelListSchema,
    explode=True,
)
request_query_list_fields = api_client.QueryParameter(
    name="list_fields",
    style=api_client.ParameterStyle.FORM,
    schema=ListFieldsSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
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
IdMemberSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idBoard': typing.Union[IdBoardSchema, str, ],
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


request_path_id_board = api_client.PathParameter(
    name="idBoard",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdBoardSchema,
    required=True,
)
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

    def _get_members_cards_by_id_board_by_id_member_mapped_args(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if actions is not None:
            _query_params["actions"] = actions
        if attachments is not None:
            _query_params["attachments"] = attachments
        if attachment_fields is not None:
            _query_params["attachment_fields"] = attachment_fields
        if members is not None:
            _query_params["members"] = members
        if member_fields is not None:
            _query_params["member_fields"] = member_fields
        if check_item_states is not None:
            _query_params["checkItemStates"] = check_item_states
        if checklists is not None:
            _query_params["checklists"] = checklists
        if board is not None:
            _query_params["board"] = board
        if board_fields is not None:
            _query_params["board_fields"] = board_fields
        if _list is not None:
            _query_params["list"] = _list
        if list_fields is not None:
            _query_params["list_fields"] = list_fields
        if filter is not None:
            _query_params["filter"] = filter
        if fields is not None:
            _query_params["fields"] = fields
        if id_board is not None:
            _path_params["idBoard"] = id_board
        if id_member is not None:
            _path_params["idMember"] = id_member
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_members_cards_by_id_board_by_id_member_oapg(
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
        getBoardsMembersCardsByIdBoardByIdMember()
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
            request_query_attachments,
            request_query_attachment_fields,
            request_query_members,
            request_query_member_fields,
            request_query_check_item_states,
            request_query_checklists,
            request_query_board,
            request_query_board_fields,
            request_query__list,
            request_query_list_fields,
            request_query_filter,
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
            path_template='/boards/{idBoard}/members/{idMember}/cards',
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


    def _get_members_cards_by_id_board_by_id_member_oapg(
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
        getBoardsMembersCardsByIdBoardByIdMember()
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
            request_query_attachments,
            request_query_attachment_fields,
            request_query_members,
            request_query_member_fields,
            request_query_check_item_states,
            request_query_checklists,
            request_query_board,
            request_query_board_fields,
            request_query__list,
            request_query_list_fields,
            request_query_filter,
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
            path_template='/boards/{idBoard}/members/{idMember}/cards',
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


class GetMembersCardsByIdBoardByIdMemberRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_members_cards_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_members_cards_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            actions=actions,
            attachments=attachments,
            attachment_fields=attachment_fields,
            members=members,
            member_fields=member_fields,
            check_item_states=check_item_states,
            checklists=checklists,
            board=board,
            board_fields=board_fields,
            _list=_list,
            list_fields=list_fields,
            filter=filter,
            fields=fields,
        )
        return await self._aget_members_cards_by_id_board_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_members_cards_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_members_cards_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            actions=actions,
            attachments=attachments,
            attachment_fields=attachment_fields,
            members=members,
            member_fields=member_fields,
            check_item_states=check_item_states,
            checklists=checklists,
            board=board,
            board_fields=board_fields,
            _list=_list,
            list_fields=list_fields,
            filter=filter,
            fields=fields,
        )
        return self._get_members_cards_by_id_board_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetMembersCardsByIdBoardByIdMember(BaseApi):

    async def aget_members_cards_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_members_cards_by_id_board_by_id_member(
            id_board=id_board,
            id_member=id_member,
            actions=actions,
            attachments=attachments,
            attachment_fields=attachment_fields,
            members=members,
            member_fields=member_fields,
            check_item_states=check_item_states,
            checklists=checklists,
            board=board,
            board_fields=board_fields,
            _list=_list,
            list_fields=list_fields,
            filter=filter,
            fields=fields,
            **kwargs,
        )
    
    
    def get_members_cards_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_members_cards_by_id_board_by_id_member(
            id_board=id_board,
            id_member=id_member,
            actions=actions,
            attachments=attachments,
            attachment_fields=attachment_fields,
            members=members,
            member_fields=member_fields,
            check_item_states=check_item_states,
            checklists=checklists,
            board=board,
            board_fields=board_fields,
            _list=_list,
            list_fields=list_fields,
            filter=filter,
            fields=fields,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_members_cards_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            actions=actions,
            attachments=attachments,
            attachment_fields=attachment_fields,
            members=members,
            member_fields=member_fields,
            check_item_states=check_item_states,
            checklists=checklists,
            board=board,
            board_fields=board_fields,
            _list=_list,
            list_fields=list_fields,
            filter=filter,
            fields=fields,
        )
        return await self._aget_members_cards_by_id_board_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_board: str,
        id_member: str,
        actions: typing.Optional[str] = None,
        attachments: typing.Optional[str] = None,
        attachment_fields: typing.Optional[str] = None,
        members: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        check_item_states: typing.Optional[str] = None,
        checklists: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        list_fields: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_members_cards_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            actions=actions,
            attachments=attachments,
            attachment_fields=attachment_fields,
            members=members,
            member_fields=member_fields,
            check_item_states=check_item_states,
            checklists=checklists,
            board=board,
            board_fields=board_fields,
            _list=_list,
            list_fields=list_fields,
            filter=filter,
            fields=fields,
        )
        return self._get_members_cards_by_id_board_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
        )

