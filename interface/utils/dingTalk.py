import requests
import json


def ding_talk(content):
    headers = {'Content-Type': 'application/json'}
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c3df22311e0dfdb8b183f1e066cc146f29c10b7f7645d563c7ead973b5c98bf1'
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    requests.post(webhook, data=json.dumps(data), headers=headers)  # 发送post请求
