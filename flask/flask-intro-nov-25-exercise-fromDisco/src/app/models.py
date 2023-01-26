import psycopg2


config = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
    "database": "flask_intro",
}


# Singular form of a class name to represent a table
# table will be mostly plural
class Reminder:
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return_string = f"<{self.__class__.__name__} id={self.id}, title={self.title}, description={self.description}>"
        return return_string

    def set_id(self, reminder_id):
        self.id = reminder_id

    def save(self):
        """
        Stores the values of title and description in the table
        """
        connection = psycopg2.connect(**config)
        cur = connection.cursor()

        cur.execute(
            f"""INSERT INTO reminders (title, description) 
            VALUES('{self.title}', '{self.description}') RETURNING id, title, description"""
        )
        # persist the changes
        connection.commit()

        values = cur.fetchone()
        cur.close()
        connection.close()
        # set id of current instance
        self.set_id(values[0])

        return self

    @classmethod
    def find(cls, reminder_id):
        """
        Search for id in db and create an instance of the db entry
        """
        connection = psycopg2.connect(**config)
        cur = connection.cursor()

        cur.execute(
            f"select row_to_json(reminders) from reminders where id={reminder_id}"
        )
        values = cur.fetchone()[0]

        cur.close()
        connection.close()

        reminder_obj = cls(values["title"], values["description"])
        reminder_obj.set_id(values["id"])

        return reminder_obj
