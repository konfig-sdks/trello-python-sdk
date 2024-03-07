# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.members_id_member_board_backgrounds.post import AddBoardBackgrounds
from trello_python_sdk.paths.members_id_member_board_stars.post import AddBoardStarsByIdMember
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds.post import AddCustomBoardBackgrounds
from trello_python_sdk.paths.members_id_member_custom_emoji.post import AddCustomEmojiByIdMember
from trello_python_sdk.paths.members_id_member_custom_stickers.post import AddCustomStickers
from trello_python_sdk.paths.members_id_member_one_time_messages_dismissed.post import AddOneTimeMessagesDismissedByIdMember
from trello_python_sdk.paths.members_id_member_saved_searches.post import CreateSavedSearch
from trello_python_sdk.paths.members_id_member_board_backgrounds_id_board_background.delete import DeleteBoardBackground
from trello_python_sdk.paths.members_id_member_board_backgrounds_id_board_background.get import GetBoardBackgroundByIds
from trello_python_sdk.paths.members_id_member_board_backgrounds.get import GetBoardBackgroundsById
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star.get import GetBoardStarByIdMember
from trello_python_sdk.paths.members_id_member_board_stars.get import GetBoardStarsById
from trello_python_sdk.paths.members_id_member_boards_filter.get import GetBoards
from trello_python_sdk.paths.members_id_member_boards.get import GetBoardsByIdMember
from trello_python_sdk.paths.members_id_member_boards_invited_field.get import GetBoardsInvitedByIdMemberByField
from trello_python_sdk.paths.members_id_member_field.get import GetByField
from trello_python_sdk.paths.members_id_member.get import GetById
from trello_python_sdk.paths.members_id_member_cards_filter.get import GetCardsByFilter
from trello_python_sdk.paths.members_id_member_cards.get import GetCardsByIdMember
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds_id_board_background.get import GetCustomBoardBackgroundByIds
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds.get import GetCustomBoardBackgroundsById
from trello_python_sdk.paths.members_id_member_custom_emoji_id_custom_emoji.get import GetCustomEmojiByIds
from trello_python_sdk.paths.members_id_member_custom_stickers_id_custom_sticker.get import GetCustomStickerByIds
from trello_python_sdk.paths.members_id_member_custom_stickers.get import GetCustomStickersByIdMember
from trello_python_sdk.paths.members_id_member_deltas.get import GetDeltasByIdMember
from trello_python_sdk.paths.members_id_member_boards_invited.get import GetInvitedBoards
from trello_python_sdk.paths.members_id_member_notifications.get import GetNotificationsByIdMember
from trello_python_sdk.paths.members_id_member_notifications_filter.get import GetNotificationsByIdMemberByFilter
from trello_python_sdk.paths.members_id_member_organizations_filter.get import GetOrganizations
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search.get import GetSavedSearchByIds
from trello_python_sdk.paths.members_id_member_saved_searches.get import GetSavedSearchesByIdMember
from trello_python_sdk.paths.members_id_member_tokens.get import GetTokensByIdMember
from trello_python_sdk.paths.members_id_member_actions.get import ListActionsByIdMember
from trello_python_sdk.paths.members_id_member_custom_emoji.get import ListCustomEmojiByIdMember
from trello_python_sdk.paths.members_id_member_organizations_invited.get import ListInvitedOrganizationsById
from trello_python_sdk.paths.members_id_member_organizations.get import ListOrganizationsById
from trello_python_sdk.paths.members_id_member_organizations_invited_field.get import ListOrganizationsInvitedByIdMemberByField
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star.delete import RemoveBoardStarByIdMemberByIdBoardStar
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds_id_board_background.delete import RemoveCustomBoardBackgroundById
from trello_python_sdk.paths.members_id_member_custom_stickers_id_custom_sticker.delete import RemoveCustomStickerByIds
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search.delete import RemoveSavedSearchByIds
from trello_python_sdk.paths.members_id_member_avatar_source.put import UpdateAvatarSource
from trello_python_sdk.paths.members_id_member_bio.put import UpdateBioById
from trello_python_sdk.paths.members_id_member_board_backgrounds_id_board_background.put import UpdateBoardBackgroundsById
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star.put import UpdateBoardStar
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star_pos.put import UpdateBoardStarPosByIdMemberByIdBoardStar
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star_id_board.put import UpdateBoardStarsIdBoard
from trello_python_sdk.paths.members_id_member.put import UpdateByIdMember
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds_id_board_background.put import UpdateCustomBoardBackgrounds
from trello_python_sdk.paths.members_id_member_full_name.put import UpdateFullName
from trello_python_sdk.paths.members_id_member_initials.put import UpdateInitialsByIdMember
from trello_python_sdk.paths.members_id_member_prefs_color_blind.put import UpdatePrefsColorBlindByIdMember
from trello_python_sdk.paths.members_id_member_prefs_locale.put import UpdatePrefsLocaleByIdMember
from trello_python_sdk.paths.members_id_member_prefs_minutes_between_summaries.put import UpdatePrefsMinutesBetweenSummariesById
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search_query.put import UpdateSavedSearchQueryByIdMemberByIdSavedSearch
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search.put import UpdateSavedSearchesByIdMemberByIdSavedSearch
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search_name.put import UpdateSavedSearchesNameByIdMemberByIdSavedSearch
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search_pos.put import UpdateSavedSearchesPosByIdMemberByIdSavedSearch
from trello_python_sdk.paths.members_id_member_username.put import UpdateUsernameById
from trello_python_sdk.paths.members_id_member_avatar.post import UploadAvatarById
from trello_python_sdk.apis.tags.member_api_raw import MemberApiRaw


class MemberApi(
    AddBoardBackgrounds,
    AddBoardStarsByIdMember,
    AddCustomBoardBackgrounds,
    AddCustomEmojiByIdMember,
    AddCustomStickers,
    AddOneTimeMessagesDismissedByIdMember,
    CreateSavedSearch,
    DeleteBoardBackground,
    GetBoardBackgroundByIds,
    GetBoardBackgroundsById,
    GetBoardStarByIdMember,
    GetBoardStarsById,
    GetBoards,
    GetBoardsByIdMember,
    GetBoardsInvitedByIdMemberByField,
    GetByField,
    GetById,
    GetCardsByFilter,
    GetCardsByIdMember,
    GetCustomBoardBackgroundByIds,
    GetCustomBoardBackgroundsById,
    GetCustomEmojiByIds,
    GetCustomStickerByIds,
    GetCustomStickersByIdMember,
    GetDeltasByIdMember,
    GetInvitedBoards,
    GetNotificationsByIdMember,
    GetNotificationsByIdMemberByFilter,
    GetOrganizations,
    GetSavedSearchByIds,
    GetSavedSearchesByIdMember,
    GetTokensByIdMember,
    ListActionsByIdMember,
    ListCustomEmojiByIdMember,
    ListInvitedOrganizationsById,
    ListOrganizationsById,
    ListOrganizationsInvitedByIdMemberByField,
    RemoveBoardStarByIdMemberByIdBoardStar,
    RemoveCustomBoardBackgroundById,
    RemoveCustomStickerByIds,
    RemoveSavedSearchByIds,
    UpdateAvatarSource,
    UpdateBioById,
    UpdateBoardBackgroundsById,
    UpdateBoardStar,
    UpdateBoardStarPosByIdMemberByIdBoardStar,
    UpdateBoardStarsIdBoard,
    UpdateByIdMember,
    UpdateCustomBoardBackgrounds,
    UpdateFullName,
    UpdateInitialsByIdMember,
    UpdatePrefsColorBlindByIdMember,
    UpdatePrefsLocaleByIdMember,
    UpdatePrefsMinutesBetweenSummariesById,
    UpdateSavedSearchQueryByIdMemberByIdSavedSearch,
    UpdateSavedSearchesByIdMemberByIdSavedSearch,
    UpdateSavedSearchesNameByIdMemberByIdSavedSearch,
    UpdateSavedSearchesPosByIdMemberByIdSavedSearch,
    UpdateUsernameById,
    UploadAvatarById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MemberApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MemberApiRaw(api_client)
