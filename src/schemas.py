from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    phone: str = Field(max_length=50)
    birth_date: datetime
    additional: str = Field(max_length=250)



class ContactResponse(ContactBase):
    id: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

