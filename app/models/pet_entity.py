import uuid

class PetEntity:
    def __init__(self, name: str, age: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
