from flask import jsonify, request
from sqlalchemy.inspection import inspect
from werkzeug.security import generate_password_hash, check_password_hash

from . import create_app, db
from .models import Reminder, User

app = create_app()
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    reminder_data = (
        Reminder.query.all()
    )  # Queries the database using a SQLAlchemy model

    # Do not touch the code below (Fix code up there 👆👆)
    reminder_data = [item.to_json() for item in reminder_data]
    return jsonify({"reminders": reminder_data})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    try:

        title = request.json.get("title")
        description = request.json.get("description")
        user_id = request.json.get("user_id")

        reminder_data = Reminder(title=title, description=description, user_id=user_id)
        db.session.add(reminder_data)
        db.session.commit()

        # DO not touch code below
        return jsonify(reminder_data.to_json())
    except Exception as e:
        print(e)
        return jsonify({"message": "Something bad happened"}), 500


@app.route("/reminders/<int:reminder_id>")
def reminder(reminder_id):
    reminder_data = Reminder.query.get(reminder_id)

    # DO NOT TOUCH the code below this line
    if not reminder_data:
        return jsonify({"message": "Reminder not found"}), 404
    return jsonify(reminder_data.to_json())


@app.route("/reminders/<int:reminder_id>", methods=["DELETE"])
def delete_reminder(reminder_id):
    instance = Reminder.query.get(reminder_id)
    db.session.delete(instance)
    db.session.commit()

    # Do not touch code below
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:reminder_id>/update", methods=["PUT"])
def update_reminder(reminder_id):
    try:
        reminder_data = Reminder.query.get(reminder_id)
        reminder_data.title = request.json.get("title", reminder_data.title)
        reminder_data.description = request.json.get(
            "description", reminder_data.description
        )
        db.session.commit()
        return jsonify(reminder_data.to_json()), 201
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


#########################################
# User ##################################


@app.route("/users")
def user_index():
    user_instances = User.query.all()  # Queries the database using a SQLAlchemy model

    # Do not touch the code below (Fix code up there 👆👆)
    user_instances = [item.to_json() for item in user_instances]
    return jsonify({"users": user_instances})


@app.route("/add-user", methods=["POST"])
def add_user():
    try:
        username = request.json.get("username")
        password = request.json.get("password")

        user_instance = User(username=username, password_hash=password)
        user_instance.password(password)

        db.session.add(user_instance)
        db.session.commit()

        # DO not touch code below
        return jsonify(user_instance.to_json())

    except Exception as e:
        print(e)
        return jsonify({"message": "Something bad happened"}), 500


@app.route("/users/<int:user_id>/find")
def find_user(user_id):
    instance = User.query.get(user_id)

    if not instance:
        return jsonify({"message": "Reminder not found"}), 404
    return jsonify(instance.to_json())


@app.route("/users/<int:user_id>/update", methods=["PUT"])
def update_user(user_id):
    try:
        instance = User.query.get(user_id)
        instance.id = request.json.get("id", instance.id)
        instance.username = request.json.get("username", instance.username)
        instance.password = request.json.get("password", instance.password)
        db.session.commit()
        return jsonify(instance.to_json()), 201
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    instance = User.query.get(user_id)
    db.session.delete(instance)
    db.session.commit()

    # Do not touch code below
    return jsonify({"message": "Successfully deleted!"})
