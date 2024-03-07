from trello_python_sdk.paths.actions_id_action.get import ApiForget
from trello_python_sdk.paths.actions_id_action.put import ApiForput
from trello_python_sdk.paths.actions_id_action.delete import ApiFordelete


class ActionsIdAction(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
