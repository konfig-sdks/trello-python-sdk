# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.boards_id_board_checklists.post import AddChecklistsRaw
from trello_python_sdk.paths.boards_id_board_labels.post import AddLabelsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_power_ups.post import AddPowerUpsByIdBoardRaw
from trello_python_sdk.paths.boards.post import CreateBoardRaw
from trello_python_sdk.paths.boards_id_board_lists.post import CreateListsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_cards_filter.get import FilterCardsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_calendar_key_generate.post import GenerateCalendarKeyByIdRaw
from trello_python_sdk.paths.boards_id_board_email_key_generate.post import GenerateEmailKeyRaw
from trello_python_sdk.paths.boards_id_board_board_stars.get import GetBoardStarsByIdRaw
from trello_python_sdk.paths.boards_id_board.get import GetByIdRaw
from trello_python_sdk.paths.boards_id_board_field.get import GetByIdFieldRaw
from trello_python_sdk.paths.boards_id_board_cards.get import GetCardsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_cards_id_card.get import GetCardsByIdBoardByIdCardRaw
from trello_python_sdk.paths.boards_id_board_checklists.get import GetChecklistsByIdRaw
from trello_python_sdk.paths.boards_id_board_deltas.get import GetDeltasByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_labels_id_label.get import GetLabelsByIdBoardByIdLabelRaw
from trello_python_sdk.paths.boards_id_board_lists_filter.get import GetListsByFilterRaw
from trello_python_sdk.paths.boards_id_board_lists.get import GetListsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_members_filter.get import GetMembersByFilterRaw
from trello_python_sdk.paths.boards_id_board_members.get import GetMembersByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_members_id_member_cards.get import GetMembersCardsByIdBoardByIdMemberRaw
from trello_python_sdk.paths.boards_id_board_members_invited_field.get import GetMembersInvitedByFieldRaw
from trello_python_sdk.paths.boards_id_board_members_invited.get import GetMembersInvitedByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_memberships.get import GetMembershipsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_memberships_id_membership.get import GetMembershipsByIdBoardByIdMembershipRaw
from trello_python_sdk.paths.boards_id_board_my_prefs.get import GetMyPrefsByIdRaw
from trello_python_sdk.paths.boards_id_board_organization.get import GetOrganizationByIdRaw
from trello_python_sdk.paths.boards_id_board_organization_field.get import GetOrganizationByIdBoardByFieldRaw
from trello_python_sdk.paths.boards_id_board_actions.get import ListActionsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_labels.get import ListLabelsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_mark_as_viewed.post import MarkAsViewedByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_members_id_member.delete import RemoveMemberRaw
from trello_python_sdk.paths.boards_id_board_power_ups_power_up.delete import RemovePowerUpRaw
from trello_python_sdk.paths.boards_id_board.put import UpdateByIdRaw
from trello_python_sdk.paths.boards_id_board_closed.put import UpdateClosedByIdRaw
from trello_python_sdk.paths.boards_id_board_desc.put import UpdateDescriptionByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_label_names_blue.put import UpdateLabelNamesBlueByIdRaw
from trello_python_sdk.paths.boards_id_board_label_names_green.put import UpdateLabelNamesGreenByIdBoardPutRaw
from trello_python_sdk.paths.boards_id_board_label_names_orange.put import UpdateLabelNamesOrangeByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_label_names_purple.put import UpdateLabelNamesPurpleByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_label_names_red.put import UpdateLabelNamesRedRaw
from trello_python_sdk.paths.boards_id_board_label_names_yellow.put import UpdateLabelNamesYellowByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_members.put import UpdateMembersByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_members_id_member.put import UpdateMembersByIdBoardByIdMemberRaw
from trello_python_sdk.paths.boards_id_board_memberships_id_membership.put import UpdateMembershipsByIdBoardByIdMembershipRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_id_email_list.put import UpdateMyPrefsEmailListByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_email_position.put import UpdateMyPrefsEmailPositionByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_show_list_guide.put import UpdateMyPrefsShowListGuideByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar.put import UpdateMyPrefsShowSidebarRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar_board_actions.put import UpdateMyPrefsShowSidebarActionsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar_activity.put import UpdateMyPrefsShowSidebarActivityByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_name.put import UpdateNameByIdRaw
from trello_python_sdk.paths.boards_id_board_id_organization.put import UpdateOrganizationByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_prefs_background.put import UpdatePrefsBackgroundByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_prefs_calendar_feed_enabled.put import UpdatePrefsCalendarFeedEnabledByIdRaw
from trello_python_sdk.paths.boards_id_board_prefs_card_aging.put import UpdatePrefsCardAgingByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_prefs_card_covers.put import UpdatePrefsCardCoversByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_prefs_comments.put import UpdatePrefsCommentsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_prefs_invitations.put import UpdatePrefsInvitationsByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_prefs_permission_level.put import UpdatePrefsPermissionLevelByIdRaw
from trello_python_sdk.paths.boards_id_board_prefs_self_join.put import UpdatePrefsSelfJoinByIdBoardRaw
from trello_python_sdk.paths.boards_id_board_my_prefs_show_sidebar_members.put import UpdatePrefsShowSidebarMembersByIdRaw
from trello_python_sdk.paths.boards_id_board_subscribed.put import UpdateSubscribedByIdRaw
from trello_python_sdk.paths.boards_id_board_prefs_voting.put import UpdateVotingPrefsByIdRaw


class BoardApiRaw(
    AddChecklistsRaw,
    AddLabelsByIdBoardRaw,
    AddPowerUpsByIdBoardRaw,
    CreateBoardRaw,
    CreateListsByIdBoardRaw,
    FilterCardsByIdBoardRaw,
    GenerateCalendarKeyByIdRaw,
    GenerateEmailKeyRaw,
    GetBoardStarsByIdRaw,
    GetByIdRaw,
    GetByIdFieldRaw,
    GetCardsByIdBoardRaw,
    GetCardsByIdBoardByIdCardRaw,
    GetChecklistsByIdRaw,
    GetDeltasByIdBoardRaw,
    GetLabelsByIdBoardByIdLabelRaw,
    GetListsByFilterRaw,
    GetListsByIdBoardRaw,
    GetMembersByFilterRaw,
    GetMembersByIdBoardRaw,
    GetMembersCardsByIdBoardByIdMemberRaw,
    GetMembersInvitedByFieldRaw,
    GetMembersInvitedByIdBoardRaw,
    GetMembershipsByIdBoardRaw,
    GetMembershipsByIdBoardByIdMembershipRaw,
    GetMyPrefsByIdRaw,
    GetOrganizationByIdRaw,
    GetOrganizationByIdBoardByFieldRaw,
    ListActionsByIdBoardRaw,
    ListLabelsByIdBoardRaw,
    MarkAsViewedByIdBoardRaw,
    RemoveMemberRaw,
    RemovePowerUpRaw,
    UpdateByIdRaw,
    UpdateClosedByIdRaw,
    UpdateDescriptionByIdBoardRaw,
    UpdateLabelNamesBlueByIdRaw,
    UpdateLabelNamesGreenByIdBoardPutRaw,
    UpdateLabelNamesOrangeByIdBoardRaw,
    UpdateLabelNamesPurpleByIdBoardRaw,
    UpdateLabelNamesRedRaw,
    UpdateLabelNamesYellowByIdBoardRaw,
    UpdateMembersByIdBoardRaw,
    UpdateMembersByIdBoardByIdMemberRaw,
    UpdateMembershipsByIdBoardByIdMembershipRaw,
    UpdateMyPrefsEmailListByIdBoardRaw,
    UpdateMyPrefsEmailPositionByIdBoardRaw,
    UpdateMyPrefsShowListGuideByIdBoardRaw,
    UpdateMyPrefsShowSidebarRaw,
    UpdateMyPrefsShowSidebarActionsByIdBoardRaw,
    UpdateMyPrefsShowSidebarActivityByIdBoardRaw,
    UpdateNameByIdRaw,
    UpdateOrganizationByIdBoardRaw,
    UpdatePrefsBackgroundByIdBoardRaw,
    UpdatePrefsCalendarFeedEnabledByIdRaw,
    UpdatePrefsCardAgingByIdBoardRaw,
    UpdatePrefsCardCoversByIdBoardRaw,
    UpdatePrefsCommentsByIdBoardRaw,
    UpdatePrefsInvitationsByIdBoardRaw,
    UpdatePrefsPermissionLevelByIdRaw,
    UpdatePrefsSelfJoinByIdBoardRaw,
    UpdatePrefsShowSidebarMembersByIdRaw,
    UpdateSubscribedByIdRaw,
    UpdateVotingPrefsByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
