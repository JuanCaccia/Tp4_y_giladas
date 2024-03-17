from fastapi import FastAPI  # Importamos fastapi
from routers import products, users
from fastapi.staticfiles import StaticFiles  # Para montar imagenes

app = FastAPI()

# Añadiendo los routers
app.include_router(users.router)
app.include_router(products.router)
app.mount("/statics", StaticFiles(directory="statics"), name="statics")  # Montando la imagen


@app.get("/")
async def root():
    return {"message": "Que onda paaaaaaa"}


@app.get("/url")
async def url():
    return {"url": "https://www.binance.com/es"}
