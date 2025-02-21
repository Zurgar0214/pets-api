from pydantic import BaseModel, Field
import uuid
class PetEntity(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    age: int