import typing_extensions

from trello_python_sdk.apis.tags import TagValues
from trello_python_sdk.apis.tags.board_api import BoardApi
from trello_python_sdk.apis.tags.member_api import MemberApi
from trello_python_sdk.apis.tags.card_api import CardApi
from trello_python_sdk.apis.tags.organization_api import OrganizationApi
from trello_python_sdk.apis.tags.action_api import ActionApi
from trello_python_sdk.apis.tags.notification_api import NotificationApi
from trello_python_sdk.apis.tags.model_list_api import ModelListApi
from trello_python_sdk.apis.tags.checklist_api import ChecklistApi
from trello_python_sdk.apis.tags.token_api import TokenApi
from trello_python_sdk.apis.tags.webhook_api import WebhookApi
from trello_python_sdk.apis.tags.label_api import LabelApi
from trello_python_sdk.apis.tags.session_api import SessionApi
from trello_python_sdk.apis.tags.search_api import SearchApi
from trello_python_sdk.apis.tags.batch_api import BatchApi
from trello_python_sdk.apis.tags.type_api import TypeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BOARD: BoardApi,
        TagValues.MEMBER: MemberApi,
        TagValues.CARD: CardApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.ACTION: ActionApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.LIST: ModelListApi,
        TagValues.CHECKLIST: ChecklistApi,
        TagValues.TOKEN: TokenApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.LABEL: LabelApi,
        TagValues.SESSION: SessionApi,
        TagValues.SEARCH: SearchApi,
        TagValues.BATCH: BatchApi,
        TagValues.TYPE: TypeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BOARD: BoardApi,
        TagValues.MEMBER: MemberApi,
        TagValues.CARD: CardApi,
        TagValues.ORGANIZATION: OrganizationApi,
        TagValues.ACTION: ActionApi,
        TagValues.NOTIFICATION: NotificationApi,
        TagValues.LIST: ModelListApi,
        TagValues.CHECKLIST: ChecklistApi,
        TagValues.TOKEN: TokenApi,
        TagValues.WEBHOOK: WebhookApi,
        TagValues.LABEL: LabelApi,
        TagValues.SESSION: SessionApi,
        TagValues.SEARCH: SearchApi,
        TagValues.BATCH: BatchApi,
        TagValues.TYPE: TypeApi,
    }
)
