from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
   subdomain: str = "d3v-haggen-it"
   username: str = "juan@haggen-it.com/token"
   password: str = "3kBi95xPJJXsFQm7vyEWeXAKzfOsPFyRAT6F1mVO"


class User(BaseModel):
   active: bool | None
   alias: str | None
   created_at: str | None
   details: str | None
   email: str | None
   id: int | None
   last_login_at: str | None
   name: str | None
   phone: str | None
   role: str | None
   role_type: int | None
   ticket_restriction: str | None
   url: str | None


class Users_Response(BaseModel):
   users: list[User]
   links: dict[str, str]
