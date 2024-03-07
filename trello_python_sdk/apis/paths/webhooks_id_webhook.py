from trello_python_sdk.paths.webhooks_id_webhook.get import ApiForget
from trello_python_sdk.paths.webhooks_id_webhook.put import ApiForput
from trello_python_sdk.paths.webhooks_id_webhook.delete import ApiFordelete


class WebhooksIdWebhook(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
