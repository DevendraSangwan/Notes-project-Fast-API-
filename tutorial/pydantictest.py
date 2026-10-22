
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "name": "John Doe",
    "signup_ts": "2026-06-01T12:22:00",
    "friends": [1, "2", 3],
}

user = User(**external_data)

print(user)
print(user.id)
