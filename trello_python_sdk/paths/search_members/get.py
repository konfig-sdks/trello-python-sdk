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
QuerySchema = schemas.StrSchema
LimitSchema = schemas.StrSchema
IdBoardSchema = schemas.StrSchema
IdOrganizationSchema = schemas.StrSchema
OnlyOrgMembersSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'query': typing.Union[QuerySchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, str, ],
        'idBoard': typing.Union[IdBoardSchema, str, ],
        'idOrganization': typing.Union[IdOrganizationSchema, str, ],
        'onlyOrgMembers': typing.Union[OnlyOrgMembersSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_query = api_client.QueryParameter(
    name="query",
    style=api_client.ParameterStyle.FORM,
    schema=QuerySchema,
    required=True,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_id_board = api_client.QueryParameter(
    name="idBoard",
    style=api_client.ParameterStyle.FORM,
    schema=IdBoardSchema,
    explode=True,
)
request_query_id_organization = api_client.QueryParameter(
    name="idOrganization",
    style=api_client.ParameterStyle.FORM,
    schema=IdOrganizationSchema,
    explode=True,
)
request_query_only_org_members = api_client.QueryParameter(
    name="onlyOrgMembers",
    style=api_client.ParameterStyle.FORM,
    schema=OnlyOrgMembersSchema,
    explode=True,
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

    def _find_members_mapped_args(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if query is not None:
            _query_params["query"] = query
        if limit is not None:
            _query_params["limit"] = limit
        if id_board is not None:
            _query_params["idBoard"] = id_board
        if id_organization is not None:
            _query_params["idOrganization"] = id_organization
        if only_org_members is not None:
            _query_params["onlyOrgMembers"] = only_org_members
        args.query = _query_params
        return args

    async def _afind_members_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        getSearchMembers()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_limit,
            request_query_id_board,
            request_query_id_organization,
            request_query_only_org_members,
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
            path_template='/search/members',
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


    def _find_members_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        getSearchMembers()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_limit,
            request_query_id_board,
            request_query_id_organization,
            request_query_only_org_members,
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
            path_template='/search/members',
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


class FindMembersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def afind_members(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_members_mapped_args(
            query=query,
            limit=limit,
            id_board=id_board,
            id_organization=id_organization,
            only_org_members=only_org_members,
        )
        return await self._afind_members_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def find_members(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_members_mapped_args(
            query=query,
            limit=limit,
            id_board=id_board,
            id_organization=id_organization,
            only_org_members=only_org_members,
        )
        return self._find_members_oapg(
            query_params=args.query,
        )

class FindMembers(BaseApi):

    async def afind_members(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.afind_members(
            query=query,
            limit=limit,
            id_board=id_board,
            id_organization=id_organization,
            only_org_members=only_org_members,
            **kwargs,
        )
    
    
    def find_members(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.find_members(
            query=query,
            limit=limit,
            id_board=id_board,
            id_organization=id_organization,
            only_org_members=only_org_members,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._find_members_mapped_args(
            query=query,
            limit=limit,
            id_board=id_board,
            id_organization=id_organization,
            only_org_members=only_org_members,
        )
        return await self._afind_members_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        query: str,
        limit: typing.Optional[str] = None,
        id_board: typing.Optional[str] = None,
        id_organization: typing.Optional[str] = None,
        only_org_members: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._find_members_mapped_args(
            query=query,
            limit=limit,
            id_board=id_board,
            id_organization=id_organization,
            only_org_members=only_org_members,
        )
        return self._find_members_oapg(
            query_params=args.query,
        )

