from Models.pet_entity import PetEntity

def create_pet_service(name:str, age:int) -> PetEntity:
    return PetEntity(name=name, age=age)