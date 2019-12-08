import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    menu_template = TemplateSendMessage(
        alt_Text= "button template",
        template = ButtonsTemplate(
            title = "menu",
            text =  "1/2",
            actions = [
                MessageTemplateAction(
                    label = '1',
                    text = '1'
                ),
                MessageTemplateAction(
                    label = '2',
                    text = '2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, menu_template)
    return "OK"
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
