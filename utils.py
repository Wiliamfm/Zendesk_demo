import requests as req
import models


def get_users_by_role(domain: str, user: str, pwd: str, role: str, pagination: int | None):
   if (not pagination):
      url = f"https://{domain}/api/v2/users?role={role}"
   else:
      url = f"https://{domain}/api/v2/users?role={role}&page[size]={pagination}"
   r = req.get(url, auth=(user, pwd))
   print(r.json())
   users: models.Users_Response = models.Users_Response(**r.json())
   return users
