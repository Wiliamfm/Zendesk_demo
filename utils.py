import requests as req
import models


def get_users_by_role(url: str | None, domain: str, user: str, pwd: str, role: str, pagination: int | None):
   if (not url):
      if (not pagination):
         url = f"https://{domain}/api/v2/users?role={role}"
      else:
         url = f"https://{domain}/api/v2/users?role={role}&page[size]={pagination}"
   r = req.get(url, auth=(user, pwd))
   users: models.Users_Response = models.Users_Response(**r.json())
   return users
