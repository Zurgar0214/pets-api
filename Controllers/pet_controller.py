from fastapi import APIRouter

from Models.pet_entity import PetEntity

pet_router = APIRouter(prefix="/pets",tags=["pet"])

@pet_router.post(
        "/create"
        )
async def create_pet(pet:str):
        return 'ok'

#TODO: Define services for CRUD