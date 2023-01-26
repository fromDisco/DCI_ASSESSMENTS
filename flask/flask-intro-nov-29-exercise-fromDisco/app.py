from flask import Flask, jsonify, request
from models import Reminder, make_connection

app = Flask(__name__)

db_con = make_connection()
connection = db_con.get("connection")
cur = db_con.get("cur")


@app.route("/")
def index():
    # Fetch all the reminders from the database
    cur.execute("SELECT id, title, description FROM reminders")
    reminder_data = cur.fetchall()
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
    cur.execute(
        f"INSERT INTO reminders (title, description) VALUES('{title}', '{description}') RETURNING id, title, description;"
    )
    connection.commit()
    values = cur.fetchone()
    output = {"id": values[0], "title": values[1], "description": values[2]}
    # change the return value from empty list to have REMINDERS instead
    return jsonify(output)


# FIND
@app.route("/find-reminder", methods=["POST"])
def reminder():
    kwargs = request.json
    reminder_instance = Reminder.find(**kwargs)

    reminder_dict = {
        "id": reminder_instance.id,
        "title": reminder_instance.title,
        "description": reminder_instance.description,
    }
    return jsonify(reminder_dict)


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    cur.execute(f"DELETE FROM reminders WHERE id={id};")
    # commit the changes
    connection.commit()
    return jsonify({"message": "Successfully deleted!"})


@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    cur.execute(
        f"""
        UPDATE reminders
        SET title='{request.json.get('title')}', 
        description='{request.json.get('description')}'
        WHERE id={id} RETURNING id, title, description
    """
    )
    values = cur.fetchone()
    # values -> None
    # values[0] -> throws an error
    connection.commit()
    try:
        return jsonify({"id": values[0], "title": values[1], "description": values[2]})
    except TypeError:
        return jsonify({"message": "Reminder not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
