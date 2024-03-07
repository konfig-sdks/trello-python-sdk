from trello_python_sdk.paths.tokens_token_webhooks.get import ApiForget
from trello_python_sdk.paths.tokens_token_webhooks.put import ApiForput
from trello_python_sdk.paths.tokens_token_webhooks.post import ApiForpost


class TokensTokenWebhooks(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
