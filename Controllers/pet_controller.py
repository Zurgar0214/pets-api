from fastapi import APIRouter

from Models.pet_entity import PetEntity
from Services.pets_service import create_pet_service

pet_router = APIRouter(prefix="/pets",tags=["pet"])

@pet_router.post(
        "/create"
        )
async def create_pet(name:str, age:int) -> PetEntity:
        return create_pet_service(name, age)

#TODO: Define services for CRUD