# This Python file uses the following encoding: utf-8
import requests
import json
# workspace_id = '78793c33-1e01-40fe-9b67-083069dea915'
workspace_id = 'c0aee474-01d3-41fc-b06f-03125be8c0bf'
username = 'edefd882-2a75-47aa-ba3a-61d33063a0ef'
password = 'vZ2Qki3JrP8K'
excel_data = [{"value": "d10_equilibrio_personal_neutral", "type": "synonyms", "synonyms": ["estable", "rela"}]

# url='https://gateway.watsonplatform.net/conversation/api/v1/workspaces/2b454151-bb2e-486f-aafd-313dfa4674bb/intents?version=2017-04-21'
# data= json.dumps({"intent":"Cuidar_animales_nega","examples":[{"text":"Gatos"},{"text":"Perros"}]})
# r = requests.post(url, auth=('4fc19737-7d0c-4b50-8d91-9fa1d907978a', 'gLVPF6nD4Gtp'), headers = {'content-type': 'application/json'}, data=data)
# print(r)
#
# url1='https://gateway.watsonplatform.net/conversation/api/v1/workspaces/2b454151-bb2e-486f-aafd-313dfa4674bb/entities?version=2017-04-21'
# data1= json.dumps({"entity":"plats","values":[{"value":"pizza"},{"value":"spaguetti"}]})
# re = requests.post(url1, auth=('4fc19737-7d0c-4b50-8d91-9fa1d907978a', 'gLVPF6nD4Gtp'), headers = {'content-type': 'application/json'}, data=data1)
# print(re)

# Prueba para obtener intents workspace con 4 intents
# url = "https://gateway.watsonplatform.net/conversation/api/v1/workspaces/78793c33-1e01-40fe-9b67-083069dea915/intents?version=2017-05-26&export=true"
# r = requests.get(url, auth=('eb0753c2-ddd4-4464-a91c-8972a727a56a', '7Hah6ooFVOwj'))
# intents = r.json()['intents']
# train = [intent['intent'] for intent in intents]
# print(train)

# Obtener intents de workspace real
# url = "https://gateway.watsonplatform.net/conversation/api/v1/workspaces/{0}/intents?version=2017-05-26&export=true&page_limit=1000".format(workspace_id)
# r = requests.get(url, auth=(username, password))
# intents = r.json()['intents']
# train = [intent['intent'] for intent in intents]
# print(train)
# print(len(train))

url = "https://gateway.watsonplatform.net/conversation/api/v1/workspaces/{0}/entities/temas/values?version=2017-05-26".format(workspace_id)
for data in excel_data:
    example = json.dumps(data)
    r = requests.post(url, auth=(username, password), headers={'content-type': 'application/json'}, data=example)
    print(r)
    if r.status_code == 201:
        print('exito')
    else:
        print(r.text)
        # pass
