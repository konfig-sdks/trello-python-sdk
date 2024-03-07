# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from trello_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACTIONS_ID_ACTION = "/actions/{idAction}"
    ACTIONS_ID_ACTION_BOARD = "/actions/{idAction}/board"
    ACTIONS_ID_ACTION_BOARD_FIELD = "/actions/{idAction}/board/{field}"
    ACTIONS_ID_ACTION_CARD = "/actions/{idAction}/card"
    ACTIONS_ID_ACTION_CARD_FIELD = "/actions/{idAction}/card/{field}"
    ACTIONS_ID_ACTION_DISPLAY = "/actions/{idAction}/display"
    ACTIONS_ID_ACTION_ENTITIES = "/actions/{idAction}/entities"
    ACTIONS_ID_ACTION_LIST = "/actions/{idAction}/list"
    ACTIONS_ID_ACTION_LIST_FIELD = "/actions/{idAction}/list/{field}"
    ACTIONS_ID_ACTION_MEMBER = "/actions/{idAction}/member"
    ACTIONS_ID_ACTION_MEMBER_FIELD = "/actions/{idAction}/member/{field}"
    ACTIONS_ID_ACTION_MEMBER_CREATOR = "/actions/{idAction}/memberCreator"
    ACTIONS_ID_ACTION_MEMBER_CREATOR_FIELD = "/actions/{idAction}/memberCreator/{field}"
    ACTIONS_ID_ACTION_ORGANIZATION = "/actions/{idAction}/organization"
    ACTIONS_ID_ACTION_ORGANIZATION_FIELD = "/actions/{idAction}/organization/{field}"
    ACTIONS_ID_ACTION_TEXT = "/actions/{idAction}/text"
    ACTIONS_ID_ACTION_FIELD = "/actions/{idAction}/{field}"
    BATCH = "/batch"
    BOARDS = "/boards"
    BOARDS_ID_BOARD = "/boards/{idBoard}"
    BOARDS_ID_BOARD_ACTIONS = "/boards/{idBoard}/actions"
    BOARDS_ID_BOARD_BOARD_STARS = "/boards/{idBoard}/boardStars"
    BOARDS_ID_BOARD_CALENDAR_KEY_GENERATE = "/boards/{idBoard}/calendarKey/generate"
    BOARDS_ID_BOARD_CARDS = "/boards/{idBoard}/cards"
    BOARDS_ID_BOARD_CARDS_FILTER = "/boards/{idBoard}/cards/{filter}"
    BOARDS_ID_BOARD_CARDS_ID_CARD = "/boards/{idBoard}/cards/{idCard}"
    BOARDS_ID_BOARD_CHECKLISTS = "/boards/{idBoard}/checklists"
    BOARDS_ID_BOARD_CLOSED = "/boards/{idBoard}/closed"
    BOARDS_ID_BOARD_DELTAS = "/boards/{idBoard}/deltas"
    BOARDS_ID_BOARD_DESC = "/boards/{idBoard}/desc"
    BOARDS_ID_BOARD_EMAIL_KEY_GENERATE = "/boards/{idBoard}/emailKey/generate"
    BOARDS_ID_BOARD_ID_ORGANIZATION = "/boards/{idBoard}/idOrganization"
    BOARDS_ID_BOARD_LABEL_NAMES_BLUE = "/boards/{idBoard}/labelNames/blue"
    BOARDS_ID_BOARD_LABEL_NAMES_GREEN = "/boards/{idBoard}/labelNames/green"
    BOARDS_ID_BOARD_LABEL_NAMES_ORANGE = "/boards/{idBoard}/labelNames/orange"
    BOARDS_ID_BOARD_LABEL_NAMES_PURPLE = "/boards/{idBoard}/labelNames/purple"
    BOARDS_ID_BOARD_LABEL_NAMES_RED = "/boards/{idBoard}/labelNames/red"
    BOARDS_ID_BOARD_LABEL_NAMES_YELLOW = "/boards/{idBoard}/labelNames/yellow"
    BOARDS_ID_BOARD_LABELS = "/boards/{idBoard}/labels"
    BOARDS_ID_BOARD_LABELS_ID_LABEL = "/boards/{idBoard}/labels/{idLabel}"
    BOARDS_ID_BOARD_LISTS = "/boards/{idBoard}/lists"
    BOARDS_ID_BOARD_LISTS_FILTER = "/boards/{idBoard}/lists/{filter}"
    BOARDS_ID_BOARD_MARK_AS_VIEWED = "/boards/{idBoard}/markAsViewed"
    BOARDS_ID_BOARD_MEMBERS = "/boards/{idBoard}/members"
    BOARDS_ID_BOARD_MEMBERS_FILTER = "/boards/{idBoard}/members/{filter}"
    BOARDS_ID_BOARD_MEMBERS_ID_MEMBER = "/boards/{idBoard}/members/{idMember}"
    BOARDS_ID_BOARD_MEMBERS_ID_MEMBER_CARDS = "/boards/{idBoard}/members/{idMember}/cards"
    BOARDS_ID_BOARD_MEMBERS_INVITED = "/boards/{idBoard}/membersInvited"
    BOARDS_ID_BOARD_MEMBERS_INVITED_FIELD = "/boards/{idBoard}/membersInvited/{field}"
    BOARDS_ID_BOARD_MEMBERSHIPS = "/boards/{idBoard}/memberships"
    BOARDS_ID_BOARD_MEMBERSHIPS_ID_MEMBERSHIP = "/boards/{idBoard}/memberships/{idMembership}"
    BOARDS_ID_BOARD_MY_PREFS = "/boards/{idBoard}/myPrefs"
    BOARDS_ID_BOARD_MY_PREFS_EMAIL_POSITION = "/boards/{idBoard}/myPrefs/emailPosition"
    BOARDS_ID_BOARD_MY_PREFS_ID_EMAIL_LIST = "/boards/{idBoard}/myPrefs/idEmailList"
    BOARDS_ID_BOARD_MY_PREFS_SHOW_LIST_GUIDE = "/boards/{idBoard}/myPrefs/showListGuide"
    BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR = "/boards/{idBoard}/myPrefs/showSidebar"
    BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_ACTIVITY = "/boards/{idBoard}/myPrefs/showSidebarActivity"
    BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_BOARD_ACTIONS = "/boards/{idBoard}/myPrefs/showSidebarBoardActions"
    BOARDS_ID_BOARD_MY_PREFS_SHOW_SIDEBAR_MEMBERS = "/boards/{idBoard}/myPrefs/showSidebarMembers"
    BOARDS_ID_BOARD_NAME = "/boards/{idBoard}/name"
    BOARDS_ID_BOARD_ORGANIZATION = "/boards/{idBoard}/organization"
    BOARDS_ID_BOARD_ORGANIZATION_FIELD = "/boards/{idBoard}/organization/{field}"
    BOARDS_ID_BOARD_POWER_UPS = "/boards/{idBoard}/powerUps"
    BOARDS_ID_BOARD_POWER_UPS_POWER_UP = "/boards/{idBoard}/powerUps/{powerUp}"
    BOARDS_ID_BOARD_PREFS_BACKGROUND = "/boards/{idBoard}/prefs/background"
    BOARDS_ID_BOARD_PREFS_CALENDAR_FEED_ENABLED = "/boards/{idBoard}/prefs/calendarFeedEnabled"
    BOARDS_ID_BOARD_PREFS_CARD_AGING = "/boards/{idBoard}/prefs/cardAging"
    BOARDS_ID_BOARD_PREFS_CARD_COVERS = "/boards/{idBoard}/prefs/cardCovers"
    BOARDS_ID_BOARD_PREFS_COMMENTS = "/boards/{idBoard}/prefs/comments"
    BOARDS_ID_BOARD_PREFS_INVITATIONS = "/boards/{idBoard}/prefs/invitations"
    BOARDS_ID_BOARD_PREFS_PERMISSION_LEVEL = "/boards/{idBoard}/prefs/permissionLevel"
    BOARDS_ID_BOARD_PREFS_SELF_JOIN = "/boards/{idBoard}/prefs/selfJoin"
    BOARDS_ID_BOARD_PREFS_VOTING = "/boards/{idBoard}/prefs/voting"
    BOARDS_ID_BOARD_SUBSCRIBED = "/boards/{idBoard}/subscribed"
    BOARDS_ID_BOARD_FIELD = "/boards/{idBoard}/{field}"
    CARDS = "/cards"
    CARDS_ID_CARD = "/cards/{idCard}"
    CARDS_ID_CARD_ACTIONS = "/cards/{idCard}/actions"
    CARDS_ID_CARD_ACTIONS_COMMENTS = "/cards/{idCard}/actions/comments"
    CARDS_ID_CARD_ACTIONS_ID_ACTION_COMMENTS = "/cards/{idCard}/actions/{idAction}/comments"
    CARDS_ID_CARD_ATTACHMENTS = "/cards/{idCard}/attachments"
    CARDS_ID_CARD_ATTACHMENTS_ID_ATTACHMENT = "/cards/{idCard}/attachments/{idAttachment}"
    CARDS_ID_CARD_BOARD = "/cards/{idCard}/board"
    CARDS_ID_CARD_BOARD_FIELD = "/cards/{idCard}/board/{field}"
    CARDS_ID_CARD_CHECK_ITEM_STATES = "/cards/{idCard}/checkItemStates"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CURRENT_CHECK_ITEM_ID_CHECK_ITEM = "/cards/{idCard}/checklist/{idChecklistCurrent}/checkItem/{idCheckItem}"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM = "/cards/{idCard}/checklist/{idChecklist}/checkItem"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM = "/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_CONVERT_TO_CARD = "/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/convertToCard"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_NAME = "/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/name"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_POS = "/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/pos"
    CARDS_ID_CARD_CHECKLIST_ID_CHECKLIST_CHECK_ITEM_ID_CHECK_ITEM_STATE = "/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/state"
    CARDS_ID_CARD_CHECKLISTS = "/cards/{idCard}/checklists"
    CARDS_ID_CARD_CHECKLISTS_ID_CHECKLIST = "/cards/{idCard}/checklists/{idChecklist}"
    CARDS_ID_CARD_CLOSED = "/cards/{idCard}/closed"
    CARDS_ID_CARD_DESC = "/cards/{idCard}/desc"
    CARDS_ID_CARD_DUE = "/cards/{idCard}/due"
    CARDS_ID_CARD_ID_ATTACHMENT_COVER = "/cards/{idCard}/idAttachmentCover"
    CARDS_ID_CARD_ID_BOARD = "/cards/{idCard}/idBoard"
    CARDS_ID_CARD_ID_LABELS = "/cards/{idCard}/idLabels"
    CARDS_ID_CARD_ID_LABELS_ID_LABEL = "/cards/{idCard}/idLabels/{idLabel}"
    CARDS_ID_CARD_ID_LIST = "/cards/{idCard}/idList"
    CARDS_ID_CARD_ID_MEMBERS = "/cards/{idCard}/idMembers"
    CARDS_ID_CARD_ID_MEMBERS_ID_MEMBER = "/cards/{idCard}/idMembers/{idMember}"
    CARDS_ID_CARD_LABELS = "/cards/{idCard}/labels"
    CARDS_ID_CARD_LABELS_COLOR = "/cards/{idCard}/labels/{color}"
    CARDS_ID_CARD_LIST = "/cards/{idCard}/list"
    CARDS_ID_CARD_LIST_FIELD = "/cards/{idCard}/list/{field}"
    CARDS_ID_CARD_MARK_ASSOCIATED_NOTIFICATIONS_READ = "/cards/{idCard}/markAssociatedNotificationsRead"
    CARDS_ID_CARD_MEMBERS = "/cards/{idCard}/members"
    CARDS_ID_CARD_MEMBERS_VOTED = "/cards/{idCard}/membersVoted"
    CARDS_ID_CARD_MEMBERS_VOTED_ID_MEMBER = "/cards/{idCard}/membersVoted/{idMember}"
    CARDS_ID_CARD_NAME = "/cards/{idCard}/name"
    CARDS_ID_CARD_POS = "/cards/{idCard}/pos"
    CARDS_ID_CARD_STICKERS = "/cards/{idCard}/stickers"
    CARDS_ID_CARD_STICKERS_ID_STICKER = "/cards/{idCard}/stickers/{idSticker}"
    CARDS_ID_CARD_SUBSCRIBED = "/cards/{idCard}/subscribed"
    CARDS_ID_CARD_FIELD = "/cards/{idCard}/{field}"
    CHECKLISTS = "/checklists"
    CHECKLISTS_ID_CHECKLIST = "/checklists/{idChecklist}"
    CHECKLISTS_ID_CHECKLIST_BOARD = "/checklists/{idChecklist}/board"
    CHECKLISTS_ID_CHECKLIST_BOARD_FIELD = "/checklists/{idChecklist}/board/{field}"
    CHECKLISTS_ID_CHECKLIST_CARDS = "/checklists/{idChecklist}/cards"
    CHECKLISTS_ID_CHECKLIST_CARDS_FILTER = "/checklists/{idChecklist}/cards/{filter}"
    CHECKLISTS_ID_CHECKLIST_CHECK_ITEMS = "/checklists/{idChecklist}/checkItems"
    CHECKLISTS_ID_CHECKLIST_CHECK_ITEMS_ID_CHECK_ITEM = "/checklists/{idChecklist}/checkItems/{idCheckItem}"
    CHECKLISTS_ID_CHECKLIST_ID_CARD = "/checklists/{idChecklist}/idCard"
    CHECKLISTS_ID_CHECKLIST_NAME = "/checklists/{idChecklist}/name"
    CHECKLISTS_ID_CHECKLIST_POS = "/checklists/{idChecklist}/pos"
    CHECKLISTS_ID_CHECKLIST_FIELD = "/checklists/{idChecklist}/{field}"
    LABELS = "/labels"
    LABELS_ID_LABEL = "/labels/{idLabel}"
    LABELS_ID_LABEL_BOARD = "/labels/{idLabel}/board"
    LABELS_ID_LABEL_BOARD_FIELD = "/labels/{idLabel}/board/{field}"
    LABELS_ID_LABEL_COLOR = "/labels/{idLabel}/color"
    LABELS_ID_LABEL_NAME = "/labels/{idLabel}/name"
    LISTS = "/lists"
    LISTS_ID_LIST = "/lists/{idList}"
    LISTS_ID_LIST_ACTIONS = "/lists/{idList}/actions"
    LISTS_ID_LIST_ARCHIVE_ALL_CARDS = "/lists/{idList}/archiveAllCards"
    LISTS_ID_LIST_BOARD = "/lists/{idList}/board"
    LISTS_ID_LIST_BOARD_FIELD = "/lists/{idList}/board/{field}"
    LISTS_ID_LIST_CARDS = "/lists/{idList}/cards"
    LISTS_ID_LIST_CARDS_FILTER = "/lists/{idList}/cards/{filter}"
    LISTS_ID_LIST_CLOSED = "/lists/{idList}/closed"
    LISTS_ID_LIST_ID_BOARD = "/lists/{idList}/idBoard"
    LISTS_ID_LIST_MOVE_ALL_CARDS = "/lists/{idList}/moveAllCards"
    LISTS_ID_LIST_NAME = "/lists/{idList}/name"
    LISTS_ID_LIST_POS = "/lists/{idList}/pos"
    LISTS_ID_LIST_SUBSCRIBED = "/lists/{idList}/subscribed"
    LISTS_ID_LIST_FIELD = "/lists/{idList}/{field}"
    MEMBERS_ID_MEMBER = "/members/{idMember}"
    MEMBERS_ID_MEMBER_ACTIONS = "/members/{idMember}/actions"
    MEMBERS_ID_MEMBER_AVATAR = "/members/{idMember}/avatar"
    MEMBERS_ID_MEMBER_AVATAR_SOURCE = "/members/{idMember}/avatarSource"
    MEMBERS_ID_MEMBER_BIO = "/members/{idMember}/bio"
    MEMBERS_ID_MEMBER_BOARD_BACKGROUNDS = "/members/{idMember}/boardBackgrounds"
    MEMBERS_ID_MEMBER_BOARD_BACKGROUNDS_ID_BOARD_BACKGROUND = "/members/{idMember}/boardBackgrounds/{idBoardBackground}"
    MEMBERS_ID_MEMBER_BOARD_STARS = "/members/{idMember}/boardStars"
    MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR = "/members/{idMember}/boardStars/{idBoardStar}"
    MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR_ID_BOARD = "/members/{idMember}/boardStars/{idBoardStar}/idBoard"
    MEMBERS_ID_MEMBER_BOARD_STARS_ID_BOARD_STAR_POS = "/members/{idMember}/boardStars/{idBoardStar}/pos"
    MEMBERS_ID_MEMBER_BOARDS = "/members/{idMember}/boards"
    MEMBERS_ID_MEMBER_BOARDS_FILTER = "/members/{idMember}/boards/{filter}"
    MEMBERS_ID_MEMBER_BOARDS_INVITED = "/members/{idMember}/boardsInvited"
    MEMBERS_ID_MEMBER_BOARDS_INVITED_FIELD = "/members/{idMember}/boardsInvited/{field}"
    MEMBERS_ID_MEMBER_CARDS = "/members/{idMember}/cards"
    MEMBERS_ID_MEMBER_CARDS_FILTER = "/members/{idMember}/cards/{filter}"
    MEMBERS_ID_MEMBER_CUSTOM_BOARD_BACKGROUNDS = "/members/{idMember}/customBoardBackgrounds"
    MEMBERS_ID_MEMBER_CUSTOM_BOARD_BACKGROUNDS_ID_BOARD_BACKGROUND = "/members/{idMember}/customBoardBackgrounds/{idBoardBackground}"
    MEMBERS_ID_MEMBER_CUSTOM_EMOJI = "/members/{idMember}/customEmoji"
    MEMBERS_ID_MEMBER_CUSTOM_EMOJI_ID_CUSTOM_EMOJI = "/members/{idMember}/customEmoji/{idCustomEmoji}"
    MEMBERS_ID_MEMBER_CUSTOM_STICKERS = "/members/{idMember}/customStickers"
    MEMBERS_ID_MEMBER_CUSTOM_STICKERS_ID_CUSTOM_STICKER = "/members/{idMember}/customStickers/{idCustomSticker}"
    MEMBERS_ID_MEMBER_DELTAS = "/members/{idMember}/deltas"
    MEMBERS_ID_MEMBER_FULL_NAME = "/members/{idMember}/fullName"
    MEMBERS_ID_MEMBER_INITIALS = "/members/{idMember}/initials"
    MEMBERS_ID_MEMBER_NOTIFICATIONS = "/members/{idMember}/notifications"
    MEMBERS_ID_MEMBER_NOTIFICATIONS_FILTER = "/members/{idMember}/notifications/{filter}"
    MEMBERS_ID_MEMBER_ONE_TIME_MESSAGES_DISMISSED = "/members/{idMember}/oneTimeMessagesDismissed"
    MEMBERS_ID_MEMBER_ORGANIZATIONS = "/members/{idMember}/organizations"
    MEMBERS_ID_MEMBER_ORGANIZATIONS_FILTER = "/members/{idMember}/organizations/{filter}"
    MEMBERS_ID_MEMBER_ORGANIZATIONS_INVITED = "/members/{idMember}/organizationsInvited"
    MEMBERS_ID_MEMBER_ORGANIZATIONS_INVITED_FIELD = "/members/{idMember}/organizationsInvited/{field}"
    MEMBERS_ID_MEMBER_PREFS_COLOR_BLIND = "/members/{idMember}/prefs/colorBlind"
    MEMBERS_ID_MEMBER_PREFS_LOCALE = "/members/{idMember}/prefs/locale"
    MEMBERS_ID_MEMBER_PREFS_MINUTES_BETWEEN_SUMMARIES = "/members/{idMember}/prefs/minutesBetweenSummaries"
    MEMBERS_ID_MEMBER_SAVED_SEARCHES = "/members/{idMember}/savedSearches"
    MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH = "/members/{idMember}/savedSearches/{idSavedSearch}"
    MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_NAME = "/members/{idMember}/savedSearches/{idSavedSearch}/name"
    MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_POS = "/members/{idMember}/savedSearches/{idSavedSearch}/pos"
    MEMBERS_ID_MEMBER_SAVED_SEARCHES_ID_SAVED_SEARCH_QUERY = "/members/{idMember}/savedSearches/{idSavedSearch}/query"
    MEMBERS_ID_MEMBER_TOKENS = "/members/{idMember}/tokens"
    MEMBERS_ID_MEMBER_USERNAME = "/members/{idMember}/username"
    MEMBERS_ID_MEMBER_FIELD = "/members/{idMember}/{field}"
    NOTIFICATIONS_ALL_READ = "/notifications/all/read"
    NOTIFICATIONS_ID_NOTIFICATION = "/notifications/{idNotification}"
    NOTIFICATIONS_ID_NOTIFICATION_BOARD = "/notifications/{idNotification}/board"
    NOTIFICATIONS_ID_NOTIFICATION_BOARD_FIELD = "/notifications/{idNotification}/board/{field}"
    NOTIFICATIONS_ID_NOTIFICATION_CARD = "/notifications/{idNotification}/card"
    NOTIFICATIONS_ID_NOTIFICATION_CARD_FIELD = "/notifications/{idNotification}/card/{field}"
    NOTIFICATIONS_ID_NOTIFICATION_DISPLAY = "/notifications/{idNotification}/display"
    NOTIFICATIONS_ID_NOTIFICATION_ENTITIES = "/notifications/{idNotification}/entities"
    NOTIFICATIONS_ID_NOTIFICATION_LIST = "/notifications/{idNotification}/list"
    NOTIFICATIONS_ID_NOTIFICATION_LIST_FIELD = "/notifications/{idNotification}/list/{field}"
    NOTIFICATIONS_ID_NOTIFICATION_MEMBER = "/notifications/{idNotification}/member"
    NOTIFICATIONS_ID_NOTIFICATION_MEMBER_FIELD = "/notifications/{idNotification}/member/{field}"
    NOTIFICATIONS_ID_NOTIFICATION_MEMBER_CREATOR = "/notifications/{idNotification}/memberCreator"
    NOTIFICATIONS_ID_NOTIFICATION_MEMBER_CREATOR_FIELD = "/notifications/{idNotification}/memberCreator/{field}"
    NOTIFICATIONS_ID_NOTIFICATION_ORGANIZATION = "/notifications/{idNotification}/organization"
    NOTIFICATIONS_ID_NOTIFICATION_ORGANIZATION_FIELD = "/notifications/{idNotification}/organization/{field}"
    NOTIFICATIONS_ID_NOTIFICATION_UNREAD = "/notifications/{idNotification}/unread"
    NOTIFICATIONS_ID_NOTIFICATION_FIELD = "/notifications/{idNotification}/{field}"
    ORGANIZATIONS = "/organizations"
    ORGANIZATIONS_ID_ORG = "/organizations/{idOrg}"
    ORGANIZATIONS_ID_ORG_ACTIONS = "/organizations/{idOrg}/actions"
    ORGANIZATIONS_ID_ORG_BOARDS = "/organizations/{idOrg}/boards"
    ORGANIZATIONS_ID_ORG_BOARDS_FILTER = "/organizations/{idOrg}/boards/{filter}"
    ORGANIZATIONS_ID_ORG_DELTAS = "/organizations/{idOrg}/deltas"
    ORGANIZATIONS_ID_ORG_DESC = "/organizations/{idOrg}/desc"
    ORGANIZATIONS_ID_ORG_DISPLAY_NAME = "/organizations/{idOrg}/displayName"
    ORGANIZATIONS_ID_ORG_LOGO = "/organizations/{idOrg}/logo"
    ORGANIZATIONS_ID_ORG_MEMBERS = "/organizations/{idOrg}/members"
    ORGANIZATIONS_ID_ORG_MEMBERS_FILTER = "/organizations/{idOrg}/members/{filter}"
    ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER = "/organizations/{idOrg}/members/{idMember}"
    ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_ALL = "/organizations/{idOrg}/members/{idMember}/all"
    ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_CARDS = "/organizations/{idOrg}/members/{idMember}/cards"
    ORGANIZATIONS_ID_ORG_MEMBERS_ID_MEMBER_DEACTIVATED = "/organizations/{idOrg}/members/{idMember}/deactivated"
    ORGANIZATIONS_ID_ORG_MEMBERS_INVITED = "/organizations/{idOrg}/membersInvited"
    ORGANIZATIONS_ID_ORG_MEMBERS_INVITED_FIELD = "/organizations/{idOrg}/membersInvited/{field}"
    ORGANIZATIONS_ID_ORG_MEMBERSHIPS = "/organizations/{idOrg}/memberships"
    ORGANIZATIONS_ID_ORG_MEMBERSHIPS_ID_MEMBERSHIP = "/organizations/{idOrg}/memberships/{idMembership}"
    ORGANIZATIONS_ID_ORG_NAME = "/organizations/{idOrg}/name"
    ORGANIZATIONS_ID_ORG_PREFS_ASSOCIATED_DOMAIN = "/organizations/{idOrg}/prefs/associatedDomain"
    ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_ORG = "/organizations/{idOrg}/prefs/boardVisibilityRestrict/org"
    ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_PRIVATE = "/organizations/{idOrg}/prefs/boardVisibilityRestrict/private"
    ORGANIZATIONS_ID_ORG_PREFS_BOARD_VISIBILITY_RESTRICT_PUBLIC = "/organizations/{idOrg}/prefs/boardVisibilityRestrict/public"
    ORGANIZATIONS_ID_ORG_PREFS_EXTERNAL_MEMBERS_DISABLED = "/organizations/{idOrg}/prefs/externalMembersDisabled"
    ORGANIZATIONS_ID_ORG_PREFS_GOOGLE_APPS_VERSION = "/organizations/{idOrg}/prefs/googleAppsVersion"
    ORGANIZATIONS_ID_ORG_PREFS_ORG_INVITE_RESTRICT = "/organizations/{idOrg}/prefs/orgInviteRestrict"
    ORGANIZATIONS_ID_ORG_PREFS_PERMISSION_LEVEL = "/organizations/{idOrg}/prefs/permissionLevel"
    ORGANIZATIONS_ID_ORG_WEBSITE = "/organizations/{idOrg}/website"
    ORGANIZATIONS_ID_ORG_FIELD = "/organizations/{idOrg}/{field}"
    SEARCH = "/search"
    SEARCH_MEMBERS = "/search/members"
    SESSIONS = "/sessions"
    SESSIONS_SOCKET = "/sessions/socket"
    SESSIONS_ID_SESSION = "/sessions/{idSession}"
    SESSIONS_ID_SESSION_STATUS = "/sessions/{idSession}/status"
    TOKENS_TOKEN = "/tokens/{token}"
    TOKENS_TOKEN_MEMBER = "/tokens/{token}/member"
    TOKENS_TOKEN_MEMBER_FIELD = "/tokens/{token}/member/{field}"
    TOKENS_TOKEN_WEBHOOKS = "/tokens/{token}/webhooks"
    TOKENS_TOKEN_WEBHOOKS_ID_WEBHOOK = "/tokens/{token}/webhooks/{idWebhook}"
    TOKENS_TOKEN_FIELD = "/tokens/{token}/{field}"
    TYPES_ID = "/types/{id}"
    WEBHOOKS = "/webhooks"
    WEBHOOKS_ID_WEBHOOK = "/webhooks/{idWebhook}"
    WEBHOOKS_ID_WEBHOOK_ACTIVE = "/webhooks/{idWebhook}/active"
    WEBHOOKS_ID_WEBHOOK_CALLBACK_URL = "/webhooks/{idWebhook}/callbackURL"
    WEBHOOKS_ID_WEBHOOK_DESCRIPTION = "/webhooks/{idWebhook}/description"
    WEBHOOKS_ID_WEBHOOK_ID_MODEL = "/webhooks/{idWebhook}/idModel"
    WEBHOOKS_ID_WEBHOOK_FIELD = "/webhooks/{idWebhook}/{field}"
