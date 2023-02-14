import requests as req
import models


def get_users_by_role(domain: str, user: str, pwd: str, role: str):
   r = req.get(
       f"https://{domain}/api/v2/users?role={role}&page[size]=5", auth=(user, pwd))
   users: models.Users_Response = models.Users_Response(**r.json())
   return users
