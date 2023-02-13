import requests as req
import models


def get_users_by_role(domain: str, user: str, pwd: str, role: str):
   r = req.get(
       f"https://{domain}/api/v2/users?role={role}", auth=(user, pwd))
   users: models.Users = models.Users(**r.json())
   return users
