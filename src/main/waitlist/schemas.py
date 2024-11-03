from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistEntryCreateSchema(Schema):
    # create -> Data
    # waitlistEntryIn
    email : EmailStr


class WaitlistEntryListSchema(Schema):
    # get -> Data
    # waitlistEntryout
    id : int 
    email : EmailStr 


from pydantic import BaseModel
from datetime import datetime

class WaitlistEntryDetailSchema(Schema):
    email: str
    timestamp: datetime  # Make sure this matches the model's `DateTimeField`

    class Config:
        orm_mode = True  # Allows Pydantic to work directly with Django model instances