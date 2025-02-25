from app.models.pet_entity import PetEntity
from app.schemas.pet_schemas import PetCreateRequest, PetSuccessResponse, PetUpdateRequest, PetResponse
from typing import List

class PetService:
    def __init__(self):
        self._pets: List[PetEntity] = []

    def create_pet(self, pet: PetCreateRequest) -> PetResponse:
        new_pet = PetEntity(name=pet.name, age=pet.age)
        self._pets.append(new_pet)
        return PetResponse(code='200', message="Pet created successfully!", data = PetSuccessResponse(id=new_pet.id, name=new_pet.name, age=new_pet.age))

    def get_pets(self) -> List[PetSuccessResponse]:
        return [PetSuccessResponse(id=p.id, name=p.name, age=p.age) for p in self._pets]

    def get_pet_by_id(self, pet_id: str) -> PetResponse:
        old_pet = next((pet for pet in self._pets if pet.id == pet_id), None)
        if not old_pet:
            raise ValueError(f"Pet with ID {pet_id} not found")
        return PetResponse(code='200', message="Pet found!", data=PetSuccessResponse(id=old_pet.id, name=old_pet.name, age=old_pet.age))

    def update_pet(self, new_pet: PetUpdateRequest) -> PetResponse:
        old_pet = next((pet for pet in self._pets if pet.id == new_pet.id), None)
        if not old_pet:
            raise ValueError(f"Pet with ID {new_pet.id} not found")
        old_pet.name = new_pet.name
        old_pet.age = new_pet.age
        return PetResponse(code='200', message="Pet updated successfully!", data = PetSuccessResponse(id=old_pet.id, name=old_pet.name, age=old_pet.age))

    def delete_pet(self, pet_id: str) -> PetResponse:
        old_pet = next((pet for pet in self._pets if pet.id == pet_id), None)
        if not old_pet:
            raise ValueError(f"Pet with ID {pet_id} not found")
        self._pets.remove(old_pet)
        return PetResponse(code='200', message="Pet deleted successfully", data=None)

    def get_average_age(self) -> PetResponse:
        if not self._pets:
            return PetResponse(code='200', message="No pets available", data=None)

        total_age = sum(pet.age for pet in self._pets)
        count = len(self._pets)
        average_age = total_age / count

        return PetResponse(code='200', message="Average pet age calculated successfully",
                           data={"average_age": average_age})