import uuid
class PetEntity():
    id: str
    name: str
    age: int

    def __init__(self, name, age):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age