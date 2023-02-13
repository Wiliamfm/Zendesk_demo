from typing import Union

from fastapi import FastAPI
import models
import utils

settings = models.Settings()
app = FastAPI()


@app.get("/users")
def list_users():
   users = utils.get_users_by_role(
       f"{settings.subdomain}.zendesk.com", settings.username, settings.password, "end-user")
   print(type(users))
   return users


@app.get("/info")
async def info():
   return settings


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
   return {"item_id": item_id, "q": q}
