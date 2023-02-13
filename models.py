from pydantic import BaseSettings


class Settings(BaseSettings):
    subdomain: str = "d3v-haggen-it"
    username: str = "juan@haggen-it.com/token"
    password: str = "3kBi95xPJJXsFQm7vyEWeXAKzfOsPFyRAT6F1mVO"
