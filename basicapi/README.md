## Basic User Management API
This is a simple RESTful API build using django and DRF that provides basic CRUD (Create, Read, Update, Delete) operations for managing users.

### Features
- Create a User
- Retrieve all users
- Retrieve a single user
- Update a user
- Delete a user

### Installation and Setup
Install python and pip
#### Steps
##### Create Virtual environment
`python -m venv crud`
`crud\Scripts\activate #on windows` 
##### Install dependencies
`pip install -r requirements.txt`
##### Run migrations
`python manage.py makemigrations`
`python manage.py migrate`
##### Start the server
`python manage.py runserver`

### API Endpoints
API will be available at `http://127.0.0.1:8000/api/`

| Method | Endpoint           | Function                 |
|--------|--------------------|--------------------------|
| GET    | `/api/users/`      | Retrieve all users       |
| GET    | `/api/users/{id}`  | Retrieve a user by id    |
| POST   | `/api/users/`      | Create a new user        |
| PUT    | `/api/users/{id}`  | Update a user by id      |
| DELETE | `/api/users/{id}`  | Delete a user by id      |

### Example Request and Responses
#### - Create a user
Request
```json
{
    "name": "Anjana",
    "email": "anjana@gmail.com",
    "age": 30
  }
```
Response
```json
{
    "id": 1,
    "name": "Anjana",
    "email": "anjana@gmail.com",
    "age": 30
  }
```
#### - Retrieve all users
Request:
`GET /api/users/`
Response:
```json
[
  {
    "id": 1,
    "name": "Anjanavs",
    "email": "anjana@gmail.com",
    "age": 30
  },
  {
    "id": 2,
    "name": "aryadevi",
    "email": "arya@gmail.com",
    "age": 27
  }
]
```
#### - Retrieve a User
Request:
`GET /api/users/1/`
Response:
```json
  {
    "id": 1,
    "name": "Anjanavs",
    "email": "anjana@gmail.com",
    "age": 30
  },
```
#### - Update a user
Request:
`PUT /api/users/1/`

```json
{
    "id": 1,
    "name": "Anjanavs",
    "email": "anjana@gmail.com",
    "age": 30
  }
```
Response:
```json
{
    "id": 1,
    "name": "Anjanavs",
    "email": "anjana@gmail.com",
    "age": 30
  }
```
#### - Delete a user
Request:
`DELETE /api/users/4/`
Response
```json
{
  "message": "User deleted successfully"
}
```

### Testing Tool
Used Thunder Client(VS Code Extension) to test API endpoints.






