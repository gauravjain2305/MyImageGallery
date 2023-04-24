# MyImageGallery
A Django REST framework based web application that allows users to view, upload and discover images. 
Users can register themselves on the application and can upload, delete and edit the details of the images uploaded by them. 
Users can search images and also see the related images based on the searched image.

## What is Django REST framework?
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.<br>
It is built on top of the Django web framework that reduces the amount of code you need to write to create REST interfaces. 

## Requirements
- Python 3.6
- Django 3.1
- Django REST Framework
- Simple JWT

## Installation
After cloning the repository, you have to create a virtual environment, so you can have a clean python installation.
You can do this by running the command
```
python -m venv venv
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt
```

You can start the Django's development server using
```
python manage.py runserver
```

## URLs
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

Endpoint |HTTP Method | Result
--- | --- |---
`images/list` | GET | Get all records
`images/detail/:id` | GET | Get a single record
`images/register`| POST | Register a user
`images/login`| POST | Login a user
`images/logout`| POST | Logout a user
`images/create`| POST | Create a new record
`images/update/:id` | PUT | Update a record
`images/delete/:id` | DELETE | Delete a record

## APIs
All apis working bullet points & Screenshot of Postman result

### images/register
* This API is used to register a user.

### images/login
* This API is used to login user.

### images/logout
* This API is used to logout user.

### images/detail/:id
* This API is used to get image details.

### images/list
* This API is used to get a list of images.

### images/create
* This API is used to create images.

### images/update/:id
* This API is used to update image details.

### images/delete/:id
* This API is used to delete images.