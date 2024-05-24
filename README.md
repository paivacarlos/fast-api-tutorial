# My project FastAPI

This project is a RESTful API built with FastAPI and PostgreSQL. It includes CRUD operations for managing registers, along with data validation and error handling. The API supports creating, reading, updating, and deleting register entries.


## Table of Contents

- **Features**

- **Requirements**
- **Installation**
- **Configuration**
- **Usage**
- **Testing**
- **Project Structure**

## Features
- **Create Register**: Create a new register entry.
- **Get Register**: Retrieve a specific register entry by ID.
- **Get All Registers**: Retrieve all register entries.
- **Update Registe**r: Update an existing register entry.
- **Delete Register**: Delete a register entry by ID.
- **Health Check**: Verify if the server is online.
- **Data Validation**: Validate CPF and other register fields.

## Requirements
- Python 3.11.1
- PostgreSQL
- pip for package management

## Installation

## Clone the Repository

`git clone https://github.com/yourusername/fastapi-postgres-project.git`

`cd fastapi-postgres-project`

**Create and Activate a Virtual Environment**

`python -m venv venv`

`source venv/bin/activate   # On Windows, use venv\Scripts\activate`

**Create and Activate a Virtual Environment**

`pip install -r requirements.txt`


## **Configuration**

## **Set Up Environment Variables**

Create a .env file in the root of the project and add the following:

`DEV_URL_BASE=http://localhost:8000`


`DATABASE_URL=postgresql://username:password@localhost/dbname`


Replace **username**, **password**, and **dbname** with your PostgreSQL credentials and database name


## Usage

**Run the Application**

`uvicorn app.main:app --reload
`

The API will be available at http://localhost:8000.

## API Endpoints

- `GET` `/health-check`: Check if the server is online.
- `POST` `/create-register`: Create a new register.
- `GET` `/register/{register_id}`: Retrieve a register by ID.
- `GET` `/all-registers`: Retrieve all registers.
- `PUT` `/update-register/{register_id}`: Update a register by ID.
- `DELETE` `/delete-register/{register_id}`: Delete a register by ID.

## Testing

## Run Tests
To run the tests using pytest, execute the following command:


`pytest tests/api`

`Project Structure`

```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── ...
│   ├── routers
│   │   ├── __init__.py
│   │   └── ...
│   ├── services
│   │   ├── __init__.py
│   │   └── ...
│   └── database
│       ├── __init__.py
│       └── ...
├── tests
│   ├── __init__.py
│   ├── test_example.py
│   └── utils
│       ├── __init__.py
│       └── base_url.py
├── requirements.txt
└── .env

