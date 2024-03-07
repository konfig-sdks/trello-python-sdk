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
IdBoardsSchema = schemas.StrSchema
IdOrganizationsSchema = schemas.StrSchema
IdCardsSchema = schemas.StrSchema
ModelTypesSchema = schemas.StrSchema
BoardFieldsSchema = schemas.StrSchema
BoardsLimitSchema = schemas.StrSchema
CardFieldsSchema = schemas.StrSchema
CardsLimitSchema = schemas.StrSchema
CardsPageSchema = schemas.StrSchema
CardBoardSchema = schemas.StrSchema
CardListSchema = schemas.StrSchema
CardMembersSchema = schemas.StrSchema
CardStickersSchema = schemas.StrSchema
CardAttachmentsSchema = schemas.StrSchema
OrganizationFieldsSchema = schemas.StrSchema
OrganizationsLimitSchema = schemas.StrSchema
MemberFieldsSchema = schemas.StrSchema
MembersLimitSchema = schemas.StrSchema
PartialSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'query': typing.Union[QuerySchema, str, ],
        'idOrganizations': typing.Union[IdOrganizationsSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'idBoards': typing.Union[IdBoardsSchema, str, ],
        'idCards': typing.Union[IdCardsSchema, str, ],
        'modelTypes': typing.Union[ModelTypesSchema, str, ],
        'board_fields': typing.Union[BoardFieldsSchema, str, ],
        'boards_limit': typing.Union[BoardsLimitSchema, str, ],
        'card_fields': typing.Union[CardFieldsSchema, str, ],
        'cards_limit': typing.Union[CardsLimitSchema, str, ],
        'cards_page': typing.Union[CardsPageSchema, str, ],
        'card_board': typing.Union[CardBoardSchema, str, ],
        'card_list': typing.Union[CardListSchema, str, ],
        'card_members': typing.Union[CardMembersSchema, str, ],
        'card_stickers': typing.Union[CardStickersSchema, str, ],
        'card_attachments': typing.Union[CardAttachmentsSchema, str, ],
        'organization_fields': typing.Union[OrganizationFieldsSchema, str, ],
        'organizations_limit': typing.Union[OrganizationsLimitSchema, str, ],
        'member_fields': typing.Union[MemberFieldsSchema, str, ],
        'members_limit': typing.Union[MembersLimitSchema, str, ],
        'partial': typing.Union[PartialSchema, str, ],
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
request_query_id_boards = api_client.QueryParameter(
    name="idBoards",
    style=api_client.ParameterStyle.FORM,
    schema=IdBoardsSchema,
    explode=True,
)
request_query_id_organizations = api_client.QueryParameter(
    name="idOrganizations",
    style=api_client.ParameterStyle.FORM,
    schema=IdOrganizationsSchema,
    required=True,
    explode=True,
)
request_query_id_cards = api_client.QueryParameter(
    name="idCards",
    style=api_client.ParameterStyle.FORM,
    schema=IdCardsSchema,
    explode=True,
)
request_query_model_types = api_client.QueryParameter(
    name="modelTypes",
    style=api_client.ParameterStyle.FORM,
    schema=ModelTypesSchema,
    explode=True,
)
request_query_board_fields = api_client.QueryParameter(
    name="board_fields",
    style=api_client.ParameterStyle.FORM,
    schema=BoardFieldsSchema,
    explode=True,
)
request_query_boards_limit = api_client.QueryParameter(
    name="boards_limit",
    style=api_client.ParameterStyle.FORM,
    schema=BoardsLimitSchema,
    explode=True,
)
request_query_card_fields = api_client.QueryParameter(
    name="card_fields",
    style=api_client.ParameterStyle.FORM,
    schema=CardFieldsSchema,
    explode=True,
)
request_query_cards_limit = api_client.QueryParameter(
    name="cards_limit",
    style=api_client.ParameterStyle.FORM,
    schema=CardsLimitSchema,
    explode=True,
)
request_query_cards_page = api_client.QueryParameter(
    name="cards_page",
    style=api_client.ParameterStyle.FORM,
    schema=CardsPageSchema,
    explode=True,
)
request_query_card_board = api_client.QueryParameter(
    name="card_board",
    style=api_client.ParameterStyle.FORM,
    schema=CardBoardSchema,
    explode=True,
)
request_query_card_list = api_client.QueryParameter(
    name="card_list",
    style=api_client.ParameterStyle.FORM,
    schema=CardListSchema,
    explode=True,
)
request_query_card_members = api_client.QueryParameter(
    name="card_members",
    style=api_client.ParameterStyle.FORM,
    schema=CardMembersSchema,
    explode=True,
)
request_query_card_stickers = api_client.QueryParameter(
    name="card_stickers",
    style=api_client.ParameterStyle.FORM,
    schema=CardStickersSchema,
    explode=True,
)
request_query_card_attachments = api_client.QueryParameter(
    name="card_attachments",
    style=api_client.ParameterStyle.FORM,
    schema=CardAttachmentsSchema,
    explode=True,
)
request_query_organization_fields = api_client.QueryParameter(
    name="organization_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationFieldsSchema,
    explode=True,
)
request_query_organizations_limit = api_client.QueryParameter(
    name="organizations_limit",
    style=api_client.ParameterStyle.FORM,
    schema=OrganizationsLimitSchema,
    explode=True,
)
request_query_member_fields = api_client.QueryParameter(
    name="member_fields",
    style=api_client.ParameterStyle.FORM,
    schema=MemberFieldsSchema,
    explode=True,
)
request_query_members_limit = api_client.QueryParameter(
    name="members_limit",
    style=api_client.ParameterStyle.FORM,
    schema=MembersLimitSchema,
    explode=True,
)
request_query_partial = api_client.QueryParameter(
    name="partial",
    style=api_client.ParameterStyle.FORM,
    schema=PartialSchema,
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

    def _get_results_mapped_args(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if query is not None:
            _query_params["query"] = query
        if id_boards is not None:
            _query_params["idBoards"] = id_boards
        if id_organizations is not None:
            _query_params["idOrganizations"] = id_organizations
        if id_cards is not None:
            _query_params["idCards"] = id_cards
        if model_types is not None:
            _query_params["modelTypes"] = model_types
        if board_fields is not None:
            _query_params["board_fields"] = board_fields
        if boards_limit is not None:
            _query_params["boards_limit"] = boards_limit
        if card_fields is not None:
            _query_params["card_fields"] = card_fields
        if cards_limit is not None:
            _query_params["cards_limit"] = cards_limit
        if cards_page is not None:
            _query_params["cards_page"] = cards_page
        if card_board is not None:
            _query_params["card_board"] = card_board
        if card_list is not None:
            _query_params["card_list"] = card_list
        if card_members is not None:
            _query_params["card_members"] = card_members
        if card_stickers is not None:
            _query_params["card_stickers"] = card_stickers
        if card_attachments is not None:
            _query_params["card_attachments"] = card_attachments
        if organization_fields is not None:
            _query_params["organization_fields"] = organization_fields
        if organizations_limit is not None:
            _query_params["organizations_limit"] = organizations_limit
        if member_fields is not None:
            _query_params["member_fields"] = member_fields
        if members_limit is not None:
            _query_params["members_limit"] = members_limit
        if partial is not None:
            _query_params["partial"] = partial
        args.query = _query_params
        return args

    async def _aget_results_oapg(
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
        getSearch()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_id_boards,
            request_query_id_organizations,
            request_query_id_cards,
            request_query_model_types,
            request_query_board_fields,
            request_query_boards_limit,
            request_query_card_fields,
            request_query_cards_limit,
            request_query_cards_page,
            request_query_card_board,
            request_query_card_list,
            request_query_card_members,
            request_query_card_stickers,
            request_query_card_attachments,
            request_query_organization_fields,
            request_query_organizations_limit,
            request_query_member_fields,
            request_query_members_limit,
            request_query_partial,
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
            path_template='/search',
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


    def _get_results_oapg(
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
        getSearch()
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_query,
            request_query_id_boards,
            request_query_id_organizations,
            request_query_id_cards,
            request_query_model_types,
            request_query_board_fields,
            request_query_boards_limit,
            request_query_card_fields,
            request_query_cards_limit,
            request_query_cards_page,
            request_query_card_board,
            request_query_card_list,
            request_query_card_members,
            request_query_card_stickers,
            request_query_card_attachments,
            request_query_organization_fields,
            request_query_organizations_limit,
            request_query_member_fields,
            request_query_members_limit,
            request_query_partial,
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
            path_template='/search',
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


class GetResultsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_results(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_results_mapped_args(
            query=query,
            id_organizations=id_organizations,
            id_boards=id_boards,
            id_cards=id_cards,
            model_types=model_types,
            board_fields=board_fields,
            boards_limit=boards_limit,
            card_fields=card_fields,
            cards_limit=cards_limit,
            cards_page=cards_page,
            card_board=card_board,
            card_list=card_list,
            card_members=card_members,
            card_stickers=card_stickers,
            card_attachments=card_attachments,
            organization_fields=organization_fields,
            organizations_limit=organizations_limit,
            member_fields=member_fields,
            members_limit=members_limit,
            partial=partial,
        )
        return await self._aget_results_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_results(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_results_mapped_args(
            query=query,
            id_organizations=id_organizations,
            id_boards=id_boards,
            id_cards=id_cards,
            model_types=model_types,
            board_fields=board_fields,
            boards_limit=boards_limit,
            card_fields=card_fields,
            cards_limit=cards_limit,
            cards_page=cards_page,
            card_board=card_board,
            card_list=card_list,
            card_members=card_members,
            card_stickers=card_stickers,
            card_attachments=card_attachments,
            organization_fields=organization_fields,
            organizations_limit=organizations_limit,
            member_fields=member_fields,
            members_limit=members_limit,
            partial=partial,
        )
        return self._get_results_oapg(
            query_params=args.query,
        )

class GetResults(BaseApi):

    async def aget_results(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aget_results(
            query=query,
            id_organizations=id_organizations,
            id_boards=id_boards,
            id_cards=id_cards,
            model_types=model_types,
            board_fields=board_fields,
            boards_limit=boards_limit,
            card_fields=card_fields,
            cards_limit=cards_limit,
            cards_page=cards_page,
            card_board=card_board,
            card_list=card_list,
            card_members=card_members,
            card_stickers=card_stickers,
            card_attachments=card_attachments,
            organization_fields=organization_fields,
            organizations_limit=organizations_limit,
            member_fields=member_fields,
            members_limit=members_limit,
            partial=partial,
            **kwargs,
        )
    
    
    def get_results(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.get_results(
            query=query,
            id_organizations=id_organizations,
            id_boards=id_boards,
            id_cards=id_cards,
            model_types=model_types,
            board_fields=board_fields,
            boards_limit=boards_limit,
            card_fields=card_fields,
            cards_limit=cards_limit,
            cards_page=cards_page,
            card_board=card_board,
            card_list=card_list,
            card_members=card_members,
            card_stickers=card_stickers,
            card_attachments=card_attachments,
            organization_fields=organization_fields,
            organizations_limit=organizations_limit,
            member_fields=member_fields,
            members_limit=members_limit,
            partial=partial,
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_results_mapped_args(
            query=query,
            id_organizations=id_organizations,
            id_boards=id_boards,
            id_cards=id_cards,
            model_types=model_types,
            board_fields=board_fields,
            boards_limit=boards_limit,
            card_fields=card_fields,
            cards_limit=cards_limit,
            cards_page=cards_page,
            card_board=card_board,
            card_list=card_list,
            card_members=card_members,
            card_stickers=card_stickers,
            card_attachments=card_attachments,
            organization_fields=organization_fields,
            organizations_limit=organizations_limit,
            member_fields=member_fields,
            members_limit=members_limit,
            partial=partial,
        )
        return await self._aget_results_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        query: str,
        id_organizations: str,
        id_boards: typing.Optional[str] = None,
        id_cards: typing.Optional[str] = None,
        model_types: typing.Optional[str] = None,
        board_fields: typing.Optional[str] = None,
        boards_limit: typing.Optional[str] = None,
        card_fields: typing.Optional[str] = None,
        cards_limit: typing.Optional[str] = None,
        cards_page: typing.Optional[str] = None,
        card_board: typing.Optional[str] = None,
        card_list: typing.Optional[str] = None,
        card_members: typing.Optional[str] = None,
        card_stickers: typing.Optional[str] = None,
        card_attachments: typing.Optional[str] = None,
        organization_fields: typing.Optional[str] = None,
        organizations_limit: typing.Optional[str] = None,
        member_fields: typing.Optional[str] = None,
        members_limit: typing.Optional[str] = None,
        partial: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_results_mapped_args(
            query=query,
            id_organizations=id_organizations,
            id_boards=id_boards,
            id_cards=id_cards,
            model_types=model_types,
            board_fields=board_fields,
            boards_limit=boards_limit,
            card_fields=card_fields,
            cards_limit=cards_limit,
            cards_page=cards_page,
            card_board=card_board,
            card_list=card_list,
            card_members=card_members,
            card_stickers=card_stickers,
            card_attachments=card_attachments,
            organization_fields=organization_fields,
            organizations_limit=organizations_limit,
            member_fields=member_fields,
            members_limit=members_limit,
            partial=partial,
        )
        return self._get_results_oapg(
            query_params=args.query,
        )

