from pydantic import BaseModel

class PetCreateRequest(BaseModel):
    name: str
    age: int

class PetSuccessResponse(BaseModel):
    id: str
    name: str
    age: int

class PetResponse(BaseModel):
    code: str
    message: str
    data: PetSuccessResponse | None

class PetUpdateRequest(BaseModel):
    id: str
    name: str
    age: int
