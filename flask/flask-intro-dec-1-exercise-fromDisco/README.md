## Some helpful instructions:

Running the flask project 

`FLASK_DEBUG=True FLASK_APP=main.py flask run`

Please watch the terminal in case of an error it might be that your web server crashed and you need to manually restart it.

- Reset the database by running the `create.sql` file again.
- Some organizational structure has been added to the project so that it plays nicely with your existing database - closely reflects an MVC design pattern.

# In-class live coding exercise to be done together with teacher

- Use the flask-sqlalchemy ORM
- Please note that at this stage, no tests are required beyond manual testing with Postman.
- You can also use `flask shell` to access the database objects.

# Tasks and Activities
1. Design a method in the Reminder class called `to_json()` instance method that returns a dictionary that looks like this:
    
```json
{ "id": 1, "title": "Some title", "description": "Some description" }
```

2. After this method is designed, go through the code base in a file called `views.py` and make changes to places where you see the `TODO` word.

# Exercise to be done without the teacher's direct help

- Add a new model called `User` and make sure the table name is `users`
- Create a 1 to many relationship between Users and Reminder
- Self study about relationships in database tables


References: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/ 
