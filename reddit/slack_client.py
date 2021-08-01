import requests
import json

from constants import post_body_no_self
slack_token = "xapp-1-A025LGFRJSC-2163682997765-28ef453d50427b1452bdfa9b93d45bf1f6d36ba1b538fcc8eb9d33c3c8a057fd"
slack_channel = ""
slack_icon_emoji = ""
slack_user_name = "Leeds Rising"

def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': post_body_no_self,
        'icon_emoji': slack_icon_emoji,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()	