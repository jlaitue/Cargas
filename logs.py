import requests,json
from random import randint
user_ids = [n for n in range(2,51)]
values = [randint(50,100) for n in range(2,51)]
exitos = 0
fracasos = 0

print(user_ids)
print(values)
for index in range(len(user_ids)):
    url1='http://127.0.0.1:8000/admin/logs/'
    data1 = {
    'factor':{"name": "Calidad de vida de los animales"},
    'perfil':user_ids[index],
    'valor':values[index]
    }
    re = requests.post(url1,data=json.dumps(data1),headers = {'content-type': 'application/json'})
    if re.status_code == 201:
        exitos+=1
    else:
        print(re.text)
        fracasos+=1

    print(re)
    print("Exitos "+str(exitos))
    print("Fracasos "+str(fracasos))
