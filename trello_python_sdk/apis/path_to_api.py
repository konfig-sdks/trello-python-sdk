import typing_extensions

from trello_python_sdk.paths import PathValues
from trello_python_sdk.apis.paths.actions_id_action import ActionsIdAction
from trello_python_sdk.apis.paths.actions_id_action_board import ActionsIdActionBoard
from trello_python_sdk.apis.paths.actions_id_action_board_field import ActionsIdActionBoardField
from trello_python_sdk.apis.paths.actions_id_action_card import ActionsIdActionCard
from trello_python_sdk.apis.paths.actions_id_action_card_field import ActionsIdActionCardField
from trello_python_sdk.apis.paths.actions_id_action_display import ActionsIdActionDisplay
from trello_python_sdk.apis.paths.actions_id_action_entities import ActionsIdActionEntities
from trello_python_sdk.apis.paths.actions_id_action_list import ActionsIdActionList
from trello_python_sdk.apis.paths.actions_id_action_list_field import ActionsIdActionListField
from trello_python_sdk.apis.paths.actions_id_action_member import ActionsIdActionMember
from trello_python_sdk.apis.paths.actions_id_action_member_field import ActionsIdActionMemberField
from trello_python_sdk.apis.paths.actions_id_action_member_creator import ActionsIdActionMemberCreator
from trello_python_sdk.apis.paths.actions_id_action_member_creator_field import ActionsIdActionMemberCreatorField
from trello_python_sdk.apis.paths.actions_id_action_organization import ActionsIdActionOrganization
from trello_python_sdk.apis.paths.actions_id_action_organization_field import ActionsIdActionOrganizationField
from trello_python_sdk.apis.paths.actions_id_action_text import ActionsIdActionText
from trello_python_sdk.apis.paths.actions_id_action_field import ActionsIdActionField
from trello_python_sdk.apis.paths.batch import Batch
from trello_python_sdk.apis.paths.boards import Boards
from trello_python_sdk.apis.paths.boards_id_board import BoardsIdBoard
from trello_python_sdk.apis.paths.boards_id_board_actions import BoardsIdBoardActions
from trello_python_sdk.apis.paths.boards_id_board_board_stars import BoardsIdBoardBoardStars
from trello_python_sdk.apis.paths.boards_id_board_calendar_key_generate import BoardsIdBoardCalendarKeyGenerate
from trello_python_sdk.apis.paths.boards_id_board_cards import BoardsIdBoardCards
from trello_python_sdk.apis.paths.boards_id_board_cards_filter import BoardsIdBoardCardsFilter
from trello_python_sdk.apis.paths.boards_id_board_cards_id_card import BoardsIdBoardCardsIdCard
from trello_python_sdk.apis.paths.boards_id_board_checklists import BoardsIdBoardChecklists
from trello_python_sdk.apis.paths.boards_id_board_closed import BoardsIdBoardClosed
from trello_python_sdk.apis.paths.boards_id_board_deltas import BoardsIdBoardDeltas
from trello_python_sdk.apis.paths.boards_id_board_desc import BoardsIdBoardDesc
from trello_python_sdk.apis.paths.boards_id_board_email_key_generate import BoardsIdBoardEmailKeyGenerate
from trello_python_sdk.apis.paths.boards_id_board_id_organization import BoardsIdBoardIdOrganization
from trello_python_sdk.apis.paths.boards_id_board_label_names_blue import BoardsIdBoardLabelNamesBlue
from trello_python_sdk.apis.paths.boards_id_board_label_names_green import BoardsIdBoardLabelNamesGreen
from trello_python_sdk.apis.paths.boards_id_board_label_names_orange import BoardsIdBoardLabelNamesOrange
from trello_python_sdk.apis.paths.boards_id_board_label_names_purple import BoardsIdBoardLabelNamesPurple
from trello_python_sdk.apis.paths.boards_id_board_label_names_red import BoardsIdBoardLabelNamesRed
from trello_python_sdk.apis.paths.boards_id_board_label_names_yellow import BoardsIdBoardLabelNamesYellow
from trello_python_sdk.apis.paths.boards_id_board_labels import BoardsIdBoardLabels
from trello_python_sdk.apis.paths.boards_id_board_labels_id_label import BoardsIdBoardLabelsIdLabel
from trello_python_sdk.apis.paths.boards_id_board_lists import BoardsIdBoardLists
from trello_python_sdk.apis.paths.boards_id_board_lists_filter import BoardsIdBoardListsFilter
from trello_python_sdk.apis.paths.boards_id_board_mark_as_viewed import BoardsIdBoardMarkAsViewed
from trello_python_sdk.apis.paths.boards_id_board_members import BoardsIdBoardMembers
from trello_python_sdk.apis.paths.boards_id_board_members_filter import BoardsIdBoardMembersFilter
from trello_python_sdk.apis.paths.boards_id_board_members_id_member import BoardsIdBoardMembersIdMember
from trello_python_sdk.apis.paths.boards_id_board_members_id_member_cards import BoardsIdBoardMembersIdMemberCards
from trello_python_sdk.apis.paths.boards_id_board_members_invited import BoardsIdBoardMembersInvited
from trello_python_sdk.apis.paths.boards_id_board_members_invited_field import BoardsIdBoardMembersInvitedField
from trello_python_sdk.apis.paths.boards_id_board_memberships import BoardsIdBoardMemberships
from trello_python_sdk.apis.paths.boards_id_board_memberships_id_membership import BoardsIdBoardMembershipsIdMembership
from trello_python_sdk.apis.paths.boards_id_board_my_prefs import BoardsIdBoardMyPrefs
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_email_position import BoardsIdBoardMyPrefsEmailPosition
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_id_email_list import BoardsIdBoardMyPrefsIdEmailList
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_show_list_guide import BoardsIdBoardMyPrefsShowListGuide
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_show_sidebar import BoardsIdBoardMyPrefsShowSidebar
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_show_sidebar_activity import BoardsIdBoardMyPrefsShowSidebarActivity
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_show_sidebar_board_actions import BoardsIdBoardMyPrefsShowSidebarBoardActions
from trello_python_sdk.apis.paths.boards_id_board_my_prefs_show_sidebar_members import BoardsIdBoardMyPrefsShowSidebarMembers
from trello_python_sdk.apis.paths.boards_id_board_name import BoardsIdBoardName
from trello_python_sdk.apis.paths.boards_id_board_organization import BoardsIdBoardOrganization
from trello_python_sdk.apis.paths.boards_id_board_organization_field import BoardsIdBoardOrganizationField
from trello_python_sdk.apis.paths.boards_id_board_power_ups import BoardsIdBoardPowerUps
from trello_python_sdk.apis.paths.boards_id_board_power_ups_power_up import BoardsIdBoardPowerUpsPowerUp
from trello_python_sdk.apis.paths.boards_id_board_prefs_background import BoardsIdBoardPrefsBackground
from trello_python_sdk.apis.paths.boards_id_board_prefs_calendar_feed_enabled import BoardsIdBoardPrefsCalendarFeedEnabled
from trello_python_sdk.apis.paths.boards_id_board_prefs_card_aging import BoardsIdBoardPrefsCardAging
from trello_python_sdk.apis.paths.boards_id_board_prefs_card_covers import BoardsIdBoardPrefsCardCovers
from trello_python_sdk.apis.paths.boards_id_board_prefs_comments import BoardsIdBoardPrefsComments
from trello_python_sdk.apis.paths.boards_id_board_prefs_invitations import BoardsIdBoardPrefsInvitations
from trello_python_sdk.apis.paths.boards_id_board_prefs_permission_level import BoardsIdBoardPrefsPermissionLevel
from trello_python_sdk.apis.paths.boards_id_board_prefs_self_join import BoardsIdBoardPrefsSelfJoin
from trello_python_sdk.apis.paths.boards_id_board_prefs_voting import BoardsIdBoardPrefsVoting
from trello_python_sdk.apis.paths.boards_id_board_subscribed import BoardsIdBoardSubscribed
from trello_python_sdk.apis.paths.boards_id_board_field import BoardsIdBoardField
from trello_python_sdk.apis.paths.cards import Cards
from trello_python_sdk.apis.paths.cards_id_card import CardsIdCard
from trello_python_sdk.apis.paths.cards_id_card_actions import CardsIdCardActions
from trello_python_sdk.apis.paths.cards_id_card_actions_comments import CardsIdCardActionsComments
from trello_python_sdk.apis.paths.cards_id_card_actions_id_action_comments import CardsIdCardActionsIdActionComments
from trello_python_sdk.apis.paths.cards_id_card_attachments import CardsIdCardAttachments
from trello_python_sdk.apis.paths.cards_id_card_attachments_id_attachment import CardsIdCardAttachmentsIdAttachment
from trello_python_sdk.apis.paths.cards_id_card_board import CardsIdCardBoard
from trello_python_sdk.apis.paths.cards_id_card_board_field import CardsIdCardBoardField
from trello_python_sdk.apis.paths.cards_id_card_check_item_states import CardsIdCardCheckItemStates
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_current_check_item_id_check_item import CardsIdCardChecklistIdChecklistCurrentCheckItemIdCheckItem
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_check_item import CardsIdCardChecklistIdChecklistCheckItem
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item import CardsIdCardChecklistIdChecklistCheckItemIdCheckItem
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_convert_to_card import CardsIdCardChecklistIdChecklistCheckItemIdCheckItemConvertToCard
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_name import CardsIdCardChecklistIdChecklistCheckItemIdCheckItemName
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_pos import CardsIdCardChecklistIdChecklistCheckItemIdCheckItemPos
from trello_python_sdk.apis.paths.cards_id_card_checklist_id_checklist_check_item_id_check_item_state import CardsIdCardChecklistIdChecklistCheckItemIdCheckItemState
from trello_python_sdk.apis.paths.cards_id_card_checklists import CardsIdCardChecklists
from trello_python_sdk.apis.paths.cards_id_card_checklists_id_checklist import CardsIdCardChecklistsIdChecklist
from trello_python_sdk.apis.paths.cards_id_card_closed import CardsIdCardClosed
from trello_python_sdk.apis.paths.cards_id_card_desc import CardsIdCardDesc
from trello_python_sdk.apis.paths.cards_id_card_due import CardsIdCardDue
from trello_python_sdk.apis.paths.cards_id_card_id_attachment_cover import CardsIdCardIdAttachmentCover
from trello_python_sdk.apis.paths.cards_id_card_id_board import CardsIdCardIdBoard
from trello_python_sdk.apis.paths.cards_id_card_id_labels import CardsIdCardIdLabels
from trello_python_sdk.apis.paths.cards_id_card_id_labels_id_label import CardsIdCardIdLabelsIdLabel
from trello_python_sdk.apis.paths.cards_id_card_id_list import CardsIdCardIdList
from trello_python_sdk.apis.paths.cards_id_card_id_members import CardsIdCardIdMembers
from trello_python_sdk.apis.paths.cards_id_card_id_members_id_member import CardsIdCardIdMembersIdMember
from trello_python_sdk.apis.paths.cards_id_card_labels import CardsIdCardLabels
from trello_python_sdk.apis.paths.cards_id_card_labels_color import CardsIdCardLabelsColor
from trello_python_sdk.apis.paths.cards_id_card_list import CardsIdCardList
from trello_python_sdk.apis.paths.cards_id_card_list_field import CardsIdCardListField
from trello_python_sdk.apis.paths.cards_id_card_mark_associated_notifications_read import CardsIdCardMarkAssociatedNotificationsRead
from trello_python_sdk.apis.paths.cards_id_card_members import CardsIdCardMembers
from trello_python_sdk.apis.paths.cards_id_card_members_voted import CardsIdCardMembersVoted
from trello_python_sdk.apis.paths.cards_id_card_members_voted_id_member import CardsIdCardMembersVotedIdMember
from trello_python_sdk.apis.paths.cards_id_card_name import CardsIdCardName
from trello_python_sdk.apis.paths.cards_id_card_pos import CardsIdCardPos
from trello_python_sdk.apis.paths.cards_id_card_stickers import CardsIdCardStickers
from trello_python_sdk.apis.paths.cards_id_card_stickers_id_sticker import CardsIdCardStickersIdSticker
from trello_python_sdk.apis.paths.cards_id_card_subscribed import CardsIdCardSubscribed
from trello_python_sdk.apis.paths.cards_id_card_field import CardsIdCardField
from trello_python_sdk.apis.paths.checklists import Checklists
from trello_python_sdk.apis.paths.checklists_id_checklist import ChecklistsIdChecklist
from trello_python_sdk.apis.paths.checklists_id_checklist_board import ChecklistsIdChecklistBoard
from trello_python_sdk.apis.paths.checklists_id_checklist_board_field import ChecklistsIdChecklistBoardField
from trello_python_sdk.apis.paths.checklists_id_checklist_cards import ChecklistsIdChecklistCards
from trello_python_sdk.apis.paths.checklists_id_checklist_cards_filter import ChecklistsIdChecklistCardsFilter
from trello_python_sdk.apis.paths.checklists_id_checklist_check_items import ChecklistsIdChecklistCheckItems
from trello_python_sdk.apis.paths.checklists_id_checklist_check_items_id_check_item import ChecklistsIdChecklistCheckItemsIdCheckItem
from trello_python_sdk.apis.paths.checklists_id_checklist_id_card import ChecklistsIdChecklistIdCard
from trello_python_sdk.apis.paths.checklists_id_checklist_name import ChecklistsIdChecklistName
from trello_python_sdk.apis.paths.checklists_id_checklist_pos import ChecklistsIdChecklistPos
from trello_python_sdk.apis.paths.checklists_id_checklist_field import ChecklistsIdChecklistField
from trello_python_sdk.apis.paths.labels import Labels
from trello_python_sdk.apis.paths.labels_id_label import LabelsIdLabel
from trello_python_sdk.apis.paths.labels_id_label_board import LabelsIdLabelBoard
from trello_python_sdk.apis.paths.labels_id_label_board_field import LabelsIdLabelBoardField
from trello_python_sdk.apis.paths.labels_id_label_color import LabelsIdLabelColor
from trello_python_sdk.apis.paths.labels_id_label_name import LabelsIdLabelName
from trello_python_sdk.apis.paths.lists import Lists
from trello_python_sdk.apis.paths.lists_id_list import ListsIdList
from trello_python_sdk.apis.paths.lists_id_list_actions import ListsIdListActions
from trello_python_sdk.apis.paths.lists_id_list_archive_all_cards import ListsIdListArchiveAllCards
from trello_python_sdk.apis.paths.lists_id_list_board import ListsIdListBoard
from trello_python_sdk.apis.paths.lists_id_list_board_field import ListsIdListBoardField
from trello_python_sdk.apis.paths.lists_id_list_cards import ListsIdListCards
from trello_python_sdk.apis.paths.lists_id_list_cards_filter import ListsIdListCardsFilter
from trello_python_sdk.apis.paths.lists_id_list_closed import ListsIdListClosed
from trello_python_sdk.apis.paths.lists_id_list_id_board import ListsIdListIdBoard
from trello_python_sdk.apis.paths.lists_id_list_move_all_cards import ListsIdListMoveAllCards
from trello_python_sdk.apis.paths.lists_id_list_name import ListsIdListName
from trello_python_sdk.apis.paths.lists_id_list_pos import ListsIdListPos
from trello_python_sdk.apis.paths.lists_id_list_subscribed import ListsIdListSubscribed
from trello_python_sdk.apis.paths.lists_id_list_field import ListsIdListField
from trello_python_sdk.apis.paths.members_id_member import MembersIdMember
from trello_python_sdk.apis.paths.members_id_member_actions import MembersIdMemberActions
from trello_python_sdk.apis.paths.members_id_member_avatar import MembersIdMemberAvatar
from trello_python_sdk.apis.paths.members_id_member_avatar_source import MembersIdMemberAvatarSource
from trello_python_sdk.apis.paths.members_id_member_bio import MembersIdMemberBio
from trello_python_sdk.apis.paths.members_id_member_board_backgrounds import MembersIdMemberBoardBackgrounds
from trello_python_sdk.apis.paths.members_id_member_board_backgrounds_id_board_background import MembersIdMemberBoardBackgroundsIdBoardBackground
from trello_python_sdk.apis.paths.members_id_member_board_stars import MembersIdMemberBoardStars
from trello_python_sdk.apis.paths.members_id_member_board_stars_id_board_star import MembersIdMemberBoardStarsIdBoardStar
from trello_python_sdk.apis.paths.members_id_member_board_stars_id_board_star_id_board import MembersIdMemberBoardStarsIdBoardStarIdBoard
from trello_python_sdk.apis.paths.members_id_member_board_stars_id_board_star_pos import MembersIdMemberBoardStarsIdBoardStarPos
from trello_python_sdk.apis.paths.members_id_member_boards import MembersIdMemberBoards
from trello_python_sdk.apis.paths.members_id_member_boards_filter import MembersIdMemberBoardsFilter
from trello_python_sdk.apis.paths.members_id_member_boards_invited import MembersIdMemberBoardsInvited
from trello_python_sdk.apis.paths.members_id_member_boards_invited_field import MembersIdMemberBoardsInvitedField
from trello_python_sdk.apis.paths.members_id_member_cards import MembersIdMemberCards
from trello_python_sdk.apis.paths.members_id_member_cards_filter import MembersIdMemberCardsFilter
from trello_python_sdk.apis.paths.members_id_member_custom_board_backgrounds import MembersIdMemberCustomBoardBackgrounds
from trello_python_sdk.apis.paths.members_id_member_custom_board_backgrounds_id_board_background import MembersIdMemberCustomBoardBackgroundsIdBoardBackground
from trello_python_sdk.apis.paths.members_id_member_custom_emoji import MembersIdMemberCustomEmoji
from trello_python_sdk.apis.paths.members_id_member_custom_emoji_id_custom_emoji import MembersIdMemberCustomEmojiIdCustomEmoji
from trello_python_sdk.apis.paths.members_id_member_custom_stickers import MembersIdMemberCustomStickers
from trello_python_sdk.apis.paths.members_id_member_custom_stickers_id_custom_sticker import MembersIdMemberCustomStickersIdCustomSticker
from trello_python_sdk.apis.paths.members_id_member_deltas import MembersIdMemberDeltas
from trello_python_sdk.apis.paths.members_id_member_full_name import MembersIdMemberFullName
from trello_python_sdk.apis.paths.members_id_member_initials import MembersIdMemberInitials
from trello_python_sdk.apis.paths.members_id_member_notifications import MembersIdMemberNotifications
from trello_python_sdk.apis.paths.members_id_member_notifications_filter import MembersIdMemberNotificationsFilter
from trello_python_sdk.apis.paths.members_id_member_one_time_messages_dismissed import MembersIdMemberOneTimeMessagesDismissed
from trello_python_sdk.apis.paths.members_id_member_organizations import MembersIdMemberOrganizations
from trello_python_sdk.apis.paths.members_id_member_organizations_filter import MembersIdMemberOrganizationsFilter
from trello_python_sdk.apis.paths.members_id_member_organizations_invited import MembersIdMemberOrganizationsInvited
from trello_python_sdk.apis.paths.members_id_member_organizations_invited_field import MembersIdMemberOrganizationsInvitedField
from trello_python_sdk.apis.paths.members_id_member_prefs_color_blind import MembersIdMemberPrefsColorBlind
from trello_python_sdk.apis.paths.members_id_member_prefs_locale import MembersIdMemberPrefsLocale
from trello_python_sdk.apis.paths.members_id_member_prefs_minutes_between_summaries import MembersIdMemberPrefsMinutesBetweenSummaries
from trello_python_sdk.apis.paths.members_id_member_saved_searches import MembersIdMemberSavedSearches
from trello_python_sdk.apis.paths.members_id_member_saved_searches_id_saved_search import MembersIdMemberSavedSearchesIdSavedSearch
from trello_python_sdk.apis.paths.members_id_member_saved_searches_id_saved_search_name import MembersIdMemberSavedSearchesIdSavedSearchName
from trello_python_sdk.apis.paths.members_id_member_saved_searches_id_saved_search_pos import MembersIdMemberSavedSearchesIdSavedSearchPos
from trello_python_sdk.apis.paths.members_id_member_saved_searches_id_saved_search_query import MembersIdMemberSavedSearchesIdSavedSearchQuery
from trello_python_sdk.apis.paths.members_id_member_tokens import MembersIdMemberTokens
from trello_python_sdk.apis.paths.members_id_member_username import MembersIdMemberUsername
from trello_python_sdk.apis.paths.members_id_member_field import MembersIdMemberField
from trello_python_sdk.apis.paths.notifications_all_read import NotificationsAllRead
from trello_python_sdk.apis.paths.notifications_id_notification import NotificationsIdNotification
from trello_python_sdk.apis.paths.notifications_id_notification_board import NotificationsIdNotificationBoard
from trello_python_sdk.apis.paths.notifications_id_notification_board_field import NotificationsIdNotificationBoardField
from trello_python_sdk.apis.paths.notifications_id_notification_card import NotificationsIdNotificationCard
from trello_python_sdk.apis.paths.notifications_id_notification_card_field import NotificationsIdNotificationCardField
from trello_python_sdk.apis.paths.notifications_id_notification_display import NotificationsIdNotificationDisplay
from trello_python_sdk.apis.paths.notifications_id_notification_entities import NotificationsIdNotificationEntities
from trello_python_sdk.apis.paths.notifications_id_notification_list import NotificationsIdNotificationList
from trello_python_sdk.apis.paths.notifications_id_notification_list_field import NotificationsIdNotificationListField
from trello_python_sdk.apis.paths.notifications_id_notification_member import NotificationsIdNotificationMember
from trello_python_sdk.apis.paths.notifications_id_notification_member_field import NotificationsIdNotificationMemberField
from trello_python_sdk.apis.paths.notifications_id_notification_member_creator import NotificationsIdNotificationMemberCreator
from trello_python_sdk.apis.paths.notifications_id_notification_member_creator_field import NotificationsIdNotificationMemberCreatorField
from trello_python_sdk.apis.paths.notifications_id_notification_organization import NotificationsIdNotificationOrganization
from trello_python_sdk.apis.paths.notifications_id_notification_organization_field import NotificationsIdNotificationOrganizationField
from trello_python_sdk.apis.paths.notifications_id_notification_unread import NotificationsIdNotificationUnread
from trello_python_sdk.apis.paths.notifications_id_notification_field import NotificationsIdNotificationField
from trello_python_sdk.apis.paths.organizations import Organizations
from trello_python_sdk.apis.paths.organizations_id_org import OrganizationsIdOrg
from trello_python_sdk.apis.paths.organizations_id_org_actions import OrganizationsIdOrgActions
from trello_python_sdk.apis.paths.organizations_id_org_boards import OrganizationsIdOrgBoards
from trello_python_sdk.apis.paths.organizations_id_org_boards_filter import OrganizationsIdOrgBoardsFilter
from trello_python_sdk.apis.paths.organizations_id_org_deltas import OrganizationsIdOrgDeltas
from trello_python_sdk.apis.paths.organizations_id_org_desc import OrganizationsIdOrgDesc
from trello_python_sdk.apis.paths.organizations_id_org_display_name import OrganizationsIdOrgDisplayName
from trello_python_sdk.apis.paths.organizations_id_org_logo import OrganizationsIdOrgLogo
from trello_python_sdk.apis.paths.organizations_id_org_members import OrganizationsIdOrgMembers
from trello_python_sdk.apis.paths.organizations_id_org_members_filter import OrganizationsIdOrgMembersFilter
from trello_python_sdk.apis.paths.organizations_id_org_members_id_member import OrganizationsIdOrgMembersIdMember
from trello_python_sdk.apis.paths.organizations_id_org_members_id_member_all import OrganizationsIdOrgMembersIdMemberAll
from trello_python_sdk.apis.paths.organizations_id_org_members_id_member_cards import OrganizationsIdOrgMembersIdMemberCards
from trello_python_sdk.apis.paths.organizations_id_org_members_id_member_deactivated import OrganizationsIdOrgMembersIdMemberDeactivated
from trello_python_sdk.apis.paths.organizations_id_org_members_invited import OrganizationsIdOrgMembersInvited
from trello_python_sdk.apis.paths.organizations_id_org_members_invited_field import OrganizationsIdOrgMembersInvitedField
from trello_python_sdk.apis.paths.organizations_id_org_memberships import OrganizationsIdOrgMemberships
from trello_python_sdk.apis.paths.organizations_id_org_memberships_id_membership import OrganizationsIdOrgMembershipsIdMembership
from trello_python_sdk.apis.paths.organizations_id_org_name import OrganizationsIdOrgName
from trello_python_sdk.apis.paths.organizations_id_org_prefs_associated_domain import OrganizationsIdOrgPrefsAssociatedDomain
from trello_python_sdk.apis.paths.organizations_id_org_prefs_board_visibility_restrict_org import OrganizationsIdOrgPrefsBoardVisibilityRestrictOrg
from trello_python_sdk.apis.paths.organizations_id_org_prefs_board_visibility_restrict_private import OrganizationsIdOrgPrefsBoardVisibilityRestrictPrivate
from trello_python_sdk.apis.paths.organizations_id_org_prefs_board_visibility_restrict_public import OrganizationsIdOrgPrefsBoardVisibilityRestrictPublic
from trello_python_sdk.apis.paths.organizations_id_org_prefs_external_members_disabled import OrganizationsIdOrgPrefsExternalMembersDisabled
from trello_python_sdk.apis.paths.organizations_id_org_prefs_google_apps_version import OrganizationsIdOrgPrefsGoogleAppsVersion
from trello_python_sdk.apis.paths.organizations_id_org_prefs_org_invite_restrict import OrganizationsIdOrgPrefsOrgInviteRestrict
from trello_python_sdk.apis.paths.organizations_id_org_prefs_permission_level import OrganizationsIdOrgPrefsPermissionLevel
from trello_python_sdk.apis.paths.organizations_id_org_website import OrganizationsIdOrgWebsite
from trello_python_sdk.apis.paths.organizations_id_org_field import OrganizationsIdOrgField
from trello_python_sdk.apis.paths.search import Search
from trello_python_sdk.apis.paths.search_members import SearchMembers
from trello_python_sdk.apis.paths.sessions import Sessions
from trello_python_sdk.apis.paths.sessions_socket import SessionsSocket
from trello_python_sdk.apis.paths.sessions_id_session import SessionsIdSession
from trello_python_sdk.apis.paths.sessions_id_session_status import SessionsIdSessionStatus
from trello_python_sdk.apis.paths.tokens_token import TokensToken
from trello_python_sdk.apis.paths.tokens_token_member import TokensTokenMember
from trello_python_sdk.apis.paths.tokens_token_member_field import TokensTokenMemberField
from trello_python_sdk.apis.paths.tokens_token_webhooks import TokensTokenWebhooks
from trello_python_sdk.apis.paths.tokens_token_webhooks_id_webhook import TokensTokenWebhooksIdWebhook
from trello_python_sdk.apis.paths.tokens_token_field import TokensTokenField
from trello_python_sdk.apis.paths.types_id import TypesId
from trello_python_sdk.apis.paths.webhooks import Webhooks
from trello_python_sdk.apis.paths.webhooks_id_webhook import WebhooksIdWebhook
from trello_python_sdk.apis.paths.webhooks_id_webhook_active import WebhooksIdWebhookActive
from trello_python_sdk.apis.paths.webhooks_id_webhook_callback_url import WebhooksIdWebhookCallbackURL
from trello_python_sdk.apis.paths.webhooks_id_webhook_description import WebhooksIdWebhookDescription
from trello_python_sdk.apis.paths.webhooks_id_webhook_id_model import WebhooksIdWebhookIdModel
from trello_python_sdk.apis.paths.webhooks_id_webhook_field import WebhooksIdWebhookField

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTIONS_ID_ACTION: ActionsIdAction,
        PathValues.ACTIONS_ID_ACTION_BOARD: ActionsIdActionBoard,
        PathValues.ACTIONS_ID_ACTION_BOARD_FIELD: ActionsIdActionBoardField,
        PathValues.ACTIONS_ID_ACTION_CARD: ActionsIdActionCard,
        PathValues.ACTIONS_ID_ACTION_CARD_FIELD: ActionsIdActionCardField,
        PathValues.ACTIONS_ID_ACTION_DISPLAY: ActionsIdActionDisplay,
        PathValues.ACTIONS_ID_ACTION_ENTITIES: ActionsIdActionEntities,
        PathValues.ACTIONS_ID_ACTION_LIST: ActionsIdActionList,
        PathValues.ACTIONS_ID_ACTION_LIST_FIELD: ActionsIdActionListField,
        PathValues.ACTIONS_ID_ACTION_MEMBER: ActionsIdActionMember,
        PathValues.ACTIONS_ID_ACTION_MEMBER_FIELD: ActionsIdActionMemberField,
        PathValues.ACTIONS_ID_ACTION_MEMBER_CREATOR: ActionsIdActionMemberCreator,
        PathValues.ACTIONS_ID_ACTION_MEMBER_CREATOR_FIELD: ActionsIdActionMemberCreatorField,
        PathValues.ACTIONS_ID_ACTION_ORGANIZATION: ActionsIdActionOrganization,
        PathValues.ACTIONS_ID_ACTION_ORGANIZATION_FIELD: ActionsIdActionOrganizationField,
        PathValues.ACTIONS_ID_ACTION_TEXT: ActionsIdActionText,
        PathValues.ACTIONS_ID_ACTION_FIELD: ActionsIdActionField,
        PathValues.BATCH: Batch,
        PathValues.BOARDS: Boards,
        PathValues.BOARDS_ID_BOARD: BoardsIdBoard,
        PathValues.BOARDS_ID_BOARD_ACTIONS: BoardsIdBoardActions,
        PathValues.BOARDS_ID_BOARD_BOARD_STARS: BoardsIdBoardBoardStars,
        PathValues.BOARDS_ID_BOARD_CALENDAR_KEY_GENERATE: BoardsIdBoardCalendarKeyGenerate,
        PathValues.BOARDS_ID_BOARD_CARDS: BoardsIdBoardCards,
        PathValues.BOARDS_ID_BOARD_CARDS_FILTER: BoardsIdBoardCardsFilter,
        PathValues.BOARDS_ID_BOARD_CARDS_ID_CARD: BoardsIdBoardCardsIdCard,
        PathValues.BOARDS_ID_BOARD_CHECKLISTS: BoardsIdBoardChecklists,
        PathValues.BOARDS_ID_BOARD_CLOSED: BoardsIdBoardClosed,
        PathValues.BOARDS_ID_BOARD_DELTAS: BoardsIdBoardDeltas,
        PathValues.BOARDS_ID_BOARD_DESC: BoardsIdBoardDesc,
        PathValues.BOARDS_ID_BOARD_EMAIL_KEY_GENERATE: BoardsIdBoardEmailKeyGenerate,
        PathValues.BOARDS_ID_BOARD_ID_ORGANIZATION: BoardsIdBoardIdOrganization,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_BLUE: BoardsIdBoardLabelNamesBlue,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_GREEN: BoardsIdBoardLabelNamesGreen,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_ORANGE: BoardsIdBoardLabelNamesOrange,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_PURPLE: BoardsIdBoardLabelNamesPurple,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_RED: BoardsIdBoardLabelNamesRed,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_YELLOW: BoardsIdBoardLabelNamesYellow,
        PathValues.BOARDS_ID_BOARD_LABELS: BoardsIdBoardLabels,
        PathValues.BOARDS_ID_BOARD_LABELS_ID_LABEL: BoardsIdBoardLabelsIdLabel,
        PathValues.BOARDS_ID_BOARD_LISTS: BoardsIdBoardLists,
        PathValues.BOARDS_ID_BOARD_LISTS_FILTER: BoardsIdBoardListsFilter,
        PathValues.BOARDS_ID_BOARD_MARK_AS_VIEWED: BoardsIdBoardMarkAsViewed,
        PathValues.BOARDS_ID_BOARD_MEMBERS: BoardsIdBoardMembers,
        PathValues.BOARDS_ID_BOARD_MEMBERS_FILTER: BoardsIdBoardMembersFilter,
        PathValues.BOARDS_ID_BOARD_MEMBERS_ID_MEMBER: BoardsIdBoardMembersIdMember,
        PathValues.BOARDS_ID_BOARD_MEMBERS_ID_MEMBER_CARDS: BoardsIdBoardMembersIdMemberCards,
        PathValues.BOARDS_ID_BOARD_MEMBERS_INVITED: BoardsIdBoardMembersInvited,
        PathValues.BOARDS_ID_BOARD_MEMBERS_INVITED_FIELD: BoardsIdBoardMembersInvitedField,
        PathValues.BOARDS_ID_BOARD_MEMBERSHIPS: BoardsIdBoardMemberships,
        PathValues.BOARDS_ID_BOARD_MEMBERSHIPS_ID_MEMBERSHIP: BoardsIdBoardMembershipsIdMembership,
        PathValues.BOARDS_ID_BOARD_MY_PREFS: BoardsIdBoardMyPrefs,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_EMAIL_POSITION: BoardsIdBoardMyPrefsEmailPosition,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_ID_EMAIL_LIST: BoardsIdBoardMyPrefsIdEmailList,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_LIST_GUIDE: BoardsIdBoardMyPrefsShowListGuide,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR: BoardsIdBoardMyPrefsShowSidebar,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_ACTIVITY: BoardsIdBoardMyPrefsShowSidebarActivity,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_BOARD_ACTIONS: BoardsIdBoardMyPrefsShowSidebarBoardActions,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_MEMBERS: BoardsIdBoardMyPrefsShowSidebarMembers,
        PathValues.BOARDS_ID_BOARD_NAME: BoardsIdBoardName,
        PathValues.BOARDS_ID_BOARD_ORGANIZATION: BoardsIdBoardOrganization,
        PathValues.BOARDS_ID_BOARD_ORGANIZATION_FIELD: BoardsIdBoardOrganizationField,
        PathValues.BOARDS_ID_BOARD_POWER_UPS: BoardsIdBoardPowerUps,
        PathValues.BOARDS_ID_BOARD_POWER_UPS_POWER_UP: BoardsIdBoardPowerUpsPowerUp,
        PathValues.BOARDS_ID_BOARD_PREFS_BACKGROUND: BoardsIdBoardPrefsBackground,
        PathValues.BOARDS_ID_BOARD_PREFS_CALENDAR_FEED_ENABLED: BoardsIdBoardPrefsCalendarFeedEnabled,
        PathValues.BOARDS_ID_BOARD_PREFS_CARD_AGING: BoardsIdBoardPrefsCardAging,
        PathValues.BOARDS_ID_BOARD_PREFS_CARD_COVERS: BoardsIdBoardPrefsCardCovers,
        PathValues.BOARDS_ID_BOARD_PREFS_COMMENTS: BoardsIdBoardPrefsComments,
        PathValues.BOARDS_ID_BOARD_PREFS_INVITATIONS: BoardsIdBoardPrefsInvitations,
        PathValues.BOARDS_ID_BOARD_PREFS_PERMISSION_LEVEL: BoardsIdBoardPrefsPermissionLevel,
        PathValues.BOARDS_ID_BOARD_PREFS_SELF_JOIN: BoardsIdBoardPrefsSelfJoin,
        PathValues.BOARDS_ID_BOARD_PREFS_VOTING: BoardsIdBoardPrefsVoting,
        PathValues.BOARDS_ID_BOARD_SUBSCRIBED: BoardsIdBoardSubscribed,
        PathValues.BOARDS_ID_BOARD_FIELD: BoardsIdBoardField,
        PathValues.CARDS: Cards,
        PathValues.CARDS_ID_CARD: CardsIdCard,
        PathValues.CARDS_ID_CARD_ACTIONS: CardsIdCardActions,
        PathValues.CARDS_ID_CARD_ACTIONS_COMMENTS: CardsIdCardActionsComments,
        PathValues.CARDS_ID_CARD_ACTIONS_ID_ACTION_COMMENTS: CardsIdCardActionsIdActionComments,
        PathValues.CARDS_ID_CARD_ATTACHMENTS: CardsIdCardAttachments,
        PathValues.CARDS_ID_CARD_ATTACHMENTS_ID_ATTACHMENT: CardsIdCardAttachmentsIdAttachment,
        PathValues.CARDS_ID_CARD_BOARD: CardsIdCardBoard,
        PathValues.CARDS_ID_CARD_BOARD_FIELD: CardsIdCardBoardField,
        PathValues.CARDS_ID_CARD_CHECK_ITEM_STATES: CardsIdCardCheckItemStates,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CURRENT_CHECK_ITEM_ID_CHECK_ITEM: CardsIdCardChecklistIdChecklistCurrentCheckItemIdCheckItem,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM: CardsIdCardChecklistIdChecklistCheckItem,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM: CardsIdCardChecklistIdChecklistCheckItemIdCheckItem,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_CONVERT_TO_CARD: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemConvertToCard,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_NAME: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemName,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_POS: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemPos,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_STATE: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemState,
        PathValues.CARDS_ID_CARD_CHECKLISTS: CardsIdCardChecklists,
        PathValues.CARDS_ID_CARD_CHECKLISTS_ID_CHECKLIST: CardsIdCardChecklistsIdChecklist,
        PathValues.CARDS_ID_CARD_CLOSED: CardsIdCardClosed,
        PathValues.CARDS_ID_CARD_DESC: CardsIdCardDesc,
        PathValues.CARDS_ID_CARD_DUE: CardsIdCardDue,
        PathValues.CARDS_ID_CARD_ID_ATTACHMENT_COVER: CardsIdCardIdAttachmentCover,
        PathValues.CARDS_ID_CARD_ID_BOARD: CardsIdCardIdBoard,
        PathValues.CARDS_ID_CARD_ID_LABELS: CardsIdCardIdLabels,
        PathValues.CARDS_ID_CARD_ID_LABELS_ID_LABEL: CardsIdCardIdLabelsIdLabel,
        PathValues.CARDS_ID_CARD_ID_LIST: CardsIdCardIdList,
        PathValues.CARDS_ID_CARD_ID_MEMBERS: CardsIdCardIdMembers,
        PathValues.CARDS_ID_CARD_ID_MEMBERS_ID_MEMBER: CardsIdCardIdMembersIdMember,
        PathValues.CARDS_ID_CARD_LABELS: CardsIdCardLabels,
        PathValues.CARDS_ID_CARD_LABELS_COLOR: CardsIdCardLabelsColor,
        PathValues.CARDS_ID_CARD_LIST: CardsIdCardList,
        PathValues.CARDS_ID_CARD_LIST_FIELD: CardsIdCardListField,
        PathValues.CARDS_ID_CARD_MARK_ASSOCIATED_NOTIFICATIONS_READ: CardsIdCardMarkAssociatedNotificationsRead,
        PathValues.CARDS_ID_CARD_MEMBERS: CardsIdCardMembers,
        PathValues.CARDS_ID_CARD_MEMBERS_VOTED: CardsIdCardMembersVoted,
        PathValues.CARDS_ID_CARD_MEMBERS_VOTED_ID_MEMBER: CardsIdCardMembersVotedIdMember,
        PathValues.CARDS_ID_CARD_NAME: CardsIdCardName,
        PathValues.CARDS_ID_CARD_POS: CardsIdCardPos,
        PathValues.CARDS_ID_CARD_STICKERS: CardsIdCardStickers,
        PathValues.CARDS_ID_CARD_STICKERS_ID_STICKER: CardsIdCardStickersIdSticker,
        PathValues.CARDS_ID_CARD_SUBSCRIBED: CardsIdCardSubscribed,
        PathValues.CARDS_ID_CARD_FIELD: CardsIdCardField,
        PathValues.CHECKLISTS: Checklists,
        PathValues.CHECKLISTS_ID_CHECKLIST: ChecklistsIdChecklist,
        PathValues.CHECKLISTS_ID_CHECKLIST_BOARD: ChecklistsIdChecklistBoard,
        PathValues.CHECKLISTS_ID_CHECKLIST_BOARD_FIELD: ChecklistsIdChecklistBoardField,
        PathValues.CHECKLISTS_ID_CHECKLIST_CARDS: ChecklistsIdChecklistCards,
        PathValues.CHECKLISTS_ID_CHECKLIST_CARDS_FILTER: ChecklistsIdChecklistCardsFilter,
        PathValues.CHECKLISTS_ID_CHECKLIST_CHECK_ITEMS: ChecklistsIdChecklistCheckItems,
        PathValues.CHECKLISTS_ID_CHECKLIST_CHECK_ITEMS_ID_CHECK_ITEM: ChecklistsIdChecklistCheckItemsIdCheckItem,
        PathValues.CHECKLISTS_ID_CHECKLIST_ID_CARD: ChecklistsIdChecklistIdCard,
        PathValues.CHECKLISTS_ID_CHECKLIST_NAME: ChecklistsIdChecklistName,
        PathValues.CHECKLISTS_ID_CHECKLIST_POS: ChecklistsIdChecklistPos,
        PathValues.CHECKLISTS_ID_CHECKLIST_FIELD: ChecklistsIdChecklistField,
        PathValues.LABELS: Labels,
        PathValues.LABELS_ID_LABEL: LabelsIdLabel,
        PathValues.LABELS_ID_LABEL_BOARD: LabelsIdLabelBoard,
        PathValues.LABELS_ID_LABEL_BOARD_FIELD: LabelsIdLabelBoardField,
        PathValues.LABELS_ID_LABEL_COLOR: LabelsIdLabelColor,
        PathValues.LABELS_ID_LABEL_NAME: LabelsIdLabelName,
        PathValues.LISTS: Lists,
        PathValues.LISTS_ID_LIST: ListsIdList,
        PathValues.LISTS_ID_LIST_ACTIONS: ListsIdListActions,
        PathValues.LISTS_ID_LIST_ARCHIVE_ALL_CARDS: ListsIdListArchiveAllCards,
        PathValues.LISTS_ID_LIST_BOARD: ListsIdListBoard,
        PathValues.LISTS_ID_LIST_BOARD_FIELD: ListsIdListBoardField,
        PathValues.LISTS_ID_LIST_CARDS: ListsIdListCards,
        PathValues.LISTS_ID_LIST_CARDS_FILTER: ListsIdListCardsFilter,
        PathValues.LISTS_ID_LIST_CLOSED: ListsIdListClosed,
        PathValues.LISTS_ID_LIST_ID_BOARD: ListsIdListIdBoard,
        PathValues.LISTS_ID_LIST_MOVE_ALL_CARDS: ListsIdListMoveAllCards,
        PathValues.LISTS_ID_LIST_NAME: ListsIdListName,
        PathValues.LISTS_ID_LIST_POS: ListsIdListPos,
        PathValues.LISTS_ID_LIST_SUBSCRIBED: ListsIdListSubscribed,
        PathValues.LISTS_ID_LIST_FIELD: ListsIdListField,
        PathValues.MEMBERS_ID_MEMBER: MembersIdMember,
        PathValues.MEMBERS_ID_MEMBER_ACTIONS: MembersIdMemberActions,
        PathValues.MEMBERS_ID_MEMBER_AVATAR: MembersIdMemberAvatar,
        PathValues.MEMBERS_ID_MEMBER_AVATAR_SOURCE: MembersIdMemberAvatarSource,
        PathValues.MEMBERS_ID_MEMBER_BIO: MembersIdMemberBio,
        PathValues.MEMBERS_ID_MEMBER_BOARD_BACKGROUNDS: MembersIdMemberBoardBackgrounds,
        PathValues.MEMBERS_ID_MEMBER_BOARD_BACKGROUNDS_ID_BOARD_BACKGROUND: MembersIdMemberBoardBackgroundsIdBoardBackground,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS: MembersIdMemberBoardStars,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR: MembersIdMemberBoardStarsIdBoardStar,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR_ID_BOARD: MembersIdMemberBoardStarsIdBoardStarIdBoard,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR_POS: MembersIdMemberBoardStarsIdBoardStarPos,
        PathValues.MEMBERS_ID_MEMBER_BOARDS: MembersIdMemberBoards,
        PathValues.MEMBERS_ID_MEMBER_BOARDS_FILTER: MembersIdMemberBoardsFilter,
        PathValues.MEMBERS_ID_MEMBER_BOARDS_INVITED: MembersIdMemberBoardsInvited,
        PathValues.MEMBERS_ID_MEMBER_BOARDS_INVITED_FIELD: MembersIdMemberBoardsInvitedField,
        PathValues.MEMBERS_ID_MEMBER_CARDS: MembersIdMemberCards,
        PathValues.MEMBERS_ID_MEMBER_CARDS_FILTER: MembersIdMemberCardsFilter,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_BOARD_BACKGROUNDS: MembersIdMemberCustomBoardBackgrounds,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_BOARD_BACKGROUNDS_ID_BOARD_BACKGROUND: MembersIdMemberCustomBoardBackgroundsIdBoardBackground,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_EMOJI: MembersIdMemberCustomEmoji,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_EMOJI_ID_CUSTOM_EMOJI: MembersIdMemberCustomEmojiIdCustomEmoji,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_STICKERS: MembersIdMemberCustomStickers,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_STICKERS_ID_CUSTOM_STICKER: MembersIdMemberCustomStickersIdCustomSticker,
        PathValues.MEMBERS_ID_MEMBER_DELTAS: MembersIdMemberDeltas,
        PathValues.MEMBERS_ID_MEMBER_FULL_NAME: MembersIdMemberFullName,
        PathValues.MEMBERS_ID_MEMBER_INITIALS: MembersIdMemberInitials,
        PathValues.MEMBERS_ID_MEMBER_NOTIFICATIONS: MembersIdMemberNotifications,
        PathValues.MEMBERS_ID_MEMBER_NOTIFICATIONS_FILTER: MembersIdMemberNotificationsFilter,
        PathValues.MEMBERS_ID_MEMBER_ONE_TIME_MESSAGES_DISMISSED: MembersIdMemberOneTimeMessagesDismissed,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS: MembersIdMemberOrganizations,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS_FILTER: MembersIdMemberOrganizationsFilter,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS_INVITED: MembersIdMemberOrganizationsInvited,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS_INVITED_FIELD: MembersIdMemberOrganizationsInvitedField,
        PathValues.MEMBERS_ID_MEMBER_PREFS_COLOR_BLIND: MembersIdMemberPrefsColorBlind,
        PathValues.MEMBERS_ID_MEMBER_PREFS_LOCALE: MembersIdMemberPrefsLocale,
        PathValues.MEMBERS_ID_MEMBER_PREFS_MINUTES_BETWEEN_SUMMARIES: MembersIdMemberPrefsMinutesBetweenSummaries,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES: MembersIdMemberSavedSearches,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH: MembersIdMemberSavedSearchesIdSavedSearch,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_NAME: MembersIdMemberSavedSearchesIdSavedSearchName,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_POS: MembersIdMemberSavedSearchesIdSavedSearchPos,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_QUERY: MembersIdMemberSavedSearchesIdSavedSearchQuery,
        PathValues.MEMBERS_ID_MEMBER_TOKENS: MembersIdMemberTokens,
        PathValues.MEMBERS_ID_MEMBER_USERNAME: MembersIdMemberUsername,
        PathValues.MEMBERS_ID_MEMBER_FIELD: MembersIdMemberField,
        PathValues.NOTIFICATIONS_ALL_READ: NotificationsAllRead,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION: NotificationsIdNotification,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_BOARD: NotificationsIdNotificationBoard,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_BOARD_FIELD: NotificationsIdNotificationBoardField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_CARD: NotificationsIdNotificationCard,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_CARD_FIELD: NotificationsIdNotificationCardField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_DISPLAY: NotificationsIdNotificationDisplay,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_ENTITIES: NotificationsIdNotificationEntities,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_LIST: NotificationsIdNotificationList,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_LIST_FIELD: NotificationsIdNotificationListField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER: NotificationsIdNotificationMember,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER_FIELD: NotificationsIdNotificationMemberField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER_CREATOR: NotificationsIdNotificationMemberCreator,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER_CREATOR_FIELD: NotificationsIdNotificationMemberCreatorField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_ORGANIZATION: NotificationsIdNotificationOrganization,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_ORGANIZATION_FIELD: NotificationsIdNotificationOrganizationField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_UNREAD: NotificationsIdNotificationUnread,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_FIELD: NotificationsIdNotificationField,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID_ORG: OrganizationsIdOrg,
        PathValues.ORGANIZATIONS_ID_ORG_ACTIONS: OrganizationsIdOrgActions,
        PathValues.ORGANIZATIONS_ID_ORG_BOARDS: OrganizationsIdOrgBoards,
        PathValues.ORGANIZATIONS_ID_ORG_BOARDS_FILTER: OrganizationsIdOrgBoardsFilter,
        PathValues.ORGANIZATIONS_ID_ORG_DELTAS: OrganizationsIdOrgDeltas,
        PathValues.ORGANIZATIONS_ID_ORG_DESC: OrganizationsIdOrgDesc,
        PathValues.ORGANIZATIONS_ID_ORG_DISPLAY_NAME: OrganizationsIdOrgDisplayName,
        PathValues.ORGANIZATIONS_ID_ORG_LOGO: OrganizationsIdOrgLogo,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS: OrganizationsIdOrgMembers,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_FILTER: OrganizationsIdOrgMembersFilter,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER: OrganizationsIdOrgMembersIdMember,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_ALL: OrganizationsIdOrgMembersIdMemberAll,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_CARDS: OrganizationsIdOrgMembersIdMemberCards,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_DEACTIVATED: OrganizationsIdOrgMembersIdMemberDeactivated,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_INVITED: OrganizationsIdOrgMembersInvited,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_INVITED_FIELD: OrganizationsIdOrgMembersInvitedField,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERSHIPS: OrganizationsIdOrgMemberships,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERSHIPS_ID_MEMBERSHIP: OrganizationsIdOrgMembershipsIdMembership,
        PathValues.ORGANIZATIONS_ID_ORG_NAME: OrganizationsIdOrgName,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_ASSOCIATED_DOMAIN: OrganizationsIdOrgPrefsAssociatedDomain,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_ORG: OrganizationsIdOrgPrefsBoardVisibilityRestrictOrg,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_PRIVATE: OrganizationsIdOrgPrefsBoardVisibilityRestrictPrivate,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_PUBLIC: OrganizationsIdOrgPrefsBoardVisibilityRestrictPublic,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_EXTERNAL_MEMBERS_DISABLED: OrganizationsIdOrgPrefsExternalMembersDisabled,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_GOOGLE_APPS_VERSION: OrganizationsIdOrgPrefsGoogleAppsVersion,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_ORG_INVITE_RESTRICT: OrganizationsIdOrgPrefsOrgInviteRestrict,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_PERMISSION_LEVEL: OrganizationsIdOrgPrefsPermissionLevel,
        PathValues.ORGANIZATIONS_ID_ORG_WEBSITE: OrganizationsIdOrgWebsite,
        PathValues.ORGANIZATIONS_ID_ORG_FIELD: OrganizationsIdOrgField,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_MEMBERS: SearchMembers,
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_SOCKET: SessionsSocket,
        PathValues.SESSIONS_ID_SESSION: SessionsIdSession,
        PathValues.SESSIONS_ID_SESSION_STATUS: SessionsIdSessionStatus,
        PathValues.TOKENS_TOKEN: TokensToken,
        PathValues.TOKENS_TOKEN_MEMBER: TokensTokenMember,
        PathValues.TOKENS_TOKEN_MEMBER_FIELD: TokensTokenMemberField,
        PathValues.TOKENS_TOKEN_WEBHOOKS: TokensTokenWebhooks,
        PathValues.TOKENS_TOKEN_WEBHOOKS_ID_WEBHOOK: TokensTokenWebhooksIdWebhook,
        PathValues.TOKENS_TOKEN_FIELD: TokensTokenField,
        PathValues.TYPES_ID: TypesId,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID_WEBHOOK: WebhooksIdWebhook,
        PathValues.WEBHOOKS_ID_WEBHOOK_ACTIVE: WebhooksIdWebhookActive,
        PathValues.WEBHOOKS_ID_WEBHOOK_CALLBACK_URL: WebhooksIdWebhookCallbackURL,
        PathValues.WEBHOOKS_ID_WEBHOOK_DESCRIPTION: WebhooksIdWebhookDescription,
        PathValues.WEBHOOKS_ID_WEBHOOK_ID_MODEL: WebhooksIdWebhookIdModel,
        PathValues.WEBHOOKS_ID_WEBHOOK_FIELD: WebhooksIdWebhookField,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTIONS_ID_ACTION: ActionsIdAction,
        PathValues.ACTIONS_ID_ACTION_BOARD: ActionsIdActionBoard,
        PathValues.ACTIONS_ID_ACTION_BOARD_FIELD: ActionsIdActionBoardField,
        PathValues.ACTIONS_ID_ACTION_CARD: ActionsIdActionCard,
        PathValues.ACTIONS_ID_ACTION_CARD_FIELD: ActionsIdActionCardField,
        PathValues.ACTIONS_ID_ACTION_DISPLAY: ActionsIdActionDisplay,
        PathValues.ACTIONS_ID_ACTION_ENTITIES: ActionsIdActionEntities,
        PathValues.ACTIONS_ID_ACTION_LIST: ActionsIdActionList,
        PathValues.ACTIONS_ID_ACTION_LIST_FIELD: ActionsIdActionListField,
        PathValues.ACTIONS_ID_ACTION_MEMBER: ActionsIdActionMember,
        PathValues.ACTIONS_ID_ACTION_MEMBER_FIELD: ActionsIdActionMemberField,
        PathValues.ACTIONS_ID_ACTION_MEMBER_CREATOR: ActionsIdActionMemberCreator,
        PathValues.ACTIONS_ID_ACTION_MEMBER_CREATOR_FIELD: ActionsIdActionMemberCreatorField,
        PathValues.ACTIONS_ID_ACTION_ORGANIZATION: ActionsIdActionOrganization,
        PathValues.ACTIONS_ID_ACTION_ORGANIZATION_FIELD: ActionsIdActionOrganizationField,
        PathValues.ACTIONS_ID_ACTION_TEXT: ActionsIdActionText,
        PathValues.ACTIONS_ID_ACTION_FIELD: ActionsIdActionField,
        PathValues.BATCH: Batch,
        PathValues.BOARDS: Boards,
        PathValues.BOARDS_ID_BOARD: BoardsIdBoard,
        PathValues.BOARDS_ID_BOARD_ACTIONS: BoardsIdBoardActions,
        PathValues.BOARDS_ID_BOARD_BOARD_STARS: BoardsIdBoardBoardStars,
        PathValues.BOARDS_ID_BOARD_CALENDAR_KEY_GENERATE: BoardsIdBoardCalendarKeyGenerate,
        PathValues.BOARDS_ID_BOARD_CARDS: BoardsIdBoardCards,
        PathValues.BOARDS_ID_BOARD_CARDS_FILTER: BoardsIdBoardCardsFilter,
        PathValues.BOARDS_ID_BOARD_CARDS_ID_CARD: BoardsIdBoardCardsIdCard,
        PathValues.BOARDS_ID_BOARD_CHECKLISTS: BoardsIdBoardChecklists,
        PathValues.BOARDS_ID_BOARD_CLOSED: BoardsIdBoardClosed,
        PathValues.BOARDS_ID_BOARD_DELTAS: BoardsIdBoardDeltas,
        PathValues.BOARDS_ID_BOARD_DESC: BoardsIdBoardDesc,
        PathValues.BOARDS_ID_BOARD_EMAIL_KEY_GENERATE: BoardsIdBoardEmailKeyGenerate,
        PathValues.BOARDS_ID_BOARD_ID_ORGANIZATION: BoardsIdBoardIdOrganization,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_BLUE: BoardsIdBoardLabelNamesBlue,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_GREEN: BoardsIdBoardLabelNamesGreen,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_ORANGE: BoardsIdBoardLabelNamesOrange,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_PURPLE: BoardsIdBoardLabelNamesPurple,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_RED: BoardsIdBoardLabelNamesRed,
        PathValues.BOARDS_ID_BOARD_LABEL_NAMES_YELLOW: BoardsIdBoardLabelNamesYellow,
        PathValues.BOARDS_ID_BOARD_LABELS: BoardsIdBoardLabels,
        PathValues.BOARDS_ID_BOARD_LABELS_ID_LABEL: BoardsIdBoardLabelsIdLabel,
        PathValues.BOARDS_ID_BOARD_LISTS: BoardsIdBoardLists,
        PathValues.BOARDS_ID_BOARD_LISTS_FILTER: BoardsIdBoardListsFilter,
        PathValues.BOARDS_ID_BOARD_MARK_AS_VIEWED: BoardsIdBoardMarkAsViewed,
        PathValues.BOARDS_ID_BOARD_MEMBERS: BoardsIdBoardMembers,
        PathValues.BOARDS_ID_BOARD_MEMBERS_FILTER: BoardsIdBoardMembersFilter,
        PathValues.BOARDS_ID_BOARD_MEMBERS_ID_MEMBER: BoardsIdBoardMembersIdMember,
        PathValues.BOARDS_ID_BOARD_MEMBERS_ID_MEMBER_CARDS: BoardsIdBoardMembersIdMemberCards,
        PathValues.BOARDS_ID_BOARD_MEMBERS_INVITED: BoardsIdBoardMembersInvited,
        PathValues.BOARDS_ID_BOARD_MEMBERS_INVITED_FIELD: BoardsIdBoardMembersInvitedField,
        PathValues.BOARDS_ID_BOARD_MEMBERSHIPS: BoardsIdBoardMemberships,
        PathValues.BOARDS_ID_BOARD_MEMBERSHIPS_ID_MEMBERSHIP: BoardsIdBoardMembershipsIdMembership,
        PathValues.BOARDS_ID_BOARD_MY_PREFS: BoardsIdBoardMyPrefs,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_EMAIL_POSITION: BoardsIdBoardMyPrefsEmailPosition,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_ID_EMAIL_LIST: BoardsIdBoardMyPrefsIdEmailList,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_LIST_GUIDE: BoardsIdBoardMyPrefsShowListGuide,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR: BoardsIdBoardMyPrefsShowSidebar,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_ACTIVITY: BoardsIdBoardMyPrefsShowSidebarActivity,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_BOARD_ACTIONS: BoardsIdBoardMyPrefsShowSidebarBoardActions,
        PathValues.BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_MEMBERS: BoardsIdBoardMyPrefsShowSidebarMembers,
        PathValues.BOARDS_ID_BOARD_NAME: BoardsIdBoardName,
        PathValues.BOARDS_ID_BOARD_ORGANIZATION: BoardsIdBoardOrganization,
        PathValues.BOARDS_ID_BOARD_ORGANIZATION_FIELD: BoardsIdBoardOrganizationField,
        PathValues.BOARDS_ID_BOARD_POWER_UPS: BoardsIdBoardPowerUps,
        PathValues.BOARDS_ID_BOARD_POWER_UPS_POWER_UP: BoardsIdBoardPowerUpsPowerUp,
        PathValues.BOARDS_ID_BOARD_PREFS_BACKGROUND: BoardsIdBoardPrefsBackground,
        PathValues.BOARDS_ID_BOARD_PREFS_CALENDAR_FEED_ENABLED: BoardsIdBoardPrefsCalendarFeedEnabled,
        PathValues.BOARDS_ID_BOARD_PREFS_CARD_AGING: BoardsIdBoardPrefsCardAging,
        PathValues.BOARDS_ID_BOARD_PREFS_CARD_COVERS: BoardsIdBoardPrefsCardCovers,
        PathValues.BOARDS_ID_BOARD_PREFS_COMMENTS: BoardsIdBoardPrefsComments,
        PathValues.BOARDS_ID_BOARD_PREFS_INVITATIONS: BoardsIdBoardPrefsInvitations,
        PathValues.BOARDS_ID_BOARD_PREFS_PERMISSION_LEVEL: BoardsIdBoardPrefsPermissionLevel,
        PathValues.BOARDS_ID_BOARD_PREFS_SELF_JOIN: BoardsIdBoardPrefsSelfJoin,
        PathValues.BOARDS_ID_BOARD_PREFS_VOTING: BoardsIdBoardPrefsVoting,
        PathValues.BOARDS_ID_BOARD_SUBSCRIBED: BoardsIdBoardSubscribed,
        PathValues.BOARDS_ID_BOARD_FIELD: BoardsIdBoardField,
        PathValues.CARDS: Cards,
        PathValues.CARDS_ID_CARD: CardsIdCard,
        PathValues.CARDS_ID_CARD_ACTIONS: CardsIdCardActions,
        PathValues.CARDS_ID_CARD_ACTIONS_COMMENTS: CardsIdCardActionsComments,
        PathValues.CARDS_ID_CARD_ACTIONS_ID_ACTION_COMMENTS: CardsIdCardActionsIdActionComments,
        PathValues.CARDS_ID_CARD_ATTACHMENTS: CardsIdCardAttachments,
        PathValues.CARDS_ID_CARD_ATTACHMENTS_ID_ATTACHMENT: CardsIdCardAttachmentsIdAttachment,
        PathValues.CARDS_ID_CARD_BOARD: CardsIdCardBoard,
        PathValues.CARDS_ID_CARD_BOARD_FIELD: CardsIdCardBoardField,
        PathValues.CARDS_ID_CARD_CHECK_ITEM_STATES: CardsIdCardCheckItemStates,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CURRENT_CHECK_ITEM_ID_CHECK_ITEM: CardsIdCardChecklistIdChecklistCurrentCheckItemIdCheckItem,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM: CardsIdCardChecklistIdChecklistCheckItem,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM: CardsIdCardChecklistIdChecklistCheckItemIdCheckItem,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_CONVERT_TO_CARD: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemConvertToCard,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_NAME: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemName,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_POS: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemPos,
        PathValues.CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_STATE: CardsIdCardChecklistIdChecklistCheckItemIdCheckItemState,
        PathValues.CARDS_ID_CARD_CHECKLISTS: CardsIdCardChecklists,
        PathValues.CARDS_ID_CARD_CHECKLISTS_ID_CHECKLIST: CardsIdCardChecklistsIdChecklist,
        PathValues.CARDS_ID_CARD_CLOSED: CardsIdCardClosed,
        PathValues.CARDS_ID_CARD_DESC: CardsIdCardDesc,
        PathValues.CARDS_ID_CARD_DUE: CardsIdCardDue,
        PathValues.CARDS_ID_CARD_ID_ATTACHMENT_COVER: CardsIdCardIdAttachmentCover,
        PathValues.CARDS_ID_CARD_ID_BOARD: CardsIdCardIdBoard,
        PathValues.CARDS_ID_CARD_ID_LABELS: CardsIdCardIdLabels,
        PathValues.CARDS_ID_CARD_ID_LABELS_ID_LABEL: CardsIdCardIdLabelsIdLabel,
        PathValues.CARDS_ID_CARD_ID_LIST: CardsIdCardIdList,
        PathValues.CARDS_ID_CARD_ID_MEMBERS: CardsIdCardIdMembers,
        PathValues.CARDS_ID_CARD_ID_MEMBERS_ID_MEMBER: CardsIdCardIdMembersIdMember,
        PathValues.CARDS_ID_CARD_LABELS: CardsIdCardLabels,
        PathValues.CARDS_ID_CARD_LABELS_COLOR: CardsIdCardLabelsColor,
        PathValues.CARDS_ID_CARD_LIST: CardsIdCardList,
        PathValues.CARDS_ID_CARD_LIST_FIELD: CardsIdCardListField,
        PathValues.CARDS_ID_CARD_MARK_ASSOCIATED_NOTIFICATIONS_READ: CardsIdCardMarkAssociatedNotificationsRead,
        PathValues.CARDS_ID_CARD_MEMBERS: CardsIdCardMembers,
        PathValues.CARDS_ID_CARD_MEMBERS_VOTED: CardsIdCardMembersVoted,
        PathValues.CARDS_ID_CARD_MEMBERS_VOTED_ID_MEMBER: CardsIdCardMembersVotedIdMember,
        PathValues.CARDS_ID_CARD_NAME: CardsIdCardName,
        PathValues.CARDS_ID_CARD_POS: CardsIdCardPos,
        PathValues.CARDS_ID_CARD_STICKERS: CardsIdCardStickers,
        PathValues.CARDS_ID_CARD_STICKERS_ID_STICKER: CardsIdCardStickersIdSticker,
        PathValues.CARDS_ID_CARD_SUBSCRIBED: CardsIdCardSubscribed,
        PathValues.CARDS_ID_CARD_FIELD: CardsIdCardField,
        PathValues.CHECKLISTS: Checklists,
        PathValues.CHECKLISTS_ID_CHECKLIST: ChecklistsIdChecklist,
        PathValues.CHECKLISTS_ID_CHECKLIST_BOARD: ChecklistsIdChecklistBoard,
        PathValues.CHECKLISTS_ID_CHECKLIST_BOARD_FIELD: ChecklistsIdChecklistBoardField,
        PathValues.CHECKLISTS_ID_CHECKLIST_CARDS: ChecklistsIdChecklistCards,
        PathValues.CHECKLISTS_ID_CHECKLIST_CARDS_FILTER: ChecklistsIdChecklistCardsFilter,
        PathValues.CHECKLISTS_ID_CHECKLIST_CHECK_ITEMS: ChecklistsIdChecklistCheckItems,
        PathValues.CHECKLISTS_ID_CHECKLIST_CHECK_ITEMS_ID_CHECK_ITEM: ChecklistsIdChecklistCheckItemsIdCheckItem,
        PathValues.CHECKLISTS_ID_CHECKLIST_ID_CARD: ChecklistsIdChecklistIdCard,
        PathValues.CHECKLISTS_ID_CHECKLIST_NAME: ChecklistsIdChecklistName,
        PathValues.CHECKLISTS_ID_CHECKLIST_POS: ChecklistsIdChecklistPos,
        PathValues.CHECKLISTS_ID_CHECKLIST_FIELD: ChecklistsIdChecklistField,
        PathValues.LABELS: Labels,
        PathValues.LABELS_ID_LABEL: LabelsIdLabel,
        PathValues.LABELS_ID_LABEL_BOARD: LabelsIdLabelBoard,
        PathValues.LABELS_ID_LABEL_BOARD_FIELD: LabelsIdLabelBoardField,
        PathValues.LABELS_ID_LABEL_COLOR: LabelsIdLabelColor,
        PathValues.LABELS_ID_LABEL_NAME: LabelsIdLabelName,
        PathValues.LISTS: Lists,
        PathValues.LISTS_ID_LIST: ListsIdList,
        PathValues.LISTS_ID_LIST_ACTIONS: ListsIdListActions,
        PathValues.LISTS_ID_LIST_ARCHIVE_ALL_CARDS: ListsIdListArchiveAllCards,
        PathValues.LISTS_ID_LIST_BOARD: ListsIdListBoard,
        PathValues.LISTS_ID_LIST_BOARD_FIELD: ListsIdListBoardField,
        PathValues.LISTS_ID_LIST_CARDS: ListsIdListCards,
        PathValues.LISTS_ID_LIST_CARDS_FILTER: ListsIdListCardsFilter,
        PathValues.LISTS_ID_LIST_CLOSED: ListsIdListClosed,
        PathValues.LISTS_ID_LIST_ID_BOARD: ListsIdListIdBoard,
        PathValues.LISTS_ID_LIST_MOVE_ALL_CARDS: ListsIdListMoveAllCards,
        PathValues.LISTS_ID_LIST_NAME: ListsIdListName,
        PathValues.LISTS_ID_LIST_POS: ListsIdListPos,
        PathValues.LISTS_ID_LIST_SUBSCRIBED: ListsIdListSubscribed,
        PathValues.LISTS_ID_LIST_FIELD: ListsIdListField,
        PathValues.MEMBERS_ID_MEMBER: MembersIdMember,
        PathValues.MEMBERS_ID_MEMBER_ACTIONS: MembersIdMemberActions,
        PathValues.MEMBERS_ID_MEMBER_AVATAR: MembersIdMemberAvatar,
        PathValues.MEMBERS_ID_MEMBER_AVATAR_SOURCE: MembersIdMemberAvatarSource,
        PathValues.MEMBERS_ID_MEMBER_BIO: MembersIdMemberBio,
        PathValues.MEMBERS_ID_MEMBER_BOARD_BACKGROUNDS: MembersIdMemberBoardBackgrounds,
        PathValues.MEMBERS_ID_MEMBER_BOARD_BACKGROUNDS_ID_BOARD_BACKGROUND: MembersIdMemberBoardBackgroundsIdBoardBackground,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS: MembersIdMemberBoardStars,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR: MembersIdMemberBoardStarsIdBoardStar,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR_ID_BOARD: MembersIdMemberBoardStarsIdBoardStarIdBoard,
        PathValues.MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR_POS: MembersIdMemberBoardStarsIdBoardStarPos,
        PathValues.MEMBERS_ID_MEMBER_BOARDS: MembersIdMemberBoards,
        PathValues.MEMBERS_ID_MEMBER_BOARDS_FILTER: MembersIdMemberBoardsFilter,
        PathValues.MEMBERS_ID_MEMBER_BOARDS_INVITED: MembersIdMemberBoardsInvited,
        PathValues.MEMBERS_ID_MEMBER_BOARDS_INVITED_FIELD: MembersIdMemberBoardsInvitedField,
        PathValues.MEMBERS_ID_MEMBER_CARDS: MembersIdMemberCards,
        PathValues.MEMBERS_ID_MEMBER_CARDS_FILTER: MembersIdMemberCardsFilter,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_BOARD_BACKGROUNDS: MembersIdMemberCustomBoardBackgrounds,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_BOARD_BACKGROUNDS_ID_BOARD_BACKGROUND: MembersIdMemberCustomBoardBackgroundsIdBoardBackground,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_EMOJI: MembersIdMemberCustomEmoji,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_EMOJI_ID_CUSTOM_EMOJI: MembersIdMemberCustomEmojiIdCustomEmoji,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_STICKERS: MembersIdMemberCustomStickers,
        PathValues.MEMBERS_ID_MEMBER_CUSTOM_STICKERS_ID_CUSTOM_STICKER: MembersIdMemberCustomStickersIdCustomSticker,
        PathValues.MEMBERS_ID_MEMBER_DELTAS: MembersIdMemberDeltas,
        PathValues.MEMBERS_ID_MEMBER_FULL_NAME: MembersIdMemberFullName,
        PathValues.MEMBERS_ID_MEMBER_INITIALS: MembersIdMemberInitials,
        PathValues.MEMBERS_ID_MEMBER_NOTIFICATIONS: MembersIdMemberNotifications,
        PathValues.MEMBERS_ID_MEMBER_NOTIFICATIONS_FILTER: MembersIdMemberNotificationsFilter,
        PathValues.MEMBERS_ID_MEMBER_ONE_TIME_MESSAGES_DISMISSED: MembersIdMemberOneTimeMessagesDismissed,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS: MembersIdMemberOrganizations,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS_FILTER: MembersIdMemberOrganizationsFilter,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS_INVITED: MembersIdMemberOrganizationsInvited,
        PathValues.MEMBERS_ID_MEMBER_ORGANIZATIONS_INVITED_FIELD: MembersIdMemberOrganizationsInvitedField,
        PathValues.MEMBERS_ID_MEMBER_PREFS_COLOR_BLIND: MembersIdMemberPrefsColorBlind,
        PathValues.MEMBERS_ID_MEMBER_PREFS_LOCALE: MembersIdMemberPrefsLocale,
        PathValues.MEMBERS_ID_MEMBER_PREFS_MINUTES_BETWEEN_SUMMARIES: MembersIdMemberPrefsMinutesBetweenSummaries,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES: MembersIdMemberSavedSearches,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH: MembersIdMemberSavedSearchesIdSavedSearch,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_NAME: MembersIdMemberSavedSearchesIdSavedSearchName,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_POS: MembersIdMemberSavedSearchesIdSavedSearchPos,
        PathValues.MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_QUERY: MembersIdMemberSavedSearchesIdSavedSearchQuery,
        PathValues.MEMBERS_ID_MEMBER_TOKENS: MembersIdMemberTokens,
        PathValues.MEMBERS_ID_MEMBER_USERNAME: MembersIdMemberUsername,
        PathValues.MEMBERS_ID_MEMBER_FIELD: MembersIdMemberField,
        PathValues.NOTIFICATIONS_ALL_READ: NotificationsAllRead,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION: NotificationsIdNotification,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_BOARD: NotificationsIdNotificationBoard,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_BOARD_FIELD: NotificationsIdNotificationBoardField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_CARD: NotificationsIdNotificationCard,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_CARD_FIELD: NotificationsIdNotificationCardField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_DISPLAY: NotificationsIdNotificationDisplay,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_ENTITIES: NotificationsIdNotificationEntities,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_LIST: NotificationsIdNotificationList,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_LIST_FIELD: NotificationsIdNotificationListField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER: NotificationsIdNotificationMember,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER_FIELD: NotificationsIdNotificationMemberField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER_CREATOR: NotificationsIdNotificationMemberCreator,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_MEMBER_CREATOR_FIELD: NotificationsIdNotificationMemberCreatorField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_ORGANIZATION: NotificationsIdNotificationOrganization,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_ORGANIZATION_FIELD: NotificationsIdNotificationOrganizationField,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_UNREAD: NotificationsIdNotificationUnread,
        PathValues.NOTIFICATIONS_ID_NOTIFICATION_FIELD: NotificationsIdNotificationField,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.ORGANIZATIONS_ID_ORG: OrganizationsIdOrg,
        PathValues.ORGANIZATIONS_ID_ORG_ACTIONS: OrganizationsIdOrgActions,
        PathValues.ORGANIZATIONS_ID_ORG_BOARDS: OrganizationsIdOrgBoards,
        PathValues.ORGANIZATIONS_ID_ORG_BOARDS_FILTER: OrganizationsIdOrgBoardsFilter,
        PathValues.ORGANIZATIONS_ID_ORG_DELTAS: OrganizationsIdOrgDeltas,
        PathValues.ORGANIZATIONS_ID_ORG_DESC: OrganizationsIdOrgDesc,
        PathValues.ORGANIZATIONS_ID_ORG_DISPLAY_NAME: OrganizationsIdOrgDisplayName,
        PathValues.ORGANIZATIONS_ID_ORG_LOGO: OrganizationsIdOrgLogo,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS: OrganizationsIdOrgMembers,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_FILTER: OrganizationsIdOrgMembersFilter,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER: OrganizationsIdOrgMembersIdMember,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_ALL: OrganizationsIdOrgMembersIdMemberAll,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_CARDS: OrganizationsIdOrgMembersIdMemberCards,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_DEACTIVATED: OrganizationsIdOrgMembersIdMemberDeactivated,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_INVITED: OrganizationsIdOrgMembersInvited,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERS_INVITED_FIELD: OrganizationsIdOrgMembersInvitedField,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERSHIPS: OrganizationsIdOrgMemberships,
        PathValues.ORGANIZATIONS_ID_ORG_MEMBERSHIPS_ID_MEMBERSHIP: OrganizationsIdOrgMembershipsIdMembership,
        PathValues.ORGANIZATIONS_ID_ORG_NAME: OrganizationsIdOrgName,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_ASSOCIATED_DOMAIN: OrganizationsIdOrgPrefsAssociatedDomain,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_ORG: OrganizationsIdOrgPrefsBoardVisibilityRestrictOrg,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_PRIVATE: OrganizationsIdOrgPrefsBoardVisibilityRestrictPrivate,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_PUBLIC: OrganizationsIdOrgPrefsBoardVisibilityRestrictPublic,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_EXTERNAL_MEMBERS_DISABLED: OrganizationsIdOrgPrefsExternalMembersDisabled,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_GOOGLE_APPS_VERSION: OrganizationsIdOrgPrefsGoogleAppsVersion,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_ORG_INVITE_RESTRICT: OrganizationsIdOrgPrefsOrgInviteRestrict,
        PathValues.ORGANIZATIONS_ID_ORG_PREFS_PERMISSION_LEVEL: OrganizationsIdOrgPrefsPermissionLevel,
        PathValues.ORGANIZATIONS_ID_ORG_WEBSITE: OrganizationsIdOrgWebsite,
        PathValues.ORGANIZATIONS_ID_ORG_FIELD: OrganizationsIdOrgField,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_MEMBERS: SearchMembers,
        PathValues.SESSIONS: Sessions,
        PathValues.SESSIONS_SOCKET: SessionsSocket,
        PathValues.SESSIONS_ID_SESSION: SessionsIdSession,
        PathValues.SESSIONS_ID_SESSION_STATUS: SessionsIdSessionStatus,
        PathValues.TOKENS_TOKEN: TokensToken,
        PathValues.TOKENS_TOKEN_MEMBER: TokensTokenMember,
        PathValues.TOKENS_TOKEN_MEMBER_FIELD: TokensTokenMemberField,
        PathValues.TOKENS_TOKEN_WEBHOOKS: TokensTokenWebhooks,
        PathValues.TOKENS_TOKEN_WEBHOOKS_ID_WEBHOOK: TokensTokenWebhooksIdWebhook,
        PathValues.TOKENS_TOKEN_FIELD: TokensTokenField,
        PathValues.TYPES_ID: TypesId,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID_WEBHOOK: WebhooksIdWebhook,
        PathValues.WEBHOOKS_ID_WEBHOOK_ACTIVE: WebhooksIdWebhookActive,
        PathValues.WEBHOOKS_ID_WEBHOOK_CALLBACK_URL: WebhooksIdWebhookCallbackURL,
        PathValues.WEBHOOKS_ID_WEBHOOK_DESCRIPTION: WebhooksIdWebhookDescription,
        PathValues.WEBHOOKS_ID_WEBHOOK_ID_MODEL: WebhooksIdWebhookIdModel,
        PathValues.WEBHOOKS_ID_WEBHOOK_FIELD: WebhooksIdWebhookField,
    }
)
