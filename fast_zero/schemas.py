from pydantic import BaseModel


class Message(BaseModel):
    """Message"""

    message: str
