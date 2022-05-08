from flask import Flask, request, abort

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

line_bot_api = LineBotApi('Channel_access_token')
handler = WebhookHandler('Channel_secret')
    # Channel_access_token
    # Channel_secret
@app.route("/")
def test():
     return "Okay"


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
    if event.message.txt == "Thank you":
        reply_message = "No problem"
    else:
        reply_message = f"You sent {event.message.txt}"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))

   

if __name__ == "__main__":
    app.run()