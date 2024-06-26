from sqlmodel import SQLModel, Field
from typing import Optional
import uuid

class UserService(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str = Field(index=True, unique=True, nullable=False)
    cell_number: int
    hashed_password: str
    full_name: str

    
