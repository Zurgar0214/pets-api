from typing import List

from fastapi import APIRouter

from app.schemas.pet_schemas import PetSuccessResponse, PetCreateRequest, PetUpdateRequest, PetResponse
from app.services.pets_service import PetService

pet_router = APIRouter(prefix="/pets",tags=["pet"])
pet_service = PetService()
@pet_router.post(
        "/create",
         response_model = PetResponse
        )
def create_pet(request: PetCreateRequest):
        return pet_service.create_pet(request)
@pet_router.get(
        "/get",
        response_model=List[PetSuccessResponse],
        )
def get_pets() -> List[PetSuccessResponse]:
        return pet_service.get_pets()
@pet_router.get(
        "/get_by_id",
        response_model=PetResponse
        )
def get_pet_by_id(pet_id: str) -> PetResponse:
        return pet_service.get_pet_by_id(pet_id)
@pet_router.put(
        "/update",
        response_model=PetResponse
        )
def update_pet(request: PetUpdateRequest):
        return pet_service.update_pet(request)
@pet_router.delete(
        "/delete",
        response_model=PetResponse
        )
def delete_pet(pet_id: str) -> PetResponse:
        return pet_service.delete_pet(pet_id)
@pet_router.get(
        "/get_age_average",
        response_model=PetResponse
        )
def get_pet_age_average() -> PetResponse:
        return pet_service.get_average_age()