# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.cards_id_card_actions_comments.post import AddActionsCommentsByIdCard
from trello_python_sdk.paths.cards_id_card_attachments.post import AddAttachmentsByIdCard
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item.post import AddChecklistCheckItem
from trello_python_sdk.paths.cards_id_card_checklists.post import AddChecklists
from trello_python_sdk.paths.cards_id_card_id_labels.post import AddIdLabelsToCard
from trello_python_sdk.paths.cards_id_card_labels.post import AddLabels
from trello_python_sdk.paths.cards_id_card_id_members.post import AddMembers
from trello_python_sdk.paths.cards_id_card_members_voted.post import AddMembersVoted
from trello_python_sdk.paths.cards_id_card_stickers.post import AddStickersByIdCard
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_convert_to_card.post import ConvertCheckItemToCard
from trello_python_sdk.paths.cards.post import CreateAndUpdate
from trello_python_sdk.paths.cards_id_card_attachments_id_attachment.delete import DeleteAttachmentsByIdCardByIdAttachment
from trello_python_sdk.paths.cards_id_card_checklists_id_checklist.delete import DeleteChecklistByIdCardByIdChecklist
from trello_python_sdk.paths.cards_id_card_attachments.get import GetAttachmentsByIdCard
from trello_python_sdk.paths.cards_id_card_attachments_id_attachment.get import GetAttachmentsByIds
from trello_python_sdk.paths.cards_id_card_board.get import GetBoardById
from trello_python_sdk.paths.cards_id_card_board_field.get import GetBoardByIdCardByField
from trello_python_sdk.paths.cards_id_card.get import GetById
from trello_python_sdk.paths.cards_id_card_field.get import GetByIdField
from trello_python_sdk.paths.cards_id_card_list_field.get import GetCardsListByIdCardByField
from trello_python_sdk.paths.cards_id_card_check_item_states.get import GetCheckItemStatesById
from trello_python_sdk.paths.cards_id_card_checklists.get import GetChecklistsById
from trello_python_sdk.paths.cards_id_card_list.get import GetListById
from trello_python_sdk.paths.cards_id_card_members_voted.get import GetMembersVotedByIdCard
from trello_python_sdk.paths.cards_id_card_stickers_id_sticker.get import GetStickerByIds
from trello_python_sdk.paths.cards_id_card_stickers.get import GetStickersByIdCard
from trello_python_sdk.paths.cards_id_card_actions.get import ListCardActionsById
from trello_python_sdk.paths.cards_id_card_members.get import ListMembersByIdCard
from trello_python_sdk.paths.cards_id_card_mark_associated_notifications_read.post import MarkAssociatedNotificationsRead
from trello_python_sdk.paths.cards_id_card_actions_id_action_comments.delete import RemoveActionCommentByIdCardByIdAction
from trello_python_sdk.paths.cards_id_card.delete import RemoveByIdCard
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item.delete import RemoveChecklistCheckItem
from trello_python_sdk.paths.cards_id_card_id_labels_id_label.delete import RemoveLabelByIdCardByIdLabel
from trello_python_sdk.paths.cards_id_card_labels_color.delete import RemoveLabelsByIdCardByColor
from trello_python_sdk.paths.cards_id_card_id_members_id_member.delete import RemoveMemberByIdMember
from trello_python_sdk.paths.cards_id_card_members_voted_id_member.delete import RemoveMembersVotedByIdCardByIdMember
from trello_python_sdk.paths.cards_id_card_stickers_id_sticker.delete import RemoveStickerByIds
from trello_python_sdk.paths.cards_id_card_actions_id_action_comments.put import UpdateActionCommentByIdCardByIdAction
from trello_python_sdk.paths.cards_id_card_id_attachment_cover.put import UpdateAttachmentCoverByIdCard
from trello_python_sdk.paths.cards_id_card_id_board.put import UpdateBoardByIdCard
from trello_python_sdk.paths.cards_id_card.put import UpdateByIdCard
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_pos.put import UpdateCheckItemPosById
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_current_check_item_id_check_item.put import UpdateChecklistCheckItem
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_name.put import UpdateChecklistCheckItemNameById
from trello_python_sdk.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_state.put import UpdateChecklistCheckItemState
from trello_python_sdk.paths.cards_id_card_closed.put import UpdateClosedById
from trello_python_sdk.paths.cards_id_card_desc.put import UpdateDescriptionByIdCard
from trello_python_sdk.paths.cards_id_card_due.put import UpdateDueById
from trello_python_sdk.paths.cards_id_card_id_list.put import UpdateIdListByIdCard
from trello_python_sdk.paths.cards_id_card_id_members.put import UpdateIdMembers
from trello_python_sdk.paths.cards_id_card_labels.put import UpdateLabels
from trello_python_sdk.paths.cards_id_card_name.put import UpdateNameById
from trello_python_sdk.paths.cards_id_card_pos.put import UpdatePosByIdCard
from trello_python_sdk.paths.cards_id_card_stickers_id_sticker.put import UpdateStickersByIdCardByIdSticker
from trello_python_sdk.paths.cards_id_card_subscribed.put import UpdateSubscribedByIdCard
from trello_python_sdk.apis.tags.card_api_raw import CardApiRaw


class CardApi(
    AddActionsCommentsByIdCard,
    AddAttachmentsByIdCard,
    AddChecklistCheckItem,
    AddChecklists,
    AddIdLabelsToCard,
    AddLabels,
    AddMembers,
    AddMembersVoted,
    AddStickersByIdCard,
    ConvertCheckItemToCard,
    CreateAndUpdate,
    DeleteAttachmentsByIdCardByIdAttachment,
    DeleteChecklistByIdCardByIdChecklist,
    GetAttachmentsByIdCard,
    GetAttachmentsByIds,
    GetBoardById,
    GetBoardByIdCardByField,
    GetById,
    GetByIdField,
    GetCardsListByIdCardByField,
    GetCheckItemStatesById,
    GetChecklistsById,
    GetListById,
    GetMembersVotedByIdCard,
    GetStickerByIds,
    GetStickersByIdCard,
    ListCardActionsById,
    ListMembersByIdCard,
    MarkAssociatedNotificationsRead,
    RemoveActionCommentByIdCardByIdAction,
    RemoveByIdCard,
    RemoveChecklistCheckItem,
    RemoveLabelByIdCardByIdLabel,
    RemoveLabelsByIdCardByColor,
    RemoveMemberByIdMember,
    RemoveMembersVotedByIdCardByIdMember,
    RemoveStickerByIds,
    UpdateActionCommentByIdCardByIdAction,
    UpdateAttachmentCoverByIdCard,
    UpdateBoardByIdCard,
    UpdateByIdCard,
    UpdateCheckItemPosById,
    UpdateChecklistCheckItem,
    UpdateChecklistCheckItemNameById,
    UpdateChecklistCheckItemState,
    UpdateClosedById,
    UpdateDescriptionByIdCard,
    UpdateDueById,
    UpdateIdListByIdCard,
    UpdateIdMembers,
    UpdateLabels,
    UpdateNameById,
    UpdatePosByIdCard,
    UpdateStickersByIdCardByIdSticker,
    UpdateSubscribedByIdCard,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CardApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CardApiRaw(api_client)
