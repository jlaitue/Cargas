from pymongo import MongoClient
client_conversations = MongoClient('mongodb://eliel:rapture@ds137760.mlab.com:37760/conversations')
db_conversations = client_conversations.conversations
key = 1
message_id = 3
flag = 0
intent_grade = 1
response_grade = 0
collection = db_conversations.get_collection("user_{0}".format(key))
message_keys = collection.find({"message_id": message_id})
keys = [key for key in message_keys][0]
print(keys['intent'])


# if flag == 0:
#     collection.update(
#     {"message_id":message_id},
#     {"$set":{"intent_grade":intent_grade}}
#     )
# else:
#     collection.update(
#     {"message_id":message_id},
#     {"$set":{"response_grade":response_grade}}
#     )
# message_graded = collection.find()
# keys = [key for key in message_graded]
# print(keys)
# for key in collection.find():
#     print(key)
#     if "message_checked" not in key:
#         print(True)
#         break
# if "response_grade" in keys and "intent_grade" in keys:
#     collection.update(
#     {"message_id":message_id},
#     {"$set":{"message_checked":True}}
#     )
