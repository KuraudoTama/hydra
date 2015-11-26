from base_action import BaseAction
from pyslack import pyslack


class PostSlackMessage(BaseAction):
    def __init__(self, config):
        self._slack_token = config.get('token')
        self._slackclient = pyslack.SlackClient(self._slack_token)

    def do(self, **kwargs):
        channel = kwargs.get('channel')
        kwargs.pop('channel')
        text = kwargs.get('text')
        kwargs.pop('text')
        self._slackclient.chat_post_message(channel, text, **kwargs)
