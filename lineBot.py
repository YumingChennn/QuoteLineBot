from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction

from randomAccess import randomGet
import specificTopic

app = Flask(__name__)


line_bot_api = LineBotApi('5IZ6N7xGUmdslH1n5pTgDcSMZASTyJSlt6TN4UWlZj+Pq6Vwo8y2A5aQ/QV3RTWxfn0m6cMJHaE2Qjpw4DvIuB4WjQuWOYaW2LKsvjJUrG8re6XrQ5TXD0HpUDeB8UAoXhOpWFbzeYzrxAlGxyzg/wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3cfea4a1ba9ef1c1739b50bd457b5d58')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    metext = event.message.text
    if metext == '隨機取得':
        try:
            randomQuote= randomGet()
            message = TextMessage(text=str(randomQuote))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))

    if metext == '特定主題':
        try:
            message = TextSendMessage(
                text = '請選擇你喜歡的主題內容',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="positive",text="positive")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="motivational", text="motivational")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="inspirational", text="inspirational")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="life", text="life")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="funny", text="funny")
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))

    # 特定主題之Reply功能
    if metext == 'positive':
        try:
            posQuote = specificTopic.posQuoGet()
            message = TextMessage(text =str(posQuote))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))
    # 特定主題之Reply功能
    if metext == 'motivational':
        try:
            motiQuote = specificTopic.motiQuoGet()
            message = TextMessage(text =str(motiQuote))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))
    # 特定主題之Reply功能
    if metext == 'inspirational':
        try:
            inspQuote = specificTopic.inspQuoGet()
            message = TextMessage(text = str(inspQuote))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))
    # 特定主題之Reply功能
    if metext == 'life':
        try:
            lifeQuote = specificTopic.lifeQuoGet()
            message = TextMessage(text = str(lifeQuote))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))
    # 特定主題之Reply功能
    if metext == 'funny':
        try:
            funnyQuote = specificTopic.lifeQuoGet()
            message = TextMessage(text = str(funnyQuote))
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))

    if metext == '收藏功能':
        try:
            message = TextMessage(
                text = "生命不是要等待暴風雨過去，而是要學會在風雨中跳舞。")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))

    if metext == '每日推送':
        try:
            message = TextMessage(
                text = "成功不是最終目的，失敗也不是致命的災難，勇氣繼續前進才是最重要的。")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))

    if metext == '互動遊戲':
        try:
            message = TextMessage(
                text = "無論你在什麼時候開始，重要的是開始之後就不要停止。")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))

    if metext == '設定':
        try:
            message = TextMessage(
                text = "如果那天話能好好說")
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextMessage(text='發生錯誤'))


if __name__ == '__main__':
    app.run()
