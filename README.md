# Pets API

Pets API is a RESTful API built with FastAPI to manage pet information, including creating, retrieving, updating, and deleting pets.

## Features
- Create a new pet
- Retrieve all pets
- Get pet details by ID
- Update pet information
- Delete a pet
- Calculate the average age of all pets

## Technologies Used
- Python 3
- FastAPI
- Pydantic
- Uvicorn

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Zurgar0214/pets-api.git
   cd pets-api
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the API

Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Create a Pet
**POST** `/pets/create`
- Request Body:
  ```json
  {
    "name": "Buddy",
    "age": 3
  }
  ```
- Response:
  ```json
  {
    "code": "200",
    "message": "Pet created successfully!",
    "data": {
      "id": "1",
      "name": "Buddy",
      "age": 3
    }
  }
  ```

### Get All Pets
**GET** `/pets`
- Response:
  ```json
  [
    {
      "id": "1",
      "name": "Buddy",
      "age": 3
    }
  ]
  ```

### Get Pet by ID
**GET** `/pets/{pet_id}`
- Response:
  ```json
  {
    "code": "200",
    "message": "Pet found!",
    "data": {
      "id": "1",
      "name": "Buddy",
      "age": 3
    }
  }
  ```

### Update a Pet
**PUT** `/pets/update`
- Request Body:
  ```json
  {
    "id": "1",
    "name": "Buddy",
    "age": 4
  }
  ```
- Response:
  ```json
  {
    "code": "200",
    "message": "Pet updated successfully!",
    "data": {
      "id": "1",
      "name": "Buddy",
      "age": 4
    }
  }
  ```

### Delete a Pet
**DELETE** `/pets/delete/{pet_id}`
- Response:
  ```json
  {
    "code": "200",
    "message": "Pet deleted successfully",
    "data": null
  }
  ```

### Calculate Average Age of Pets
**GET** `/pets/average-age`
- Response:
  ```json
  {
    "code": "200",
    "message": "Average age calculated successfully",
    "data": 3.5
  }
  ```

## API Documentation
FastAPI provides interactive API documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Created By:
Juan Diego Varón Valencia - Manizales University | Programming 3

