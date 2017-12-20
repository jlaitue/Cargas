from lxml import html
import requests,json
import re

emails = [str(n)+"@zgmzailz.com" for n in range(11,31)]
users=["user_"+str(n) for n in range(11,31)]
print(emails)
print(users)
signup = {}
signup_list =[]
exitos = 0
fracasos = 0
# page = requests.get('http://coolusernames.weebly.com/list-of-random-usernames.html')
# tree = html.fromstring(page.content)
#
# for x in range(1,101):
#     username = tree.xpath('//*[@id="wsite-content"]/div/div[2]/text()['+str(x)+']')
#     if len(username) != 0:
#         usernames.append(username)
#
# for i in range(1,len(usernames)):
#     string = usernames[i][0]
#     string = re.sub('\n','',string)
#     string = re.sub(' ','',string)
#     string = re.sub('\xa0+','',string)
#     # string = re.sub('*$','',string)
#     users.append(string)
# users.pop()
# users.pop()
# users[87]=users[87].replace('*','')
# users[88]=users[88].replace('*','')

# signup.update({'username':'julian'})
# signup.update({'email':'julian.lechuga305@gmail.com'})
# signup.update({'password1':'haldev2017'})
# signup.update({'password2':'haldev2017'})
# signup_list.append(dict(signup))

for a in range(0,len(users)):
    signup.update({'username':users[a]})
    signup.update({'email':emails[a]})
    signup.update({'password1':'haldev2017'})
    signup.update({'password2':'haldev2017'})
    signup_list.append(dict(signup))
for index in range(0,len(signup_list)):
    url1='https://jenny.hellodave.mx/rest-auth/registration/'
    # url1='http://127.0.0.1:8000/rest-auth/registration/'
    data1= signup_list[index]
    re = requests.post(url1,data=json.dumps(data1),headers = {'content-type': 'application/json'})
    if re.status_code == 200:
        exitos+=1
    else:
        print(re.text)
        fracasos+=1

    print(re)
    print("Exitos "+str(exitos))
    print("Fracasos "+str(fracasos))
