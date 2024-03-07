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
CardsSchema = schemas.StrSchema
CardFieldsSchema = schemas.StrSchema
CheckItemsSchema = schemas.StrSchema
CheckItemFieldsSchema = schemas.StrSchema
FieldsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'cards': typing.Union[CardsSchema, str, ],
        'card_fields': typing.Union[CardFieldsSchema, str, ],
        'checkItems': typing.Union[CheckItemsSchema, str, ],
        'checkItem_fields': typing.Union[CheckItemFieldsSchema, str, ],
        'fields': typing.Union[FieldsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
request_query_check_items = api_client.QueryParameter(
    name="checkItems",
    style=api_client.ParameterStyle.FORM,
    schema=CheckItemsSchema,
    explode=True,
)
request_query_check_item_fields = api_client.QueryParameter(
    name="checkItem_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CheckItemFieldsSchema,
    explode=True,
)
request_query_fields = api_client.QueryParameter(
    name="fields",
    style=api_client.ParameterStyle.FORM,
    schema=FieldsSchema,
    explode=True,
)
# Path params
IdChecklistSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'idChecklist': typing.Union[IdChecklistSchema, str, ],
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


request_path_id_checklist = api_client.PathParameter(
    name="idChecklist",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdChecklistSchema,
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

    def _get_by_id_mapped_args(
        self,
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if cards is not None:
            _query_params["cards"] = cards
        if card_fields is not None:
            _query_params["card_fields"] = card_fields
        if check_items is not None:
            _query_params["checkItems"] = check_items
        if check_item_fields is not None:
            _query_params["checkItem_fields"] = check_item_fields
        if fields is not None:
            _query_params["fields"] = fields
        if id_checklist is not None:
            _path_params["idChecklist"] = id_checklist
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
        getChecklistsByIdChecklist()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_checklist,
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
            request_query_cards,
            request_query_card_fields,
            request_query_check_items,
            request_query_check_item_fields,
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
            path_template='/checklists/{idChecklist}',
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
        getChecklistsByIdChecklist()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id_checklist,
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
            request_query_cards,
            request_query_card_fields,
            request_query_check_items,
            request_query_check_item_fields,
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
            path_template='/checklists/{idChecklist}',
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
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_checklist=id_checklist,
            cards=cards,
            card_fields=card_fields,
            check_items=check_items,
            check_item_fields=check_item_fields,
            fields=fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_id(
        self,
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_checklist=id_checklist,
            cards=cards,
            card_fields=card_fields,
            check_items=check_items,
            check_item_fields=check_item_fields,
            fields=fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetById(BaseApi):

    async def aget_by_id(
        self,
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_by_id(
            id_checklist=id_checklist,
            cards=cards,
            card_fields=card_fields,
            check_items=check_items,
            check_item_fields=check_item_fields,
            fields=fields,
            **kwargs,
        )
    
    
    def get_by_id(
        self,
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_by_id(
            id_checklist=id_checklist,
            cards=cards,
            card_fields=card_fields,
            check_items=check_items,
            check_item_fields=check_item_fields,
            fields=fields,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id_checklist=id_checklist,
            cards=cards,
            card_fields=card_fields,
            check_items=check_items,
            check_item_fields=check_item_fields,
            fields=fields,
        )
        return await self._aget_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id_checklist: str,
        cards: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        check_items: typing.Optional[str] = None,
        check_item_fields: typing.Optional[str] = None,
        fields: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id_checklist=id_checklist,
            cards=cards,
            card_fields=card_fields,
            check_items=check_items,
            check_item_fields=check_item_fields,
            fields=fields,
        )
        return self._get_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

