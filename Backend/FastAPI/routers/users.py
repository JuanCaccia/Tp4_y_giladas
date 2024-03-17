from fastapi import APIRouter, HTTPException  # Importamos apirouter
from pydantic import BaseModel  # Importamos fastapi

router = APIRouter(prefix="/user", tags=["Users"], responses={404: {"message": "User/s Not Found"}})  # instanciamos fasapi
'''
Con /docs accederemos a nuestra documentacion generada automaticamnete con Swaggger UI: http://127.0.0.1:8000/docs

Con el comando 'uvicorn main:app --reload' levantaremos el servidor, con Ctrl+C lo detendremos

@app.get("/")  # usamos la instancia del fastapi
async def root():  # Ejecutamos una foncion asincrona
    return {"mensaje": "Que onda paa"}


@app.get("/siu")  # usamos la instancia del fastapi
async def siu():  # Ejecutamos una foncion asincrona
    return {"siu": "SIUUUUUUUUUU"}


@app.get("/temon")  # usamos la instancia del fastapi
async def temon():  # Ejecutamos una foncion asincrona
    return {"url": "https://open.spotify.com/intl-es/track/4vlrKddAtbNTgxXvr24ovy?si=26dc145dfcb14338"}



# Creando un api para usuarios con json


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Juan", "surname": "Caccia", "developer": "Python", "age": 19},
            {"name": "Esteban", "surname": "Quito", "developer": "JavaScript", "age": 44},
            {"name": "Micho", "surname": "Tito", "developer": "C", "age": 20}]
'''

# Creando un api para usuarios con una clase


class User(BaseModel):
    id: int
    name: str
    surname: str
    developer: str
    age: int


users_list = [User(id=1, name="Juan", surname="Caccia", developer="Python", age=19),
              User(id=2, name="Esteban", surname="Quito", developer="JavaScript", age=44),
              User(id=3, name="Micho", surname="Tito", developer="C", age=20)]


def search_users(id: int):
    users = filter(lambda user: user.id == id, users_list)  # Devuelve un objeto
    try:
        return list(users)[0]  # lo convertimos a lista
    except:
        raise HTTPException(404, "User Not Found")


@router.get("/{id}")  # se pasa por path, es decir, que el parametro esta en el propio path de la url
async def user(id: int):
    return search_users(id)  # este 'id' lo toma el .get desde la url del navegador(es el que se define en la funcion)


@router.get("/")  # se pasa por query, es decir, se le agregan parametros extra en la url: http://127.0.0.1:8000/userquery/?id=1
async def userquery(id: int):
    return search_users(id)  # este 'id' lo toma el .get desde la url del navegador(es el que se define en la funcion)


@router.get("/")
async def users():
    return users_list


@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_users(user.id)) == User:
        raise HTTPException(204, "User Alredy Exist")  # Fijarse la documentacion de http exceptions: https://developer.mozilla.org/es/docs/Web/HTTP/Status
        # return {"error": "User Alredy Exist"}

    users_list.append(user)
    return user


@router.put("/", status_code=202)
async def user(user: User):
    encontrao = False
    for num, usuario in enumerate(users_list):
        if usuario.id == user.id:
            users_list[num] = user
            encontrao = True

    if not encontrao:
        raise HTTPException(404, "User Not Found")
        # return {"error": "User Not Found"}

    return user


@router.delete("/{id}")
async def user(id: int):
    encontrao = False
    for num, usuario in enumerate(users_list):
        if usuario.id == id:
            del users_list[num]
            encontrao = True
            return usuario
    if not encontrao:
        raise HTTPException(404, "User Not Found")
