from fastapi import FastAPI, status

from app.controllers.pet_controller import pet_router

app = FastAPI(
    title="Pets API",
    debug=True
)

# CORS enabled
origins = [
    "*",
]

app.include_router(pet_router)

@app.get(
        "/check",
        status_code=status.HTTP_200_OK
        )
def health_check():
    '''app is already working!'''
    return {"message": "All works, let's try with some pets :)!"}

@app.get(
    "/"
)
def home():
    return {"message": "Welcome to Pets API. Go -> /docs to see the documentation"}
