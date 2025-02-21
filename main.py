from fastapi import FastAPI, status

from Controllers.pet_controller import pet_router

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
        "/healthCheck",
        status_code=status.HTTP_200_OK
        )
async def healthCheck():
    '''app is already working!'''
    return {"message": "All works!"}
