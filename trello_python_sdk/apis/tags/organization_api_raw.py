# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.organizations.post import CreateRaw
from trello_python_sdk.paths.organizations_id_org_prefs_associated_domain.delete import DeletePrefsAssociatedDomainByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_actions.get import GetActionsByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_boards_filter.get import GetBoardsByIdOrgByFilterRaw
from trello_python_sdk.paths.organizations_id_org_boards.get import GetBoardsByOrgIdRaw
from trello_python_sdk.paths.organizations_id_org_field.get import GetByIdAndFieldRaw
from trello_python_sdk.paths.organizations_id_org.get import GetByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_members.get import GetMembersByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_members_invited.get import GetMembersInvitedByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_members_invited_field.get import GetMembersInvitedByIdOrgByFieldRaw
from trello_python_sdk.paths.organizations_id_org_memberships_id_membership.get import GetMembershipsByIdOrgByIdMembershipRaw
from trello_python_sdk.paths.organizations_id_org_deltas.get import GetOrganizationDeltasRaw
from trello_python_sdk.paths.organizations_id_org_members_filter.get import ListMembersByIdOrgByFilterRaw
from trello_python_sdk.paths.organizations_id_org_members_id_member_cards.get import ListMembersCardsByIdOrgByIdMemberRaw
from trello_python_sdk.paths.organizations_id_org_memberships.get import ListMembershipsByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org.delete import RemoveByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_org_invite_restrict.delete import RemoveInviteRestrictByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_logo.delete import RemoveLogoByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_members_id_member_all.delete import RemoveMemberAllRaw
from trello_python_sdk.paths.organizations_id_org_members_id_member.delete import RemoveMemberByIdOrgByIdMemberRaw
from trello_python_sdk.paths.organizations_id_org.put import UpdateByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_desc.put import UpdateDescriptionByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_display_name.put import UpdateDisplayNameByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_members.put import UpdateMembersByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_members_id_member.put import UpdateMembersByIdOrgByIdMemberRaw
from trello_python_sdk.paths.organizations_id_org_members_id_member_deactivated.put import UpdateMembersDeactivatedByIdOrgByIdMemberRaw
from trello_python_sdk.paths.organizations_id_org_memberships_id_membership.put import UpdateMembershipByIdOrgByIdMembershipRaw
from trello_python_sdk.paths.organizations_id_org_name.put import UpdateNameByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_associated_domain.put import UpdatePrefsAssociatedDomainByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_board_visibility_restrict_org.put import UpdatePrefsBoardVisibilityRestrictByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_board_visibility_restrict_public.put import UpdatePrefsBoardVisibilityRestrictPublicByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_external_members_disabled.put import UpdatePrefsExternalMembersDisabledByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_google_apps_version.put import UpdatePrefsGoogleAppsVersionByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_org_invite_restrict.put import UpdatePrefsOrgInviteRestrictByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_permission_level.put import UpdatePrefsPermissionLevelByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_prefs_board_visibility_restrict_private.put import UpdatePrefsVisibilityByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_website.put import UpdateWebsiteByIdOrgRaw
from trello_python_sdk.paths.organizations_id_org_logo.post import UploadLogoByIdOrgRaw


class OrganizationApiRaw(
    CreateRaw,
    DeletePrefsAssociatedDomainByIdOrgRaw,
    GetActionsByIdOrgRaw,
    GetBoardsByIdOrgByFilterRaw,
    GetBoardsByOrgIdRaw,
    GetByIdAndFieldRaw,
    GetByIdOrgRaw,
    GetMembersByIdOrgRaw,
    GetMembersInvitedByIdOrgRaw,
    GetMembersInvitedByIdOrgByFieldRaw,
    GetMembershipsByIdOrgByIdMembershipRaw,
    GetOrganizationDeltasRaw,
    ListMembersByIdOrgByFilterRaw,
    ListMembersCardsByIdOrgByIdMemberRaw,
    ListMembershipsByIdOrgRaw,
    RemoveByIdOrgRaw,
    RemoveInviteRestrictByIdOrgRaw,
    RemoveLogoByIdOrgRaw,
    RemoveMemberAllRaw,
    RemoveMemberByIdOrgByIdMemberRaw,
    UpdateByIdOrgRaw,
    UpdateDescriptionByIdOrgRaw,
    UpdateDisplayNameByIdOrgRaw,
    UpdateMembersByIdOrgRaw,
    UpdateMembersByIdOrgByIdMemberRaw,
    UpdateMembersDeactivatedByIdOrgByIdMemberRaw,
    UpdateMembershipByIdOrgByIdMembershipRaw,
    UpdateNameByIdOrgRaw,
    UpdatePrefsAssociatedDomainByIdOrgRaw,
    UpdatePrefsBoardVisibilityRestrictByIdOrgRaw,
    UpdatePrefsBoardVisibilityRestrictPublicByIdOrgRaw,
    UpdatePrefsExternalMembersDisabledByIdOrgRaw,
    UpdatePrefsGoogleAppsVersionByIdOrgRaw,
    UpdatePrefsOrgInviteRestrictByIdOrgRaw,
    UpdatePrefsPermissionLevelByIdOrgRaw,
    UpdatePrefsVisibilityByIdOrgRaw,
    UpdateWebsiteByIdOrgRaw,
    UploadLogoByIdOrgRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
