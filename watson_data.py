# This Python file uses the following encoding: utf-8
import requests
import json
# workspace_id = '78793c33-1e01-40fe-9b67-083069dea915'
workspace_id = 'c0aee474-01d3-41fc-b06f-03125be8c0bf'
username = 'edefd882-2a75-47aa-ba3a-61d33063a0ef'
password = 'vZ2Qki3JrP8K'
excel_data = [{"value": "d10_equilibrio_personal_neutral", "type": "synonyms", "synonyms": ["estable", "rela"}]


url = "https://gateway.watsonplatform.net/conversation/api/v1/workspaces/{0}/entities/temas/values?version=2017-05-26".format(workspace_id)
for data in excel_data:
    example = json.dumps(data)
    r = requests.post(url, auth=(username, password), headers={'content-type': 'application/json'}, data=example)
    print(r)
    if r.status_code == 201:
        print('Éxito')
    else:
        print(r.text)
