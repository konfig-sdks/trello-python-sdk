# coding: utf-8

"""
    Trello

    This document describes the REST API of Trello as published by Trello.com.  - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>  - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>

    The version of the OpenAPI document: 1.0
    Created by: https://trello.com/home
"""

from trello_python_sdk.paths.organizations.post import Create
from trello_python_sdk.paths.organizations_id_org_prefs_associated_domain.delete import DeletePrefsAssociatedDomainByIdOrg
from trello_python_sdk.paths.organizations_id_org_actions.get import GetActionsByIdOrg
from trello_python_sdk.paths.organizations_id_org_boards_filter.get import GetBoardsByIdOrgByFilter
from trello_python_sdk.paths.organizations_id_org_boards.get import GetBoardsByOrgId
from trello_python_sdk.paths.organizations_id_org_field.get import GetByIdAndField
from trello_python_sdk.paths.organizations_id_org.get import GetByIdOrg
from trello_python_sdk.paths.organizations_id_org_members.get import GetMembersByIdOrg
from trello_python_sdk.paths.organizations_id_org_members_invited.get import GetMembersInvitedByIdOrg
from trello_python_sdk.paths.organizations_id_org_members_invited_field.get import GetMembersInvitedByIdOrgByField
from trello_python_sdk.paths.organizations_id_org_memberships_id_membership.get import GetMembershipsByIdOrgByIdMembership
from trello_python_sdk.paths.organizations_id_org_deltas.get import GetOrganizationDeltas
from trello_python_sdk.paths.organizations_id_org_members_filter.get import ListMembersByIdOrgByFilter
from trello_python_sdk.paths.organizations_id_org_members_id_member_cards.get import ListMembersCardsByIdOrgByIdMember
from trello_python_sdk.paths.organizations_id_org_memberships.get import ListMembershipsByIdOrg
from trello_python_sdk.paths.organizations_id_org.delete import RemoveByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_org_invite_restrict.delete import RemoveInviteRestrictByIdOrg
from trello_python_sdk.paths.organizations_id_org_logo.delete import RemoveLogoByIdOrg
from trello_python_sdk.paths.organizations_id_org_members_id_member_all.delete import RemoveMemberAll
from trello_python_sdk.paths.organizations_id_org_members_id_member.delete import RemoveMemberByIdOrgByIdMember
from trello_python_sdk.paths.organizations_id_org.put import UpdateByIdOrg
from trello_python_sdk.paths.organizations_id_org_desc.put import UpdateDescriptionByIdOrg
from trello_python_sdk.paths.organizations_id_org_display_name.put import UpdateDisplayNameByIdOrg
from trello_python_sdk.paths.organizations_id_org_members.put import UpdateMembersByIdOrg
from trello_python_sdk.paths.organizations_id_org_members_id_member.put import UpdateMembersByIdOrgByIdMember
from trello_python_sdk.paths.organizations_id_org_members_id_member_deactivated.put import UpdateMembersDeactivatedByIdOrgByIdMember
from trello_python_sdk.paths.organizations_id_org_memberships_id_membership.put import UpdateMembershipByIdOrgByIdMembership
from trello_python_sdk.paths.organizations_id_org_name.put import UpdateNameByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_associated_domain.put import UpdatePrefsAssociatedDomainByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_board_visibility_restrict_org.put import UpdatePrefsBoardVisibilityRestrictByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_board_visibility_restrict_public.put import UpdatePrefsBoardVisibilityRestrictPublicByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_external_members_disabled.put import UpdatePrefsExternalMembersDisabledByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_google_apps_version.put import UpdatePrefsGoogleAppsVersionByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_org_invite_restrict.put import UpdatePrefsOrgInviteRestrictByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_permission_level.put import UpdatePrefsPermissionLevelByIdOrg
from trello_python_sdk.paths.organizations_id_org_prefs_board_visibility_restrict_private.put import UpdatePrefsVisibilityByIdOrg
from trello_python_sdk.paths.organizations_id_org_website.put import UpdateWebsiteByIdOrg
from trello_python_sdk.paths.organizations_id_org_logo.post import UploadLogoByIdOrg
from trello_python_sdk.apis.tags.organization_api_raw import OrganizationApiRaw


class OrganizationApi(
    Create,
    DeletePrefsAssociatedDomainByIdOrg,
    GetActionsByIdOrg,
    GetBoardsByIdOrgByFilter,
    GetBoardsByOrgId,
    GetByIdAndField,
    GetByIdOrg,
    GetMembersByIdOrg,
    GetMembersInvitedByIdOrg,
    GetMembersInvitedByIdOrgByField,
    GetMembershipsByIdOrgByIdMembership,
    GetOrganizationDeltas,
    ListMembersByIdOrgByFilter,
    ListMembersCardsByIdOrgByIdMember,
    ListMembershipsByIdOrg,
    RemoveByIdOrg,
    RemoveInviteRestrictByIdOrg,
    RemoveLogoByIdOrg,
    RemoveMemberAll,
    RemoveMemberByIdOrgByIdMember,
    UpdateByIdOrg,
    UpdateDescriptionByIdOrg,
    UpdateDisplayNameByIdOrg,
    UpdateMembersByIdOrg,
    UpdateMembersByIdOrgByIdMember,
    UpdateMembersDeactivatedByIdOrgByIdMember,
    UpdateMembershipByIdOrgByIdMembership,
    UpdateNameByIdOrg,
    UpdatePrefsAssociatedDomainByIdOrg,
    UpdatePrefsBoardVisibilityRestrictByIdOrg,
    UpdatePrefsBoardVisibilityRestrictPublicByIdOrg,
    UpdatePrefsExternalMembersDisabledByIdOrg,
    UpdatePrefsGoogleAppsVersionByIdOrg,
    UpdatePrefsOrgInviteRestrictByIdOrg,
    UpdatePrefsPermissionLevelByIdOrg,
    UpdatePrefsVisibilityByIdOrg,
    UpdateWebsiteByIdOrg,
    UploadLogoByIdOrg,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OrganizationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OrganizationApiRaw(api_client)
