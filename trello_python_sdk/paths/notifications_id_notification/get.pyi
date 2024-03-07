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
DisplaySchema = schemas.StrSchema
EntitiesSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema
MemberCreatorSchema = schemas.StrSchema
MemberCreatorFieldsSchema = schemas.StrSchema
BoardSchema = schemas.StrSchema
BoardFieldsSchema = schemas.StrSchema
ModelListSchema = schemas.StrSchema
CardSchema = schemas.StrSchema
CardFieldsSchema = schemas.StrSchema
OrganizationSchema = schemas.StrSchema
OrganizationFieldsSchema = schemas.StrSchema
MemberSchema = schemas.StrSchema
MemberFieldsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'display': typing.Union[DisplaySchema, str, ],
        'entities': typing.Union[EntitiesSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
        'memberCreator': typing.Union[MemberCreatorSchema, str, ],
        'memberCreator_fields': typing.Union[MemberCreatorFieldsSchema, str, ],
        'board': typing.Union[BoardSchema, str, ],
        'board_fields': typing.Union[BoardFieldsSchema, str, ],
        'list': typing.Union[ModelListSchema, str, ],
        'card': typing.Union[CardSchema, str, ],
        'card_fields': typing.Union[CardFieldsSchema, str, ],
        'organization': typing.Union[OrganizationSchema, str, ],
        'organization_fields': typing.Union[OrganizationFieldsSchema, str, ],
        'member': typing.Union[MemberSchema, str, ],
        'member_fields': typing.Union[MemberFieldsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_display = api_client.QueryParameter(
    name="display",
    style=api_client.ParameterStyle.FORM,
    schema=DisplaySchema,
    explode=True,
)
request_query_entities = api_client.QueryParameter(
    name="entities",
    style=api_client.ParameterStyle.FORM,
    schema=EntitiesSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
request_query_member_creator = api_client.QueryParameter(
    name="memberCreator",
    style=api_client.ParameterStyle.FORM,
    schema=MemberCreatorSchema,
    explode=True,
)
request_query_member_creator_fields = api_client.QueryParameter(
    name="memberCreator_fields",
    style=api_client.ParameterStyle.FORM,
    schema=MemberCreatorFieldsSchema,
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
request_query_card = api_client.QueryParameter(
    name="card",
    style=api_client.ParameterStyle.FORM,
    schema=CardSchema,
    explode=True,
)
request_query_card_fields = api_client.QueryParameter(
    name="card_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CardFieldsSchema,
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
request_query_member = api_client.QueryParameter(
    name="member",
    style=api_client.ParameterStyle.FORM,
    schema=MemberSchema,
    explode=True,
)
request_query_member_fields = api_client.QueryParameter(
    name="member_fields",
    style=api_client.ParameterStyle.FORM,
    schema=MemberFieldsSchema,
    explode=True,
)
# Path params
IdNotificationSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idNotification': typing.Union[IdNotificationSchema, str, ],
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


request_path_id_notification = api_client.PathParameter(
    name="idNotification",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdNotificationSchema,
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
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if display is not None:
            _query_params["display"] = display
        if entities is not None:
            _query_params["entities"] = entities
        if fields is not None:
            _query_params["fields"] = fields
        if member_creator is not None:
            _query_params["memberCreator"] = member_creator
        if member_creator_fields is not None:
            _query_params["memberCreator_fields"] = member_creator_fields
        if board is not None:
            _query_params["board"] = board
        if board_fields is not None:
            _query_params["board_fields"] = board_fields
        if _list is not None:
            _query_params["list"] = _list
        if card is not None:
            _query_params["card"] = card
        if card_fields is not None:
            _query_params["card_fields"] = card_fields
        if organization is not None:
            _query_params["organization"] = organization
        if organization_fields is not None:
            _query_params["organization_fields"] = organization_fields
        if member is not None:
            _query_params["member"] = member
        if member_fields is not None:
            _query_params["member_fields"] = member_fields
        if id_notification is not None:
            _path_params["idNotification"] = id_notification
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
        getNotificationsByIdNotification()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_notification,
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
            request_query_display,
            request_query_entities,
            request_query_fields,
            request_query_member_creator,
            request_query_member_creator_fields,
            request_query_board,
            request_query_board_fields,
            request_query__list,
            request_query_card,
            request_query_card_fields,
            request_query_organization,
            request_query_organization_fields,
            request_query_member,
            request_query_member_fields,
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
            path_template='/notifications/{idNotification}',
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
        getNotificationsByIdNotification()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_notification,
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
            request_query_display,
            request_query_entities,
            request_query_fields,
            request_query_member_creator,
            request_query_member_creator_fields,
            request_query_board,
            request_query_board_fields,
            request_query__list,
            request_query_card,
            request_query_card_fields,
            request_query_organization,
            request_query_organization_fields,
            request_query_member,
            request_query_member_fields,
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
            path_template='/notifications/{idNotification}',
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
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_notification=id_notification,
            display=display,
            entities=entities,
            fields=fields,
            member_creator=member_creator,
            member_creator_fields=member_creator_fields,
            board=board,
            board_fields=board_fields,
            _list=_list,
            card=card,
            card_fields=card_fields,
            organization=organization,
            organization_fields=organization_fields,
            member=member,
            member_fields=member_fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_id(
        self,
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_notification=id_notification,
            display=display,
            entities=entities,
            fields=fields,
            member_creator=member_creator,
            member_creator_fields=member_creator_fields,
            board=board,
            board_fields=board_fields,
            _list=_list,
            card=card,
            card_fields=card_fields,
            organization=organization,
            organization_fields=organization_fields,
            member=member,
            member_fields=member_fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetById(BaseApi):

    async def aget_by_id(
        self,
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_by_id(
            id_notification=id_notification,
            display=display,
            entities=entities,
            fields=fields,
            member_creator=member_creator,
            member_creator_fields=member_creator_fields,
            board=board,
            board_fields=board_fields,
            _list=_list,
            card=card,
            card_fields=card_fields,
            organization=organization,
            organization_fields=organization_fields,
            member=member,
            member_fields=member_fields,
            **kwargs,
        )
    
    
    def get_by_id(
        self,
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_by_id(
            id_notification=id_notification,
            display=display,
            entities=entities,
            fields=fields,
            member_creator=member_creator,
            member_creator_fields=member_creator_fields,
            board=board,
            board_fields=board_fields,
            _list=_list,
            card=card,
            card_fields=card_fields,
            organization=organization,
            organization_fields=organization_fields,
            member=member,
            member_fields=member_fields,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_notification=id_notification,
            display=display,
            entities=entities,
            fields=fields,
            member_creator=member_creator,
            member_creator_fields=member_creator_fields,
            board=board,
            board_fields=board_fields,
            _list=_list,
            card=card,
            card_fields=card_fields,
            organization=organization,
            organization_fields=organization_fields,
            member=member,
            member_fields=member_fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_notification: str,
        display: typing.Optional[str] = None,
        entities: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        member_creator: typing.Optional[str] = None,
        member_creator_fields: typing.Optional[str] = None,
        board: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        _list: typing.Optional[str] = None,
        card: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        organization: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        member: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_notification=id_notification,
            display=display,
            entities=entities,
            fields=fields,
            member_creator=member_creator,
            member_creator_fields=member_creator_fields,
            board=board,
            board_fields=board_fields,
            _list=_list,
            card=card,
            card_fields=card_fields,
            organization=organization,
            organization_fields=organization_fields,
            member=member,
            member_fields=member_fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

