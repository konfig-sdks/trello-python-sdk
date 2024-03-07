# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.lists_id_list_archive_all_cards.post import ArchiveAllCardsByIdList
from trello_python_sdk.paths.lists_id_list_cards.post import CreateCardsByIdList
from trello_python_sdk.paths.lists.post import CreateList
from trello_python_sdk.paths.lists_id_list_actions.get import GetActionsByIdList
from trello_python_sdk.paths.lists_id_list_board_field.get import GetBoardByIdListByField
from trello_python_sdk.paths.lists_id_list.get import GetByIdList
from trello_python_sdk.paths.lists_id_list_field.get import GetByIdListByField
from trello_python_sdk.paths.lists_id_list_cards_filter.get import GetCardsByFilter
from trello_python_sdk.paths.lists_id_list_cards.get import GetCardsByIdList
from trello_python_sdk.paths.lists_id_list_board.get import IdBoardGet
from trello_python_sdk.paths.lists_id_list_move_all_cards.post import MoveAllCardsByIdList
from trello_python_sdk.paths.lists_id_list.put import UpdateByIdList
from trello_python_sdk.paths.lists_id_list_closed.put import UpdateClosedByIdList
from trello_python_sdk.paths.lists_id_list_id_board.put import UpdateIdBoardByIdList
from trello_python_sdk.paths.lists_id_list_name.put import UpdateNameByIdList
from trello_python_sdk.paths.lists_id_list_pos.put import UpdatePosByIdList
from trello_python_sdk.paths.lists_id_list_subscribed.put import UpdateSubscribedByIdList
from trello_python_sdk.apis.tags.model_list_api_raw import ModelListApiRaw


class ModelListApi(
    ArchiveAllCardsByIdList,
    CreateCardsByIdList,
    CreateList,
    GetActionsByIdList,
    GetBoardByIdListByField,
    GetByIdList,
    GetByIdListByField,
    GetCardsByFilter,
    GetCardsByIdList,
    IdBoardGet,
    MoveAllCardsByIdList,
    UpdateByIdList,
    UpdateClosedByIdList,
    UpdateIdBoardByIdList,
    UpdateNameByIdList,
    UpdatePosByIdList,
    UpdateSubscribedByIdList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ModelListApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ModelListApiRaw(api_client)