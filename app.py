from flask import Flask, request, abort#用flask來架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('GgnWvEtJ8bxtjADOwUgn5mhKWsTqimM8V6uHTDVoRhr9m+nwdwc1W59egZJREoHplY8afQMl/CAeKbkzeos9mWrnJCqj+OL44aVk9+enBWhaDihsAhlFOvqNgm5pHC1USl3vSDK8Rm6AEZIS1/JPHgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('38a58c2a6e5c58fcb85251f25e091d76')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()