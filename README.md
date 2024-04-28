# Vendor Management System in Django

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

## Prerequisites

- Python=3.12

## Installation

# 1. Clone the repository:
Clone the repository or download it as zip

# 2.Create a virtual environment:
Install virtualenv using "pip install virtualenv"
Create a new virtual environement using "python -m venv venv_name"

source venv_name/bin/activate  # For Linux/Mac  
venv_name\Scripts\activate     # For Windows  

# 3.Install dependencies:
pip install -r requirements.txt  

# 4.Migrating the DB:
python manage.py makemigrations  
python manage.py migrate  

# 5. Create superuser
python manage.py createsuperuser

# 6. Create a normal user
python manage.py runserver
goto http://localhost:8000/admin/ and login with the superuser details created in step 5
under AUTHENTICATION ND AUTHORIZATION click on +ADD against users
Fill in the required details and click on save

## Usage
# 1.Start the server:
python manage.py runserver

# 2.Obtain token
make a post request to http://localhost:8000/gettoken/ in postman, the payload should be of example { "username":"superuser","password":"superuser" }
obtain the token from the response and add it in the Headers of the Postman collection

# 3.openAPI schema/ Swagger UI
goto http://localhost:8000/api/schema/redoc/
goto http://localhost:8000/api/schema/swagger-ui/  

Once the token is obtained from Postman, the requests and response can be handled by http://localhost:8000/api/schema/swagger-ui/


## Running Tests  
Run the test suite:  
  python manage.py test  

