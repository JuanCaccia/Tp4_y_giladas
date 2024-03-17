from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/product", tags=["Products"], responses={404: {"message": "Product/s Not Found"}})

product_list = []


def search_product(id: int):
    product = filter(lambda product: product.id == id, product_list)  # Devuelve un objeto
    try:
        return list(product)[0]  # lo convertimos a lista
    except:
        raise HTTPException(404, "Product Not Found")


@router.get("/")
async def products():
    return product_list


@router.get("/{id}")  # se pasa por path, es decir, que el parametro esta en el propio path de la url
async def product(id: int):
    return search_product(id)
