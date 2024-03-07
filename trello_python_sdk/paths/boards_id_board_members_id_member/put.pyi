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

from trello_python_sdk.model.boards_members import BoardsMembers as BoardsMembersSchema

from trello_python_sdk.type.boards_members import BoardsMembers

from ...api_client import Dictionary
from trello_python_sdk.pydantic.boards_members import BoardsMembers as BoardsMembersPydantic

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
# body param
SchemaForRequestBodyApplicationJson = BoardsMembersSchema


request_body_boards_members = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
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

    def _update_members_by_id_board_by_id_member_mapped_args(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if email is not None:
            _body["email"] = email
        if full_name is not None:
            _body["fullName"] = full_name
        if type is not None:
            _body["type"] = type
        args.body = _body
        if id_board is not None:
            _path_params["idBoard"] = id_board
        if id_member is not None:
            _path_params["idMember"] = id_member
        args.path = _path_params
        return args

    async def _aupdate_members_by_id_board_by_id_member_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        updateBoardsMembersByIdBoardByIdMember()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/boards/{idBoard}/members/{idMember}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_boards_members.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _update_members_by_id_board_by_id_member_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        updateBoardsMembersByIdBoardByIdMember()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/boards/{idBoard}/members/{idMember}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_boards_members.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class UpdateMembersByIdBoardByIdMemberRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_members_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_members_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            email=email,
            full_name=full_name,
            type=type,
        )
        return await self._aupdate_members_by_id_board_by_id_member_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_members_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_members_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            email=email,
            full_name=full_name,
            type=type,
        )
        return self._update_members_by_id_board_by_id_member_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateMembersByIdBoardByIdMember(BaseApi):

    async def aupdate_members_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_members_by_id_board_by_id_member(
            id_board=id_board,
            id_member=id_member,
            email=email,
            full_name=full_name,
            type=type,
            **kwargs,
        )
    
    
    def update_members_by_id_board_by_id_member(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_members_by_id_board_by_id_member(
            id_board=id_board,
            id_member=id_member,
            email=email,
            full_name=full_name,
            type=type,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_members_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            email=email,
            full_name=full_name,
            type=type,
        )
        return await self._aupdate_members_by_id_board_by_id_member_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        id_board: str,
        id_member: str,
        email: typing.Optional[str] = None,
        full_name: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_members_by_id_board_by_id_member_mapped_args(
            id_board=id_board,
            id_member=id_member,
            email=email,
            full_name=full_name,
            type=type,
        )
        return self._update_members_by_id_board_by_id_member_oapg(
            body=args.body,
            path_params=args.path,
        )

