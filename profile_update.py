import requests
import json
import random
user_ids = [str(n) for n in range(1, 76)]
nombres = ['Alejandro','Noe','Miriam','Fernando','José','Grecia','Mariana','Diana','Ninelth','Olga']
apellidos = ['Lechuga','López','Rodríguez','Fernández','Maguey','Mastr','Elbjorn','Villalobos','Avila','Camacho','Gutierrez','Zlatan']
images = [
"http://www.elpopular.pe/sites/default/files/styles/img_620x465/public/imagen/2015/06/24/Noticia-130667-edgar-vivar.jpg?itok=2s2fPW6s",
"https://mi.eng.cam.ac.uk/~cipolla/images/roberto.jpg",
"https://pbs.twimg.com/profile_images/555808804278116352/2RWKgOer.jpeg",
"https://s-media-cache-ak0.pinimg.com/736x/59/f0/40/59f04084ea569bce9ccf19cce612fe7e.jpg",
"http://creativefan.com/important/cf/2012/10/gang-tattoos/mora-tattoo.jpg",
]
exitos = 0
fracasos = 0
print(user_ids)

for user in user_ids:
    print(user)
    url1 = 'https://jenny.hellodave.mx/admin/profileupdatedata/{0}/'.format(user)
    print(url1)
    data1 = {
        'imagen_perfil': random.choice(images),
    }
    re = requests.patch(url1,data=json.dumps(data1), headers={'content-type': 'application/json',"Authorization": "Token 	d2a6a85b9fd56a4a638ca743d6a8f9a55fb99ffe"})
    if re.status_code == 200:
        exitos += 1
    else:
        print(re.text)
        fracasos += 1

    print(re)
    print("Exitos "+str(exitos))
    print("Fracasos "+str(fracasos))
