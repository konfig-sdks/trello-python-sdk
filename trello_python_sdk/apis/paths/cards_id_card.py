from trello_python_sdk.paths.cards_id_card.get import ApiForget
from trello_python_sdk.paths.cards_id_card.put import ApiForput
from trello_python_sdk.paths.cards_id_card.delete import ApiFordelete


class CardsIdCard(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
