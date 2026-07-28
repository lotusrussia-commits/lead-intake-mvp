from pydantic import BaseModel


class Lead(BaseModel):
    name: str
    contact: str
    source: str
    comment: str