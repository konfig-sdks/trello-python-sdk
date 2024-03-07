operation_parameter_map = {
    '/actions/{idAction}/board-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/actions/{idAction}/board/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'display'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/actions/{idAction}/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}/card-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/actions/{idAction}/card/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}/display-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
        ]
    },
    '/actions/{idAction}/entities-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
        ]
    },
    '/actions/{idAction}/list-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/actions/{idAction}/list/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}/member/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}/member-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/actions/{idAction}/memberCreator/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}/memberCreator-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/actions/{idAction}/organization/{field}-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/actions/{idAction}/organization-GET': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/actions/{idAction}-DELETE': {
        'parameters': [
            {
                'name': 'idAction'
            },
        ]
    },
    '/actions/{idAction}-PUT': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/actions/{idAction}/text-PUT': {
        'parameters': [
            {
                'name': 'idAction'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/batch-GET': {
        'parameters': [
            {
                'name': 'urls'
            },
        ]
    },
    '/boards/{idBoard}/checklists-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/boards/{idBoard}/labels-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'color'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/boards/{idBoard}/powerUps-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards-POST': {
        'parameters': [
            {
                'name': 'closed'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'idBoardSource'
            },
            {
                'name': 'idOrganization'
            },
            {
                'name': 'keepFromSource'
            },
            {
                'name': 'labelNames/blue'
            },
            {
                'name': 'labelNames/green'
            },
            {
                'name': 'labelNames/orange'
            },
            {
                'name': 'labelNames/purple'
            },
            {
                'name': 'labelNames/red'
            },
            {
                'name': 'labelNames/yellow'
            },
            {
                'name': 'name'
            },
            {
                'name': 'powerUps'
            },
            {
                'name': 'prefs/background'
            },
            {
                'name': 'prefs/calendarFeedEnabled'
            },
            {
                'name': 'prefs/cardAging'
            },
            {
                'name': 'prefs/cardCovers'
            },
            {
                'name': 'prefs/comments'
            },
            {
                'name': 'prefs/invitations'
            },
            {
                'name': 'prefs/permissionLevel'
            },
            {
                'name': 'prefs/selfJoin'
            },
            {
                'name': 'prefs/voting'
            },
            {
                'name': 'prefs_background'
            },
            {
                'name': 'prefs_cardAging'
            },
            {
                'name': 'prefs_cardCovers'
            },
            {
                'name': 'prefs_comments'
            },
            {
                'name': 'prefs_invitations'
            },
            {
                'name': 'prefs_permissionLevel'
            },
            {
                'name': 'prefs_selfJoin'
            },
            {
                'name': 'prefs_voting'
            },
            {
                'name': 'subscribed'
            },
        ]
    },
    '/boards/{idBoard}/lists-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/boards/{idBoard}/cards/{filter}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/boards/{idBoard}/calendarKey/generate-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
        ]
    },
    '/boards/{idBoard}/emailKey/generate-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
        ]
    },
    '/boards/{idBoard}/boardStars-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/boards/{idBoard}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_display'
            },
            {
                'name': 'actions_format'
            },
            {
                'name': 'actions_since'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'action_member'
            },
            {
                'name': 'action_member_fields'
            },
            {
                'name': 'action_memberCreator'
            },
            {
                'name': 'action_memberCreator_fields'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'card_attachments'
            },
            {
                'name': 'card_attachment_fields'
            },
            {
                'name': 'card_checklists'
            },
            {
                'name': 'card_stickers'
            },
            {
                'name': 'boardStars'
            },
            {
                'name': 'labels'
            },
            {
                'name': 'label_fields'
            },
            {
                'name': 'labels_limit'
            },
            {
                'name': 'lists'
            },
            {
                'name': 'list_fields'
            },
            {
                'name': 'memberships'
            },
            {
                'name': 'memberships_member'
            },
            {
                'name': 'memberships_member_fields'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'membersInvited'
            },
            {
                'name': 'membersInvited_fields'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'checklist_fields'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'organization_fields'
            },
            {
                'name': 'organization_memberships'
            },
            {
                'name': 'myPrefs'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/{field}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/boards/{idBoard}/cards-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'stickers'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/cards/{idCard}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idCard'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_display'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'action_memberCreator_fields'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checkItemState_fields'
            },
            {
                'name': 'labels'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'checklist_fields'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/checklists-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'checkItems'
            },
            {
                'name': 'checkItem_fields'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/deltas-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'ixLastUpdate'
            },
        ]
    },
    '/boards/{idBoard}/labels/{idLabel}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idLabel'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/lists/{filter}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/boards/{idBoard}/lists-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/members/{filter}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/boards/{idBoard}/members-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'activity'
            },
        ]
    },
    '/boards/{idBoard}/members/{idMember}/cards-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idMember'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'board'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'list'
            },
            {
                'name': 'list_fields'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/membersInvited/{field}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/boards/{idBoard}/membersInvited-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/memberships-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
        ]
    },
    '/boards/{idBoard}/memberships/{idMembership}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idMembership'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
        ]
    },
    '/boards/{idBoard}/organization-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/boards/{idBoard}/organization/{field}-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/boards/{idBoard}/actions-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'display'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'format'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'page'
            },
            {
                'name': 'idModels'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/boards/{idBoard}/labels-GET': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/boards/{idBoard}/markAsViewed-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
        ]
    },
    '/boards/{idBoard}/members/{idMember}-DELETE': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idMember'
            },
        ]
    },
    '/boards/{idBoard}/powerUps/{powerUp}-DELETE': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'powerUp'
            },
        ]
    },
    '/boards/{idBoard}-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'closed'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'idBoardSource'
            },
            {
                'name': 'idOrganization'
            },
            {
                'name': 'keepFromSource'
            },
            {
                'name': 'labelNames/blue'
            },
            {
                'name': 'labelNames/green'
            },
            {
                'name': 'labelNames/orange'
            },
            {
                'name': 'labelNames/purple'
            },
            {
                'name': 'labelNames/red'
            },
            {
                'name': 'labelNames/yellow'
            },
            {
                'name': 'name'
            },
            {
                'name': 'powerUps'
            },
            {
                'name': 'prefs/background'
            },
            {
                'name': 'prefs/calendarFeedEnabled'
            },
            {
                'name': 'prefs/cardAging'
            },
            {
                'name': 'prefs/cardCovers'
            },
            {
                'name': 'prefs/comments'
            },
            {
                'name': 'prefs/invitations'
            },
            {
                'name': 'prefs/permissionLevel'
            },
            {
                'name': 'prefs/selfJoin'
            },
            {
                'name': 'prefs/voting'
            },
            {
                'name': 'prefs_background'
            },
            {
                'name': 'prefs_cardAging'
            },
            {
                'name': 'prefs_cardCovers'
            },
            {
                'name': 'prefs_comments'
            },
            {
                'name': 'prefs_invitations'
            },
            {
                'name': 'prefs_permissionLevel'
            },
            {
                'name': 'prefs_selfJoin'
            },
            {
                'name': 'prefs_voting'
            },
            {
                'name': 'subscribed'
            },
        ]
    },
    '/boards/{idBoard}/closed-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/desc-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/labelNames/blue-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/labelNames/green-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/labelNames/orange-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/labelNames/purple-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/labelNames/red-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/labelNames/yellow-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/members-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'email'
            },
            {
                'name': 'fullName'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/boards/{idBoard}/members/{idMember}-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idMember'
            },
            {
                'name': 'email'
            },
            {
                'name': 'fullName'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/boards/{idBoard}/memberships/{idMembership}-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idMembership'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/idEmailList-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/emailPosition-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/showListGuide-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/showSidebar-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/showSidebarBoardActions-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/showSidebarActivity-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/name-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/idOrganization-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/background-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/calendarFeedEnabled-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/cardAging-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/cardCovers-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/comments-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/invitations-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/permissionLevel-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/selfJoin-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/myPrefs/showSidebarMembers-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/subscribed-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/boards/{idBoard}/prefs/voting-PUT': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/actions/comments-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/cards/{idCard}/attachments-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'file'
            },
            {
                'name': 'mimeType'
            },
            {
                'name': 'name'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklist}/checkItem-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/cards/{idCard}/checklists-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklistSource'
            },
            {
                'name': 'name'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/idLabels-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/labels-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'color'
            },
            {
                'name': 'name'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/idMembers-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/membersVoted-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/stickers-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'image'
            },
            {
                'name': 'left'
            },
            {
                'name': 'rotate'
            },
            {
                'name': 'top'
            },
            {
                'name': 'zIndex'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/convertToCard-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
        ]
    },
    '/cards-POST': {
        'parameters': [
            {
                'name': 'closed'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'due'
            },
            {
                'name': 'fileSource'
            },
            {
                'name': 'idAttachmentCover'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'idCardSource'
            },
            {
                'name': 'idLabels'
            },
            {
                'name': 'idList'
            },
            {
                'name': 'idMembers'
            },
            {
                'name': 'keepFromSource'
            },
            {
                'name': 'labels'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'subscribed'
            },
            {
                'name': 'urlSource'
            },
        ]
    },
    '/cards/{idCard}/attachments/{idAttachment}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idAttachment'
            },
        ]
    },
    '/cards/{idCard}/checklists/{idChecklist}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
        ]
    },
    '/cards/{idCard}/attachments-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/cards/{idCard}/attachments/{idAttachment}-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idAttachment'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/board-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/board/{field}-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/cards/{idCard}-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_display'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'action_memberCreator_fields'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'membersVoted'
            },
            {
                'name': 'memberVoted_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checkItemState_fields'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'checklist_fields'
            },
            {
                'name': 'board'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'list'
            },
            {
                'name': 'list_fields'
            },
            {
                'name': 'stickers'
            },
            {
                'name': 'sticker_fields'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/{field}-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/cards/{idCard}/list/{field}-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/cards/{idCard}/checkItemStates-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/checklists-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'checkItems'
            },
            {
                'name': 'checkItem_fields'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/list-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/membersVoted-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/stickers/{idSticker}-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idSticker'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/stickers-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/actions-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'display'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'format'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'page'
            },
            {
                'name': 'idModels'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/cards/{idCard}/members-GET': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/cards/{idCard}/markAssociatedNotificationsRead-POST': {
        'parameters': [
            {
                'name': 'idCard'
            },
        ]
    },
    '/cards/{idCard}/actions/{idAction}/comments-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idAction'
            },
        ]
    },
    '/cards/{idCard}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
        ]
    },
    '/cards/{idCard}/idLabels/{idLabel}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idLabel'
            },
        ]
    },
    '/cards/{idCard}/labels/{color}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'color'
            },
        ]
    },
    '/cards/{idCard}/idMembers/{idMember}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idMember'
            },
        ]
    },
    '/cards/{idCard}/membersVoted/{idMember}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idMember'
            },
        ]
    },
    '/cards/{idCard}/stickers/{idSticker}-DELETE': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idSticker'
            },
        ]
    },
    '/cards/{idCard}/actions/{idAction}/comments-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idAction'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/cards/{idCard}/idAttachmentCover-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/idBoard-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idList'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'closed'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'due'
            },
            {
                'name': 'fileSource'
            },
            {
                'name': 'idAttachmentCover'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'idCardSource'
            },
            {
                'name': 'idLabels'
            },
            {
                'name': 'idList'
            },
            {
                'name': 'idMembers'
            },
            {
                'name': 'keepFromSource'
            },
            {
                'name': 'labels'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'subscribed'
            },
            {
                'name': 'urlSource'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/pos-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklistCurrent}/checkItem/{idCheckItem}-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklistCurrent'
            },
            {
                'name': 'idCheckItem'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'state'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/name-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/state-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/closed-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/desc-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/due-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/idList-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/idMembers-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/labels-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'color'
            },
            {
                'name': 'name'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/name-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/pos-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cards/{idCard}/stickers/{idSticker}-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'idSticker'
            },
            {
                'name': 'image'
            },
            {
                'name': 'left'
            },
            {
                'name': 'rotate'
            },
            {
                'name': 'top'
            },
            {
                'name': 'zIndex'
            },
        ]
    },
    '/cards/{idCard}/subscribed-PUT': {
        'parameters': [
            {
                'name': 'idCard'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/checklists/{idChecklist}/checkItems-POST': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'checked'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/checklists-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklistSource'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/checklists/{idChecklist}/board-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/checklists/{idChecklist}/board/{field}-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/checklists/{idChecklist}-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'checkItems'
            },
            {
                'name': 'checkItem_fields'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/checklists/{idChecklist}/{field}-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/checklists/{idChecklist}/cards/{filter}-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/checklists/{idChecklist}/checkItems-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/checklists/{idChecklist}/checkItems/{idCheckItem}-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/checklists/{idChecklist}/cards-GET': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'stickers'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/checklists/{idChecklist}-DELETE': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
        ]
    },
    '/checklists/{idChecklist}/checkItems/{idCheckItem}-DELETE': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idCheckItem'
            },
        ]
    },
    '/checklists/{idChecklist}-PUT': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'idCard'
            },
            {
                'name': 'idChecklistSource'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/checklists/{idChecklist}/idCard-PUT': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/checklists/{idChecklist}/name-PUT': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/checklists/{idChecklist}/pos-PUT': {
        'parameters': [
            {
                'name': 'idChecklist'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/labels-POST': {
        'parameters': [
            {
                'name': 'color'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/labels/{idLabel}/board-GET': {
        'parameters': [
            {
                'name': 'idLabel'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/labels/{idLabel}/board/{field}-GET': {
        'parameters': [
            {
                'name': 'idLabel'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/labels/{idLabel}-GET': {
        'parameters': [
            {
                'name': 'idLabel'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/labels/{idLabel}-DELETE': {
        'parameters': [
            {
                'name': 'idLabel'
            },
        ]
    },
    '/labels/{idLabel}-PUT': {
        'parameters': [
            {
                'name': 'idLabel'
            },
            {
                'name': 'color'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/labels/{idLabel}/color-PUT': {
        'parameters': [
            {
                'name': 'idLabel'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/labels/{idLabel}/name-PUT': {
        'parameters': [
            {
                'name': 'idLabel'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/lists/{idList}/archiveAllCards-POST': {
        'parameters': [
            {
                'name': 'idList'
            },
        ]
    },
    '/lists/{idList}/cards-POST': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'due'
            },
            {
                'name': 'idMembers'
            },
            {
                'name': 'labels'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/lists-POST': {
        'parameters': [
            {
                'name': 'closed'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'idListSource'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'subscribed'
            },
        ]
    },
    '/lists/{idList}/actions-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'display'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'format'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'page'
            },
            {
                'name': 'idModels'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/lists/{idList}/board/{field}-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/lists/{idList}-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'board'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/lists/{idList}/{field}-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/lists/{idList}/cards/{filter}-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/lists/{idList}/cards-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'stickers'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/lists/{idList}/board-GET': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/lists/{idList}/moveAllCards-POST': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'idBoard'
            },
        ]
    },
    '/lists/{idList}-PUT': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'closed'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'idListSource'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'subscribed'
            },
        ]
    },
    '/lists/{idList}/closed-PUT': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/lists/{idList}/idBoard-PUT': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/lists/{idList}/name-PUT': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/lists/{idList}/pos-PUT': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/lists/{idList}/subscribed-PUT': {
        'parameters': [
            {
                'name': 'idList'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/boardBackgrounds-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'brightness'
            },
            {
                'name': 'file'
            },
            {
                'name': 'tile'
            },
        ]
    },
    '/members/{idMember}/boardStars-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/members/{idMember}/customBoardBackgrounds-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'brightness'
            },
            {
                'name': 'file'
            },
            {
                'name': 'tile'
            },
        ]
    },
    '/members/{idMember}/customEmoji-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'file'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/members/{idMember}/customStickers-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/members/{idMember}/oneTimeMessagesDismissed-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/savedSearches-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/members/{idMember}/boardBackgrounds/{idBoardBackground}-DELETE': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardBackground'
            },
        ]
    },
    '/members/{idMember}/boardBackgrounds/{idBoardBackground}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardBackground'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/boardBackgrounds-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/boardStars/{idBoardStar}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardStar'
            },
        ]
    },
    '/members/{idMember}/boardStars-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
        ]
    },
    '/members/{idMember}/boards/{filter}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/boards-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'actions_format'
            },
            {
                'name': 'actions_since'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'memberships'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'organization_fields'
            },
            {
                'name': 'lists'
            },
        ]
    },
    '/members/{idMember}/boardsInvited/{field}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/members/{idMember}/{field}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/members/{idMember}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_display'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'action_since'
            },
            {
                'name': 'action_before'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'card_members'
            },
            {
                'name': 'card_member_fields'
            },
            {
                'name': 'card_attachments'
            },
            {
                'name': 'card_attachment_fields'
            },
            {
                'name': 'card_stickers'
            },
            {
                'name': 'boards'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'board_actions'
            },
            {
                'name': 'board_actions_entities'
            },
            {
                'name': 'board_actions_display'
            },
            {
                'name': 'board_actions_format'
            },
            {
                'name': 'board_actions_since'
            },
            {
                'name': 'board_actions_limit'
            },
            {
                'name': 'board_action_fields'
            },
            {
                'name': 'board_lists'
            },
            {
                'name': 'board_memberships'
            },
            {
                'name': 'board_organization'
            },
            {
                'name': 'board_organization_fields'
            },
            {
                'name': 'boardsInvited'
            },
            {
                'name': 'boardsInvited_fields'
            },
            {
                'name': 'boardStars'
            },
            {
                'name': 'savedSearches'
            },
            {
                'name': 'organizations'
            },
            {
                'name': 'organization_fields'
            },
            {
                'name': 'organization_paid_account'
            },
            {
                'name': 'organizationsInvited'
            },
            {
                'name': 'organizationsInvited_fields'
            },
            {
                'name': 'notifications'
            },
            {
                'name': 'notifications_entities'
            },
            {
                'name': 'notifications_display'
            },
            {
                'name': 'notifications_limit'
            },
            {
                'name': 'notification_fields'
            },
            {
                'name': 'notification_memberCreator'
            },
            {
                'name': 'notification_memberCreator_fields'
            },
            {
                'name': 'notification_before'
            },
            {
                'name': 'notification_since'
            },
            {
                'name': 'tokens'
            },
            {
                'name': 'paid_account'
            },
            {
                'name': 'boardBackgrounds'
            },
            {
                'name': 'customBoardBackgrounds'
            },
            {
                'name': 'customStickers'
            },
            {
                'name': 'customEmoji'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/cards/{filter}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/cards-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'stickers'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/customBoardBackgrounds/{idBoardBackground}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardBackground'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/customBoardBackgrounds-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/customEmoji/{idCustomEmoji}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idCustomEmoji'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/customStickers/{idCustomSticker}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idCustomSticker'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/customStickers-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/deltas-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'ixLastUpdate'
            },
        ]
    },
    '/members/{idMember}/boardsInvited-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/notifications-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'display'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'read_filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
            {
                'name': 'before'
            },
            {
                'name': 'since'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/members/{idMember}/notifications/{filter}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/organizations/{filter}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/savedSearches/{idSavedSearch}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idSavedSearch'
            },
        ]
    },
    '/members/{idMember}/savedSearches-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
        ]
    },
    '/members/{idMember}/tokens-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/actions-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'display'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'format'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'page'
            },
            {
                'name': 'idModels'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/members/{idMember}/customEmoji-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/members/{idMember}/organizationsInvited-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/members/{idMember}/organizations-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'paid_account'
            },
        ]
    },
    '/members/{idMember}/organizationsInvited/{field}-GET': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/members/{idMember}/boardStars/{idBoardStar}-DELETE': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardStar'
            },
        ]
    },
    '/members/{idMember}/customBoardBackgrounds/{idBoardBackground}-DELETE': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardBackground'
            },
        ]
    },
    '/members/{idMember}/customStickers/{idCustomSticker}-DELETE': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idCustomSticker'
            },
        ]
    },
    '/members/{idMember}/savedSearches/{idSavedSearch}-DELETE': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idSavedSearch'
            },
        ]
    },
    '/members/{idMember}/avatarSource-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/bio-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/boardBackgrounds/{idBoardBackground}-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardBackground'
            },
            {
                'name': 'brightness'
            },
            {
                'name': 'file'
            },
            {
                'name': 'tile'
            },
        ]
    },
    '/members/{idMember}/boardStars/{idBoardStar}-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardStar'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/members/{idMember}/boardStars/{idBoardStar}/pos-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardStar'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/boardStars/{idBoardStar}/idBoard-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardStar'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'avatarSource'
            },
            {
                'name': 'bio'
            },
            {
                'name': 'fullName'
            },
            {
                'name': 'initials'
            },
            {
                'name': 'prefs/colorBlind'
            },
            {
                'name': 'prefs/locale'
            },
            {
                'name': 'prefs/minutesBetweenSummaries'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/members/{idMember}/customBoardBackgrounds/{idBoardBackground}-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idBoardBackground'
            },
            {
                'name': 'brightness'
            },
            {
                'name': 'file'
            },
            {
                'name': 'tile'
            },
        ]
    },
    '/members/{idMember}/fullName-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/initials-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/prefs/colorBlind-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/prefs/locale-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/prefs/minutesBetweenSummaries-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/savedSearches/{idSavedSearch}/query-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idSavedSearch'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/savedSearches/{idSavedSearch}-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idSavedSearch'
            },
            {
                'name': 'name'
            },
            {
                'name': 'pos'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/members/{idMember}/savedSearches/{idSavedSearch}/name-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idSavedSearch'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/savedSearches/{idSavedSearch}/pos-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'idSavedSearch'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/username-PUT': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/members/{idMember}/avatar-POST': {
        'parameters': [
            {
                'name': 'idMember'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/notifications/{idNotification}/board/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/{idNotification}/board-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/notifications/{idNotification}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'display'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
            {
                'name': 'board'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'list'
            },
            {
                'name': 'card'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'organization_fields'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
        ]
    },
    '/notifications/{idNotification}/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/{idNotification}/card-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/notifications/{idNotification}/card/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/{idNotification}/display-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
        ]
    },
    '/notifications/{idNotification}/entities-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
        ]
    },
    '/notifications/{idNotification}/list-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/notifications/{idNotification}/list/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/{idNotification}/member/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/{idNotification}/memberCreator/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/{idNotification}/member-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/notifications/{idNotification}/memberCreator-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/notifications/{idNotification}/organization-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/notifications/{idNotification}/organization/{field}-GET': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/notifications/all/read-POST': {
        'parameters': [
        ]
    },
    '/notifications/{idNotification}-PUT': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'unread'
            },
        ]
    },
    '/notifications/{idNotification}/unread-PUT': {
        'parameters': [
            {
                'name': 'idNotification'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations-POST': {
        'parameters': [
            {
                'name': 'desc'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'name'
            },
            {
                'name': 'prefs/associatedDomain'
            },
            {
                'name': 'prefs/boardVisibilityRestrict/org'
            },
            {
                'name': 'prefs/boardVisibilityRestrict/private'
            },
            {
                'name': 'prefs/boardVisibilityRestrict/public'
            },
            {
                'name': 'prefs/externalMembersDisabled'
            },
            {
                'name': 'prefs/googleAppsVersion'
            },
            {
                'name': 'prefs/orgInviteRestrict'
            },
            {
                'name': 'prefs/permissionLevel'
            },
            {
                'name': 'website'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/associatedDomain-DELETE': {
        'parameters': [
            {
                'name': 'idOrg'
            },
        ]
    },
    '/organizations/{idOrg}/actions-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'entities'
            },
            {
                'name': 'display'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'format'
            },
            {
                'name': 'since'
            },
            {
                'name': 'before'
            },
            {
                'name': 'page'
            },
            {
                'name': 'idModels'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'memberCreator'
            },
            {
                'name': 'memberCreator_fields'
            },
        ]
    },
    '/organizations/{idOrg}/boards/{filter}-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/organizations/{idOrg}/boards-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'actions_format'
            },
            {
                'name': 'actions_since'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'memberships'
            },
            {
                'name': 'organization'
            },
            {
                'name': 'organization_fields'
            },
            {
                'name': 'lists'
            },
        ]
    },
    '/organizations/{idOrg}/{field}-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/organizations/{idOrg}-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'actions_entities'
            },
            {
                'name': 'actions_display'
            },
            {
                'name': 'actions_limit'
            },
            {
                'name': 'action_fields'
            },
            {
                'name': 'memberships'
            },
            {
                'name': 'memberships_member'
            },
            {
                'name': 'memberships_member_fields'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'member_activity'
            },
            {
                'name': 'membersInvited'
            },
            {
                'name': 'membersInvited_fields'
            },
            {
                'name': 'boards'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'board_actions'
            },
            {
                'name': 'board_actions_entities'
            },
            {
                'name': 'board_actions_display'
            },
            {
                'name': 'board_actions_format'
            },
            {
                'name': 'board_actions_since'
            },
            {
                'name': 'board_actions_limit'
            },
            {
                'name': 'board_action_fields'
            },
            {
                'name': 'board_lists'
            },
            {
                'name': 'paid_account'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/organizations/{idOrg}/members-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'activity'
            },
        ]
    },
    '/organizations/{idOrg}/membersInvited-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/organizations/{idOrg}/membersInvited/{field}-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/organizations/{idOrg}/memberships/{idMembership}-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMembership'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
        ]
    },
    '/organizations/{idOrg}/deltas-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'ixLastUpdate'
            },
        ]
    },
    '/organizations/{idOrg}/members/{filter}-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'filter'
            },
        ]
    },
    '/organizations/{idOrg}/members/{idMember}/cards-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMember'
            },
            {
                'name': 'actions'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'attachment_fields'
            },
            {
                'name': 'members'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'checkItemStates'
            },
            {
                'name': 'checklists'
            },
            {
                'name': 'board'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'list'
            },
            {
                'name': 'list_fields'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/organizations/{idOrg}/memberships-GET': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'member'
            },
            {
                'name': 'member_fields'
            },
        ]
    },
    '/organizations/{idOrg}-DELETE': {
        'parameters': [
            {
                'name': 'idOrg'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/orgInviteRestrict-DELETE': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/logo-DELETE': {
        'parameters': [
            {
                'name': 'idOrg'
            },
        ]
    },
    '/organizations/{idOrg}/members/{idMember}/all-DELETE': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMember'
            },
        ]
    },
    '/organizations/{idOrg}/members/{idMember}-DELETE': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMember'
            },
        ]
    },
    '/organizations/{idOrg}-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'desc'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'name'
            },
            {
                'name': 'prefs/associatedDomain'
            },
            {
                'name': 'prefs/boardVisibilityRestrict/org'
            },
            {
                'name': 'prefs/boardVisibilityRestrict/private'
            },
            {
                'name': 'prefs/boardVisibilityRestrict/public'
            },
            {
                'name': 'prefs/externalMembersDisabled'
            },
            {
                'name': 'prefs/googleAppsVersion'
            },
            {
                'name': 'prefs/orgInviteRestrict'
            },
            {
                'name': 'prefs/permissionLevel'
            },
            {
                'name': 'website'
            },
        ]
    },
    '/organizations/{idOrg}/desc-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/displayName-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/members-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'email'
            },
            {
                'name': 'fullName'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/organizations/{idOrg}/members/{idMember}-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMember'
            },
            {
                'name': 'email'
            },
            {
                'name': 'fullName'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/organizations/{idOrg}/members/{idMember}/deactivated-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMember'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/memberships/{idMembership}-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'idMembership'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/organizations/{idOrg}/name-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/associatedDomain-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/boardVisibilityRestrict/org-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/boardVisibilityRestrict/public-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/externalMembersDisabled-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/googleAppsVersion-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/orgInviteRestrict-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/permissionLevel-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/prefs/boardVisibilityRestrict/private-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/website-PUT': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/organizations/{idOrg}/logo-POST': {
        'parameters': [
            {
                'name': 'idOrg'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/search/members-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'idOrganization'
            },
            {
                'name': 'onlyOrgMembers'
            },
        ]
    },
    '/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'idOrganizations'
            },
            {
                'name': 'idBoards'
            },
            {
                'name': 'idCards'
            },
            {
                'name': 'modelTypes'
            },
            {
                'name': 'board_fields'
            },
            {
                'name': 'boards_limit'
            },
            {
                'name': 'card_fields'
            },
            {
                'name': 'cards_limit'
            },
            {
                'name': 'cards_page'
            },
            {
                'name': 'card_board'
            },
            {
                'name': 'card_list'
            },
            {
                'name': 'card_members'
            },
            {
                'name': 'card_stickers'
            },
            {
                'name': 'card_attachments'
            },
            {
                'name': 'organization_fields'
            },
            {
                'name': 'organizations_limit'
            },
            {
                'name': 'member_fields'
            },
            {
                'name': 'members_limit'
            },
            {
                'name': 'partial'
            },
        ]
    },
    '/sessions-POST': {
        'parameters': [
            {
                'name': 'idBoard'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/sessions/socket-GET': {
        'parameters': [
        ]
    },
    '/sessions/{idSession}-PUT': {
        'parameters': [
            {
                'name': 'idSession'
            },
            {
                'name': 'idBoard'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/sessions/{idSession}/status-PUT': {
        'parameters': [
            {
                'name': 'idSession'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/tokens/{token}-DELETE': {
        'parameters': [
        ]
    },
    '/tokens/{token}-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'webhooks'
            },
        ]
    },
    '/tokens/{token}/{field}-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/tokens/{token}/member/{field}-GET': {
        'parameters': [
            {
                'name': 'field'
            },
        ]
    },
    '/tokens/{token}/member-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
        ]
    },
    '/tokens/{token}/webhooks/{idWebhook}-GET': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
        ]
    },
    '/tokens/{token}/webhooks-GET': {
        'parameters': [
        ]
    },
    '/tokens/{token}/webhooks-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'callbackURL'
            },
            {
                'name': 'idModel'
            },
        ]
    },
    '/tokens/{token}/webhooks/{idWebhook}-DELETE': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
        ]
    },
    '/tokens/{token}/webhooks-PUT': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'callbackURL'
            },
            {
                'name': 'idModel'
            },
        ]
    },
    '/types/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/webhooks/{idWebhook}-GET': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
        ]
    },
    '/webhooks/{idWebhook}/{field}-GET': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
            {
                'name': 'field'
            },
        ]
    },
    '/webhooks/{idWebhook}-DELETE': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
        ]
    },
    '/webhooks-PUT': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'callbackURL'
            },
            {
                'name': 'idModel'
            },
        ]
    },
    '/webhooks/{idWebhook}/active-PUT': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/webhooks/{idWebhook}-PUT': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
            {
                'name': 'description'
            },
            {
                'name': 'active'
            },
            {
                'name': 'callbackURL'
            },
            {
                'name': 'idModel'
            },
        ]
    },
    '/webhooks/{idWebhook}/callbackURL-PUT': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/webhooks/{idWebhook}/description-PUT': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/webhooks/{idWebhook}/idModel-PUT': {
        'parameters': [
            {
                'name': 'idWebhook'
            },
            {
                'name': 'value'
            },
        ]
    },
};