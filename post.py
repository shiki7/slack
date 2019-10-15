import requests
import json

# webhookURLを指定
webhook_url = "自分のチャットルームのWebhookURL"

# 送信するテキストを定義
text = "メッセージだよ!!"

# Slackに送信する
requests.post(webhook_url, data = json.dumps({
	"text": text
}));
