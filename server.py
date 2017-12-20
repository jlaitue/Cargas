from flask import Flask, request
from watson_developer_cloud import ConversationV1
import requests,json

# conversation = ConversationV1(
#     username='4fc19737-7d0c-4b50-8d91-9fa1d907978a',
#     password='gLVPF6nD4Gtp',
#     version='2016-09-20')
#
# workspace_id = '2b454151-bb2e-486f-aafd-313dfa4674bb'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

def reply(user_id, msg):
    ACCESS_TOKEN = "EAAC7sBfp9ZAEBAHvwjz7A5tOga0KUSnfuTZCTxcUcr41kZB9GGvM4R5UrUztu0ER5t1n7Be2TamxZBZAr6FB3MTeM0nYKH9mwmqPr4OLuHI9ceVVb1ZBKFfQ1my8fQwLdI9AsTEREbnXyPmrwifZCHmqkGcIxmqAI9urjUbGTZBCyAZDZD"

    resp_mess = {
                'recipient': {'id': user_id},
                'message': {'text': msg}
                }
    fb_response = requests.post("https://graph.facebook.com/v2.6/me/messages", params={"access_token": ACCESS_TOKEN},

    data=json.dumps(resp_mess),
    headers = {'content-type': 'application/json'})

    print(fb_response.content)

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.get_json()
    print (data)

    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender_id,message)
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)
