# Recipe App API

The Recipe App API is a project built with Django Rest Framework (DRF) that provides an API for managing recipes. This API allows CRUD (Create, Read, Update, Delete) operations on recipes, ingredients, and tags.

## Features

- Recipe management with detailed information.
- Administration of ingredients and tags associated with recipes.
- Swagger documentation for easy API usage.

## Requirements

- Python 3.12
- Django 3.3
- Django Rest Framework (DRF) 3.13
- Flake8 3.10

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Lukaspep/recipe-app-api.git

2. Navigate to the project director:

   ```bash
   cd recipe-app-api

3. Install dependecies:

   ```bash
   pip install -r requirements.txt

4. Apply migrations:
   
   ```bash
   docker-compose run --rm app sh -c "python manage.py migrate"

5. Start the server:

  ```bash
  docker-compose up

  The API will be available at http://127.0.0.1:8000/.
  ```
Usage
Access the Swagger documentation to explore and test the API: http://127.0.0.1:8000/api/docs/

You can also access the Django Rest Framework API documentation at: http://127.0.0.1:8000/api/schema/


Contributions are welcome! If you find bugs or have ideas to improve the project, please open an issue or submit a pull request.


This project is licensed under the MIT License - see the LICENSE file for details.
