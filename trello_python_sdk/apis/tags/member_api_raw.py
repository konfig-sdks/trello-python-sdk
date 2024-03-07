# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.members_id_member_board_backgrounds.post import AddBoardBackgroundsRaw
from trello_python_sdk.paths.members_id_member_board_stars.post import AddBoardStarsByIdMemberRaw
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds.post import AddCustomBoardBackgroundsRaw
from trello_python_sdk.paths.members_id_member_custom_emoji.post import AddCustomEmojiByIdMemberRaw
from trello_python_sdk.paths.members_id_member_custom_stickers.post import AddCustomStickersRaw
from trello_python_sdk.paths.members_id_member_one_time_messages_dismissed.post import AddOneTimeMessagesDismissedByIdMemberRaw
from trello_python_sdk.paths.members_id_member_saved_searches.post import CreateSavedSearchRaw
from trello_python_sdk.paths.members_id_member_board_backgrounds_id_board_background.delete import DeleteBoardBackgroundRaw
from trello_python_sdk.paths.members_id_member_board_backgrounds_id_board_background.get import GetBoardBackgroundByIdsRaw
from trello_python_sdk.paths.members_id_member_board_backgrounds.get import GetBoardBackgroundsByIdRaw
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star.get import GetBoardStarByIdMemberRaw
from trello_python_sdk.paths.members_id_member_board_stars.get import GetBoardStarsByIdRaw
from trello_python_sdk.paths.members_id_member_boards_filter.get import GetBoardsRaw
from trello_python_sdk.paths.members_id_member_boards.get import GetBoardsByIdMemberRaw
from trello_python_sdk.paths.members_id_member_boards_invited_field.get import GetBoardsInvitedByIdMemberByFieldRaw
from trello_python_sdk.paths.members_id_member_field.get import GetByFieldRaw
from trello_python_sdk.paths.members_id_member.get import GetByIdRaw
from trello_python_sdk.paths.members_id_member_cards_filter.get import GetCardsByFilterRaw
from trello_python_sdk.paths.members_id_member_cards.get import GetCardsByIdMemberRaw
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds_id_board_background.get import GetCustomBoardBackgroundByIdsRaw
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds.get import GetCustomBoardBackgroundsByIdRaw
from trello_python_sdk.paths.members_id_member_custom_emoji_id_custom_emoji.get import GetCustomEmojiByIdsRaw
from trello_python_sdk.paths.members_id_member_custom_stickers_id_custom_sticker.get import GetCustomStickerByIdsRaw
from trello_python_sdk.paths.members_id_member_custom_stickers.get import GetCustomStickersByIdMemberRaw
from trello_python_sdk.paths.members_id_member_deltas.get import GetDeltasByIdMemberRaw
from trello_python_sdk.paths.members_id_member_boards_invited.get import GetInvitedBoardsRaw
from trello_python_sdk.paths.members_id_member_notifications.get import GetNotificationsByIdMemberRaw
from trello_python_sdk.paths.members_id_member_notifications_filter.get import GetNotificationsByIdMemberByFilterRaw
from trello_python_sdk.paths.members_id_member_organizations_filter.get import GetOrganizationsRaw
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search.get import GetSavedSearchByIdsRaw
from trello_python_sdk.paths.members_id_member_saved_searches.get import GetSavedSearchesByIdMemberRaw
from trello_python_sdk.paths.members_id_member_tokens.get import GetTokensByIdMemberRaw
from trello_python_sdk.paths.members_id_member_actions.get import ListActionsByIdMemberRaw
from trello_python_sdk.paths.members_id_member_custom_emoji.get import ListCustomEmojiByIdMemberRaw
from trello_python_sdk.paths.members_id_member_organizations_invited.get import ListInvitedOrganizationsByIdRaw
from trello_python_sdk.paths.members_id_member_organizations.get import ListOrganizationsByIdRaw
from trello_python_sdk.paths.members_id_member_organizations_invited_field.get import ListOrganizationsInvitedByIdMemberByFieldRaw
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star.delete import RemoveBoardStarByIdMemberByIdBoardStarRaw
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds_id_board_background.delete import RemoveCustomBoardBackgroundByIdRaw
from trello_python_sdk.paths.members_id_member_custom_stickers_id_custom_sticker.delete import RemoveCustomStickerByIdsRaw
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search.delete import RemoveSavedSearchByIdsRaw
from trello_python_sdk.paths.members_id_member_avatar_source.put import UpdateAvatarSourceRaw
from trello_python_sdk.paths.members_id_member_bio.put import UpdateBioByIdRaw
from trello_python_sdk.paths.members_id_member_board_backgrounds_id_board_background.put import UpdateBoardBackgroundsByIdRaw
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star.put import UpdateBoardStarRaw
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star_pos.put import UpdateBoardStarPosByIdMemberByIdBoardStarRaw
from trello_python_sdk.paths.members_id_member_board_stars_id_board_star_id_board.put import UpdateBoardStarsIdBoardRaw
from trello_python_sdk.paths.members_id_member.put import UpdateByIdMemberRaw
from trello_python_sdk.paths.members_id_member_custom_board_backgrounds_id_board_background.put import UpdateCustomBoardBackgroundsRaw
from trello_python_sdk.paths.members_id_member_full_name.put import UpdateFullNameRaw
from trello_python_sdk.paths.members_id_member_initials.put import UpdateInitialsByIdMemberRaw
from trello_python_sdk.paths.members_id_member_prefs_color_blind.put import UpdatePrefsColorBlindByIdMemberRaw
from trello_python_sdk.paths.members_id_member_prefs_locale.put import UpdatePrefsLocaleByIdMemberRaw
from trello_python_sdk.paths.members_id_member_prefs_minutes_between_summaries.put import UpdatePrefsMinutesBetweenSummariesByIdRaw
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search_query.put import UpdateSavedSearchQueryByIdMemberByIdSavedSearchRaw
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search.put import UpdateSavedSearchesByIdMemberByIdSavedSearchRaw
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search_name.put import UpdateSavedSearchesNameByIdMemberByIdSavedSearchRaw
from trello_python_sdk.paths.members_id_member_saved_searches_id_saved_search_pos.put import UpdateSavedSearchesPosByIdMemberByIdSavedSearchRaw
from trello_python_sdk.paths.members_id_member_username.put import UpdateUsernameByIdRaw
from trello_python_sdk.paths.members_id_member_avatar.post import UploadAvatarByIdRaw


class MemberApiRaw(
    AddBoardBackgroundsRaw,
    AddBoardStarsByIdMemberRaw,
    AddCustomBoardBackgroundsRaw,
    AddCustomEmojiByIdMemberRaw,
    AddCustomStickersRaw,
    AddOneTimeMessagesDismissedByIdMemberRaw,
    CreateSavedSearchRaw,
    DeleteBoardBackgroundRaw,
    GetBoardBackgroundByIdsRaw,
    GetBoardBackgroundsByIdRaw,
    GetBoardStarByIdMemberRaw,
    GetBoardStarsByIdRaw,
    GetBoardsRaw,
    GetBoardsByIdMemberRaw,
    GetBoardsInvitedByIdMemberByFieldRaw,
    GetByFieldRaw,
    GetByIdRaw,
    GetCardsByFilterRaw,
    GetCardsByIdMemberRaw,
    GetCustomBoardBackgroundByIdsRaw,
    GetCustomBoardBackgroundsByIdRaw,
    GetCustomEmojiByIdsRaw,
    GetCustomStickerByIdsRaw,
    GetCustomStickersByIdMemberRaw,
    GetDeltasByIdMemberRaw,
    GetInvitedBoardsRaw,
    GetNotificationsByIdMemberRaw,
    GetNotificationsByIdMemberByFilterRaw,
    GetOrganizationsRaw,
    GetSavedSearchByIdsRaw,
    GetSavedSearchesByIdMemberRaw,
    GetTokensByIdMemberRaw,
    ListActionsByIdMemberRaw,
    ListCustomEmojiByIdMemberRaw,
    ListInvitedOrganizationsByIdRaw,
    ListOrganizationsByIdRaw,
    ListOrganizationsInvitedByIdMemberByFieldRaw,
    RemoveBoardStarByIdMemberByIdBoardStarRaw,
    RemoveCustomBoardBackgroundByIdRaw,
    RemoveCustomStickerByIdsRaw,
    RemoveSavedSearchByIdsRaw,
    UpdateAvatarSourceRaw,
    UpdateBioByIdRaw,
    UpdateBoardBackgroundsByIdRaw,
    UpdateBoardStarRaw,
    UpdateBoardStarPosByIdMemberByIdBoardStarRaw,
    UpdateBoardStarsIdBoardRaw,
    UpdateByIdMemberRaw,
    UpdateCustomBoardBackgroundsRaw,
    UpdateFullNameRaw,
    UpdateInitialsByIdMemberRaw,
    UpdatePrefsColorBlindByIdMemberRaw,
    UpdatePrefsLocaleByIdMemberRaw,
    UpdatePrefsMinutesBetweenSummariesByIdRaw,
    UpdateSavedSearchQueryByIdMemberByIdSavedSearchRaw,
    UpdateSavedSearchesByIdMemberByIdSavedSearchRaw,
    UpdateSavedSearchesNameByIdMemberByIdSavedSearchRaw,
    UpdateSavedSearchesPosByIdMemberByIdSavedSearchRaw,
    UpdateUsernameByIdRaw,
    UploadAvatarByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
