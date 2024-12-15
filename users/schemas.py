from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MaxLen, MinLen

class CreateUser(BaseModel):
    #Через field
    # username: str = Field(..., min_length=3, max_length=20)  
    username: Annotated[str, MaxLen(3), MaxLen(20)]     
    email: EmailStr