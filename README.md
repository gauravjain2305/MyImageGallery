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
An API is a set of defined rules that allows computers or applications to communicate with one another. It is a type of software interface, offering a service to other pieces of software.

The APIs has some restrictions:
-   The images are always associated with a creator (user who created it).
-   Only authenticated users may create and see images.
-   Only the creator may update or delete it.
-   The API doesn't allow unauthenticated requests.

We can test the APIs using [Postman](https://www.postman.com/).

### images/register
* This API is used to register a user.

![image](https://user-images.githubusercontent.com/48149431/233985101-4b16821f-b67d-4156-b76a-81e0997733d9.png)

### images/login
* This API is used to login user.

![image](https://user-images.githubusercontent.com/48149431/233985646-da69cdfd-4c01-48b1-8f7d-78336075e02f.png)

### images/logout
* This API is used to logout user.

![image](https://user-images.githubusercontent.com/48149431/233987343-3a3f7299-004b-4b9c-8976-8985b7f51583.png)

### images/detail/:id
* This API is used to get image details.

![image](https://user-images.githubusercontent.com/48149431/234035703-61652eeb-2830-4606-9f85-28106c4c6e71.png)

### images/list
* This API is used to get a list of images.

![image](https://user-images.githubusercontent.com/48149431/234035069-f1d45b00-2f50-428a-9f56-c29ab7e2bed6.png)

### images/create
* This API is used to create images.

![image](https://user-images.githubusercontent.com/48149431/233990341-56bae76d-8491-4c0d-9986-c66cb43d9d99.png)

### images/update/:id
* This API is used to update image details.

![image](https://user-images.githubusercontent.com/48149431/234034112-a158e435-3076-4716-b4cb-99c6538fc159.png)

### images/delete/:id
* This API is used to delete images.

![image](https://user-images.githubusercontent.com/48149431/234036257-93b0d998-88ed-4816-b303-89a62abdfd4f.png)
