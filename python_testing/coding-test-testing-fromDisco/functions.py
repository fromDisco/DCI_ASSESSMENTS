from utils.db import connect_db, save_to_db, close_connection


"""
Design an function called `save()`. 

The save method that takes in a dictionary with 2 key/value pairs:
{"first_name": "John", "last_name": "Doe"}

Recall that to insert data, the following is the code you 
would use:

INSERT INTO humans (first_name, last_name) values('john', 'doe');

For example:

return_value = save('John', 'Doe')
print(return_value) 
>>> { "first_name": "John", "last_name": "Doe" }
"""


def save(dictionary):
    """
    Save first_name and last_name to the database and return a dictionary
    """
    # cur is a cursor, an object through which you can perform some database actions
    connection, cur = connect_db()

    # Adding "Sr." to the name
    dictionary["last_name"] += " Sr."
    cur.execute(
        f"""
            INSERT INTO humans (first_name, last_name) 
            VALUES('{dictionary["first_name"]}', '{dictionary["last_name"]}') 
            RETURNING id, first_name, last_name;
            """
    )

    # Code below saves to the database (no need to change code here)
    [id, first_name, last_name] = cur.fetchone()
    print(id, first_name, last_name)
    save_to_db(connection)
    close_connection(connection, cur)

    # TODO: add code to return a dictionary
    human_data = {"id": id, "first_name": first_name, "last_name": last_name}

    return human_data
