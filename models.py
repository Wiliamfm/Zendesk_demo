from pydantic import BaseSettings, BaseModel
import os


class Settings(BaseSettings):
   subdomain: str = os.getenv("subdomain", "")


class User(BaseModel):
   active:	bool | None
   alias: str | None
   chat_only: bool | None
   created_at: str | None
   custom_role_id: int | None
   default_group_id: int | None
   details: str | None
   email: str | None
   external_id: str | None
   iana_time_zone: str | None
   id: int | None
   last_login_at: str | None
   locale: str | None
   locale_id: int | None
   moderator: bool | None
   name: str | None
   notes: str | None
   only_private_comments: bool | None
   organization_id: int | None
   phone: str | None
   # photo: dict | None
   remote_photo_url: str | None
   report_csv: bool | None
   restricted_agent: bool | None
   role: str | None
   role_type: int | None
   shared: bool | None
   shared_agent: bool | None
   shared_phone_number: bool | None
   signature: str | None
   suspended: bool | None
   tags: list | None
   ticket_restriction: str | None
   time_zone: str | None
   two_factor_auth_enabled: bool | None
   updated_at: str | None
   url: str | None
   # user_fields: dict | None
   verified: bool | None


class Users_Response(BaseModel):
   users: list[User]
   links: dict[str, str] | None
