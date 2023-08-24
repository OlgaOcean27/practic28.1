from pydantic import BaseModel, Field

class Period(BaseModel):
    checkin: str = Field(...)
    checkout: str = Field(...)

class BookingModel(BaseModel):
    bookingid: int = Field(None)
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    bookingdates: Period = Field(None)
    state: str = Field(None)

class User(BaseModel):
    id: int
    first_name: str
    last_name: str