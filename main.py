from typing import Union

from fastapi import FastAPI
import models

settings = models.Settings()
app = FastAPI()


@app.get("/users")
def list_users():
    return {"Hello": "World"}


@app.get("/info")
async def info():
    return settings


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
