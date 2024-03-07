# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.cards_id_card_actions_comments.post import AddActionsCommentsByIdCardRaw
from trello_python_sdk.paths.cards_id_card_attachments.post import AddAttachmentsByIdCardRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item.post import AddChecklistCheckItemRaw
from trello_python_sdk.paths.cards_id_card_checklists.post import AddChecklistsRaw
from trello_python_sdk.paths.cards_id_card_id_labels.post import AddIdLabelsToCardRaw
from trello_python_sdk.paths.cards_id_card_labels.post import AddLabelsRaw
from trello_python_sdk.paths.cards_id_card_id_members.post import AddMembersRaw
from trello_python_sdk.paths.cards_id_card_members_voted.post import AddMembersVotedRaw
from trello_python_sdk.paths.cards_id_card_stickers.post import AddStickersByIdCardRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_convert_to_card.post import ConvertCheckItemToCardRaw
from trello_python_sdk.paths.cards.post import CreateAndUpdateRaw
from trello_python_sdk.paths.cards_id_card_attachments_id_attachment.delete import DeleteAttachmentsByIdCardByIdAttachmentRaw
from trello_python_sdk.paths.cards_id_card_checklists_id_checklist.delete import DeleteChecklistByIdCardByIdChecklistRaw
from trello_python_sdk.paths.cards_id_card_attachments.get import GetAttachmentsByIdCardRaw
from trello_python_sdk.paths.cards_id_card_attachments_id_attachment.get import GetAttachmentsByIdsRaw
from trello_python_sdk.paths.cards_id_card_board.get import GetBoardByIdRaw
from trello_python_sdk.paths.cards_id_card_board_field.get import GetBoardByIdCardByFieldRaw
from trello_python_sdk.paths.cards_id_card.get import GetByIdRaw
from trello_python_sdk.paths.cards_id_card_field.get import GetByIdFieldRaw
from trello_python_sdk.paths.cards_id_card_list_field.get import GetCardsListByIdCardByFieldRaw
from trello_python_sdk.paths.cards_id_card_check_item_states.get import GetCheckItemStatesByIdRaw
from trello_python_sdk.paths.cards_id_card_checklists.get import GetChecklistsByIdRaw
from trello_python_sdk.paths.cards_id_card_list.get import GetListByIdRaw
from trello_python_sdk.paths.cards_id_card_members_voted.get import GetMembersVotedByIdCardRaw
from trello_python_sdk.paths.cards_id_card_stickers_id_sticker.get import GetStickerByIdsRaw
from trello_python_sdk.paths.cards_id_card_stickers.get import GetStickersByIdCardRaw
from trello_python_sdk.paths.cards_id_card_actions.get import ListCardActionsByIdRaw
from trello_python_sdk.paths.cards_id_card_members.get import ListMembersByIdCardRaw
from trello_python_sdk.paths.cards_id_card_mark_associated_notifications_read.post import MarkAssociatedNotificationsReadRaw
from trello_python_sdk.paths.cards_id_card_actions_id_action_comments.delete import RemoveActionCommentByIdCardByIdActionRaw
from trello_python_sdk.paths.cards_id_card.delete import RemoveByIdCardRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item.delete import RemoveChecklistCheckItemRaw
from trello_python_sdk.paths.cards_id_card_id_labels_id_label.delete import RemoveLabelByIdCardByIdLabelRaw
from trello_python_sdk.paths.cards_id_card_labels_color.delete import RemoveLabelsByIdCardByColorRaw
from trello_python_sdk.paths.cards_id_card_id_members_id_member.delete import RemoveMemberByIdMemberRaw
from trello_python_sdk.paths.cards_id_card_members_voted_id_member.delete import RemoveMembersVotedByIdCardByIdMemberRaw
from trello_python_sdk.paths.cards_id_card_stickers_id_sticker.delete import RemoveStickerByIdsRaw
from trello_python_sdk.paths.cards_id_card_actions_id_action_comments.put import UpdateActionCommentByIdCardByIdActionRaw
from trello_python_sdk.paths.cards_id_card_id_attachment_cover.put import UpdateAttachmentCoverByIdCardRaw
from trello_python_sdk.paths.cards_id_card_id_board.put import UpdateBoardByIdCardRaw
from trello_python_sdk.paths.cards_id_card.put import UpdateByIdCardRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_pos.put import UpdateCheckItemPosByIdRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_current_check_item_id_check_item.put import UpdateChecklistCheckItemRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_name.put import UpdateChecklistCheckItemNameByIdRaw
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_state.put import UpdateChecklistCheckItemStateRaw
from trello_python_sdk.paths.cards_id_card_closed.put import UpdateClosedByIdRaw
from trello_python_sdk.paths.cards_id_card_desc.put import UpdateDescriptionByIdCardRaw
from trello_python_sdk.paths.cards_id_card_due.put import UpdateDueByIdRaw
from trello_python_sdk.paths.cards_id_card_id_list.put import UpdateIdListByIdCardRaw
from trello_python_sdk.paths.cards_id_card_id_members.put import UpdateIdMembersRaw
from trello_python_sdk.paths.cards_id_card_labels.put import UpdateLabelsRaw
from trello_python_sdk.paths.cards_id_card_name.put import UpdateNameByIdRaw
from trello_python_sdk.paths.cards_id_card_pos.put import UpdatePosByIdCardRaw
from trello_python_sdk.paths.cards_id_card_stickers_id_sticker.put import UpdateStickersByIdCardByIdStickerRaw
from trello_python_sdk.paths.cards_id_card_subscribed.put import UpdateSubscribedByIdCardRaw


class CardApiRaw(
    AddActionsCommentsByIdCardRaw,
    AddAttachmentsByIdCardRaw,
    AddChecklistCheckItemRaw,
    AddChecklistsRaw,
    AddIdLabelsToCardRaw,
    AddLabelsRaw,
    AddMembersRaw,
    AddMembersVotedRaw,
    AddStickersByIdCardRaw,
    ConvertCheckItemToCardRaw,
    CreateAndUpdateRaw,
    DeleteAttachmentsByIdCardByIdAttachmentRaw,
    DeleteChecklistByIdCardByIdChecklistRaw,
    GetAttachmentsByIdCardRaw,
    GetAttachmentsByIdsRaw,
    GetBoardByIdRaw,
    GetBoardByIdCardByFieldRaw,
    GetByIdRaw,
    GetByIdFieldRaw,
    GetCardsListByIdCardByFieldRaw,
    GetCheckItemStatesByIdRaw,
    GetChecklistsByIdRaw,
    GetListByIdRaw,
    GetMembersVotedByIdCardRaw,
    GetStickerByIdsRaw,
    GetStickersByIdCardRaw,
    ListCardActionsByIdRaw,
    ListMembersByIdCardRaw,
    MarkAssociatedNotificationsReadRaw,
    RemoveActionCommentByIdCardByIdActionRaw,
    RemoveByIdCardRaw,
    RemoveChecklistCheckItemRaw,
    RemoveLabelByIdCardByIdLabelRaw,
    RemoveLabelsByIdCardByColorRaw,
    RemoveMemberByIdMemberRaw,
    RemoveMembersVotedByIdCardByIdMemberRaw,
    RemoveStickerByIdsRaw,
    UpdateActionCommentByIdCardByIdActionRaw,
    UpdateAttachmentCoverByIdCardRaw,
    UpdateBoardByIdCardRaw,
    UpdateByIdCardRaw,
    UpdateCheckItemPosByIdRaw,
    UpdateChecklistCheckItemRaw,
    UpdateChecklistCheckItemNameByIdRaw,
    UpdateChecklistCheckItemStateRaw,
    UpdateClosedByIdRaw,
    UpdateDescriptionByIdCardRaw,
    UpdateDueByIdRaw,
    UpdateIdListByIdCardRaw,
    UpdateIdMembersRaw,
    UpdateLabelsRaw,
    UpdateNameByIdRaw,
    UpdatePosByIdCardRaw,
    UpdateStickersByIdCardByIdStickerRaw,
    UpdateSubscribedByIdCardRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
