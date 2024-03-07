# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.labels.post import CreateLabels
from trello_python_sdk.paths.labels_id_label_board.get import GetBoardByIdLabel
from trello_python_sdk.paths.labels_id_label_board_field.get import GetBoardByIdLabelByField
from trello_python_sdk.paths.labels_id_label.get import GetByIdLabel
from trello_python_sdk.paths.labels_id_label.delete import RemoveByIdLabel
from trello_python_sdk.paths.labels_id_label.put import UpdateByIdLabel
from trello_python_sdk.paths.labels_id_label_color.put import UpdateColorByIdLabel
from trello_python_sdk.paths.labels_id_label_name.put import UpdateNameByIdLabel
from trello_python_sdk.apis.tags.label_api_raw import LabelApiRaw


class LabelApi(
    CreateLabels,
    GetBoardByIdLabel,
    GetBoardByIdLabelByField,
    GetByIdLabel,
    RemoveByIdLabel,
    UpdateByIdLabel,
    UpdateColorByIdLabel,
    UpdateNameByIdLabel,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LabelApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LabelApiRaw(api_client)