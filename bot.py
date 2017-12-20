import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username="4fc19737-7d0c-4b50-8d91-9fa1d907978a",
  password="gLVPF6nD4Gtp",
  version='2017-02-03'
)

# replace with your own workspace_id
workspace_id = '2b454151-bb2e-486f-aafd-313dfa4674bb'

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'Hola amigo me gusta la pizza'
    })
print(json.dumps(response, indent=2))

# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))
