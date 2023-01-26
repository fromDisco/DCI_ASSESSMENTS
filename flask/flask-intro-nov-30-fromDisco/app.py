# Exercise: Replace -- all manual database interactions with our ORM
from flask import Flask, jsonify, request
from models import Reminder

app = Flask(__name__)


@app.route("/")
def index():
    # Fetch all the reminders from the database
    reminder_data = Reminder.all()

    reminder_data = [
        {"id": item.id, "title": item.title, "description": item.description}
        for item in reminder_data
    ]
    return jsonify({"reminders": reminder_data})


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    try:
        title = request.json["title"]
    except KeyError:
        title = None

    # handle the exception (error handling)
    try:
        description = request.json["description"]
    except KeyError:
        description = None

    reminder = Reminder(title=title, description=description)
    reminder = reminder.save()

    # change the return value from empty list to have REMINDERS instead
    return jsonify(
        {
            "id": reminder.id,
            "title": reminder.title,
            "description": reminder.description,
        }
    )


@app.route("/reminders/<int:id>")
def reminder(id):
    reminder_data = Reminder.find(id)
    if not reminder_data:
        return jsonify({"message": "Reminder not found"}), 404
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data.title,
            "description": reminder_data.description,
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "Sorry something bad happened"}), 500


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    success = Reminder.delete(id)
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    instance = Reminder.find(id)
    values = instance.update(**request.json)
    try:
        return jsonify({"id": values[0], "title": values[1], "description": values[2]})
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
