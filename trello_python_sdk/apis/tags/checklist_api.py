# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.checklists_id_checklist_check_items.post import AddCheckItemsByIdChecklist
from trello_python_sdk.paths.checklists.post import Create
from trello_python_sdk.paths.checklists_id_checklist_board.get import GetBoardByIdChecklist
from trello_python_sdk.paths.checklists_id_checklist_board_field.get import GetBoardByIdChecklistByField
from trello_python_sdk.paths.checklists_id_checklist.get import GetById
from trello_python_sdk.paths.checklists_id_checklist_field.get import GetByIdField
from trello_python_sdk.paths.checklists_id_checklist_cards_filter.get import GetCardsByFilter
from trello_python_sdk.paths.checklists_id_checklist_check_items.get import GetCheckItemsByIdChecklist
from trello_python_sdk.paths.checklists_id_checklist_check_items_id_check_item.get import GetCheckItemsByIdChecklistByIdCheckItem
from trello_python_sdk.paths.checklists_id_checklist_cards.get import ListCardsByIdChecklist
from trello_python_sdk.paths.checklists_id_checklist.delete import RemoveById
from trello_python_sdk.paths.checklists_id_checklist_check_items_id_check_item.delete import RemoveByIdCheckItem
from trello_python_sdk.paths.checklists_id_checklist.put import UpdateByIdChecklist
from trello_python_sdk.paths.checklists_id_checklist_id_card.put import UpdateIdCardByIdChecklist
from trello_python_sdk.paths.checklists_id_checklist_name.put import UpdateNameByIdChecklist
from trello_python_sdk.paths.checklists_id_checklist_pos.put import UpdatePosByIdChecklist
from trello_python_sdk.apis.tags.checklist_api_raw import ChecklistApiRaw


class ChecklistApi(
    AddCheckItemsByIdChecklist,
    Create,
    GetBoardByIdChecklist,
    GetBoardByIdChecklistByField,
    GetById,
    GetByIdField,
    GetCardsByFilter,
    GetCheckItemsByIdChecklist,
    GetCheckItemsByIdChecklistByIdCheckItem,
    ListCardsByIdChecklist,
    RemoveById,
    RemoveByIdCheckItem,
    UpdateByIdChecklist,
    UpdateIdCardByIdChecklist,
    UpdateNameByIdChecklist,
    UpdatePosByIdChecklist,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChecklistApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChecklistApiRaw(api_client)
