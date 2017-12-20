import requests,json
user_ids = [str(n) for n in range(2,93)]
exitos = 0
fracasos = 0


for user in user_ids:
    url1='https://jenny.hellodave.mx/admin/facebookid/{0}/'.format(user)
    data1= {'facebook_id':'{0}'.format(user)}
    re = requests.patch(url1,data=json.dumps(data1),headers = {'content-type': 'application/json'})
    if re.status_code == 200:
        exitos+=1
    else:
        print(re.text)
        fracasos+=1

    print(re)
    print("Exitos "+str(exitos))
    print("Fracasos "+str(fracasos))
