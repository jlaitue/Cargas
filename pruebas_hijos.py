import requests
import json
user = 84
exitos = 0
fracasos = 0
url1 = 'https://jenny.hellodave.mx/admin/profileupdatedata/{0}/'.format(user)
data1 = {"hijos":[
				{
				"id":22,
				"nombre":"jonathan",
				"edad":"45"
				},
				{
				"nombre":"masterof",
				"edad":"12"
				}
				]
		}
re = requests.put(url1,data=json.dumps(data1), headers={'content-type': 'application/json',"Authorization": "Token d2a6a85b9fd56a4a638ca743d6a8f9a55fb99ffe"})
if re.status_code == 200:
    exitos += 1
else:
    print(re.text)
    fracasos += 1

print(re)
print("Exitos "+str(exitos))
print("Fracasos "+str(fracasos))
