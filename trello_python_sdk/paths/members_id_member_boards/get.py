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
FilterSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema
ActionsSchema = schemas.StrSchema
ActionsEntitiesSchema = schemas.StrSchema
ActionsLimitSchema = schemas.StrSchema
ActionsFormatSchema = schemas.StrSchema
ActionsSinceSchema = schemas.StrSchema
ActionFieldsSchema = schemas.StrSchema
MembershipsSchema = schemas.StrSchema
OrganizationSchema = schemas.StrSchema
OrganizationFieldsSchema = schemas.StrSchema
ListsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'filter': typing.Union[FilterSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
        'actions': typing.Union[ActionsSchema, str, ],
        'actions_entities': typing.Union[ActionsEntitiesSchema, str, ],
        'actions_limit': typing.Union[ActionsLimitSchema, str, ],
        'actions_format': typing.Union[ActionsFormatSchema, str, ],
        'actions_since': typing.Union[ActionsSinceSchema, str, ],
        'action_fields': typing.Union[ActionFieldsSchema, str, ],
        'memberships': typing.Union[MembershipsSchema, str, ],
        'organization': typing.Union[OrganizationSchema, str, ],
        'organization_fields': typing.Union[OrganizationFieldsSchema, str, ],
        'lists': typing.Union[ListsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
request_query_actions_limit = api_client.QueryParameter(
    name="actions_limit",
    style=api_client.ParameterStyle.FORM,
    schema=ActionsLimitSchema,
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
request_query_lists = api_client.QueryParameter(
    name="lists",
    style=api_client.ParameterStyle.FORM,
    schema=ListsSchema,
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

    def _get_boards_by_id_member_mapped_args(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if filter is not None:
            _query_params["filter"] = filter
        if fields is not None:
            _query_params["fields"] = fields
        if actions is not None:
            _query_params["actions"] = actions
        if actions_entities is not None:
            _query_params["actions_entities"] = actions_entities
        if actions_limit is not None:
            _query_params["actions_limit"] = actions_limit
        if actions_format is not None:
            _query_params["actions_format"] = actions_format
        if actions_since is not None:
            _query_params["actions_since"] = actions_since
        if action_fields is not None:
            _query_params["action_fields"] = action_fields
        if memberships is not None:
            _query_params["memberships"] = memberships
        if organization is not None:
            _query_params["organization"] = organization
        if organization_fields is not None:
            _query_params["organization_fields"] = organization_fields
        if lists is not None:
            _query_params["lists"] = lists
        if id_member is not None:
            _path_params["idMember"] = id_member
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_boards_by_id_member_oapg(
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
        getMembersBoardsByIdMember()
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
            request_query_filter,
            request_query_fields,
            request_query_actions,
            request_query_actions_entities,
            request_query_actions_limit,
            request_query_actions_format,
            request_query_actions_since,
            request_query_action_fields,
            request_query_memberships,
            request_query_organization,
            request_query_organization_fields,
            request_query_lists,
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
            path_template='/members/{idMember}/boards',
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


    def _get_boards_by_id_member_oapg(
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
        getMembersBoardsByIdMember()
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
            request_query_filter,
            request_query_fields,
            request_query_actions,
            request_query_actions_entities,
            request_query_actions_limit,
            request_query_actions_format,
            request_query_actions_since,
            request_query_action_fields,
            request_query_memberships,
            request_query_organization,
            request_query_organization_fields,
            request_query_lists,
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
            path_template='/members/{idMember}/boards',
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


class GetBoardsByIdMemberRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_boards_by_id_member(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_boards_by_id_member_mapped_args(
            id_member=id_member,
            filter=filter,
            fields=fields,
            actions=actions,
            actions_entities=actions_entities,
            actions_limit=actions_limit,
            actions_format=actions_format,
            actions_since=actions_since,
            action_fields=action_fields,
            memberships=memberships,
            organization=organization,
            organization_fields=organization_fields,
            lists=lists,
        )
        return await self._aget_boards_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_boards_by_id_member(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_boards_by_id_member_mapped_args(
            id_member=id_member,
            filter=filter,
            fields=fields,
            actions=actions,
            actions_entities=actions_entities,
            actions_limit=actions_limit,
            actions_format=actions_format,
            actions_since=actions_since,
            action_fields=action_fields,
            memberships=memberships,
            organization=organization,
            organization_fields=organization_fields,
            lists=lists,
        )
        return self._get_boards_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetBoardsByIdMember(BaseApi):

    async def aget_boards_by_id_member(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_boards_by_id_member(
            id_member=id_member,
            filter=filter,
            fields=fields,
            actions=actions,
            actions_entities=actions_entities,
            actions_limit=actions_limit,
            actions_format=actions_format,
            actions_since=actions_since,
            action_fields=action_fields,
            memberships=memberships,
            organization=organization,
            organization_fields=organization_fields,
            lists=lists,
            **kwargs,
        )
    
    
    def get_boards_by_id_member(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_boards_by_id_member(
            id_member=id_member,
            filter=filter,
            fields=fields,
            actions=actions,
            actions_entities=actions_entities,
            actions_limit=actions_limit,
            actions_format=actions_format,
            actions_since=actions_since,
            action_fields=action_fields,
            memberships=memberships,
            organization=organization,
            organization_fields=organization_fields,
            lists=lists,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_boards_by_id_member_mapped_args(
            id_member=id_member,
            filter=filter,
            fields=fields,
            actions=actions,
            actions_entities=actions_entities,
            actions_limit=actions_limit,
            actions_format=actions_format,
            actions_since=actions_since,
            action_fields=action_fields,
            memberships=memberships,
            organization=organization,
            organization_fields=organization_fields,
            lists=lists,
        )
        return await self._aget_boards_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_member: str,
        filter: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        actions: typing.Optional[str] = None,
        actions_entities: typing.Optional[str] = None,
        actions_limit: typing.Optional[str] = None,
        actions_format: typing.Optional[str] = None,
        actions_since: typing.Optional[str] = None,
        action_fields: typing.Optional[str] = None,
        memberships: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        lists: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_boards_by_id_member_mapped_args(
            id_member=id_member,
            filter=filter,
            fields=fields,
            actions=actions,
            actions_entities=actions_entities,
            actions_limit=actions_limit,
            actions_format=actions_format,
            actions_since=actions_since,
            action_fields=action_fields,
            memberships=memberships,
            organization=organization,
            organization_fields=organization_fields,
            lists=lists,
        )
        return self._get_boards_by_id_member_oapg(
            query_params=args.query,
            path_params=args.path,
        )

