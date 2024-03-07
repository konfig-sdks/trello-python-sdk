from trello_python_sdk.paths.checklists_id_checklist.get import ApiForget
from trello_python_sdk.paths.checklists_id_checklist.put import ApiForput
from trello_python_sdk.paths.checklists_id_checklist.delete import ApiFordelete


class ChecklistsIdChecklist(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
