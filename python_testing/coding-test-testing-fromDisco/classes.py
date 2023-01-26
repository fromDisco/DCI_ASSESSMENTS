from utils.db import connect_db, save_to_db, close_connection


class Human:
    """
    Design a human class that takes in two arguments for its
    constructor.

    e.g. Human('first name', 'last name')

    The Human class shall have 2 attributes
    - last_name
    - first_name

    Design an instance method called `save()`.
    The save method should when called, insert data into a database and return a dictionary value.

    Recall that to insert data, the following is the code you
    would use:

    INSERT INTO humans (first_name, last_name) values('john', 'doe');

    For example:

    h = Human('John', 'Doe')
    return_value = h.save()
    print(return_value)
    >>> {"id": 1, "first_name": "John", "last_name": "Doe" }
    """

    def __init__(self, first_name, last_name):
        """Set up constructor"""
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f"<Human(first_name={self.first_name}, last_name={self.last_name}>"

    def save(self):
        """
        Save first_name and last_name to the database and return a dictionary
        """
        # cur is a cursor, an object through which you can perform some database actions
        connection, cur = connect_db()
        cur.execute(
            f"""
            INSERT INTO humans (first_name, last_name) 
            VALUES('{self.first_name}', '{self.last_name}') 
            RETURNING id, first_name, last_name
            """
        )

        # get ID of saved human
        # human_id = cur.fetchone()[0]
        # Code below saves to the database
        save_to_db(connection)
        human_id = cur.fetchone()

        table_keys = ["id", "first_name", "last_name"]
        human_dict = dict(zip(table_keys, human_id))

        return human_dict

    @classmethod
    def get(cls, id):
        connection, cur = connect_db()
        cur.execute(f"SELECT first_name, last_name FROM humans WHERE id={id}")
        human = cur.fetchone()
        close_connection(connection, cur)

        if human:
            return cls(human[0], human[1])
        else:
            return "Human not found!"

    @staticmethod
    def delete(id):
        connection, cur = connect_db()

        # execute SELECT query
        cur.execute(f"SELECT * FROM humans WHERE id={id}")
        human = cur.fetchone()

        # Check to see if the human is in the table
        if not human:
            return "Human not found!!@$$"

        try:
            cur.execute(f"DELETE FROM humans WHERE id={id}")
            save_to_db(connection)
            return "Successfully deleted human"
        except:
            return "Something bad happened!"
