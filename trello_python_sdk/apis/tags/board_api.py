# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.boards_id_board_checklists.post import AddChecklists
from trello_python_sdk.paths.boards_id_board_labels.post import AddLabelsByIdBoard
from trello_python_sdk.paths.boards_id_board_power_ups.post import AddPowerUpsByIdBoard
from trello_python_sdk.paths.boards.post import CreateBoard
from trello_python_sdk.paths.boards_id_board_lists.post import CreateListsByIdBoard
from trello_python_sdk.paths.boards_id_board_cards_filter.get import FilterCardsByIdBoard
from trello_python_sdk.paths.boards_id_board_calendar_key_generate.post import GenerateCalendarKeyById
from trello_python_sdk.paths.boards_id_board_email_key_generate.post import GenerateEmailKey
from trello_python_sdk.paths.boards_id_board_board_stars.get import GetBoardStarsById
from trello_python_sdk.paths.boards_id_board.get import GetById
from trello_python_sdk.paths.boards_id_board_field.get import GetByIdField
from trello_python_sdk.paths.boards_id_board_cards.get import GetCardsByIdBoard
from trello_python_sdk.paths.boards_id_board_cards_id_card.get import GetCardsByIdBoardByIdCard
from trello_python_sdk.paths.boards_id_board_checklists.get import GetChecklistsById
from trello_python_sdk.paths.boards_id_board_deltas.get import GetDeltasByIdBoard
from trello_python_sdk.paths.boards_id_board_labels_id_label.get import GetLabelsByIdBoardByIdLabel
from trello_python_sdk.paths.boards_id_board_lists_filter.get import GetListsByFilter
from trello_python_sdk.paths.boards_id_board_lists.get import GetListsByIdBoard
from trello_python_sdk.paths.boards_id_board_members_filter.get import GetMembersByFilter
from trello_python_sdk.paths.boards_id_board_members.get import GetMembersByIdBoard
from trello_python_sdk.paths.boards_id_board_members_id_member_cards.get import GetMembersCardsByIdBoardByIdMember
from trello_python_sdk.paths.boards_id_board_members_invited_field.get import GetMembersInvitedByField
from trello_python_sdk.paths.boards_id_board_members_invited.get import GetMembersInvitedByIdBoard
from trello_python_sdk.paths.boards_id_board_memberships.get import GetMembershipsByIdBoard
from trello_python_sdk.paths.boards_id_board_memberships_id_membership.get import GetMembershipsByIdBoardByIdMembership
from trello_python_sdk.paths.boards_id_board_my_prefs.get import GetMyPrefsById
from trello_python_sdk.paths.boards_id_board_organization.get import GetOrganizationById
from trello_python_sdk.paths.boards_id_board_organization_field.get import GetOrganizationByIdBoardByField
from trello_python_sdk.paths.boards_id_board_actions.get import ListActionsByIdBoard
from trello_python_sdk.paths.boards_id_board_labels.get import ListLabelsByIdBoard
from trello_python_sdk.paths.boards_id_board_mark_as_viewed.post import MarkAsViewedByIdBoard
from trello_python_sdk.paths.boards_id_board_members_id_member.delete import RemoveMember
from trello_python_sdk.paths.boards_id_board_power_ups_power_up.delete import RemovePowerUp
from trello_python_sdk.paths.boards_id_board.put import UpdateById
from trello_python_sdk.paths.boards_id_board_closed.put import UpdateClosedById
from trello_python_sdk.paths.boards_id_board_desc.put import UpdateDescriptionByIdBoard
from trello_python_sdk.paths.boards_id_board_label_names_blue.put import UpdateLabelNamesBlueById
from trello_python_sdk.paths.boards_id_board_label_names_green.put import UpdateLabelNamesGreenByIdBoardPut
from trello_python_sdk.paths.boards_id_board_label_names_orange.put import UpdateLabelNamesOrangeByIdBoard
from trello_python_sdk.paths.boards_id_board_label_names_purple.put import UpdateLabelNamesPurpleByIdBoard
from trello_python_sdk.paths.boards_id_board_label_names_red.put import UpdateLabelNamesRed
from trello_python_sdk.paths.boards_id_board_label_names_yellow.put import UpdateLabelNamesYellowByIdBoard
from trello_python_sdk.paths.boards_id_board_members.put import UpdateMembersByIdBoard
from trello_python_sdk.paths.boards_id_board_members_id_member.put import UpdateMembersByIdBoardByIdMember
from trello_python_sdk.paths.boards_id_board_memberships_id_membership.put import UpdateMembershipsByIdBoardByIdMembership
from trello_python_sdk.paths.boards_id_board_my_prefs_id_email_list.put import UpdateMyPrefsEmailListByIdBoard
from trello_python_sdk.paths.boards_id_board_my_prefs_email_position.put import UpdateMyPrefsEmailPositionByIdBoard
from trello_python_sdk.paths.boards_id_board_my_prefs_show_list_guide.put import UpdateMyPrefsShowListGuideByIdBoard
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar.put import UpdateMyPrefsShowSidebar
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar_board_actions.put import UpdateMyPrefsShowSidebarActionsByIdBoard
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar_activity.put import UpdateMyPrefsShowSidebarActivityByIdBoard
from trello_python_sdk.paths.boards_id_board_name.put import UpdateNameById
from trello_python_sdk.paths.boards_id_board_id_organization.put import UpdateOrganizationByIdBoard
from trello_python_sdk.paths.boards_id_board_prefs_background.put import UpdatePrefsBackgroundByIdBoard
from trello_python_sdk.paths.boards_id_board_prefs_calendar_feed_enabled.put import UpdatePrefsCalendarFeedEnabledById
from trello_python_sdk.paths.boards_id_board_prefs_card_aging.put import UpdatePrefsCardAgingByIdBoard
from trello_python_sdk.paths.boards_id_board_prefs_card_covers.put import UpdatePrefsCardCoversByIdBoard
from trello_python_sdk.paths.boards_id_board_prefs_comments.put import UpdatePrefsCommentsByIdBoard
from trello_python_sdk.paths.boards_id_board_prefs_invitations.put import UpdatePrefsInvitationsByIdBoard
from trello_python_sdk.paths.boards_id_board_prefs_permission_level.put import UpdatePrefsPermissionLevelById
from trello_python_sdk.paths.boards_id_board_prefs_self_join.put import UpdatePrefsSelfJoinByIdBoard
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar_members.put import UpdatePrefsShowSidebarMembersById
from trello_python_sdk.paths.boards_id_board_subscribed.put import UpdateSubscribedById
from trello_python_sdk.paths.boards_id_board_prefs_voting.put import UpdateVotingPrefsById
from trello_python_sdk.apis.tags.board_api_raw import BoardApiRaw


class BoardApi(
    AddChecklists,
    AddLabelsByIdBoard,
    AddPowerUpsByIdBoard,
    CreateBoard,
    CreateListsByIdBoard,
    FilterCardsByIdBoard,
    GenerateCalendarKeyById,
    GenerateEmailKey,
    GetBoardStarsById,
    GetById,
    GetByIdField,
    GetCardsByIdBoard,
    GetCardsByIdBoardByIdCard,
    GetChecklistsById,
    GetDeltasByIdBoard,
    GetLabelsByIdBoardByIdLabel,
    GetListsByFilter,
    GetListsByIdBoard,
    GetMembersByFilter,
    GetMembersByIdBoard,
    GetMembersCardsByIdBoardByIdMember,
    GetMembersInvitedByField,
    GetMembersInvitedByIdBoard,
    GetMembershipsByIdBoard,
    GetMembershipsByIdBoardByIdMembership,
    GetMyPrefsById,
    GetOrganizationById,
    GetOrganizationByIdBoardByField,
    ListActionsByIdBoard,
    ListLabelsByIdBoard,
    MarkAsViewedByIdBoard,
    RemoveMember,
    RemovePowerUp,
    UpdateById,
    UpdateClosedById,
    UpdateDescriptionByIdBoard,
    UpdateLabelNamesBlueById,
    UpdateLabelNamesGreenByIdBoardPut,
    UpdateLabelNamesOrangeByIdBoard,
    UpdateLabelNamesPurpleByIdBoard,
    UpdateLabelNamesRed,
    UpdateLabelNamesYellowByIdBoard,
    UpdateMembersByIdBoard,
    UpdateMembersByIdBoardByIdMember,
    UpdateMembershipsByIdBoardByIdMembership,
    UpdateMyPrefsEmailListByIdBoard,
    UpdateMyPrefsEmailPositionByIdBoard,
    UpdateMyPrefsShowListGuideByIdBoard,
    UpdateMyPrefsShowSidebar,
    UpdateMyPrefsShowSidebarActionsByIdBoard,
    UpdateMyPrefsShowSidebarActivityByIdBoard,
    UpdateNameById,
    UpdateOrganizationByIdBoard,
    UpdatePrefsBackgroundByIdBoard,
    UpdatePrefsCalendarFeedEnabledById,
    UpdatePrefsCardAgingByIdBoard,
    UpdatePrefsCardCoversByIdBoard,
    UpdatePrefsCommentsByIdBoard,
    UpdatePrefsInvitationsByIdBoard,
    UpdatePrefsPermissionLevelById,
    UpdatePrefsSelfJoinByIdBoard,
    UpdatePrefsShowSidebarMembersById,
    UpdateSubscribedById,
    UpdateVotingPrefsById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BoardApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BoardApiRaw(api_client)
