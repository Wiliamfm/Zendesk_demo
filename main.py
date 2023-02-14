from typing import Union

from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import models
import utils

settings = models.Settings()
security = HTTPBasic()
app = FastAPI()


@app.get("/users")
def list_users(credentials: HTTPBasicCredentials = Depends(security), role: str = "end-user", pagination: int | None = None, next: str | None = None, prev: str | None = None):
   url: str | None = None
   if prev:
      url = prev
   if next:
      url = next
   users = utils.get_users_by_role(
       url, f"{settings.subdomain}.zendesk.com", credentials.username, credentials.password, role, pagination)
   return users


@app.get("/info")
async def info():
   return settings
