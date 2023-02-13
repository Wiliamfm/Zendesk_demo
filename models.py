from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    subdomain: str = "d3v-haggen-it"
    username: str = "juan@haggen-it.com/token"
    password: str = "3kBi95xPJJXsFQm7vyEWeXAKzfOsPFyRAT6F1mVO"


class Users(BaseModel):
    active: bool
    alias: str
    chat_only: bool
    created_at: str
    custom_role_id: int
    default_group_id: int
    details: str
    email: str
    external_id: str
    iana_time_zone: str
    id: int
    last_login_at: str
    locale: str
