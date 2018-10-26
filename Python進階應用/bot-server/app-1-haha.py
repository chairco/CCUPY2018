################## 初始化 Line Bot API ##################
import os
import dotenv
dotenv.load_dotenv()

from linebot import LineBotApi, WebhookHandler

line_bot_api = LineBotApi(os.getenv('LINE_BOT_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_BOT_SECRET'))
#########################################################


###################### 初始化 Flask #####################
from flask import Flask, request, abort

app = Flask(__name__)

############### 初始化 Callback Endpoint ################
@app.route("/", methods=['POST'])
def callback():
    # 這一段可以不需要理解，這是 Line 官方在 Line Bot Python SDK 使用說明裡
    # 提供的程式碼：https://github.com/line/line-bot-sdk-python
    from linebot.exceptions import InvalidSignatureError
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
#########################################################


################### 接收並處理文字訊息 ##################
from linebot.models import MessageEvent, TextMessage, TextSendMessage

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text.endswith('哈'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='哈' * 10))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))
#########################################################


####################### 執行 Flask ######################
if __name__ == "__main__":
    app.run()
