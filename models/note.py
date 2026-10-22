from pydantic import BaseModel
from pydantic import Field

class Note(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    desc: str = Field(min_length=1, max_length=2000)
    important: bool = False
