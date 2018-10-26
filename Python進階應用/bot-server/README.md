# Line Bot 之非常入門教學

## 前置作業

### 1. Access token 以及 Secret

開始之前我們必須先將 Line Bot API 的 Access Token 以及 Client Secret 設定在
`.env` 檔案裡，以利接下來的本機端開發。你會需要創建一個叫做 `.env` 的檔案並在裡
面放入這些內容：

```
LINE_BOT_ACCESS_TOKEN=把你的 access token 放在這裡
LINE_BOT_SECRET=把你的 secret 放在這裡
```

其中的 acccess token 可以在 Messaging settings 中的 "Channel access token
(long-lived)" 欄位裡按下 "Issue" 以後取得；而 secret 可以在 Basic Information
中的 "Channel secret" 取得。

### 2. 安裝相關套件

在 command line 執行以下指令：

```
pip install -r requirements.txt
```

### 3. 啟動 ngrok 並且設定 Line Bot 的 Webhook URL

請按照 "03. 使用 ngrok 測試" 中的指示啟動 ngrok。

啟動後你會看到 "Forwarding" 的字樣，將其對應的 URL 複製（不過需要去除前面的
`https://`）並填入 Line developers console 介面裡面 Messaging settings 中的
Webhook URL 欄位裡。


## 開始開發！

在 command line 裡執行：

```
python app.py
```

`app.py` 裡面是一個 echo bot，你傳什麼訊息他就回答什麼。試試看在你的 Line 裡面
傳一則訊息給它吧！

課堂中我們會藉由修改 `app.py` 來打造更豐富的 Line Bot。


## 練習 / 挑戰

### 1. 敷衍的機器人

收到訊息時，檢查訊息內是否含有「哈」字，如果是的話回傳 10 個哈。

### 2. 午餐吃什麼

從一個你自己制定的餐廳列表中，隨機挑一個出來。每一次應該跳出不一樣的結果。

<sub>提示：可以用 `random` 模組的 `choice` 函式來隨機取出一個 `list` 的其中
一個元素</sub>

### 3. 增加新的午餐選項

如果使用者輸入一個像這樣的訊息：`/add 吃自己`，要把吃自己加入選項裡。

<sub>提示：</sub>
```python
>>> 'hi there'.split()
['hi', 'there']
```

### 4. 列出午餐選項

如果使用者輸入 `/list`，要把目前的選項列出來給使用者看。

<sub>提示：</sub>
```python
>>> ' '.join(['hi', 'there'])
'hi there'
```
