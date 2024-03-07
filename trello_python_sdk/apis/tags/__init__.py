# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from trello_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BOARD = "board"
    MEMBER = "member"
    CARD = "card"
    ORGANIZATION = "organization"
    ACTION = "action"
    NOTIFICATION = "notification"
    LIST = "list"
    CHECKLIST = "checklist"
    TOKEN = "token"
    WEBHOOK = "webhook"
    LABEL = "label"
    SESSION = "session"
    SEARCH = "search"
    BATCH = "batch"
    TYPE = "type"
