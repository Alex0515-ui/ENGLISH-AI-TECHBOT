from pydantic import BaseModel
from typing import Optional


# Create user validation
class UserCreateSchema(BaseModel):
    first_name: str
    telegram_id: int
    username: Optional[str] = None

