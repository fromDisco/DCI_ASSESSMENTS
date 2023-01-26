# Exercise: Replace -- all manual database interactions with flask-alchemy
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    # Fetch all the reminders from the database
    # cur.execute("SELECT id, title, description FROM reminders")
    # reminder_data = cur.fetchall()
    reminder_data = [
        {"id": item[0], "title": item[1], "description": item[2]}
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
    # cur.execute(
    #     f"INSERT INTO reminders (title, description) VALUES('{title}', '{description}') RETURNING id, title, description;"
    # )
    # connection.commit()
    # values = cur.fetchone()
    # change the return value from empty list to have REMINDERS instead
    return jsonify({})


@app.route("/reminders/<int:id>")
def reminder(id):
    # cur.execute(f"SELECT title, description FROM reminders WHERE id = {id};")
    # reminder_data = cur.fetchone()
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data[0],
            "description": reminder_data[1],
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "Sorry something bad happened"}), 500


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    # cur.execute(f"DELETE FROM reminders WHERE id={id};")
    # commit the changes
    # connection.commit()
    # TODO: Implement a flask-sqlalchemy solution
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    # TODO: Iplement a flask-sqlalchemy solution
    # values = cur.fetchone()
    # values -> None
    # values[0] -> throws an error
    try:
        return jsonify({"id": values[0], "title": values[1], "description": values[2]})
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
