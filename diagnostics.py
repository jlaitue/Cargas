import requests
import json
from random import randint
exitos = 0
fracasos = 0
suma_reactivos = 0
dimension_ids = [82, 83]

for dimension_id in dimension_ids:
    print("-----------------------------------------------DIMENSION {0}--------------------------------------------------------".format(dimension_id))
    url = 'https://cmsadmin.jenny.mx/admin/factorsperdimension/{0}/'.format(dimension_id)
    re = requests.get(url, headers={
                    "Authorization": "Token d7a06b0c4c35b931bf5b9a93f61d74037a63c23d"})
    factors = re.json()
    factors_ids = [factor['id'] for factor in factors]
    total_factores = len(factors_ids)
    print("IDs de factores por dimension: {0}".format(len(factors_ids)))
    print(factors_ids)
    print("\n")

    for factor_id in factors_ids:
        url = 'https://cmsadmin.jenny.mx/admin/reactivesperfactor/{0}/'.format(factor_id)
        re = requests.get(url, headers={
                        "Authorization": "Token d7a06b0c4c35b931bf5b9a93f61d74037a63c23d"})
        reactives = re.json()["reactivos"]
        suma_reactivos += len(reactives)

        for reactivo in reactives:
            react_number = reactivo["codigo"].split(".")[-1]
            reactivo["numero"] = react_number
            data = reactivo
            re = requests.patch(url, data=json.dumps(data), headers={"content-type": "application/json",
                            "Authorization": "Token d7a06b0c4c35b931bf5b9a93f61d74037a63c23d"})
            if re.status_code == 200:
                exitos += 1
            else:
                print(re.text)
                print("REACTIVO CON FALLA")
                print(factor_id)
                print(reactivo[id])
                fracasos += 1

        print("Total de reactivos de factor id {0}".format(factor_id))
        print(len(reactives))

    print("DIMENSION ID: {0}".format(dimension_id))
    print("TOTAL FACTORES")
    print(total_factores)
    print("TOTAL REACTIVOS")
    print(suma_reactivos)
    print("Exitos "+str(exitos))
    print("Fracasos "+str(fracasos))
