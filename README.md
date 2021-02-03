# Acedemic Registration System
System to assign professors to courses, and for students to register to courses.
<br> Genesys Coding Challenge - Morgan Reilly

## API Documentation
Visit: https://app.swaggerhub.com/apis/MorganReilly/AcademicRegistrationAPI/1.0
## Backend | Database
The backend for this application is built using Flask and Connexion.<br>
Flask is a micro web framework written in python.<br>
Connexion is framework which sits on top of Flask to handle HTTP requests defined using OpenAPI.<br>
Connexion allows a user to write specifications, and then maps the endpoints to Python functions. <br>
To connect to the database I first established a connection to the database in the [config.py](./flask-webapp/config.py) file. Then for each handler I create a cursor for each request to execute SQL statements on the database.<br>
The database used for this project is a MySQL database.<br>
To test the endpoints on this project I sent requests using Postman and cURL.<br> Only two HTTP methods were needed for this project `GET` and `POST`.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) documentation
* [Connexion](https://connexion.readthedocs.io/en/latest/) documentation
* [OpenAPI Specificaion](./flask-webapp/swagger.yml)
* [Example](./flask-webapp/students.py) of mapping of endpoint to python handler
* [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
* [Database Schema](./academicdb.sql)
* [Postman Test Suite](./academicregsys.postman_collection.json)
## Hosting
An Amazon RDS is used to host host the database for this project.<br>
To allow the application to communicate I had to modify the [config.py](./flask-webapp) file to include the updated connection points.<br>
An Amazon EC2 instance is used as a virtual machine and Nginx is used as a web server in order to host the flask application.<br>
On the EC2 instance the application is served using uWSGI.
* [RDS Documentation](https://docs.aws.amazon.com/rds/index.html)
* [EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html)
* [Nginx Documentation](https://nginx.org/en/docs/)
* [uWSGI Documentation](https://uwsgi-docs.readthedocs.io/en/latest/)

## Endpoint Testing with cURL | Postman
Note: This assumes you have `cURL` on your machine.
* Follow [this](https://developer.ft.com/portal/docs-start-install-postman-and-import-request-collection) for instructions on importing collection and sending requests
### Professors 
* Get all Professors using `GET` request:<br>
`$ curl http://18.203.101.103/api/professors`
* Create new Professor `POST` request:<br> `$ curl http://18.203.101.103/api/professors -d '{"fname":"John","lname":"Doe"}' -H "Content-Type: application/json"`

### Courses 
* Get all Courses using `GET` request:<br>
`$ curl http://18.203.101.103/api/courses`
* Create new Course `POST` request:<br> `$ curl http://18.203.101.103/api/courses -d '{"title":"Computer Science","p_id":1}' -H "Content-Type: application/json"`

### Students 
* Get all Students using `GET` request:<br>
`$ curl http://18.203.101.103/api/students`
* Create new Student `POST` request:<br> `$ curl http://18.203.101.103/api/students -d '{"fname":"Kelly","lname":"Appleseed"}' -H "Content-Type: application/json"`

### Registries
Note: This must have an existing course id, an existing student id, and must be unique in entry.
* Get all Registries using `GET` request:<br>
`$ curl http://18.203.101.103/api/registries`
* Create new Registry `POST` request:<br> `$ curl http://18.203.101.103/api/registries -d '{"c_id":102,"s_id":3}' -H "Content-Type: application/json"`

### References | Other Links
* [Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/) - Helpful in getting moving quickly with Flask
* [Flask Connexion Tutorial](https://realpython.com/flask-connexion-rest-api/) - Helpful in seeing how Connexion and SQLite works with Flask in a ReSTful way
* [Flask Server Deployment](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04) - Helpful in both setting up the server and deploying the application