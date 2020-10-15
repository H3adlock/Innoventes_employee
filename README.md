# Innoventes_employee_rest_api
API for employee management
- Add/Update/Delete Employee records
- Get/Get All Employee records WITHOUT Address details
- Get Employee (by employee ID) ALONG WITH Address details
- Add/Update/Delete an address for an employee
- List all addresses for a particular employee(by employee ID)

## Setting up project Linux
```
# create a virtualenv 
virtualenv venv
source venv/bin/activate
```
## Setting up project Windows
```
# create a virtualenv 
virtualenv venv
source venv\Scripts\activate
```
## Dependencies and Initializing
```
pip install -r reuqirements.txt
./manage.py migrate
./manage.py runserver
./manage.py load_dataset
```
## .env file for Environment variables in Dev setup
```
SECRET_KEY=8bnc6ww1a3o29ow2=i$q5))biz&(#642(ycf)=*wng_#9o$#h1
ENV=dev
```

## Demo
deployed in Heroku
https://innoventes-employee.herokuapp.com/api/employees/

# Postman Documentation
------------

# API request examples
APIs for Generic or Anonymous user 
### For Authentication
retrieve auth token by providing username and password in body
https://innoventes-employee.herokuapp.com/api-token-auth/

### For Generic or Admin Users
- Add/Update/Delete Employee records
    https://innoventes-employee.herokuapp.com/api/employees/ and https://innoventes-employee.herokuapp.com/api/employees/<pk>

- Get/Get All Employee records WITHOUT Address details
https://innoventes-employee.herokuapp.com/api/employees/list/

- Get Employee (by employee ID) ALONG WITH Address details
https://innoventes-employee.herokuapp.com/api/employees/<pk>

- Add/Update/Delete an address for an employee
https://innoventes-employee.herokuapp.com/api/address/
https://innoventes-employee.herokuapp.com/api/address/<pk>
and https://innoventes-employee.herokuapp.com/api/employees/<pk>

- List all addresses for a particular employee(by employee ID)
https://innoventes-employee.herokuapp.com/api/employees/<pk>