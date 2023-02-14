from typing import Union

from fastapi import FastAPI
import models
import utils

settings = models.Settings()
app = FastAPI()


@app.get("/users")
def list_users(role: str = "end-user", pagination: int | None = None):
   users = utils.get_users_by_role(
       f"{settings.subdomain}.zendesk.com", settings.username, settings.password, role, pagination)
   return users


@app.get("/info")
async def info():
   return settings
